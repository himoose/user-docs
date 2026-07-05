# Google Search Console

## What this helps you do

Connect Google Search Console so Hi, Moose can bring your first-party Google search performance — impressions, clicks, and query data — into the same local evidence base used by [Visibility](../visibility/overview.md), [AEO audits](../features/aeo-audits.md), and [content briefs](../features/content-briefs.md).

!!! note "Availability"
    Google Search Console connection is included on BYOK Premium and Paid Managed. It isn't included on BYOK Free or Preview Mode — see [Account Types & Modes](../getting-started/account-modes.md).

## Why this stays local

Search Console access requires your Google account's OAuth credentials, and Hi, Moose treats those as sensitive by design: authorization happens in your system browser, and the resulting tokens are stored **only on your machine**. Hi, Moose's cloud services never receive your Google access tokens, refresh tokens, or client secrets for this connection — the desktop app is the only thing that talks to Google Search Console on your behalf.

## Setting up a connection

1. Open **Connections** in the desktop app and choose Google Search Console.
2. Authorize access in your system browser.
3. Bind one Search Console property to the active [project](../getting-started/projects.md).

## What you can do with it

- Pull a local snapshot of page and query performance for the bound property.
- Compare the latest snapshot against a prior window to see meaningful changes.
- Ask the operator bounded questions about your Search Console data directly in chat — the model helps interpret your question, but the desktop app owns validating and running the underlying query locally, so your data and token custody stay on-device.
- Feed Search Console evidence into visibility diagnosis and into prioritizing which pages deserve a content brief or an AEO audit.

## Current scope

This connection is read-only in v1 — Hi, Moose does not write back to Search Console. One property can be bound per project at this time.
