# Webhooks

Instead of polling, register an https endpoint and Hi, Moose posts a signed JSON event there when a run finishes. Registering, testing and deleting webhooks needs the **manage tracking** permission. Listing them and their deliveries needs only read.

## Endpoints

| Endpoint | What it does |
|---|---|
| `POST /projects/{id}/webhooks` | Register an endpoint. Body: `url` (public https), `events` (default `run.completed` and `run.failed`), optional `description`. The signing secret comes back once in this response. Up to 5 per project. |
| `GET /projects/{id}/webhooks` | List the project's webhooks, without secrets |
| `DELETE /projects/{id}/webhooks/{webhookId}` | Remove one |
| `POST /projects/{id}/webhooks/{webhookId}/test` | Send a `ping` event now, to check your endpoint and signature code |
| `GET /projects/{id}/webhooks/{webhookId}/deliveries` | The last 50 deliveries with every attempt, status and error |

## Register one

```bash
curl -X POST https://api.himoose.com/v1/projects/PROJECT_ID/webhooks \
  -H "Authorization: Bearer hmk_live_..." -H "Content-Type: application/json" \
  -d '{"url":"https://reports.acme.example/himoose","description":"Nightly dashboard refresh"}'
```

```json
{
  "id": "BGXhe1dlOnmy36j6rRTa",
  "url": "https://reports.acme.example/himoose",
  "events": ["run.completed", "run.failed"],
  "description": "Nightly dashboard refresh",
  "active": true,
  "createdAt": "2026-10-15T03:20:10.000Z",
  "secret": "whsec_..."
}
```

Store `secret` next to your key. It is shown only in this response. The URL must be public and use https; private addresses, localhost and plain http are refused with `400 invalid_parameter`.

Then send yourself a ping:

```bash
curl -X POST https://api.himoose.com/v1/projects/PROJECT_ID/webhooks/WEBHOOK_ID/test \
  -H "Authorization: Bearer hmk_live_..."
```

The response is the delivery record, and the deliveries endpoint shows the attempt with the HTTP status your endpoint answered.

## The event

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

| Event | When |
|---|---|
| `run.completed` | A run finished and its answers are stored. Scheduled runs, runs from the Run now button and runs from the API all count. |
| `run.failed` | A run ended with `status` `failed` or `canceled`. `data.error` says why. |
| `ping` | Sent by the test endpoint. `data` carries the project id and a message. |

`data.requestId` is set when the run was started through the API, so you can match the event to your run request. It is `null` for scheduled runs and runs started in Hi, Moose.

The event is a signal, not the data. On `run.completed`, follow `data.links.answers` or refresh your daily stats. Daily summaries for the run's days are rebuilt within ten minutes of the run finishing; `incompleteDays` on the stats response says when they are not ready yet.

## Headers

| Header | Value |
|---|---|
| `X-HiMoose-Signature` | `t=<unix seconds>,v1=<hex>`, see below |
| `X-HiMoose-Event` | The event name |
| `X-HiMoose-Delivery` | The delivery id, the same as on the deliveries endpoint |
| `User-Agent` | `HiMoose-Webhooks/1.0` |
| `Content-Type` | `application/json` |

## Verify the signature

`v1` is HMAC-SHA256 over `<t>.<raw body>` with your webhook secret, as a lowercase hex string. Verify it on the raw request body before you parse the JSON, compare in constant time, and reject timestamps older than five minutes.

=== "JavaScript"

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

=== "Python"

    ```python
    import hashlib
    import hmac
    import time

    def verify_himoose_signature(raw_body: bytes, header: str, secret: str) -> bool:
        parts = dict(part.split("=", 1) for part in header.split(",") if "=" in part)
        if "t" not in parts or "v1" not in parts:
            return False
        if abs(time.time() - int(parts["t"])) > 300:
            return False
        expected = hmac.new(secret.encode(), f"{parts['t']}.".encode() + raw_body, hashlib.sha256).hexdigest()
        return hmac.compare_digest(expected, parts["v1"])
    ```

Most web frameworks parse JSON before your code runs. Make sure you sign the bytes as received, not a re-serialised copy, or the signature will not match.

## Delivery rules

- Answer with a 2xx status within 10 seconds. Do the work after answering, not before. Redirects are not followed.
- Failed deliveries are retried after 1 minute, 5 minutes, 30 minutes, 2 hours and 12 hours, 6 attempts in all. A delivery is `pending` while retries remain, `delivered` after a 2xx, `failed` after the last attempt.
- After 20 consecutive failures the webhook is turned off, `active` becomes false, and no more events are sent. Delete it and register it again to resume.
- An event can arrive more than once. Use `id` to ignore repeats.
- Events for one project may arrive out of order when a retry is involved. Use `createdAt` if order matters.

## Seeing deliveries

```bash
curl https://api.himoose.com/v1/projects/PROJECT_ID/webhooks/WEBHOOK_ID/deliveries \
  -H "Authorization: Bearer hmk_live_..."
```

Each delivery lists every attempt with its time, the HTTP status your endpoint answered, how long it took and any error. When an endpoint misbehaves this is the first place to look.

The account owner sees every webhook of the current project under **Settings → Hi, Moose REST API** with its last delivery status, and can delete one there.
