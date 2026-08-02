!!! info "Not translated yet"
    This page is not available in your language yet, so it is shown in English.

# AI Mode Grounding Queries

## What this helps you do

This workstream shows you the Google searches Gemini ran while grounding its answer to a prompt, along with the sources it cited and the grounded response it wrote.

!!! info "What this is, precisely"
    Hi, Moose asks the Gemini API to answer your prompt with Google Search grounding switched on, then reads back the list of searches that model issued. It is not a recording of Google's consumer AI Mode. AI Mode is a separate surface, and it does not expose its internal queries to anyone. What you get is the closest available proxy: the same search index, the same model family, and query phrasings that closely track what AI Mode produces. Treat it as a strong signal rather than a transcript, and expect some variation between runs of the same prompt.

!!! note "Availability"
    This capability runs a managed Gemini grounding call behind the scenes, so it requires a **Paid Managed** workspace. This holds even on BYOK plans — BYOK keeps your core chat generation local, but grounding-query capture itself uses Hi, Moose managed infrastructure that costs us money to run, so it isn't included on BYOK Free or BYOK Premium. Preview Mode doesn't include it either.

## Running it

1. From [Chat](../chat/overview.md), choose the **Capture AI Mode grounding queries** quick start (or ask for it directly).
2. Enter the prompt you want to inspect.
3. Hi, Moose checks Gemini's grounding queries for that prompt and returns:
    - The grounding queries Gemini actually used.
    - The cited sources.
    - The grounded response itself.

## Why this matters

Grounding queries show you how an answer engine turns one prompt into a spread of real searches. That is useful for understanding why your page is or isn't getting picked up, and for spotting query variations you aren't currently tracking in [Visibility](../visibility/overview.md) or [Prompt Manager](../visibility/prompt-manager.md).

## If a run fails

If Hi, Moose can't collect real grounding queries for a prompt, it tells you so rather than presenting a guess — try again in a moment, or double-check that the workspace has a managed subscription active.
