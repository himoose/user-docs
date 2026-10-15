# Changelog

The contract version is in `info.version` of [openapi.json](https://api.himoose.com/v1/openapi.json) and in the heading of the [endpoint reference](reference.md). The base URL stays `/v1` for every version listed here; a breaking change would get a new base URL and a long notice.

## 1.2.1, 2026-10-15

First public release.

- **Reading:** projects, engines, topics, prompts, competitors, runs, answers with full text, daily stats, competitor stats and capabilities.
- **Managing tracking:** create and change projects, replace competitors, add, change and delete prompts, set engines and the schedule.
- **Runs:** start a run with an allowance check, one at a time, 24 per day, with idempotency keys and a status to poll.
- **Webhooks:** `run.completed` and `run.failed` events with HMAC signatures, retries and a deliveries log.
- **Limits:** 300 requests per minute per key, 50,000 per day per account.
- `PUT /projects/{id}/tracking` with `engineIds` changes the default engines only. Existing prompts keep their engines unless `applyEnginesToPrompts` is `true`.

## Planned

- Tracking changes on bring-your-own-key plans, whose settings live on the host computer today.
- Opportunities, the ranked work queue from the Opportunities tab.
