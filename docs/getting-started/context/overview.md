# Context

## What this helps you do

**Context** is the grounding layer in the desktop app's left navigation. It's the shared operating context for your current project — the information the operator, chat, and every generation capability reuse instead of starting cold on every request.

Context is made up of four pieces:

| | Scope | What it's for |
|---|---|---|
| **[Brand Voice](brand-voice.md)** | Per project | How your brand should sound — tone, audience, values, terminology. Shapes the writing style of everything Hi, Moose generates. |
| **[Brand Truth Profile](brand-truth-profile.md)** | Per project | A machine-readable source of truth for what your company actually is, sells, and serves — used to detect when AI answers misrepresent or drift from that truth. |
| **[Brand Documents](brand-documents.md)** | Per project | Your own message house, style guide, and positioning documents. Hi, Moose splits them into sections, applies your writing rules to everything, and pulls in the rest when a piece of work needs it. |
| **[About You](about-you.md)** | Per device, not per project | Notes about you personally — your role, goals, and how you like to work — so chat feels like it knows the person, not just the brand. |

## Why separate artifacts

Brand Voice and Brand Truth Profile answer different questions, even though both describe your brand:

- **Brand Voice** answers "how should this sound?" — tone, style, vocabulary preferences. It's creative and stylistic guidance for generated content.
- **Brand Truth Profile** answers "what is actually true about us?" — canonical description, ideal customer, offerings, competitors, and the specific things AI tends to get wrong. It's a factual reference used to catch misrepresentation, not a style guide.

**Brand Documents** hold the full source material behind both. Brand Voice and the Brand Truth Profile stay short summaries. Your documents keep the detail, and Hi, Moose searches them for the sections that fit each piece of work. You can also use them to fill in the two profiles.

**About You** is different from all of these: it isn't about the brand at all. It's personal context about **you**, the person using the app, stored locally on your device rather than attached to a project — so it follows you across projects instead of resetting every time you switch workspaces.

## Where Context is used

- **Brand Voice** is reused across [Content Briefs](../../features/content-briefs.md), [FAQ Generator](../../features/faq-generator.md), [Key Points Extractor](../../features/key-points.md), [Drafts, Preview & Publishing](../../features/drafts-and-publishing.md), and [AEO Audit](../../features/aeo-audits.md) recommendations.
- **Brand Truth Profile** is reused during [Visibility](../../visibility/overview.md) runs, where Hi, Moose checks whether an AI engine's response about your brand lines up with your canonical description, offerings, competitors, and known misrepresentation patterns.
- **Brand Documents** are reused in Content Briefs, blog post drafts, Key Points, FAQ Generator, [Send Moose](../../send-moose/overview.md) research, and [Chat](../../chat/overview.md), where chat can also search them. See [Where your documents are used](brand-documents.md#where-your-documents-are-used).
- **About You** is reused in [Chat](../../chat/overview.md) so responses can reflect your role, goals, and preferred communication style.

## Filling it in

Each artifact tracks how many fields you've filled in and shows a short preview once you've added anything. All fields are optional — Hi, Moose works with partial context and gets more precise as you add more.

For Brand Voice specifically, you don't have to fill every field by hand: an **auto-fill** action can crawl your project's website locally and suggest values for empty fields.

If you already have a message house or style guide, upload it under [Brand Documents](brand-documents.md) and click **Fill profiles from documents**. Hi, Moose suggests values for both Brand Voice and the Brand Truth Profile, each backed by a quote from your document, and you choose which ones to apply.

## Local-first storage and cloud sync

By default, Brand Voice, Brand Truth Profile, and Brand Documents are stored **locally for the current project**, and About You is stored **locally on your device**. Cloud sync — which backs up Brand Voice, Brand Truth Profile, and Brand Documents and shares them across your team — is available on **every paid plan**, including paid BYOK plans. Preview Mode and BYOK Free stay local-only; upgrading turns on sync so your team shares the same grounding and it's protected if anything happens to your local machine.

!!! note "On BYOK plans"
    Brand-context crawling (the auto-fill step) and Brand Truth analysis run locally in the desktop app. Hi, Moose does not need to see your site content on its own servers to build or use this context.
