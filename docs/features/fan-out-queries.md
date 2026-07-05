# ChatGPT Fan-out Queries

## What this helps you do

This worksteam captures the hidden "fan-out" queries ChatGPT Search runs while answering a prompt — the individual searches OpenAI's web-search step actually performed — along with the sources it cited and a preview of the response.

!!! note "Availability"
    This capability runs a managed OpenAI web-search trace capture behind the scenes, so it requires a **Paid Managed** workspace. This holds even on BYOK plans — BYOK keeps core model execution local, but fan-out capture itself uses Hi, Moose managed infrastructure that costs us money to run, so it isn't included on BYOK Free or BYOK Premium. Preview Mode doesn't include it either.

## Running it

1. From [Chat](../chat/overview.md), choose the **Capture ChatGPT fan-out queries** quick start (or ask for it directly).
2. Enter the prompt you want to inspect.
3. Hi, Moose captures ChatGPT's response payload and returns:
    - The distinct fan-out queries ChatGPT ran.
    - The cited sources.
    - A preview of the response.

If OpenAI didn't expose any distinct fan-out queries for a given run, Hi, Moose still shows you the managed search trace and cited sources it did capture, rather than presenting an empty or fabricated result.

## Why this matters

Fan-out queries expose the real query expansion behind a ChatGPT Search answer — useful for understanding which specific phrasings are driving (or missing) citations to your content, feeding directly into what you track in [Visibility](../visibility/overview.md) and plan for in [Content Briefs](content-briefs.md).
