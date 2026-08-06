# Recover Lost Visibility

## What this helps you do

This is the workflow recipe for **current content** — it watches your [visibility](../visibility/overview.md) results, and when something meaningful drops, it automatically figures out whether an existing page can be fixed or whether new content is needed, and stages the work for your review.

## Building the workflow

The workflow reads as one sentence, built from these choices:

> **When** [share of mentions drops / share of citations drops / share of mentions increases / share of citations increases] **by** [a threshold, 1–99 points] **for** [all topics / a specific tracked topic], Hi, Moose identifies the affected prompts, then [prepares a content fix / notifies me].

- **Trigger** — which metric to watch, and whether you care about drops or increases. Note that if you choose an "increases" trigger, the only available final action is **notify me** — increases don't have a content-fix path, since there's nothing to repair.
- **Threshold** — how many points of change should count as meaningful, so normal noise doesn't trigger the workflow.
- **Topic scope** — apply this workflow to everything you track, or scope it to one specific topic.
- **Final action** — **prepare a content fix** (continue to the branching logic below) or **notify me** (just create an inbox item without staging any content action).

## When the final action is "prepare a content fix"

Two more choices branch on whether an existing page is a good fit:

- **If matching pages exist** — choose what Hi, Moose should do: **run an AEO audit**, **generate FAQs + schema**, **generate key points**, or **nothing**.
- **If no matching page exists** — choose between **create a brief and new draft** or **nothing**.

This branching is the point of the recipe: it doesn't blindly recommend a new article every time visibility drops. It checks whether fixing something you already have is the better move first, and only proposes new content when nothing existing fits.

## How it runs

This workflow doesn't have a manual "run now" button. It evaluates automatically every time a visibility run completes, comparing the latest completed run against the previous one. When it triggers, the result — including which prompts were affected and what action was taken — lands in your [Inbox](../inbox/overview.md), linked back to the visibility change that caused it.
