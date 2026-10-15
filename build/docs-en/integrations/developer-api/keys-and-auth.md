# Keys and authentication

## Create a key

1. Open Hi, Moose and sign in as the account owner. Only the owner can create, see and revoke keys.
2. Go to **Settings → Hi, Moose REST API**.
3. Give the key a label, pick the projects it may read (all, or one), choose when it expires, and tick the permissions it needs.
4. Click **Create key** and copy the key. It is shown once. Hi, Moose cannot show it again; if you lose it, revoke it and create a new one.

Keys look like `hmk_live_` followed by 64 characters. The table under the form lists every active key with its permissions and when it was created, last used and expires. **Revoke** stops a key at once.

Hi, Moose stores only a hash of the key, the same way passwords are stored, so nobody at Hi, Moose can read a key back either.

## One key per app

Create a separate key for each app or script, with a label that says what it is for. Then a key can be revoked without breaking anything else, and the **last used** column in Settings shows which app made the calls.

## Permissions

| Permission | What the key can do |
|---|---|
| Read visibility data | Every `GET` endpoint. Always on. |
| Manage tracking | Create projects, set brand terms and competitors, add, change and delete prompts, set engines and the schedule, register and delete webhooks. |
| Start runs | Start a visibility run. Runs spend the account's allowance on cloud engines, so give this only to a key that needs it. |

A call without the needed permission answers `403 insufficient_scope` and names the permission. Pick the permissions when you create the key; they cannot be changed afterwards. Make a new key instead.

In the API the permissions appear as `visibility:read`, `tracking:write` and `runs:execute`, for example in the answer from `GET /me`.

## Project access

A key reads either every project on the account or one project, chosen when the key is created. A project the key may not read answers `404 not_found`, the same as a project that does not exist, so a key cannot be used to find out which projects an account has.

## Authentication

Send the key as a Bearer token in the `Authorization` header on every request:

```bash
curl https://api.himoose.com/v1/me \
  -H "Authorization: Bearer hmk_live_..."
```

The answer names the key, its permissions and the project ids it can read. It is a good first call to check that a key works.

A request without a key, or with a malformed, revoked or expired key, answers `401` with one of these codes:

| Code | Meaning |
|---|---|
| `invalid_key` | No `Authorization` header, a key in the wrong form, or a key Hi, Moose does not know |
| `key_revoked` | The key was revoked in Settings |
| `key_expired` | The key passed its expiry date |

## Keep the key on your server

Use the key from your own server only. The API sends no CORS headers, so a web page cannot call it directly. A browser dashboard should call your backend, and your backend calls the API. That keeps the key out of the page and out of the browser's network log.

Store the key in an environment variable or a secrets manager, never in source control. If a key leaks, revoke it in Settings and create a new one. Revoking takes effect at once.

## Expiry

A key can expire after 30, 90 or 365 days, or never. An expiring key is the safer default for a script that will be replaced; a never-expiring key suits a long-lived dashboard whose key lives in a secrets manager. The Settings table shows each key's expiry date.
