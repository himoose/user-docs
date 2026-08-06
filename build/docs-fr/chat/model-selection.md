!!! info "Not translated yet"
    This page is not available in your language yet, so it is shown in English.

# Model Selection

## What this helps you do

Every chat is powered by a specific AI model, and the model selector lets you see and change which one you're using — including local, on-device models.

## Choosing a model

Open the model selector to see the models available on your [plan](../getting-started/account-modes.md). Each option is labeled with badges so you know what you're getting before you switch:

- **Free** / **HiMoose Cloud** / **Paid or BYOK** — which plans can use this model.
- **Speed: Slow / Average / Very Fast** — a rough sense of response latency.
- **Local** — runs entirely on your device (see below).
- A **multiplier badge** on higher-cost models, showing how much more of your balance they use than the standard option.

The lineup tracks what the model providers ship, and currently includes the Claude, GPT, Gemini, and Gemma families. If a model isn't available on your current plan, Hi, Moose tells you so directly rather than silently falling back to a different one.

## Local models

Approved local models such as Google's Gemma 4 run **entirely on your computer**. No tokens used, no cloud round-trip, and no data leaves your device. The first time you select a local model, Hi, Moose walks you through setup.

Once downloaded and activated, local responses are fast on Apple Silicon. On Intel-based Macs the model runs on CPU and will be noticeably slower than cloud models, and Hi, Moose warns you about this before you commit to the download.

Local models are not a cut-down option. Gemma 4 supports tool calling, so the [chat tools](tools-and-specialists.md) work on a local model the same way they do on a cloud one.

!!! note "Preview Mode depends on a local model"
    On the free plan, [AEO audits](../features/aeo-audits.md) and visibility scoring only run with an activated local model. This is the main reason to set one up early.

## Higher-cost models

Some models use meaningfully more of your balance than the standard option. If you pick one, Hi, Moose confirms first and shows roughly how many times more tokens it uses, so you don't burn through your balance by accident.

The most expensive models are gated by plan. If yours doesn't include them, they're shown as unavailable rather than hidden.

## Web search grounding

Chat can ground its answers in live web search results for the current conversation. This is available on BYOK Premium, BYOK Agency, and all managed plans. It isn't included on BYOK Free or Preview Mode.

## Language

Chat follows a language preference, so you can work in a different language from the one the app interface uses.

## When a model can't be used

You may see a message instead of a response if:

- the selected model is temporarily unavailable (try another model),
- the model isn't allowed on your plan (choose one that's included), or
- an image was attached to a model that doesn't support image input. Hi, Moose names a model that does and offers to switch.

## Where this fits with BYOK

On BYOK plans, model selection determines which model your own OpenRouter key calls. Inference still runs locally in the desktop app. See [Account Types & Plans](../getting-started/account-modes.md) for how model access differs across plans.

Your OpenRouter key is stored per account rather than per device. If you haven't saved one yet, Hi, Moose prompts you the first time a feature needs it rather than failing silently.
