# Model Selection

## What this helps you do

Every chat is powered by a specific AI model, and the model selector lets you see and change which one you're using — including local, on-device models.

## Choosing a model

Open the model selector to see the models available to your [account mode](../getting-started/account-modes.md). Each option is labeled with badges so you know what you're getting before you switch:

- **Free** / **HiMoose Cloud** / **Paid or BYOK** — which account modes can use this model.
- **Speed: Slow / Average / Very Fast** — a rough sense of response latency.
- **Local** — runs entirely on your device (see below).

If a model isn't available for your current account mode, Hi, Moose tells you so directly rather than silently falling back to a different model.

## Local models

Approved local models (like Google's Gemma) run **entirely on your computer** — no tokens used, no cloud round-trip, and no data leaves your device. The first time you select a local model, Hi, Moose walks you through setup. Once downloaded and activated, local responses are fast on Apple Silicon; on Intel-based Macs, the model runs on CPU and will be noticeably slower than cloud models.

## Higher-cost models

Some models use meaningfully more of your token allowance than the standard option. If you pick one of these, Hi, Moose confirms first — showing roughly how many times more tokens it uses — so you don't burn through your balance by accident.

## Web search grounding

Chat can optionally ground its answers in live web search results for the current conversation. This toggle is available on **BYOK Premium** and **paid managed** plans; it isn't included on BYOK Free or Preview Mode.

## When a model can't be used

You may see a message instead of a response if:

- the selected model is temporarily unavailable (try another model),
- the model isn't allowed for your account type (choose one that's included in your plan), or
- an image was attached to a model that doesn't support image input (switch to a model that does).

## Where this fits with BYOK

In BYOK modes, model selection determines which model your own OpenRouter key calls — inference still runs locally in the desktop app. See [Account Types & Modes](../getting-started/account-modes.md) for how model access differs across Preview Mode, BYOK Free, BYOK Premium, and Paid Managed.
