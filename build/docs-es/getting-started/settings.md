!!! info "Not translated yet"
    This page is not available in your language yet, so it is shown in English.

# Settings

## What this helps you do

Settings is where you manage your profile, your plan, your models, your team, and how the app behaves on this computer. It's organized into ten sections down the left side.

| Section | What's in it |
|---|---|
| General | Profile details and app behavior on this computer |
| Usage | Credit balance and reset date |
| Account | Email, password, plan, OpenRouter key |
| Local Model | On-device model download and activation |
| Team | Seats, invitations, roles |
| [Site Monitoring](../site-monitoring/overview.md) | Crawl schedule, search index, monitored pages, blocked paths |
| [Branding](../agency/white-label.md) | White-label reports and audio attribution (paid plans only) |
| Logs | Action logs and CSV export |
| Data & Backup | Local backup and restore |
| Troubleshooting | Cache, diagnostic log, local data reset |

## General

**Profile details** — your preferred name, job title, and location. These keep the app personalized and give shared work clearer attribution.

**App behavior** controls how Hi, Moose runs on this computer:

- **Start Hi, Moose when you log in** — after a restart, the app opens quietly in the background so scheduled work keeps running. Open the window any time from the tray or menu bar.
- **Share anonymous usage analytics** — sends anonymous, aggregate events (which features run, app version, errors) so we can improve the product. It never sends your content, prompts, keys, or the sites you analyze, and your IP is discarded. You can turn it off any time.

## Usage

On managed plans, this shows your credit balance and what's left this month.

!!! note "The month is UTC"
    Credits reset at the start of each month in UTC, not your local time zone. Settings shows you the date that lands on where you are, so late on the last day of the month it can look like the reset came early.

BYOK plans don't consume a Hi, Moose credit balance for inference, since generation runs against your own key. Model costs go to OpenRouter directly.

## Account

- Update your email, verify it, and reset your password on email/password accounts. Google accounts are managed through Google.
- Email changes wait for you to confirm through a link before they take effect, and your in-app session updates afterward.
- View your current plan and change it. See [Account Types & Plans](account-modes.md).

### Adding your OpenRouter API key

On BYOK plans, add your [OpenRouter](https://openrouter.ai) key here. Hi, Moose validates the key before switching AI routing over to it. Once added:

- AI features run locally in the desktop app using your key
- You choose which supported models to use for chat and generation
- Your key and prompts are never sent through Hi, Moose's servers for BYOK inference

The key is stored per account rather than per device, so it follows you to a new install.

## Local Model

Download and activate an approved on-device model such as Gemma 4. Local execution never uses Hi, Moose's models or your OpenRouter key. It runs entirely on your machine, and it's free to run.

Local models are available on every plan, and they're **required** on Preview Mode for [AEO audits](../features/aeo-audits.md) and visibility scoring.

!!! note "Context size scales to your RAM"
    Hi, Moose sizes the model's context window to the memory available on your machine, so the same model uses a smaller window on a 16 GB laptop than on a larger workstation.

## Team

Invite members, view roles, and remove access. Seat limits depend on your plan. See [Team Management](team-management.md) for the full walkthrough.

## Site Monitoring

Crawl schedule, the local search index, monitored pages, and blocked paths. This is a substantial area with its own page: **[Site Monitoring](../site-monitoring/overview.md)**.

Connected CMS and data sources are separate, and live in the **Connections** screen rather than Settings:

- [WordPress](../integrations/wordpress.md)
- [Webflow](../integrations/webflow.md)
- [Grav](../integrations/grav.md)
- [Google Search Console](../integrations/google-search-console.md)

## Branding

White-label your exported PDF reports and embedded audio players. Available on every paid plan, editable by the subscription owner. See **[White-Label Branding](../agency/white-label.md)**.

## Logs

Action logs for the current project, showing type, user, date, status, and metadata for each recorded action. On managed plans, team-shared logs sync in alongside your local ones.

**Export CSV** downloads them. Exporting team action logs is restricted to paid managed workspace owners.

## Data & Backup

Create a compressed `.hmbk` backup of your on-device history, and import it later to restore.

**Backups include** local database records and saved BYOK visibility schedules, so your briefs, audits, previews, site monitoring history, inbox state, and other non-secret workflow artifacts stay portable.

**Backups do not include** login state, connector credentials, API keys, local model files, or file attachments.

!!! warning "Importing overwrites local data permanently"
    An import replaces this device's local Hi, Moose data with the contents of the backup. The confirmation dialog tells you how many rows will be restored and when the backup was made. Restart the app afterward so every screen reloads from the restored data.

Imports only accept `.hmbk` files exported by the Hi, Moose desktop app.

## Troubleshooting

Three recovery tools. All of them affect local desktop state only and never touch cloud data.

**Clear transient cache** — clears the HTTP cache, service workers, and other disposable state. Keeps your login and local workflow history. Try this first.

**Diagnostic log** — Hi, Moose keeps a small log of errors on this device. **Open log folder** takes you to it; if support asks for it, send the `main-errors.log` file. The log stays on your device unless you choose to share it.

**Reset local app data** — permanently removes on-device artifacts, briefs, previews, visibility history, and other local workflow state. This can't be undone. Your login and saved connector credentials stay in place.
