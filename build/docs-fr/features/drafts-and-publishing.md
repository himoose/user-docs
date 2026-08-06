!!! info "Not translated yet"
    This page is not available in your language yet, so it is shown in English.

# Drafts, Preview & Publishing

## What this helps you do

Hi, Moose doesn't stop at a recommendation — it helps you move from a brief or an edit idea all the way to a published change, with a preview and approval step in between, and a record of what happened.

## Draft Studio

Draft Studio is where drafts get written and refined. Draft generation is built to depend on a [content brief](content-briefs.md) rather than working as a blind text expander — if a piece of work needs structured planning, Hi, Moose generates or confirms the brief first, then drafts from it. Draft Studio also supports long-form editing directly.

### Content types

Draft generation follows the same template types available when [generating a content brief](content-briefs.md#generating-a-brief). Four have dedicated Chat quick starts, each with its own structure: [Blog Post Draft](blog-post-draft.md), [Glossary Post](glossary-post.md), [Landing Page Content](landing-page-content.md), and [Product Page Content](product-page-content.md). The Solutions page template is also available when generating a content brief, without a dedicated quick start.

Each template runs the same brief-first draft flow — only the structure differs, so a landing page draft is planned and shaped differently than a blog post even though both start from a [content brief](content-briefs.md).

When you ask for a post and Hi, Moose produces a brief, it goes on to generate the draft rather than stopping and waiting for you to ask again.

### Internal linking

New drafts are checked against your indexed site, and relevant internal links are inserted where they genuinely fit. This needs a built [search index](../site-monitoring/overview.md) — without one there's nothing to link to, and Hi, Moose won't invent links.

## Staging an edit

Whether it comes from a brief-driven draft, a [FAQ](faq-generator.md), [key points](key-points.md), or an [AEO audit](aeo-audits.md) recommendation, a proposed change is staged as an **edit proposal** — a durable artifact, not just chat text — before anything touches your live site.

## Preview

Before you approve anything, Hi, Moose can generate a preview of the staged change so you can see what it will look like on the actual page. For changes that need to be reviewed by someone else, Hi, Moose can generate a signed, expiring shared review link so a teammate or client can review the change without needing desktop app access.

## Approve & publish

- **Approve** — explicitly accept a staged change before it can be published. Preview and publish are always separate steps; generating a draft or preview is never treated as "done" on its own.
- **Publish** — once approved, Hi, Moose publishes the change through the relevant connection ([WordPress](../integrations/wordpress.md), [Webflow](../integrations/webflow.md), or [Grav](../integrations/grav.md)) and records what was published, when, and why.

### Per-CMS behavior

**WordPress** — drafts can be pushed to a connected site as staged drafts rather than going straight live, and the publishing flow adapts to whether the target is already staged or published. Once you've pushed a draft, Hi, Moose remembers, so you can't accidentally push the same one several times.

**Webflow** — publishing to a collection loads the collection's other required fields first and asks you to fill them in, so a publish doesn't fail partway through on a field you couldn't see.

A failed publish lands in your [inbox](../inbox/overview.md). A successful one doesn't, on purpose.

## Work Queue

The Work Queue is where staged edits, pending previews, and items waiting on your approval collect — so nothing sits only inside a chat transcript waiting to be forgotten.

## Library and History

- **[Library](../library/overview.md)** holds the durable artifacts you've generated — briefs, drafts, FAQ sets, key points, AEO audits — so you can find and reuse them later instead of regenerating from scratch.
- **[Chats (History)](../chat/chats-history.md)** is your saved chat session history — reopen, rename, or delete a previous conversation. It's conversation history, not a publish or visibility outcomes log; a dedicated record tying published changes back to the visibility signal that triggered them is planned but not yet built.

## Why this matters

This preview → approve → publish path is what turns a recommendation into a completed, accountable action. A workflow that only produces advice is incomplete; a workflow that ends in a previewed, approved, published change — with a record tying it back to the original visibility signal — is the point of Hi, Moose.
