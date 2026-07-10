!!! info "Not translated yet"
    This page is not available in your language yet, so it is shown in English.

# Chat Tools & Specialists

## What this helps you do

Beyond typing a plain request, the chat composer gives you a few extra ways to shape what Hi, Moose does with your message: attaching context, picking a specialist to focus the conversation, or launching a quick-start flow.

## Attachments

Click the attach button in the composer to add context to your message:

- **Upload file or image** — attach a file or image to the chat.
- **Capture screenshot** — choose a display or window, then drag to snip the exact area you want to send. On macOS, this requires enabling Screen Recording access for Hi, Moose the first time you use it.
- **Add from Library** — attach a saved [Library](../library/overview.md) artifact (a brief, draft, key points, or FAQs) as context instead of re-pasting it.

## Specialists

Specialists are focused entry points into the same main operator — not separate tools or separate memory, just a way to point the conversation at a specific job. Open the specialist selector to choose one:

- **Content Brief specialist** — build a tight brief with structure and next steps.
- **Google Search Console Specialist** — ask Moose about your connected [Google Search Console](../integrations/google-search-console.md) data. This specialist needs a connected Search Console account or saved property for the active project before it can answer from your first-party data.
- **Audio Generator specialist** — turn a request into a clean spoken-word script.
- **Draft specialist** — generate draft content that's ready for review and editing.
- **FAQs specialist** — draft concise FAQs around the highest-value questions.
- **Key Points specialist** — pull out the most important takeaways first.

Once a specialist is active, you'll see its badge on the conversation, and you can clear it at any time to go back to general chat.

### Custom specialists

You can also create your own local specialist: give it a name and a summary of the work it should handle, then choose which parts of your context it's allowed to use — project context, brand profile, website context, chat history, draft-biased output, or markdown-formatted output. Custom specialists can also be imported/uploaded if you have one shared with you.

## Quick starts

The composer surfaces one-click quick starts for common jobs, including:

- [Run an AEO audit](../features/aeo-audits.md)
- [Create a research-backed content brief](../features/content-briefs.md)
- [Create research-backed FAQs](../features/faq-generator.md)
- [Generate optimized key points](../features/key-points.md)
- [Create a blog post draft](../features/blog-post-draft.md)
- [Create a glossary post](../features/glossary-post.md)
- [Create landing page content](../features/landing-page-content.md)
- [Create product page content](../features/product-page-content.md)
- [Capture Google AI Mode grounding queries for a prompt](../features/grounding-queries.md)
- [Capture ChatGPT fan-out queries for a prompt](../features/fan-out-queries.md)
- [Turn text content into audio](../legacy/listen-to-this-article.md)

The grounding queries and fan-out queries quick starts reveal the hidden searches an AI engine actually ran while answering a prompt, plus the sources it cited. These are diagnostic capabilities that run a managed Gemini or OpenAI call behind the scenes, so they require a **paid managed workspace** — this holds even on BYOK plans, since the query-capture step itself uses Hi, Moose managed infrastructure rather than your local key.

The audio quick start bridges to the [legacy web app](../legacy/listen-to-this-article.md), since audio generation hasn't moved into the desktop app yet.
