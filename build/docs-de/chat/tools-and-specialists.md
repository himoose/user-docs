!!! info "Not translated yet"
    This page is not available in your language yet, so it is shown in English.

# Chat Tools & Specialists

## What this helps you do

Beyond typing a plain request, the chat composer gives you a few extra ways to shape what Hi, Moose does with your message: attaching context, picking a specialist to focus the conversation, or launching a quick-start flow.

## Attachments

Click the attach button in the composer to add context to your message:

- **Upload file or image** — `.txt`, `.md`, `.csv`, `.doc`, `.docx`, `.pdf`, `.xls`, `.xlsx`, `.jpg`, and `.png`. Spreadsheets are parsed into readable text, so you can hand Moose a workbook and ask about what's in it.
- **Capture screenshot** — choose a display or window, then drag to snip the exact area you want to send. On macOS, this requires enabling Screen Recording access for Hi, Moose the first time you use it.
- **Add from Library** — attach a saved [Library](../library/overview.md) artifact (a brief, draft, key points, or FAQs) as context instead of re-pasting it.
- **Site vector database** — attach your project's indexed site so Moose can answer from your real pages rather than from what it assumes is on them. Build the index from [Site Monitoring](../site-monitoring/overview.md).

## Tools Moose can call

Chat isn't limited to text generation. During a conversation, Moose can call tools on your behalf and shows you when it does.

| Tool | What it does |
|---|---|
| Web search | Live results, on plans that include chat web search |
| Fetch a page | Read a specific URL |
| Site index search | Answer from your own indexed pages |
| Search Console | Query your connected [Search Console](../integrations/google-search-console.md) data |
| Instant brand check | Check a query across five AI engines, see [Instant AI Search Brand Check](../tools/instant-brand-check.md) |
| Coverage check | Find whether your site already covers a topic |
| Image generation | Produce an image for a draft |
| App help | Point you at the right documentation or to support |

Tool use works on managed plans, BYOK plans, and local Gemma 4 models alike.

!!! note "Search Console questions are answered agentically"
    Moose queries your Search Console data iteratively rather than running one fixed report. Ask a vague question and it will narrow down through several queries to answer it, rather than returning a generic dump.

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
- [Turn text content into audio](../audio/overview.md)

The same set is available from the **[Tools menu](../tools/overview.md)** in the top bar, grouped by job and searchable.

The grounding queries and fan-out queries quick starts show you the searches a web-grounded AI engine ran while answering a prompt, plus the sources it cited. Both work by making a managed Gemini or OpenAI call and reading back the searches that call performed, so they are a close proxy for what AI Mode and ChatGPT Search do rather than a capture of those products themselves. Because that call runs on our infrastructure, both require a **paid managed workspace**, and that holds even on BYOK plans, since the query-capture step uses Hi, Moose managed infrastructure rather than your local key.

The audio quick start opens the [Audio](../audio/overview.md) screen in the desktop app. It used to bridge to the legacy web app; it doesn't any more.
