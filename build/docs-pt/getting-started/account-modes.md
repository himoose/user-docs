!!! info "Not translated yet"
    This page is not available in your language yet, so it is shown in English.

# Account Types & Modes

Hi, Moose supports a few different ways to run AI-powered work, depending on how much you want to rely on Hi, Moose's managed infrastructure versus your own API key and local hardware. Understanding these up front will help you understand what's free, what needs an OpenRouter API key, what runs locally, and what needs an internet connection.

## The four modes

### Preview Mode (Free)

Preview Mode is the free way to try Hi, Moose. AI-powered features work out of the box with no setup — no API key required. This mode uses Hi, Moose's included AI usage, so features come with usage limits.

- No API key needed
- Requires an internet connection for AI-powered features
- Good for trying out the product before committing to BYOK or a paid plan

### BYOK Free

BYOK ("Bring Your Own Key") Free is a local-only version of Hi, Moose. You supply your own [OpenRouter](https://openrouter.ai) API key, and model calls run **locally on your machine** using that key — not through Hi, Moose's servers.

- Requires your own OpenRouter API key
- 1 active project
- 1 user seat
- CMS connections ([Grav](../integrations/grav.md), [WordPress](../integrations/wordpress.md), [Webflow](../integrations/webflow.md)) included
- Chat web search, Workflows, Google Search Console connection, and audio generation are not included
- Limited [Library](../library/overview.md) and context storage/recall

### BYOK Premium

BYOK Premium is the full local-only plan. Same local-first model as BYOK Free — your own OpenRouter key, inference runs on your machine — with the full set of supported models, features, and limits unlocked.

- Requires your own OpenRouter API key
- Up to 3 active projects
- Unlimited user seats
- Chat web search included
- Full [Library](../library/overview.md) and context storage/recall
- [Workflows](../workflows/overview.md) included
- [Google Search Console](../integrations/google-search-console.md) connection included
- Includes a monthly allowance of audio generation

### Paid Managed

Paid Managed is the full cloud-backed paid tier. It uses Hi, Moose's managed AI models extensively, so you don't need to bring your own API key. You'll see a single usage meter — your managed AI token balance — rather than juggling multiple usage currencies. Local model support remains available as an explicit, opt-in, on-device option even on this plan.

- No API key required
- Requires an internet connection for managed AI features
- Managed AI token balance is the one usage meter to watch
- Optional local model support for on-device work

## Quick comparison

| | Preview Mode (Free) | BYOK Free | BYOK Premium | Paid Managed |
|---|---|---|---|---|
| Own API key needed | No | Yes (OpenRouter) | Yes (OpenRouter) | No |
| Runs locally | No | Yes | Yes | Optional (local models available) |
| Internet required | Yes | Only for connections/updates | Only for connections/updates | Yes |
| Projects | Limited free usage | 1 | 3 | Higher limits |
| Chat web search | Included | Not included | Included | Included |
| Saved Workflows | — | Not included | Included | Included |
| Google Search Console | — | Not included | Included | Included |
| Audio generation | — | Not included | Monthly allowance included | Included |

!!! note "What BYOK really means"
    In both BYOK Free and BYOK Premium, your OpenRouter key is used to run inference **locally from the desktop app**. Hi, Moose never proxies BYOK inference through its own servers — your key and your prompts stay on your machine. BYOK Premium is a paid plan, but it doesn't change that: you're paying for more local-first workflow capability (projects, memory, workflows, Search Console, audio), not for Hi, Moose to run your model calls for you.

## Switching modes

You can change modes at any time from **Settings**. If you're moving from Preview Mode or Paid Managed into a BYOK mode, add your OpenRouter API key first — Hi, Moose validates the key before switching your AI routing over to it.
