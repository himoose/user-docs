# Visibility Settings

## What this helps you do

Visibility Settings control how often Hi, Moose checks visibility, which model scores the results, and which brand terms and domains count toward your metrics. Prompts and topics themselves stay in [Prompt Manager](prompt-manager.md) — this screen is about the run mechanics.

## Run Schedule

- **Cadence** — Daily, Weekdays, Weekly, or Manual only.
- **Preferred run time** and, for weekly cadence, a **weekly day** — runs execute in your local timezone.
- **Samples per prompt** — scheduled runs can repeat each prompt multiple times and average the results for a more stable visibility rate. Manual **Run now** always uses a single sample. Increasing this multiplies token usage by the same factor, and Hi, Moose warns you before you save a higher value.

!!! note "Scheduled runs need this device awake"
    On **Preview Mode** and **BYOK** modes, scheduling runs locally on your machine — a scheduled run cannot start while your computer is off, asleep, or Hi, Moose is fully quit. Keep the app open (or minimized to the system tray) so scheduled runs can execute. **Paid Managed** unlocks an always-on cloud scheduler that doesn't depend on your device being awake. Local-fetch engines specifically still require the app to be open regardless of plan, since those checks run from your machine.

## Email notifications

Toggle **Scheduled visibility email reports** to receive the visibility report by email after scheduled runs complete. This is a personal notification preference, separate from the [Inbox notification settings](../inbox/notifications.md).

## Secondary brand terms and domains

- **Secondary branded terms** — alternate phrasings or spelling variations of your brand that should also count as a mention.
- **Secondary domains** — additional domains that should count as valid brand citations for this project, beyond your primary domain.

## Scoring model

Choose the model Hi, Moose uses to score sentiment, narrative drift, and feature parity once a response has been captured:

- **Automatic default** adapts to your account mode:
    - **Preview Mode** uses an activated local Gemma 4 model — scoring is skipped until one is installed and active (Settings → Local AI).
    - **BYOK** modes score using your local OpenRouter key.
    - **Paid Managed** scores through Hi, Moose's managed model routing (local model scoring still applies where supported).
- You can also select a specific model instead of Automatic.

## Default models for new prompts

Choose which engines are pre-selected whenever you add a new prompt in [Prompt Manager](prompt-manager.md) — you can still override the selection per prompt afterward. Models marked **Paid** require a paid or BYOK plan; Preview Mode is limited to local-fetch models only. Every model checked here counts toward token usage when visibility runs execute.

## Redo onboarding

Re-run the visibility onboarding wizard at any time to update your tracked domain, prompts, and tracking preferences from scratch.
