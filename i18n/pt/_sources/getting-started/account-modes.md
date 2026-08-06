# Account Types & Plans

Hi, Moose runs AI work one of two ways: on your own OpenRouter key (BYOK), or on Hi, Moose's managed models. That choice, not the price, is the real fork in the road. Everything else is project counts, seats, and how much monthly credit you get.

Plans are grouped into two tabs in the **Upgrade** screen: **Startup** and **Enterprise & Agencies**.

## The two ways to run AI

### BYOK — bring your own key

You supply an [OpenRouter](https://openrouter.ai) API key, and model calls run **from the desktop app on your machine** using that key. Hi, Moose never proxies BYOK inference through its own servers, so your key and your prompts stay local.

Paying for a BYOK plan doesn't change that. You're paying for more workflow capability — projects, seats, memory, workflows, Search Console — not for Hi, Moose to run your model calls for you. Model costs go to OpenRouter directly, and there's no Hi, Moose token meter to watch.

### Managed — Hi, Moose runs the models

No API key. Hi, Moose's managed models do the work, and you spend from a monthly **credit** balance. One meter, not several. Local model support is still available as an opt-in, on-device option on every managed plan.

## Startup plans

### Preview Mode (Free)

Preview Mode is the free way to try Hi, Moose. It is genuinely local: 1 project, 1 seat, local storage, and visibility runs that fetch from public AI search surfaces directly from your device.

- 1 project, 1 user seat
- Free and local LLMs only
- Local visibility runs
- Context storage and recall, Brand Voice and Style Guide
- Connections: WordPress, Webflow, Grav
- Limited live search and competitor data, limited AI quality, limited export options

!!! warning "Preview Mode needs a local model for scoring and audits"
    Preview Mode has no included cloud AI allowance. [AEO audits](../features/aeo-audits.md), and the sentiment, narrative, and feature-parity scoring on [visibility runs](../visibility/overview.md), only run once you've activated a local Gemma 4 model in **Settings → Local Model**. Until one is active, those checks are skipped rather than run in the cloud.

### BYOK Free

The free way to run on your own key. Same 1-project, 1-seat shape as Preview Mode, but you get access to every model OpenRouter offers instead of just the free ones.

- 1 project, 1 user seat
- Your own OpenRouter key, unlimited tokens
- All LLMs, including local models
- Local-only visibility runs
- Connections: WordPress, Webflow, Grav
- Limited context storage and recall, limited [Library](../library/overview.md)
- No chat web search, no Workflows, no Google Search Console

### BYOK Premium — $39/month or $390/year

The full local-first plan, and the point at which team seats and the scheduler unlock.

- 3 projects, plus extra projects for $10/month each
- Up to 10 team seats
- Full visibility runs with a custom scheduler
- Web search from chat
- Full context storage and recall, full [Library](../library/overview.md)
- [Workflows](../workflows/overview.md)
- Brand Voice, Style Guide, and [Brand Truth Profile](context/brand-truth-profile.md)
- Connections: WordPress, Webflow, Grav, [Google Search Console](../integrations/google-search-console.md)
- 15 [audio generations](../audio/overview.md) per month

### Managed plans

All three run on Hi, Moose's models, include unlimited team seats, unlimited audio generations, admin logging and export, and local plus cloud storage.

| Plan | Price | Projects | Monthly credits | Models |
|---|---|---|---|---|
| Standard | $79/mo or $849/yr | 3 | 1,700,000 | Standard models, plus local |
| Professional | $129/mo or $1,389/yr | 5 | 3,000,000 | All models, plus local |
| Premium | $249/mo or $2,689/yr | 10 | 6,000,000 | All models, plus local |

## Enterprise & Agency plans

### BYOK Agency — $149/month or $1,490/year

BYOK Premium at agency scale. Same local-first model and the same feature set, sized for managing many clients.

- 25 projects, plus extra projects for $10/month each
- Up to 25 team seats
- 15 audio generations per month
- [White-label branding](../agency/white-label.md) on reports and audio embeds, as on every paid plan

### Managed agency plans

| Plan | Price | Projects | Monthly credits | Storage |
|---|---|---|---|---|
| Agent Core | $449/mo or $4,849/yr | 25 | 15,000,000 | Team cloud |
| Agent Studio | $999/mo or $10,789/yr | 75 | 40,000,000 | Team cloud |
| Agent Scale | $1,999/mo or $21,589/yr | Unlimited | 120,000,000 | Team cloud |

## Quick comparison

| | Preview Mode | BYOK Free | BYOK Premium | BYOK Agency | Managed plans |
|---|---|---|---|---|---|
| Own API key needed | No | Yes | Yes | Yes | No |
| Inference runs | On your device | On your device | On your device | On your device | Hi, Moose cloud (local optional) |
| Projects | 1 | 1 | 3 | 25 | 3 to unlimited |
| Team seats | 1 | 1 | 10 | 25 | Unlimited |
| Chat web search | No | No | Yes | Yes | Yes |
| [Workflows](../workflows/overview.md) | No | No | Yes | Yes | Yes |
| [Google Search Console](../integrations/google-search-console.md) | No | No | Yes | Yes | Yes |
| [Audio](../audio/overview.md) | No | No | 15/month | 15/month | Unlimited |
| [White-label branding](../agency/white-label.md) | No | No | Yes | Yes | Yes |

## Seats, projects, and credits

**Extra projects** cost $10/month each on every paid plan. Add or remove them from **Upgrade → Extra projects**.

**Seats** are the real paid/free line. Preview Mode and BYOK Free are capped at the account owner alone. BYOK Premium allows up to 10, BYOK Agency up to 25, and managed plans are uncapped because every member spends the owner's credit balance.

**Credit top-ups** are available on managed plans when you run out mid-month:

- 500,000 credits for $25
- 2,500,000 credits for $100

Top-ups are one-time purchases, not subscriptions. They're only spent after your monthly credits run out, and they never expire.

!!! note "Audio listens are metered separately"
    Every plan that includes audio also includes the first 10,000 listens account-wide. Beyond that, listens are billed at $5.00 per 10,000 per month. On managed plans, audio *generation* also draws from your credit balance.

## Coupons

If you have a discount code, enter it during checkout on the **Upgrade** screen.

## Switching plans

Change plans any time from **Settings → Account** or the **Upgrade** screen. If you're moving from a managed plan into a BYOK plan, add your OpenRouter API key first. Hi, Moose validates the key before switching your AI routing over to it.

Your OpenRouter key is stored per account rather than per device, so it follows you to a new install.
