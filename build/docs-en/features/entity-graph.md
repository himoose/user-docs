# Entity Graph

## What this helps you do

An entity graph is the map of what your site is about: the people, products, places, organizations and topics your pages name, and how those things connect to each other.

It matters because answer engines don't read your site as a list of pages. They read it as a set of things and relationships. A site that clearly establishes "we are this company, we make these products, for these customers, in this category" gives an engine something to retrieve and cite. A site where that's implied but never stated gives it guesswork.

The entity graph shows you which of those things your site has already made clear, which are thin, and what an engine would come away believing.

Start it from **Tools → Create an entity graph**, or just ask for one in [chat](../chat/overview.md).

## Before you can build one

The graph is built from pages Hi, Moose has already crawled, so the project needs **a website and at least one completed crawl**. If there's no crawl yet, the intake card says so and links you to [Site Monitoring](../site-monitoring/overview.md) to run one.

The intake tells you what it's working from — how many crawled pages, and the date of the last completed crawl.

## Quick or Full

Two depths:

- **Quick** — structured data only. Reads the schema markup, metadata and page structure your site already publishes. Runs instantly, costs nothing.
- **Full** — everything Quick does, plus an AI pass that reads your top pages and names the entities that aren't marked up anywhere. Takes a few minutes.

On Full you choose how many top pages the AI pass may read. Larger runs take longer, and on managed plans the cloud model calls spend your monthly credits. The pass runs on whichever model is selected in chat's model menu, so pick the model first if you want a specific one — a loaded local model keeps the whole thing on your machine and free.

## What comes back

The graph reports:

- **Entities** — everything found, with its type, aliases, how many pages it appears on, and a **salience** score for how central it is to the site.
- **Relations** — how those entities connect, split three ways:
    - **Labeled** — a relationship your structured data or the AI pass states outright.
    - **Shared-page** — two entities that keep appearing on the same pages.
    - **Semantic** — two entities the language treats as related even where nothing links them.
- **Entities by type** — the breakdown, which is often the most useful single view. A site that sells software and shows forty people and three products has a story problem worth knowing about.

A **Top entities** table shows the most salient ones with their type, page count and salience. The full set exports as **CSV** or **PDF**; the on-screen table is capped, and it tells you how many more the exports contain.

## When the AI pass doesn't run

Full depth degrades rather than failing. If the AI pass can't run, you still get the graph from structured data, shared pages and semantic similarity, and the card tells you which case applied:

- **No model available** — load a local model or add an OpenRouter key, then rebuild at Full depth.
- **Nothing new to read** — every eligible page had already been analyzed on an earlier run.
- **The pass failed** — it couldn't complete.
- **Allowance ran out** — on managed plans the pass stops when your monthly credits do, and the graph includes everything analyzed up to that point.

## Moose can read it back

Once a graph exists, [chat](../chat/tools-and-specialists.md) can query it directly. Ask which entities your site is strongest on, what's connected to a particular product, or what's missing next to a topic you're trying to win, and Moose reads the graph rather than re-crawling or guessing.

[Send Moose](../send-moose/overview.md) reads it too, as part of the site intelligence it brings to a job.

## Where to go from here

- **[Site Monitoring](../site-monitoring/overview.md)** — the crawl the graph is built from.
- **[Content Briefs](content-briefs.md)** — turn a gap in the graph into a page.
- **[AEO Audits](aeo-audits.md)** — check whether an individual page states its entities clearly.
