# Google Search Console

## What this helps you do

Connect Google Search Console so Hi, Moose can bring your first-party Google search performance — impressions, clicks, and query data — into the same local evidence base used by [Visibility](../visibility/overview.md), [AEO audits](../features/aeo-audits.md), and [content briefs](../features/content-briefs.md).

!!! note "Availability"
    Google Search Console connection is included on every paid plan — BYOK Premium, BYOK Agency, and all managed plans. It isn't included on BYOK Free or Preview Mode. See [Account Types & Plans](../getting-started/account-modes.md).

## Why this stays local

Search Console access requires your Google account's OAuth credentials, and Hi, Moose treats those as sensitive by design: authorization happens in your system browser, and the resulting tokens are stored **only on your machine**. Hi, Moose's cloud services never receive your Google access tokens, refresh tokens, or client secrets for this connection — the desktop app is the only thing that talks to Google Search Console on your behalf.

## Setting up a connection

1. Open **Connections** in the desktop app and choose Google Search Console.
2. Authorize access in your system browser.
3. Bind one Search Console property to the active [project](../getting-started/projects.md).

## What you can do with it

- Pull a local snapshot of page and query performance for the bound property.
- Compare the latest snapshot against a prior window to see meaningful changes.
- Ask about your Search Console data directly in chat. Moose queries it agentically, narrowing through several queries to answer a vague question rather than running one fixed report. The model interprets your question, but the desktop app owns validating and running each underlying query locally, so your data and token custody stay on-device.
- Feed Search Console evidence into visibility diagnosis and into prioritizing which pages deserve a content brief or an AEO audit.

## Where the data lives

Search Console data pulled into Hi, Moose is stored **locally on your device**, not in Hi, Moose's cloud. It's part of your local evidence base, and it's included in a [local backup](../getting-started/settings.md#data-backup) rather than syncing between machines.

## Current scope

This connection is read-only in v1 — Hi, Moose does not write back to Search Console. One property can be bound per project at this time.

Search Console requires a paid plan. It isn't included on Preview Mode or BYOK Free.

!!! note "Update the app if connecting fails on Windows"
    Windows installers before v0.3.245 shipped without the Google credentials the connection needs, so connecting always failed on the installed app. Updating fixes it.
