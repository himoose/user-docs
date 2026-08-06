# ChatGPT Fan-out Queries

## What this helps you do

This workstream captures the individual "fan-out" searches OpenAI's web-search step ran while answering your prompt, along with the sources it cited and a preview of the response.

!!! info "What this is, precisely"
    Hi, Moose calls the OpenAI Responses API with its web search tool enabled, then reads back the searches that run performed. It is not a capture of the consumer ChatGPT product's own fan-out, which OpenAI does not expose. What you get is the closest available proxy: the same web search layer, driven by the same model family, so the query expansion closely tracks what ChatGPT Search does. Treat it as a strong signal rather than a transcript, and expect some variation between runs of the same prompt.

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

Fan-out queries expose the query expansion behind a web-grounded answer, which is useful for understanding which specific phrasings are driving (or missing) citations to your content. That feeds directly into what you track in [Visibility](../visibility/overview.md) and plan for in [Content Briefs](content-briefs.md).
