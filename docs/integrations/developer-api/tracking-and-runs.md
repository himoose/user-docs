# Tracking and runs

Changing what Hi, Moose tracks needs the **manage tracking** permission. Starting a run needs the **start runs** permission. Both are chosen when the key is created, see [Keys and authentication](keys-and-auth.md#permissions).

## The host computer

Hi, Moose runs part of its tracking on one of your own computers, the **host device**, which you pick in Hi, Moose under **Settings → Hi, Moose MCP**. The local-fetch engines (ChatGPT, Gemini, Grok, Perplexity and Google AI Mode fetched through a browser) only run there, and the schedule for them lives there.

Every change to tracking and every run through the API needs a host device chosen for the project. Without one the API answers `409 host_required` and names the setting to change. A project created through the API takes the host device of another project on the account when there is one.

After a tracking change the API hands the host computer a short job to pick up the new settings. The host does that within a minute while Hi, Moose is open there, or when it next opens. Reads show the new settings at once either way.

On bring-your-own-key plans the prompts, engines and schedule are kept on the host computer rather than in the cloud. The API can read them and start runs, but changing them answers `409 byok_not_supported`. Manage them in Hi, Moose on that computer.

`GET /projects/{id}/capabilities` tells you before you write: the plan, the allowed engines and cadences, the limits, the host computer and whether it is online, and whether a run could start now.

## Manage tracking

| Endpoint | What it does |
|---|---|
| `POST /projects` | Create a project from a name and site address, with optional brand terms and domains. The site crawl is not started; the host computer turns on the weekly scheduled crawl so it happens later. Brand Truth is not required. |
| `PATCH /projects/{id}` | Change the name, site address, brand terms or brand domains |
| `PUT /projects/{id}/competitors` | Replace the tracked competitor list, at most 50 |
| `POST /projects/{id}/prompts` | Add a prompt with optional topic ids and engine ids |
| `PATCH /projects/{id}/prompts/{promptId}` | Change a prompt's text, topics or engines, or resume a paused one |
| `DELETE /projects/{id}/prompts/{promptId}` | Stop tracking a prompt. Its stored answers are kept. |
| `PUT /projects/{id}/tracking` | Set the default engines, cadence, time of day, weekly day, timezone and samples per prompt |

Every write enforces the plan's limits: prompt count, allowed engines, allowed cadences, project count and competitor count. Over a limit the API answers `409 plan_limit` with the limit in the body.

### Engines on prompts

Each prompt has its own list of engines. `PUT /projects/{id}/tracking` with `engineIds` sets the default for prompts added later and leaves every existing prompt as it is. To change the engines on existing prompts, either send `applyEnginesToPrompts: true` in the same call, which sets the new list on every prompt in the project, or change prompts one at a time with `PATCH /projects/{id}/prompts/{promptId}`.

A prompt with no engines is kept but skipped in runs. `POST /projects/{id}/prompts` without `engineIds` gives the new prompt the project's default engines.

### Replace means replace

`PUT /projects/{id}/competitors` replaces the whole list. Send the full list you want to keep, not just the additions. An empty list removes every competitor. The same goes for `brandTerms` and `brandDomains` on `PATCH /projects/{id}`.

### Example: set up tracking on a new project

```bash
curl -X POST https://api.himoose.com/v1/projects \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '{"name":"Acme","websiteUrl":"https://acme.example","brandTerms":["Acme Cloud"]}'

curl -X PUT https://api.himoose.com/v1/projects/PROJECT_ID/tracking \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '{"engineIds":["chatgpt","gemini"],"cadence":"daily","timeOfDay":"09:00","timezone":"America/Chicago"}'

curl -X POST https://api.himoose.com/v1/projects/PROJECT_ID/prompts \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '{"text":"What are the best SAST tools?","topicIds":["sast"]}'

curl -X PUT https://api.himoose.com/v1/projects/PROJECT_ID/competitors \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '[{"name":"Competitor One","domain":"competitor-one.example"},{"name":"Competitor Two","domain":"competitor-two.example"}]'
```

Setting the engines before adding prompts means each new prompt gets them as its default.

### Schedule

| Field | Values |
|---|---|
| `cadence` | `manual` (schedule off), `daily`, `weekdays`, `weekly` |
| `timeOfDay` | `HH:MM` in the project timezone |
| `weeklyDay` | `monday` to `sunday`, used by `weekly` |
| `timezone` | An IANA name such as `Europe/Berlin` |
| `samplesPerPrompt` | How many times each prompt is asked per engine in a run. More samples cost more allowance. |

The plan decides which cadences are allowed; the capabilities endpoint lists them.

## Start a run

```bash
curl -X POST https://api.himoose.com/v1/projects/PROJECT_ID/run-requests \
  -H "Authorization: Bearer hmk_live_..." -H "Idempotency-Key: nightly-2026-10-12"
```

The API answers `202 Accepted` with a run request and a `Location` header to poll:

```json
{
  "id": "NKxlhmW52Pkc2QwVD4oP",
  "status": "queued",
  "mode": "host",
  "createdAt": "2026-10-15T03:39:56.404Z",
  "updatedAt": "2026-10-15T03:39:56.404Z",
  "completedAt": null,
  "runIds": [],
  "promptCount": 5,
  "estimatedUnits": 0,
  "warning": null,
  "error": null,
  "host": { "online": true, "lastSeenAt": "2026-10-15T03:39:20.475Z" }
}
```

| Status | Meaning |
|---|---|
| `queued` | Accepted and about to start |
| `waiting_for_host` | The host computer is off. Hi, Moose keeps the request for up to 24 hours and starts the run when it is back. The response carries a `warning` saying so. |
| `running` | In progress |
| `completed` | Done. `runIds` lists the runs to pass to the runs and answers endpoints. |
| `failed` | Did not finish. `error.code` says why, for example `host_unavailable` after 24 hours. |
| `canceled` | Stopped from Hi, Moose before it finished |

`mode` says where the run runs. Projects whose tracked engines are all cloud engines run in the cloud at once, without the host computer. Any local-fetch engine means the run is handed to the host computer, the same path the Run now button uses. Either way the project needs a host computer chosen.

### Safeguards

So a run never costs more than you expect:

- **Allowance check first.** The API estimates the run's cost on cloud engines from the prompt and engine count. If the estimate is above the remaining balance, it refuses with `409 insufficient_allowance`, the estimate and the remaining units. Nothing is spent. `GET /projects/{id}/capabilities` shows the same estimate as `allowance.estimatedUnitsPerRun`.
- **One at a time.** A second request while one is queued, waiting or running answers `409 run_in_progress` with the id of the active request.
- **Daily cap.** At most 24 run requests per project per day. Over it the API answers `429 daily_run_limit`.
- **Idempotency.** Send an `Idempotency-Key` header and a retry within 24 hours returns the same request with `200` and `replayed: true` instead of starting another run.
- **Something to run.** A project with no prompt that has an engine answers `409 no_prompts`.

### Following a run

Poll `GET /projects/{id}/run-requests/{requestId}` about once a minute. A run can take from a few minutes to over an hour on large prompt sets. Once `status` is `completed`, `runIds` has the run to read:

```bash
curl "https://api.himoose.com/v1/projects/PROJECT_ID/answers?runId=RUN_ID" \
  -H "Authorization: Bearer hmk_live_..."
```

To avoid polling, register a [webhook](webhooks.md). The `run.completed` event carries `requestId`, so you can match it to the request you made.

Runs started through the API appear in Hi, Moose like any other run, and in the **Recent agent jobs** table under **Settings → Hi, Moose MCP** with the key's label.
