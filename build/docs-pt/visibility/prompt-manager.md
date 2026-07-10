!!! info "Not translated yet"
    This page is not available in your language yet, so it is shown in English.

# Prompt Manager

## What this helps you do

Prompt Manager is where you build and organize the actual queries Hi, Moose checks against AI engines — the prompts your customers would realistically type or ask.

## Organizing prompts with categories

Prompts are grouped into categories shown in the left-hand filter list — **All prompts**, **Uncategorized**, and any custom categories you create (for example, by topic or campaign). Add a new category from the field at the bottom of the list. Free-tier workspaces are limited to 5 categories.

## Adding and editing a prompt

Type a new prompt and add it to a category. For each prompt, you can:

- Edit the prompt text.
- Choose which AI engines/models it runs against — **Select models** opens a picker covering ChatGPT, Claude, Gemini, Grok, Perplexity, Google AI Mode, Google AI Overview, and Bing Copilot (availability depends on your account mode and, for local-fetch engines, running the desktop app).
- Delete the prompt.

Unlike a single account-wide setting, **model selection is per-prompt** — one prompt can run only against ChatGPT and Gemini while another runs across all supported engines, so you only spend allowance on the engines that matter for that specific query.

## Diagnostic Prompts

**Diagnostic Prompts** is a reserved, system-managed category driven by your [Brand Truth Profile](../getting-started/context/brand-truth-profile.md). Instead of writing these by hand:

1. Click **Generate from Brand Truth** (or set up your Brand Truth Profile first if you haven't).
2. Hi, Moose proposes prompts specifically designed to catch AI describing your customers, capabilities, or competitors incorrectly.
3. Review the suggestions in a modal — toggle any prompt in or out, edit wording, or remove one entirely, before adding them to monitoring.
4. The modal shows an estimated cost before you commit: prompts × models × runs per week ≈ total runs per week.

If your Brand Truth Profile doesn't have enough content yet to generate meaningful diagnostic prompts, Hi, Moose tells you so instead of producing generic filler — add customer questions, key capabilities, or competitors to your profile first.

## Local-only prompt storage

In local-only BYOK modes, prompt categories, prompt definitions, and model selections are stored on your device rather than synced to the cloud.
