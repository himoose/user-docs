!!! info "Not translated yet"
    This page is not available in your language yet, so it is shown in English.

# Inbox Notifications

## What this helps you do

Inbox notification preferences control how — and how urgently — you're alerted when new items land in a project's [Inbox](overview.md). These settings are per-project, so a low-priority test project doesn't have to notify you the same way a client's production site does.

## Settings

- **Show inbox badge in this app** — when off, the sidebar and dock badge won't update for this project, even though items still arrive in the Inbox itself.
- **Show desktop notifications** — native macOS or Windows notifications when an item meets the severity threshold below.
- **Minimum severity for desktop notifications** — choose the lowest severity that should trigger a desktop notification (e.g. Warning). Items below that threshold still appear in the Inbox, they just won't interrupt you.
- **Email me a daily digest** — the toggle is saved, but this digest is not sent yet; it's coming soon.
- **Include informational AEO changes** — off by default, to keep the Inbox focused on things that matter. When on, low-impact AEO changes also get sent to the Inbox. Note that desktop notifications still respect the severity threshold above even if this is on.

## Why these are separate from severity itself

Severity (critical, warning, notice, info) is set on the item itself based on what actually happened — it isn't something you configure. What you control here is how much of that gets surfaced as a badge, a desktop notification, or (soon) an email — so the underlying signal stays honest while you tune how loudly it's delivered.
