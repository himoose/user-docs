# Site Monitoring

## What this helps you do

Hi, Moose keeps a local picture of your website: which pages exist, what's on them, and what changed since last time. That picture powers four things — AEO-relevant change alerts in your [inbox](../inbox/overview.md), the semantic search index Moose uses to answer questions about your own site, the page inventory that [audits](../features/aeo-audits.md) and [briefs](../features/content-briefs.md) draw on, and the [entity graph](../features/entity-graph.md) that maps what your site is about.

Everything here lives in **Settings → Site Monitoring**, scoped to the current project.

## The scheduled crawl

Turn on **Run weekly site crawl** and Hi, Moose refreshes monitored pages on a weekly cadence, notifying you when meaningful changes turn up. Pick the day and hour in your local time.

Manual crawls stay available either way. **Run crawl now** starts a full crawl immediately, with progress in the status bar at the bottom of the window. You can **Pause**, **Resume**, or **Stop** a running crawl, and pages found so far are kept rather than discarded.

Large sites take a few minutes.

### The crawler sets its own pace

Every site has a speed it's comfortable being read at, and it's different for a static site on a CDN and a database-backed store on shared hosting. Hi, Moose doesn't guess it from a setting — it finds it.

The crawl starts gently, speeds up while pages keep coming back quickly, and eases off the moment the site shows strain: a slowdown in response times, or a rate-limit or server-busy response. When that happens the status bar says **Slowing down to match the site**, and the crawl keeps going at the slower pace rather than hammering the server or giving up.

The practical effect is that inventories come back complete. A crawl that gets rate-limited halfway through used to return a partial picture of your site, which then made everything built on top of it — the search index, audits, briefs — partial too.

You don't have to configure any of this.

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

Monitored pages are locked to the project's own domain. Subdomains of it are fine; an unrelated domain is rejected, so one project's monitoring can't quietly fill up with someone else's pages.

## Blocked paths

Crawls skip blocked paths and everything under them, and matching pages are removed from monitoring.

Matching is by path segment prefix. Blocking `/results/` covers `/results/` and every sub-path under it, but **not** `/results-archive/` — the segment has to match, not just the string.

This is the right tool for search result pages, filtered listing pages, paginated archives, and anything else that generates a large number of near-identical URLs you'd rather not crawl, index, or get alerted about.

## How old is each page?

While it crawls, Hi, Moose reads the publication and last-modified dates your pages declare — in their structured data, their metadata, and their `<time>` elements — and records them alongside the page.

This matters because freshness is one of the things answer engines weigh when deciding which source to trust on a question that has a current answer. A page that says nothing about when it was written can't make that case. Your [AEO audits](../features/aeo-audits.md) use these dates in their freshness scoring, which is where you'll see the result of it.

If a page declares no date anywhere, that's itself a finding worth acting on.

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
