!!! info "Not translated yet"
    This page is not available in your language yet, so it is shown in English.

# Site Monitoring

## What this helps you do

Hi, Moose keeps a local picture of your website: which pages exist, what's on them, and what changed since last time. That picture powers three things — AEO-relevant change alerts in your [inbox](../inbox/overview.md), the semantic search index Moose uses to answer questions about your own site, and the page inventory that [audits](../features/aeo-audits.md) and [briefs](../features/content-briefs.md) draw on.

Everything here lives in **Settings → Site Monitoring**, scoped to the current project.

## The scheduled crawl

Turn on **Run weekly site crawl** and Hi, Moose refreshes monitored pages on a weekly cadence, notifying you when meaningful changes turn up. Pick the day and hour in your local time.

Manual crawls stay available either way. **Run crawl now** starts a full crawl immediately, with progress in the status bar at the bottom of the window. You can **Stop** a running crawl, and pages found so far are kept rather than discarded.

Large sites take a few minutes.

## The search index

Below the crawl controls is the **Search index** — the local semantic index Moose uses to answer questions about your site's pages. It reports how many pages are indexed, how many passages those pages produced, and when it last updated.

Indexing is passage-level, not page-level. A long page becomes many separately searchable passages, which is why Moose can quote a specific paragraph rather than telling you a page is "generally about" something.

- **Rebuild index** re-indexes from scratch.
- If pages are new or changed since the last index update, Hi, Moose tells you how many. They'll be indexed on the next crawl, or you can rebuild now.

!!! note "The index is honest about what it doesn't have"
    If you ask Moose about a page that hasn't been indexed, it says so and points you at running a crawl rather than guessing from the page's URL.

## Monitored pages

The pages Hi, Moose checks for AEO-relevant changes. Pages found by site discovery, [Google Search Console](../integrations/google-search-console.md), and [visibility runs](../visibility/overview.md) show up here automatically.

You can also add pages by hand with a full URL, search and filter the list, page through it, and remove pages you don't care about.

## Blocked paths

Crawls skip blocked paths and everything under them, and matching pages are removed from monitoring.

Matching is by path segment prefix. Blocking `/results/` covers `/results/` and every sub-path under it, but **not** `/results-archive/` — the segment has to match, not just the string.

This is the right tool for search result pages, filtered listing pages, paginated archives, and anything else that generates a large number of near-identical URLs you'd rather not crawl, index, or get alerted about.

## What lands in your inbox

A crawl produces **one digest item per run**, not one item per changed page. The digest opens into a table of changed pages with what changed, an impact rating, and per-page actions.

Impact levels are **Critical**, **Notable**, **Low**, **Unreachable**, and **Not reviewed**.

Two controls shape the noise:

- **Include informational AEO changes** — off by default. When on, low-impact changes also produce inbox items.
- **OS notification minimum severity** — only inbox items at or above this level pop a desktop notification. Set it to Info if you want low-impact changes surfaced at the OS level too.

## Ask Moose about what changed

The digest has an **Ask Moose about all of this** action that hands the whole crawl snapshot to chat and asks what matters most and what to do first. Individual pages have their own **Ask Moose** action that passes just that page's recorded change.

Both are constrained to the recorded snapshot. If the snapshot doesn't say why something changed, Moose is instructed to say so rather than invent a reason.

## Unreachable pages

If a page or the whole site can't be reached, that's reported as its own change type rather than being silently dropped. A site-wide outage produces a single **Site unreachable** item instead of one alert per page.
