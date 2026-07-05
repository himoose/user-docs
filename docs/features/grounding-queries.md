# AI Mode Grounding Queries

## What this helps you do

This worksteam reveals the hidden searches Google's AI Mode actually ran while grounding its answer to a prompt — so instead of guessing what Google searched behind the scenes, you can see the exact grounding queries, the response, and the sources it cited.

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

Grounding queries show you the real search behavior behind an AI Mode answer — useful for understanding why your page is or isn't showing up, and for spotting query variations you aren't currently tracking in [Visibility](../visibility/overview.md) or [Prompt Manager](../visibility/prompt-manager.md).

## If a run fails

If Hi, Moose can't collect real grounding queries for a prompt, it tells you so rather than presenting a guess — try again in a moment, or double-check that the workspace has a managed subscription active.
