# Settings

## What this helps you do

Settings is where you manage your account, your [account mode](account-modes.md), your AI model options, and your team, along with local app preferences.

## Account

- Update your email, verify your email address, and reset your password (email/password accounts). Google accounts are managed through Google.
- View your current account mode (Preview Mode, BYOK Free, BYOK Premium, or Paid Managed) and change plans.

## BYOK: adding your OpenRouter API key

If you're on BYOK Free or BYOK Premium, add your [OpenRouter](https://openrouter.ai) API key here. Hi, Moose validates the key before switching AI routing over to it. Once added:

- AI-powered features run locally in the desktop app using your key.
- You can choose which supported models to use for chat and generation.
- Your key and prompts are not sent through Hi, Moose's servers for BYOK inference.

## Local models

Approved local models (such as Gemma) can be enabled from Settings for on-device inference, available across account modes. Local model execution never uses Hi, Moose's or your OpenRouter key — it runs entirely on your machine.

## Usage

- **Paid Managed** accounts see a single managed AI token balance rather than multiple usage meters.
- **BYOK modes** don't consume a Hi, Moose-hosted token balance for inference, since generation runs against your own key.

## Team

Team settings — inviting members, viewing roles, and removing access — live here for plans with multiple user seats. See [Team Management](team-management.md) for the full walkthrough.

## Site monitoring & connections

Manage connected CMS and data sources (WordPress, Webflow, Google Search Console) from the Connections area. See:

- [WordPress](../integrations/wordpress.md)
- [Webflow](../integrations/webflow.md)
- [Google Search Console](../integrations/google-search-console.md)

## Data & backup

Your local memory — [Context](context/overview.md) (Brand Voice, Brand Truth Profile, About You), visibility history, drafts, and publish history — lives on your machine. Settings includes options to inspect and back up this local data so it isn't tied to a single install.

## Troubleshooting

If the app is behaving unexpectedly, Settings includes a troubleshooting section with logs you can review or export when contacting support.
