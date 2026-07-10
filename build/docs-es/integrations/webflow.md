!!! info "Not translated yet"
    This page is not available in your language yet, so it is shown in English.

# Webflow

## What this helps you do

Connect a Webflow site so Hi, Moose can inspect its pages and content, and stage previewable edits for publishing — FAQs, key points, brief-driven drafts, and AEO audit recommendations.

## Setting up a connection

1. Open **Connections** in the desktop app and choose Webflow.
2. Click **Connect Webflow MCP** — this opens Webflow's authorization page in your system browser. Complete OAuth there to finish connecting.
3. Once connected, choose which authorized Webflow site Hi, Moose should use for this [project](../getting-started/projects.md).

## Staging a preview target

Hi, Moose can discover **content surfaces** on your connected Webflow site — pages, posts, collection items, and custom code — plus a blank new-page shell for content that doesn't exist yet. Pick a target, add notes about the edit or publishing intent, and stage it as a preview target. From there, review the staged draft the same way as any other connection — see [Drafts, Preview & Publishing](../features/drafts-and-publishing.md).

## Preview and publish readiness

Not every Webflow connection can do everything yet. Hi, Moose reports one of a few readiness states for your connected site: ready for both staging preview artifacts and publishing, preview-only, publish-only, or connected but not yet ready for either. Designer-only surfaces (changes that require the Webflow Designer directly) aren't supported yet.

## Security

Webflow authorization happens through your system browser, and the resulting connection is used only by the desktop app's background process — not exposed to the renderer UI.

