# Second-turn Queries

## What this helps you do

AI engines often end an answer by inviting the next question. A second-turn query is that next question, written out in full so that it makes sense on its own. Hi, Moose captures these queries during visibility runs and lists them in the **Second-turn Queries** tab, together with how often each one came up and whether your site covers it.

For example, an engine might end an answer with "Want me to compare these two side by side?" The second-turn query is what a person would type to accept, such as "Compare standing desk converters and full standing desks for a small home office".

## Turning it on

Open [Visibility Settings](settings.md#second-turn-queries) and go to the **Second-turn queries** section. Turn on **Capture second-turn queries**. The setting is off by default, and you turn it on for each project separately.

While the setting is off, nothing is captured and the Second-turn Queries tab is hidden.

You can turn the setting on with paid managed plans, BYOK Premium and BYOK Agency. On Preview Mode and BYOK Free the toggle is greyed out and shows the note **Available on paid plans**.

Turning it on adds one small model call for each answer in a run. On paid managed plans these calls count against your plan's allowance. On BYOK Premium and BYOK Agency they are charged to your OpenRouter key.

## The Second-turn Queries tab

The tab sits right after **Opportunities** in the Visibility dashboard. It appears only when the setting is on. It stays empty until the first visibility run after you turn the setting on, because answers from earlier runs are not processed.

The tab follows the period and filters selected at the top of Visibility. A query is listed when an answer in that period contained it.

### Views

- **Most frequent** is the default view. It shows one list ranked by the number of answers that contained each query.
- **By prompt** groups the queries under the tracked prompt that each one followed.

### What a row shows

- The query.
- **Answers with this query: N**, where N is the number of answers that contained it.
- The engines and the topic.
- The [site coverage](#site-coverage) result.
- **Show details**, which lists the prompts the query followed under **Asked after these prompts**, with a **View answer** link for each prompt. It also shows the engine's closing words.

## How new queries are sorted

The first time a new query appears, Hi, Moose checks whether it is specific and on topic enough to track. It also checks whether the query means the same as one that is already listed. Queries that mean the same thing are counted together. Generic ones, such as "tell me more", are left out.

This sorting happens when you open the tab. The first time you open it after a run, the tab shows **Sorting new queries: X of Y**.

## Site coverage

Each query is checked once against the crawled pages of your project's site. The row then shows one of these results:

- **Covered on your site:** followed by the page.
- **Partly covered on your site:** followed by the page.
- **Not covered on your site**.

Coverage is checked again after a new site crawl finishes.

The check needs a completed site crawl on your device, or on the device that hosts the site index. Without a completed crawl, the row shows **Site coverage not checked**. In the web app with no desktop host, coverage is not checked.

## Buttons on each row

- **Add to tracked prompts** adds the query as a tracked prompt under the same topic as the prompt it followed. The button then reads **Tracked**.
- **Create a draft** is shown when your site does not cover the query. It opens a new chat with the [content brief](../features/content-briefs.md) intake filled in.
- **Refresh this page** is shown when your site partly covers the query. It opens the content refresh intake for that page with the query as the target.
- **Dismiss** hides the row. **Show dismissed** brings the dismissed rows back into view, and **Restore** returns a row to the list.

## When the list updates

New queries are captured from each answer during every visibility run while the setting is on. They are sorted the next time you open the tab.

Because the tab follows the selected period, a query is no longer listed when no answer in that period contained it. Choose a longer period to see it again.

## Teams and plans

On paid managed plans, the captured queries, dismissals and coverage results sync to the cloud, so team members see the same list. On BYOK Premium and BYOK Agency, everything stays on your device.

## What is not included

- Perplexity's "Related" questions and Google's "People also ask" questions are not captured.
- Second-turn queries are not part of the [PDF executive report](overview.md#exporting).
- Second-turn queries are not available through the [Hi, Moose MCP](../integrations/hi-moose-mcp.md) tools.
