# Prompt Manager

## What this helps you do

Prompt Manager is where you build and organize the actual queries Hi, Moose checks against AI engines — the prompts your customers would realistically type or ask.

## Organizing prompts with categories

Prompts are grouped into categories shown in the left-hand filter list — **All prompts**, **Uncategorized**, and any custom categories you create (for example, by topic or campaign). Add a new category from the field at the bottom of the list. Free-tier workspaces are limited to 5 categories.

## Adding and editing a prompt

Type a new prompt and add it to a category. For each prompt, you can:

- Edit the prompt text.
- Choose which AI engines it runs against — **Select models** opens a picker with every engine your plan can track, API and local-fetch versions alike (see [the engines you can track](settings.md#the-engines-you-can-track)). Local-fetch engines need the desktop app open when the run executes.
- Retire the prompt (see below).
- Delete the prompt.

Unlike a single account-wide setting, **model selection is per-prompt** — one prompt can run only against ChatGPT and Gemini while another runs across all supported engines, so you only spend allowance on the engines that matter for that specific query.

## Finding and selecting several prompts

**Search prompts** filters the list by text. Tick several prompts and the toolbar offers **Assign categories**, **Assign models**, **Retire selected** and **Delete selected**, so a change across many prompts saves in one step instead of one prompt at a time. Only prompts you created can be deleted unless you are the team owner.

## Retiring a prompt

Retire a prompt when it has gone out of date but its history is still worth keeping, for example a prompt that names last year. A retired prompt:

- keeps every past result, so trends and reports still include them;
- is left out of new runs, so it costs nothing;
- is left out of the [Opportunities](overview.md#opportunities) list.

Retired prompts sit in the **Retired prompts** section of the filter list, each with the date it was retired, and **Restore** puts one back into tracking. Adding a new prompt with the same text as a retired one does nothing; restore it instead. **Delete** also removes a prompt from future tracking and keeps the historical run data for reporting, but there is no restore.

## Diagnostic Prompts

**Diagnostic Prompts** is a reserved, system-managed category driven by your [Brand Truth Profile](../getting-started/context/brand-truth-profile.md). Instead of writing these by hand:

1. Click **Generate from Brand Truth** (or set up your Brand Truth Profile first if you haven't).
2. Hi, Moose proposes prompts specifically designed to catch AI describing your customers, capabilities, or competitors incorrectly.
3. Review the suggestions in a modal — toggle any prompt in or out, edit wording, or remove one entirely, before adding them to monitoring.
4. The modal shows an estimated cost before you commit: prompts × models × runs per week ≈ total runs per week.

If your Brand Truth Profile doesn't have enough content yet to generate meaningful diagnostic prompts, Hi, Moose tells you so instead of producing generic filler — add customer questions, key capabilities, or competitors to your profile first.

## Local-only prompt storage

In local-only BYOK modes, prompt categories, prompt definitions, and model selections are stored on your device rather than synced to the cloud.
