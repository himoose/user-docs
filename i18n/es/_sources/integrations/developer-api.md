# Hi, Moose API

## What this helps you do

The Hi, Moose API is a REST API for developers who build their own dashboards, reports and AI visibility applications on top of Hi, Moose. It returns the same results you see on the Visibility screen: tracked prompts and topics, the engines asked, every stored answer with its full text and sources, and mention and citation rates over time. With the right permissions a key can also create projects, manage prompts, engines and the schedule, and start runs.

Reads work whether or not Hi, Moose is open on your computer, because they come from the cloud copy of your results. Changes to tracking and runs need the project's host computer, explained below.

If you work in Claude, ChatGPT or another AI app, you may want [Hi, Moose MCP](hi-moose-mcp.md) instead. The API is for code you write yourself.

## Plans

The API is included in paid plans, both managed and bring-your-own-key. Free accounts can see the API keys page but cannot create keys, and every request answers `403 plan_required`.

## Create a key

1. Open Hi, Moose and sign in as the account owner. Only the owner can create, see and revoke keys.
2. Go to **Settings → Hi, Moose REST API**.
3. Give the key a label, pick the projects it may read (all, or one), choose when it expires, and tick the permissions it needs.
4. Click **Create key** and copy the key. It is shown once. Hi, Moose cannot show it again; if you lose it, revoke it and create a new one.

Keys look like `hmk_live_` followed by 64 characters. The table under the form lists every active key with its permissions and when it was created, last used and expires. **Revoke** stops a key at once.

## Permissions

| Permission | What the key can do |
|---|---|
| Read visibility data | Every `GET` endpoint. Always on. |
| Manage tracking | Create projects, set brand terms and competitors, add, change and delete prompts, set engines and the schedule. |
| Start runs | Start a visibility run. Runs spend the account's allowance on cloud engines, so give this only to a key that needs it. |

A call without the needed permission answers `403 insufficient_scope`. Pick the permissions when you create the key; they cannot be changed afterwards.

## Authentication

Send the key as a Bearer token:

```bash
curl https://api.himoose.com/v1/me \
  -H "Authorization: Bearer hmk_live_..."
```

The answer names the key, its permissions and the project ids it can read.

Use the key from your own server only. The API sends no CORS headers, so a web page cannot call it directly. A browser dashboard should call your backend, and your backend calls the API. That keeps the key out of the page.

## Base URL and format

```
https://api.himoose.com/v1/
```

