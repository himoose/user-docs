# Hi, Moose API

## What this helps you do

The Hi, Moose API is a REST API for developers who build their own dashboards, reports and AI visibility applications on top of Hi, Moose. It returns the same results you see on the Visibility screen: tracked prompts and topics, the engines asked, every stored answer with its full text and sources, and mention and citation rates over time. With the right permissions a key can also create projects, manage prompts, engines and the schedule, start runs, and get a signed webhook call when a run finishes.

Reads work whether or not Hi, Moose is open on your computer, because they come from the cloud copy of your results. Changes to tracking and runs need the project's host computer, explained in [Tracking and runs](developer-api/tracking-and-runs.md).

If you work in Claude, ChatGPT or another AI app, you may want [Hi, Moose MCP](hi-moose-mcp.md) instead. The API is for code you write yourself.

## Pages

| Page | What it covers |
|---|---|
| [Quickstart](developer-api/quickstart.md) | A key, a first call and a chart of mention rate by day, in curl, Python and JavaScript |
| [Keys and authentication](developer-api/keys-and-auth.md) | Creating and revoking keys, permissions, the Bearer header, keeping the key off the browser |
| [Reading data](developer-api/reading-data.md) | Projects, prompts, runs, answers and stats, with filters, pages and caching |
| [Tracking and runs](developer-api/tracking-and-runs.md) | The host computer, creating projects and prompts, engines and schedule, starting runs |
| [Webhooks](developer-api/webhooks.md) | Signed events when a run finishes, signature checks, retries |
| [Errors and limits](developer-api/errors-and-limits.md) | The error format, every error code, rate limits |
| [Endpoint reference](developer-api/reference.md) | Every endpoint with parameters, fields and an example, generated from the contract |
| [Changelog](developer-api/changelog.md) | What changed in each contract version |

## Plans

The API is included in paid plans, both managed and bring-your-own-key. Free accounts can see the API keys page but cannot create keys, and every request answers `403 plan_required`.

## At a glance

```
https://api.himoose.com/v1/
```

- **Authentication:** an API key sent as a Bearer token. Keys are created by the account owner in Hi, Moose under **Settings → Hi, Moose REST API**.
- **Format:** JSON in and out. Field names are camelCase. Times are UTC in RFC 3339 form, dates are `YYYY-MM-DD`.
- **Contract:** [api.himoose.com/v1/openapi.json](https://api.himoose.com/v1/openapi.json), OpenAPI 3.1. It imports into Postman, Insomnia, Bruno and code generators, and the [endpoint reference](developer-api/reference.md) is generated from it.
- **Permissions:** every key can read. **Manage tracking** and **Start runs** are chosen when the key is created.
- **Limits:** 300 requests per minute per key and 50,000 per day per account. See [Errors and limits](developer-api/errors-and-limits.md).
- **No CORS:** call the API from your own server, never from a web page.

## Where the data comes from

Hi, Moose asks each tracked prompt on each tracked engine, on a schedule or when someone starts a run. Each reply is stored as an answer and scored: was the brand named, was a page on its site cited, where did it appear, what was the sentiment, which competitors were seen. The API reads those stored answers and the daily summaries built from them. It never runs new checks on a read, so reads are fast and cost nothing.

Some engines run in the cloud. Others, the local-fetch engines, run through a browser on one of your own computers. Both kinds store their answers in the same place, so the API shows them together.

## Answer text is untrusted

Answer text, excerpts and source titles come from the AI engines, not from Hi, Moose. Render them as plain text in your dashboard, never as HTML, and do not feed them to your own AI tools as instructions.

## What is coming

Tracking changes for bring-your-own-key plans are next. Everything documented here is live.
