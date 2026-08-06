# Visibility

## What this helps you do

The Visibility dashboard shows how your brand actually performs in AI search: the queries customers use to find you, whether your brand gets shortlisted, and whether AI engines describe it accurately. This is the primary view for the [core operator loop](../index.md#the-core-operator-loop)'s **monitor** and **detect** steps.

The dashboard has three tabs:

| Tab | What it answers |
|---|---|
| **Overview** | How am I doing? |
| **[Competition](competitors.md)** | How am I doing compared to them? |
| **Topics & Engines** | Where specifically am I strong or weak? |

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

## Topics & Engines

This tab breaks performance down two ways:

- **Mention Rate by Topic** — how often each brand appears in AI answers for each topic, plotted per topic.
- **Mention Rate Trend by Topic** — the same broken out over time.
- **Mention Rate by Platform** — a heatmap of how often each brand appears in each platform's answers during the period.

Topics come from your prompt categories. If your prompts aren't categorized, this tab shows a prompt to organize them in the [Prompt Manager](prompt-manager.md) rather than an empty chart.

## Exporting

**Export** offers two formats:

- **CSV spreadsheet** — every result in the current view, for Excel or Google Sheets.
- **PDF executive report** — a print-ready report of the current view, including the competitive charts and data from the Competition tab.

Exports respect your current filters, and the PDF cover states which filters were applied so a report can't be mistaken for a full-account picture. On paid plans, the PDF carries your [white-label branding](../agency/white-label.md) if you've set it up.

## Running visibility checks

Click **Run now** for an on-demand check. Behavior depends on your [plan](../getting-started/account-modes.md):

- **Preview Mode** runs local-fetch checks directly from your device against public AI search surfaces. Hi, Moose asks you to confirm first, since back-to-back checks can trigger temporary rate-limit challenges from those surfaces. Sentiment, narrative, and parity scoring need an activated local Gemma 4 model; without one, those checks are skipped.
- **BYOK plans** run locally using your own OpenRouter key.
- **Managed plans** run through Hi, Moose's infrastructure. If your workspace doesn't have enough allowance left this month for the current schedule, scheduled runs pause until you upgrade, adjust your [run cadence](settings.md#run-schedule), or the allowance resets. Hi, Moose tells you how many units are needed against what's remaining.

You can stop a run early, and runs interrupted by an app update resume rather than being lost.

## Where to go from here

- **[Competitors & Share of Voice](competitors.md)** — competitive position, competitor citations, and gaps.
- **[Prompt Manager](prompt-manager.md)** — add, organize, and categorize the prompts being tracked.
- **[Visibility Settings](settings.md)** — run schedule, scoring model, competitor tracking, secondary brand terms and domains, and default models.
