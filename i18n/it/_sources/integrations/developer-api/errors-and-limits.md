# Errors and limits

## Errors

Errors use the Problem Details format (`application/problem+json`, RFC 9457) with a stable `code` you can branch on:

```json
{
  "type": "https://himoose.com/docs/integrations/developer-api/errors-and-limits/#errors",
  "title": "Not found",
  "status": 404,
  "detail": "No project with that id is readable with this key.",
  "code": "not_found",
  "instance": "/v1/projects/abc123",
  "requestId": "7f4c0d1a2b"
}
```

- `code` is the field to test in code. It never changes meaning.
- `detail` is written for a person and may change wording.
- `type` links to the docs section for that kind of error.
- `requestId` identifies the request. Quote it when you contact support. It is also sent as the `X-Request-Id` header on every response.

Some errors carry extra fields, named in the table.

## Error codes

| Code | Status | Meaning | What to do |
|---|---|---|---|
| `invalid_key` | 401 | No `Authorization` header, a key in the wrong form, or a key Hi, Moose does not know | Send `Authorization: Bearer hmk_live_...`. Check the key was copied in full. |
| `key_revoked` | 401 | The key was revoked in Settings | Create a new key. |
| `key_expired` | 401 | The key passed its expiry date | Create a new key. |
| `plan_required` | 403 | The account plan does not include the API | Upgrade to a paid plan. |
| `insufficient_scope` | 403 | The key lacks the permission for this call. The body names it in `scope`. | Create a key with that permission. |
| `not_found` | 404 | No such resource, or the key cannot read it. The two cases are not told apart. | Check the id and the key's project access. |
| `method_not_allowed` | 405 | The endpoint exists but not with this method | See the [reference](reference.md). |
| `invalid_parameter` | 400 | A query parameter or body field is missing, malformed or out of range. `detail` names it. | Fix the request. |
| `range_too_wide` | 400 | `from` to `to` spans more than 366 days | Ask for a narrower range. |
| `unsupported_filter_combination` | 400 | Filters that cannot be combined, for example `engine` with two of `promptId`, `topicId` and `runId` | Drop one filter. |
| `host_required` | 409 | The project has no host computer chosen | Pick one in Hi, Moose under **Settings → Hi, Moose MCP**. |
| `byok_not_supported` | 409 | On this plan tracking settings live on the host computer, so the API cannot change them | Change them in Hi, Moose on that computer. |
| `plan_limit` | 409 | A plan limit was reached. The body carries `limit`. | Check `GET /projects/{id}/capabilities` for the limits. |
| `run_in_progress` | 409 | A run request is already queued, waiting or running. The body carries `requestId` and `requestStatus`. | Wait for it to finish. |
| `insufficient_allowance` | 409 | The run would cost more than the remaining allowance. The body carries `estimatedUnits`, `remainingUnits` and `periodEndsAt`. | Top up, or reduce prompts, engines or samples. |
| `no_prompts` | 409 | The project has no tracked prompt with an engine | Add prompts and engines first. |
| `rate_limited` | 429 | The per-minute or per-day limit was reached | Wait for `Retry-After` seconds. |
| `daily_run_limit` | 429 | The project made its 24 run requests for today | Try tomorrow. |
| `internal` | 500 | Something failed on the Hi, Moose side | Retry with backoff. If it persists, contact support with the `requestId`. |

A `502` or `503` without a body means the API could not reach its backend. Retry with backoff.

## Rate limits

| Limit | Value |
|---|---|
| Per key | 300 requests per minute |
| Per account | 50,000 requests per day |
| Run requests per project | 24 per day, one at a time |
| Webhooks per project | 5 |
| Rows per page | 200 |
| Date range per request | 366 days |

Over the limit the API answers `429 rate_limited` with a `Retry-After` header. Every response carries `RateLimit-Policy`, and successful responses carry `RateLimit` with the day's remaining budget, following the IETF rate limit headers draft:

```
RateLimit-Policy: "per-minute";q=300;w=60, "per-day";q=50000;w=86400
RateLimit: "per-day";r=49871;t=61234
```

The per-minute limit is counted per key at the edge and is approximate; a short burst a little above it may pass. The per-day limit is counted per account across all its keys.

## Staying under the limits

- **Cache on your side.** Daily stats carry `Cache-Control: max-age=60`. A dashboard that refreshes every minute reads the summary once per minute per chart, not once per viewer.
- **Use the summaries.** Daily stats and competitor stats are built from a summary table. Draw charts from them, and read individual answers only when someone opens a row.
- **Use ETags.** Answers carry an `ETag`. Send it back in `If-None-Match` and a `304` costs almost nothing.
- **Use webhooks** instead of polling for a run to finish. See [Webhooks](webhooks.md).
- **Back off on 429.** Sleep for `Retry-After` seconds, then retry. Do not retry at once.

## Request ids

Every response carries `X-Request-Id`. Log it next to your own request log so that a problem report can be matched to the Hi, Moose logs. Error bodies repeat it as `requestId`.
