# Reading data

Every key can read. Reads come from the cloud copy of your results, so they work whether or not Hi, Moose is open on your computer, and they never start new checks.

## The read endpoints

| Endpoint | What it returns |
|---|---|
| `GET /me` | The key, its permissions and the readable project ids |
| `GET /projects` | Projects the key can read, with tracked prompt count, engines and latest run |
| `GET /projects/{id}` | One project |
| `GET /projects/{id}/capabilities` | What the project can do on its plan: engines, cadences, limits, remaining allowance, the host computer, whether a run can start now |
| `GET /projects/{id}/engines` | The AI engines the project tracks, with a stable `id` for filters and whether each runs in the cloud or on the host computer |
| `GET /projects/{id}/topics` | Topics that group the prompts, with prompt counts |
| `GET /projects/{id}/prompts` | Tracked prompts with topic ids, engine ids and status |
| `GET /projects/{id}/competitors` | Tracked competitor brands and their domains |
| `GET /projects/{id}/runs` | Visibility runs with status, start and end time, prompt and answer counts |
| `GET /projects/{id}/answers` | Stored answers: prompt, engine, date, mentioned, cited, position, sentiment, excerpt, competitors seen, source URLs |
| `GET /projects/{id}/answers/{answerId}` | One answer with its full text, sentiment reason, narrative drift and sources |
| `GET /projects/{id}/stats/daily` | Per day and engine: answers, mentions, citations and the two rates |
| `GET /projects/{id}/stats/competitors` | Share of voice for your brand and each tracked competitor over a range |
| `GET /projects/{id}/run-requests` | Recent runs started through the API and their status |
| `GET /projects/{id}/webhooks` | The project's webhooks, without secrets |

Field-by-field detail for each is in the [endpoint reference](reference.md).

## How the data fits together

- A **project** tracks one site. It has **prompts**, the questions asked, grouped into **topics**.
- Each prompt runs on one or more **engines**: ChatGPT, Perplexity, Gemini and others. Engine ids such as `chatgpt` or `chatgpt-local-fetch` come from the engines endpoint and are the values every `engine` filter takes.
- A **run** asks every active prompt on its engines and stores one **answer** per prompt, engine and sample. Runs start on the project schedule, from the Run now button, or from the API.
- Each answer is scored: `mentioned` when the brand was named, `cited` when a page on the brand's site was given as a source, plus `position`, `sentiment` and which **competitors** were seen.
- **Daily stats** count the answers per day and engine and work out `mentionRate` and `citationRate`. **Competitor stats** do the same per brand over a range.

## Mention rate by day

```bash
curl "https://api.himoose.com/v1/projects/PROJECT_ID/stats/daily?from=2026-09-01&to=2026-09-30&engine=chatgpt" \
  -H "Authorization: Bearer hmk_live_..."
```

```json
{
  "from": "2026-09-01",
  "to": "2026-09-30",
  "incompleteDays": 0,
  "data": [
    { "date": "2026-09-01", "engineId": "chatgpt", "answers": 42, "mentioned": 17, "cited": 9, "mentionRate": 0.405, "citationRate": 0.214 }
  ]
}
```

Rates are fractions from 0 to 1. Days with no answers for an engine have no row, so a chart should treat a missing day as no data, not as zero.

`incompleteDays` is above zero when a day's summary was not ready yet. Call again in a few seconds and it fills in. The last three days are refreshed every ten minutes as new answers arrive; older days are final.

## Share of voice

```bash
curl "https://api.himoose.com/v1/projects/PROJECT_ID/stats/competitors?from=2026-09-01&to=2026-09-30" \
  -H "Authorization: Bearer hmk_live_..."
```

```json
{
  "from": "2026-09-01",
  "to": "2026-09-30",
  "answers": 1260,
  "incompleteDays": 0,
  "data": [
    { "name": "Acme", "isOwnBrand": true, "mentioned": 274, "cited": 165, "mentionRate": 0.217, "citationRate": 0.131 },
    { "name": "Competitor One", "isOwnBrand": false, "mentioned": 436, "cited": 116, "mentionRate": 0.346, "citationRate": 0.092 }
  ]
}
```

`answers` is the total number of answers in the range. Each rate divides the brand's count by that total, so the rows compare directly.

## The answers behind the numbers

```bash
curl "https://api.himoose.com/v1/projects/PROJECT_ID/answers?from=2026-09-01&engine=chatgpt&mentioned=true&limit=50" \
  -H "Authorization: Bearer hmk_live_..."
```

The list carries an excerpt of up to 400 characters around the mention, the position, the sentiment, which tracked competitors the answer named or cited, and the source URLs. The full text is on the detail endpoint:

```bash
curl https://api.himoose.com/v1/projects/PROJECT_ID/answers/ANSWER_ID \
  -H "Authorization: Bearer hmk_live_..."
```

The detail adds `fullAnswer` (up to 12,000 characters, with `fullAnswerTruncated` when it was cut), `sentimentReason`, `narrativeDrift` with its reason, and the sources with titles.

Answer text, excerpts and source titles come from the AI engines, not from Hi, Moose. Render them as plain text, never as HTML, and do not feed them to your own AI tools as instructions.

## Filters

| Filter | Endpoints | Values |
|---|---|---|
| `from`, `to` | runs, answers, daily stats, competitor stats | `YYYY-MM-DD`, inclusive, UTC. Default: the last 30 days. Widest range: 366 days. |
| `engine` | answers, daily stats, competitor stats | An engine id. Repeat the parameter for several engines: `engine=chatgpt&engine=gemini`. |
| `topicId` | prompts, answers, daily stats | A topic id from the topics endpoint |
| `promptId` | answers | A prompt id from the prompts endpoint |
| `runId` | answers | A run id from the runs endpoint or a webhook event |
| `mentioned`, `cited` | answers | `true` or `false` |
| `status` | prompts, runs | Prompts: `active` or `paused`. Runs: `completed`, `running`, `failed` or `canceled`. |

On the answers endpoint, combine `engine` with at most one of `promptId`, `topicId` and `runId`. Other combinations answer `400 unsupported_filter_combination`.

## Pages

Lists return `data` and `nextCursor`:

```json
{ "data": [ ... ], "nextCursor": "eyJvIjoxMDB9" }
```

Pass `nextCursor` back as `cursor` to get the next page. `limit` is 50 by default and 200 at most. `nextCursor` is `null` on the last page. The cursor is opaque; do not build or parse it.

```python
def every_row(url, params=None):
    params = dict(params or {}, limit=200)
    while True:
        page = requests.get(url, headers=HEADERS, params=params, timeout=30).json()
        yield from page["data"]
        if not page["nextCursor"]:
            return
        params["cursor"] = page["nextCursor"]
```

Projects, topics, prompts, runs and answers are paged. Engines, competitors and webhooks return the whole list.

## Caching

- The answers list and the answer detail carry an `ETag`. Send it back in `If-None-Match` to get `304 Not Modified` when nothing changed. A `304` has no body and counts against the rate limit like any request, but it is fast and small.
- Daily stats carry `Cache-Control: private, max-age=60`. Hold the result for a minute before asking again.
- Everything else carries `Cache-Control: no-store`. Cache it on your side for as long as suits your dashboard.

## Time and dates

Times are UTC in RFC 3339 form, `2026-09-01T09:14:03.000Z`. Dates are `YYYY-MM-DD` and mean the UTC day. The `date` on an answer matches the `date` on the daily stats row it was counted in, so a chart and its drill-down agree.
