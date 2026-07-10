!!! info "Not translated yet"
    This page is not available in your language yet, so it is shown in English.

# Visibility

## What this helps you do

The Visibility dashboard shows how your brand actually performs in AI search — the queries customers use to find you, whether your brand gets shortlisted, and whether AI engines describe it accurately. This is the primary view for the [core operator loop](../index.md#the-core-operator-loop)'s **monitor** and **detect** steps.

## Metrics

Each run reports five headline metrics for the selected period:

- **Share of Mentions** — how often your brand is mentioned across tracked prompts and engines.
- **Share of Citations** — how often your domain is actually cited as a source.
- **Sentiment** — the average tone (positive/mixed/neutral/negative) of mentions.
- **Narrative Drift** — whether AI responses are drifting from your intended positioning.
- **Feature Parity** — whether AI responses accurately represent what you actually offer.

Narrative Drift and Feature Parity show **"Not scored"** with a **Configure brand truth profile** link until you've filled in your [Brand Truth Profile](../getting-started/context/brand-truth-profile.md) — these two metrics are only meaningful once Hi, Moose knows what's actually true about your brand to compare against.

## Filtering and time range

- Filter results by **Topic**, **AI Engine**, **Prompt** (searchable multi-select), **Sentiment**, **Narrative**, or **Feature Parity** — or clear all filters at once.
- Set a **Period** date range and click **Apply**, or click **Compare** to overlay a prior period or the previous run.
- **Export** downloads the currently filtered rows as CSV.

## Trend over Time

The trend chart plots **Mentions**, **Citations**, or **Positive %** over **Day**, **Week**, or **Month** buckets, broken out per AI engine (or **All models** combined) so you can see whether a specific engine is moving the numbers.

## Prompt-level detail

Below the chart:

- **Share of Mentions by AI Engine** breaks results out per engine.
- **Top Cited Pages** shows which of your URLs are actually getting cited, and by which engines.
- **Prompt-Level Breakdown** lets you expand any tracked prompt to see its individual run results per engine, including the full AI response, sentiment/narrative/feature-parity reasoning, and a link to **investigate in chat** — which hands the exact observation data to Hi, Moose and asks it to recommend whether the next step should be an [AEO audit](../features/aeo-audits.md) of an existing page or a new [content brief and draft](../features/content-briefs.md).

## Running visibility checks

Click **Run now** to trigger an on-demand check. Behavior depends on your [account mode](../getting-started/account-modes.md):

- **Preview Mode (Free)** runs local-fetch checks directly from your device against public AI search surfaces. Hi, Moose asks you to confirm before running, since running checks back-to-back can occasionally trigger temporary rate-limit challenges from those surfaces.
- **BYOK Free / BYOK Premium** run locally using your own OpenRouter key.
- **Paid Managed** runs through Hi, Moose's managed infrastructure. If your workspace doesn't have enough managed allowance left this month for the current schedule, scheduled runs pause until you upgrade, adjust your [run cadence](settings.md#run-schedule), or the allowance resets — Hi, Moose tells you exactly how many units are needed versus remaining.

## Where to go from here

- **[Prompt Manager](prompt-manager.md)** — add, organize, and configure the prompts being tracked.
- **[Visibility Settings](settings.md)** — run schedule, scoring model, secondary brand terms/domains, and default models.
