!!! info "Not translated yet"
    This page is not available in your language yet, so it is shown in English.

# Inbox

## What this helps you do

The Inbox is where Hi, Moose surfaces the things worth your attention — triaged findings, audits, and publishing events, each tied back to a real artifact instead of a generic notification. It turns scattered signals (visibility sentiment shifts, narrative drift, feature-parity inaccuracies, AEO audit results, publish outcomes, and approval requests) into a single prioritized work queue.

## What shows up in the Inbox

Every Inbox item points to something real you can open and act on, including:

- **Visibility signals** — negative or mixed sentiment detected in an AI answer, narrative drift or feature-parity inaccuracy compared to your [Brand Truth Profile](../getting-started/context/brand-truth-profile.md), or a completed/failed [visibility run](../visibility/overview.md).
- **AEO audit results** — a completed audit, or an audit whose action plan surfaced a high-priority recommendation.
- **Site change detections** — a single digest per [site monitoring](../site-monitoring/overview.md) crawl, opening into a table of every changed page with its impact rating. Unreachable pages and site-wide outages are reported as their own change types.
- **Workflow reports** — results from a [workflow](../workflows/overview.md) run, such as a scheduled scan that generated new posts or flagged an AI search opportunity.
- **Publishing events** — a publish that **failed**, or a change waiting on your approval. Successful publishes no longer create an inbox item, since a wall of "this worked" notices buries the ones that need you.
- **A welcome message** from Moose after you finish onboarding, pointing at a sensible first move.

Each item shows a suggested next action where one makes sense — opening the artifact, starting a brief, following up on an audit, reviewing a draft, approving a change, or retrying a failed run — so you're not just reading a notification, you're one click from doing something about it.

Site monitoring digests also carry an **Ask Moose about all of this** action that hands the crawl snapshot to [chat](../chat/overview.md) and asks what to do first.

## Filtering the Inbox

Two filters control what you see:

- **Status** — defaults to **Active**, meaning everything that isn't dismissed (open, in progress, and done items). Switch to a specific status, or **All** to include dismissed items you may want to reopen.
- **Severity** — **Critical**, **Warning**, **Notice**, **Info**, or **All severities**.

Items are grouped by date (e.g. "Yesterday," "Older") with a count badge for each group, so you can quickly see how much is waiting for you. Long inboxes are paginated rather than loaded all at once.

**Mark all as read** clears the badge across your whole inbox, not just the page you're looking at.

!!! note "The inbox keeps its most recent 200 items"
    Older items are pruned automatically. The inbox is a work queue, not an archive — anything durable lives in the [Library](../library/overview.md) or the artifact it points at.

## Controlling what notifies you

Click **Notifications** to open your per-project notification preferences — see [Inbox Notifications](notifications.md) for what each setting does.

## Managed and BYOK

The Inbox works the same way whether your workspace is managed or BYOK — items are written from whichever side actually generated the underlying event (cloud for managed workflows, the local desktop process for BYOK), and you see one unified queue either way.
