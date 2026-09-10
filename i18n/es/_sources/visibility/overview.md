# Visibility

## What this helps you do

The Visibility dashboard shows how your brand actually performs in AI search: the queries customers use to find you, whether your brand gets shortlisted, and whether AI engines describe it accurately. This is the primary view for the [core operator loop](../index.md#the-core-operator-loop)'s **monitor** and **detect** steps.

The dashboard has six tabs:

| Tab | What it answers |
|---|---|
| **Overview** | How am I doing? |
| **[Competition](competitors.md)** | How am I doing compared to them? |
| **Mentions** | Which brands get named in these answers? |
| **Citations** | Which sources do the engines lean on? |
| **Topics & Engines** | Where specifically am I strong or weak? |
| **Prompts** | What happened on each individual prompt? |

## Metrics

Each run reports headline metrics for the selected period:

- **Share of Mentions** — how often your brand is mentioned across tracked prompts and engines.
- **Share of Citations** — how often your domain is actually cited as a source.
- **Sentiment** — the average tone (positive, mixed, neutral, negative) of mentions.
- **Avg Position** — where your brand tends to land when it appears in a list or ranking. Shows **Not enough data** until there are enough positioned mentions to average.
- **Narrative Drift** — whether AI responses are drifting from your intended positioning.
- **Feature Parity** — whether AI responses accurately represent what you actually offer.

Narrative Drift and Feature Parity show **Not scored** with a **Configure brand truth profile** link until you've filled in your [Brand Truth Profile](../getting-started/context/brand-truth-profile.md). These two are only meaningful once Hi, Moose knows what's actually true about your brand to compare against.

!!! note "Failed observations are excluded, not counted as absences"
    If an engine was unavailable or a request failed, that observation is left out of every metric rather than being scored as "your brand wasn't mentioned." A run with connection problems will report on fewer observations rather than reporting a false drop. The prompt-level view labels these as **Response unavailable** and shows how many were excluded.

## Filtering and time range

- Filter by **Topic**, **AI Engine**, **Prompt** (searchable multi-select), **Page**, **Sentiment**, **Narrative**, or **Feature Parity**, or clear all filters at once.
- The **Page** filter narrows to specific URLs, searchable by path. It correctly surfaces engines where the URL was *not* cited, so you can see where a page is missing as well as where it's landing.
- Set a **Period** date range and click **Apply**, or click **Compare** to overlay a prior period or the previous run.

## Trend over Time

The trend chart plots **Mentions**, **Citations**, **Positive %**, or **Avg Position** over **Day**, **Week**, or **Month** buckets, broken out per AI engine or **All models** combined, so you can see whether one engine is moving the numbers.

## Prompt-level detail

Below the chart:

- **Mention Rate** breaks results out per engine, showing which engines mentioned you and which didn't.
- **Top Cited Pages** shows which of your URLs are getting cited, and by which engines.
- **Prompt-Level Breakdown** expands any tracked prompt to see individual run results per engine, including the full AI response and the sentiment, narrative, and feature-parity reasoning.

Each prompt has an **investigate in chat** link that hands the exact observation data to Moose and asks it to recommend whether the next step is an [AEO audit](../features/aeo-audits.md) of an existing page or a new [content brief and draft](../features/content-briefs.md).

## The Overview tab

The Overview opens with a written summary of the current cut — a few paragraphs that say where you stand, what moved, and what's worth looking at, in sentences rather than numbers. It's generated from the same fact sheet the report uses, and you can **Rewrite the summary** if you want it re-drafted. When no model is available to write it, Overview falls back to a version built straight from the numbers and says so.

Underneath the summary are two blocks:

- **Where you stand** — your Share of Voice, mention rate across the answers that were read, citations, average rank when you're named, and mention rate by engine, with the full field of tracked brands beside you.
- **Is AI describing you accurately?** — positioning alignment, tone breakdown, and a list of **answers worth a review**: the specific responses where an engine misstated a capability or drifted from your positioning. Each one opens the answer or jumps to it in the Prompts tab.

## Mentions

The **Mentions** tab is the full list of every brand, product, or website the engines named in the answers in your current cut — not just you and your tracked competitors, but everyone who showed up.

Each row shows how many prompt responses named the brand, that as a percentage of the responses in the cut, the brand's share of all mentions, its average position among the brands named in an answer, and its most common sentiment verdict. Hover any sentiment value for the positive/mixed/neutral/negative breakdown, and hover a column heading for its exact definition.

A **mention presence trend** above the table plots the most-mentioned brands, and you, over time.

This is where you find the competitors you didn't know you had. Brands are read out of the answer text by the scoring model, so the list surfaces names you never added to your tracking.

## Citations

The **Citations** tab is the same idea for sources: every domain or page the engines cited in the current cut.

Switch between **By domain** and **By page URL**, and filter to **All** or **Not you or a competitor** to see the third-party sources shaping the answers. Every source is categorized — your brand, competitor, social, review site, publication, reference, developer, or other.

The columns are:

| Column | What it means |
|---|---|
| **Prompts cited** | How many prompt responses cited this domain or URL |
| **Presence %** | That as a share of the responses in the cut |
| **Citations count** | Total times it was cited, counting repeats |
| **Visibility %** | Its share of all citations in the cut |
| **Avg. rank** | Its average position in the engines' citation lists |
| **Change** | Movement against the comparison period or previous run |

**Details** on any row lists the pages behind it and the prompts each page was cited for. Any domain in the table can be added straight to your tracked competitors with **Track as competitor**, so a name you discover here goes into [Share of Voice](competitors.md) without retyping it.

Both tables download as CSV.

!!! note "Engines that don't browse return no citations"
    Citations come from engines that fetch the web while answering. A local model, or an engine answering from its own weights, returns none — so an empty table under a narrow filter isn't necessarily a problem with your site.

## Topics & Engines

This tab breaks performance down two ways:

- **Mention Rate by Topic** — how often each brand appears in AI answers for each topic, plotted per topic.
- **Mention Rate Trend by Topic** — the same broken out over time.
- **Mention Rate by Platform** — a heatmap of how often each brand appears in each platform's answers during the period.

Topics come from your prompt categories. If your prompts aren't categorized, this tab shows a prompt to organize them in the [Prompt Manager](prompt-manager.md) rather than an empty chart.

## Exporting

**Export** offers two formats:

- **CSV spreadsheet** — every result in the current view, for Excel or Google Sheets.
- **PDF executive report** — a full 13-section report of the current view, written to be handed to someone who wasn't in the room.

The report opens with a written narrative rather than a chart dump, then works through: where you stand, whether AI is describing you accurately, movement over the period, engine by engine, where AI cites you, questions competitors win, what competitors get cited for, the full field, brands named in AI answers, domains AI cites, mention rate by engine, mention rate by topic, and a closing section explaining how to read every metric in it.

Exports respect your current filters, and the PDF cover states which filters were applied so a report can't be mistaken for a full-account picture. On paid plans, the PDF carries your [white-label branding](../agency/white-label.md) if you've set it up.

## Running visibility checks

Click **Run now** for an on-demand check. Behavior depends on your [plan](../getting-started/account-modes.md):

- **Preview Mode** runs local-fetch checks directly from your device against public AI search surfaces. Hi, Moose asks you to confirm first, since back-to-back checks can trigger temporary rate-limit challenges from those surfaces. Sentiment, narrative, and parity scoring need an activated local Gemma 4 model; without one, those checks are skipped.
- **BYOK plans** run locally using your own OpenRouter key.
- **Managed plans** run through Hi, Moose's infrastructure. If your workspace doesn't have enough allowance left this month for the current schedule, scheduled runs pause until you upgrade, adjust your [run cadence](settings.md#run-schedule), or the allowance resets. Hi, Moose tells you how many units are needed against what's remaining.

You can stop a run early, and runs interrupted by an app update resume rather than being lost.

## How much history is kept

Every observation a run produces is archived locally, so trends, comparisons, and the Mentions and Citations tables can look further back than the last few runs. The archive holds up to **400 days** per workspace, and up to 200,000 observations; beyond either limit the oldest rows are dropped.

On paid managed plans, visibility runs that execute on your machine also sync their results to the cloud, so teammates see the same history you do rather than only the runs that happened on their own device.

## Where to go from here

- **[Competitors & Share of Voice](competitors.md)** — competitive position, competitor citations, and gaps.
- **[Prompt Manager](prompt-manager.md)** — add, organize, and categorize the prompts being tracked.
- **[Visibility Settings](settings.md)** — run schedule, scoring model, competitor tracking, secondary brand terms and domains, and default models.