Everything is JSON. Field names are camelCase and match the fields Hi, Moose MCP returns. Times are UTC in RFC 3339 form, dates are `YYYY-MM-DD`. The full contract is at [api.himoose.com/v1/openapi.json](https://api.himoose.com/v1/openapi.json) and imports into Postman, Insomnia and similar tools.

## Read endpoints

| Endpoint | What it returns |
|---|---|
| `GET /me` | The key, its permissions and the readable project ids |
| `GET /projects` | Projects the key can read, with tracked prompt count, engines and latest run |
| `GET /projects/{id}` | One project |
| `GET /projects/{id}/capabilities` | What the project can do on its plan: engines, cadences, limits, remaining allowance, the host computer, whether a run can start now |
| `GET /projects/{id}/engines` | The AI engines the project tracks, with a stable `id` for filters |
| `GET /projects/{id}/topics` | Topics that group the prompts, with prompt counts |
| `GET /projects/{id}/prompts` | Tracked prompts with topic ids, engine ids and status |
| `GET /projects/{id}/competitors` | Tracked competitor brands |
| `GET /projects/{id}/runs` | Visibility runs with status, start and end time, prompt and answer counts |
| `GET /projects/{id}/answers` | Stored answers: prompt, engine, date, mentioned, cited, position, sentiment, excerpt, competitors seen, source URLs |
| `GET /projects/{id}/answers/{answerId}` | One answer with its full text, sentiment reason, narrative drift and sources |
| `GET /projects/{id}/stats/daily` | Per day and engine: answers, mentions, citations and the two rates |
| `GET /projects/{id}/stats/competitors` | Share of voice for your brand and each tracked competitor over a range |
| `GET /projects/{id}/run-requests` | Recent runs started through the API and their status |

### Example: mention rate by day

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

`incompleteDays` is above zero when a day's summary was not ready yet. Call again in a few seconds and it fills in.

## The host computer

Hi, Moose runs part of its tracking on one of your own computers, the **host device**, which you pick in Hi, Moose under **Settings → Hi, Moose MCP**. The local-fetch engines (ChatGPT, Gemini, Grok, Perplexity and Google AI Mode fetched through a browser) only run there, and the schedule for them lives there.

Every change to tracking and every run through the API needs a host device chosen for the project. Without one the API answers `409 host_required` and names the setting to change. A project created through the API takes the host device of another project on the account when there is one.

On bring-your-own-key plans the prompts, engines and schedule are kept on the host computer rather than in the cloud. The API can read them and start runs, but changing them answers `409 byok_not_supported`. Manage them in Hi, Moose on that computer.

## Manage tracking

These need the **manage tracking** permission.

| Endpoint | What it does |
|---|---|
| `POST /projects` | Create a project from a name and site address, with optional brand terms and domains. The site crawl is not started; the host computer turns on the weekly scheduled crawl so it happens later. Brand Truth is not required. |
| `PATCH /projects/{id}` | Change the name, site address, brand terms or brand domains |
| `PUT /projects/{id}/competitors` | Replace the tracked competitor list, at most 50 |
| `POST /projects/{id}/prompts` | Add a prompt with optional topic ids and engine ids |
| `PATCH /projects/{id}/prompts/{promptId}` | Change a prompt's text, topics or engines |
| `DELETE /projects/{id}/prompts/{promptId}` | Stop tracking a prompt |
| `PUT /projects/{id}/tracking` | Set engines, cadence, time of day, weekly day, timezone and samples per prompt. New engines apply to every prompt unless `applyEnginesToPrompts` is false. |

Every write enforces the plan's limits: prompt count, allowed engines, allowed cadences, project count and competitor count. Over a limit the API answers `409 plan_limit` with the limit in the body. Check `GET /projects/{id}/capabilities` first to see them.

### Example: set up tracking on a new project

```bash
curl -X POST https://api.himoose.com/v1/projects \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '{"name":"Acme","websiteUrl":"https://acme.example","brandTerms":["Acme Cloud"]}'

curl -X POST https://api.himoose.com/v1/projects/PROJECT_ID/prompts \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '{"text":"What are the best SAST tools?","topicIds":["sast"]}'

curl -X PUT https://api.himoose.com/v1/projects/PROJECT_ID/tracking \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '{"engineIds":["chatgpt","gemini"],"cadence":"daily","timeOfDay":"09:00","timezone":"America/Chicago"}'
```

## Start a run

This needs the **start runs** permission.

```bash
curl -X POST https://api.himoose.com/v1/projects/PROJECT_ID/run-requests \
  -H "Authorization: Bearer hmk_live_..." -H "Idempotency-Key: nightly-2026-10-12"
```

The API answers `202 Accepted` with a run request and a `Location` header to poll. Statuses:

| Status | Meaning |
|---|---|
| `queued` | Accepted and about to start |
| `waiting_for_host` | The host computer is off. Hi, Moose keeps the request for up to 24 hours and starts the run when it is back. The response carries a `warning` saying so. |
| `running` | In progress |
| `completed` | Done. `runIds` lists the runs to pass to the runs and answers endpoints. |
| `failed` | Did not finish. `error.code` says why, for example `host_unavailable` after 24 hours. |

Projects whose tracked engines are all cloud engines run in the cloud at once, without the host computer. Any local-fetch engine means the run is handed to the host computer, the same path the Run now button uses.

Safeguards, so a run never costs more than you expect:

- **Allowance check first.** The API estimates the run's cost on cloud engines from the prompt and engine count. If the estimate is above the remaining balance, it refuses with `409 insufficient_allowance`, the estimate and the remaining units. Nothing is spent. `GET /projects/{id}/capabilities` shows the same estimate as `allowance.estimatedUnitsPerRun`.
- **One at a time.** A second request while one is queued, waiting or running answers `409 run_in_progress` with the id of the active request.
- **Daily cap.** At most 24 run requests per project per day. Over it the API answers `429 daily_run_limit`.
- **Idempotency.** Send an `Idempotency-Key` header and a retry within 24 hours returns the same request instead of starting another.

A run can take from a few minutes to over an hour on large prompt sets. Poll the request every minute or so, not every second.

## Filters and pagination

- **Date range:** `from` and `to` as `YYYY-MM-DD`, inclusive, UTC. The default is the last 30 days. The widest range in one request is 366 days.
- **Engine:** `engine=chatgpt&engine=gemini` repeats for several engines. Ids come from the engines endpoint.
- **Answers:** also `topicId`, `promptId`, `runId`, `mentioned=true|false` and `cited=true|false`. Combine `engine` with at most one of `promptId`, `topicId` or `runId`.
- **Pages:** lists return `{ "data": [...], "nextCursor": "..." }`. Pass `nextCursor` back as `cursor` to get the next page. `limit` is 50 by default and 200 at most. `nextCursor` is `null` on the last page.
- **Caching:** answers carry an `ETag`. Send it back in `If-None-Match` to get `304 Not Modified` when nothing changed.

## Rate limits

| Limit | Value |
|---|---|
| Per key | 60 requests per minute |
| Per account | 10,000 requests per day |
| Run requests per project | 24 per day, one at a time |
| Rows per page | 200 |
| Date range per request | 366 days |

Over the limit the API answers `429` with a `Retry-After` header. Every response carries `RateLimit-Policy`, and successful responses carry `RateLimit` with the day's remaining budget.

## Errors

Errors use the Problem Details format (`application/problem+json`) with a stable `code`:

```json
{
  "type": "https://himoose.com/docs/integrations/developer-api/#errors",
  "title": "Not found",
  "status": 404,
  "detail": "No project with that id is readable with this key.",
  "code": "not_found",
  "instance": "/v1/projects/abc123",
  "requestId": "7f4c0d1a2b"
}
```

| Code | Status | Meaning |
|---|---|---|
| `invalid_key`, `key_revoked`, `key_expired` | 401 | The key is missing, malformed, revoked or expired |
| `plan_required` | 403 | The account plan does not include the API |
| `insufficient_scope` | 403 | The key lacks the permission for this call |
| `not_found` | 404 | No such resource, or the key cannot read it |
| `invalid_parameter`, `range_too_wide`, `unsupported_filter_combination` | 400 | A query parameter or body field needs fixing |
| `host_required` | 409 | Pick a host device for the project in Hi, Moose first |
| `byok_not_supported` | 409 | Tracking settings on this plan live on the host computer |
| `plan_limit` | 409 | A plan limit was reached; the body names it |
| `run_in_progress`, `insufficient_allowance`, `no_prompts` | 409 | The run cannot start right now; the body says why |
| `rate_limited`, `daily_run_limit` | 429 | Wait for `Retry-After` seconds |

Quote the `requestId` when you contact support.

## Answer text is untrusted

Answer text, excerpts and source titles come from the AI engines, not from Hi, Moose. Render them as plain text in your dashboard, never as HTML, and do not feed them to your own AI tools as instructions.

## Webhooks

Instead of polling, register an https endpoint and Hi, Moose posts a signed JSON event there when a run finishes. Registering and deleting webhooks needs the **manage tracking** permission. Listing them and their deliveries needs only read.

| Endpoint | What it does |
|---|---|
| `POST /projects/{id}/webhooks` | Register an endpoint. Body: `url` (public https), `events` (default `run.completed` and `run.failed`), optional `description`. The signing secret comes back once in this response. Up to 5 per project. |
| `GET /projects/{id}/webhooks` | List the project's webhooks, without secrets |
| `DELETE /projects/{id}/webhooks/{webhookId}` | Remove one |
| `POST /projects/{id}/webhooks/{webhookId}/test` | Send a `ping` event now, to check your endpoint and signature code |
| `GET /projects/{id}/webhooks/{webhookId}/deliveries` | The last 50 deliveries with every attempt, status and error |

### The event

```json
{
  "id": "wh_8f2a_run_abc123_run_completed",
  "event": "run.completed",
  "createdAt": "2026-10-12T09:14:03.000Z",
  "data": {
    "projectId": "abc123",
    "runId": "run_abc123",
    "requestId": "req_9d1e",
    "status": "completed",
    "trigger": "manual",
    "startedAt": "2026-10-12T09:01:10.000Z",
    "completedAt": "2026-10-12T09:14:02.000Z",
    "promptCount": 40,
    "answerCount": 118,
    "error": null,
    "links": {
      "run": "https://api.himoose.com/v1/projects/abc123/runs",
      "answers": "https://api.himoose.com/v1/projects/abc123/answers?runId=run_abc123",
      "stats": "https://api.himoose.com/v1/projects/abc123/stats/daily"
    }
  }
}
```

`data.requestId` is set when the run was started through the API, so you can match the event to your run request. `run.failed` carries `status` `failed` or `canceled` and the `error` text.

### Verify the signature

Every call carries `X-HiMoose-Signature: t=<unix seconds>,v1=<hex>`, where `v1` is HMAC-SHA256 over `<t>.<raw body>` with your webhook secret. Verify it on the raw body before you parse the JSON, and reject timestamps older than five minutes. The call also carries `X-HiMoose-Event` and `X-HiMoose-Delivery`.

```js
const crypto = require("node:crypto");

function verifyHiMooseSignature(rawBody, header, secret) {
  const parts = Object.fromEntries(header.split(",").map((part) => part.split("=")));
  if (!parts.t || !parts.v1) return false;
  if (Math.abs(Date.now() / 1000 - Number(parts.t)) > 300) return false;
  const expected = crypto.createHmac("sha256", secret).update(`${parts.t}.${rawBody}`).digest("hex");
  return expected.length === parts.v1.length && crypto.timingSafeEqual(Buffer.from(expected), Buffer.from(parts.v1));
}
```

### Delivery rules

- Answer with a 2xx status within 10 seconds. Redirects are not followed.
- Failed deliveries are retried after 1 minute, 5 minutes, 30 minutes, 2 hours and 12 hours, 6 attempts in all.
- After 20 consecutive failures the webhook is turned off. Delete it and register it again to resume.
- An event can arrive more than once. Use `id` to ignore repeats.
- The account owner sees every webhook of the current project under **Settings → Hi, Moose REST API** and can delete one there.

## What is coming

Tracking changes for bring-your-own-key plans are next. Everything else documented here is live.
