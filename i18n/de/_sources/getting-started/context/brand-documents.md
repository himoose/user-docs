# Brand Documents

## What this helps you do

Brand Documents lets you upload the brand documents your team already keeps, such as a message house, a style guide, or positioning and persona messaging. Hi, Moose reads them before it writes anything for the project, so briefs, drafts, FAQs and chat answers follow your own rules and use your approved messaging.

You don't have to paste a 50-page message house into every request. Hi, Moose splits each document into sections, keeps your writing rules on for every piece of work, and pulls in the other sections only when a piece of work needs them.

You can also use your documents to [fill in Brand Voice and the Brand Truth Profile](#fill-brand-voice-and-brand-truth-from-your-documents) in one step.

Brand Documents are scoped to the current [project](../projects.md). Open them from the **Brand documents** card on the [Context](overview.md) screen.

## Uploading a document

1. Open **Context** and click **Upload a brand document** on the Brand documents card (or **Manage brand documents** once you have some).
2. Click **Upload document** and choose a file.
3. Hi, Moose reads the file, splits it into sections, tags each section, and indexes it for search. Progress shows on the screen.

**Supported files:** Markdown, plain text, Word (`.docx`) and PDF.

Headings become sections, so a document with clear headings works best. A message house with a heading for each pillar, persona and product will split cleanly. A PDF that is one long block of text will not.

Large documents can take several minutes to tag. You can leave the screen while it runs. Hi, Moose keeps working and lets you know when the document is ready, with a notification if the app is in the background.

**Limits:** up to 25 documents per project, and about 500,000 characters per document.

## How sections are sorted

Every section gets a type. The type decides when Hi, Moose uses it.

| Type | What goes here | When it's used |
|---|---|---|
| **Rules** | How to write for this brand: voice, naming, words to use and avoid. | Always on, for every piece of work. |
| **Company core** | Positioning and identity that fits any piece. | Always on, for every piece of work. |
| **Proof** | Numbers, customers, quotes and links Hi, Moose may cite. | Pulled in when relevant. |
| **Approved copy** | Reusable text such as value propositions and boilerplates. | Pulled in when relevant. |
| **Playbooks** | Messaging for one audience, product, solution or industry. | Pulled in when relevant. |

Sections can also carry flags:

- **Always on**: the section goes into every piece of work.
- **Internal only**: the document marks this section as internal. Hi, Moose uses it to shape positioning but never quotes or paraphrases it into content.
- **Draft**: the section is marked as a draft in the source document.
- **Check approval**: the source says the content needs sign-off before use.
- **Edited here**: you changed the section inside Hi, Moose.

Flags help, but they are not a guarantee. Read every draft yourself before it goes out.

### Checking and editing sections

Click **View sections** on a document to see its sections grouped by type. Click **Edit section** to fix a section's text, then **Save section**. Edited sections are marked **Edited here**.

If the screen shows **Tagged by headings only**, no model was available when the document was processed, so sections were tagged from their headings alone. Connect an OpenRouter key, load a local model, or sign in to a paid plan, then replace the document to get richer tags.

## Replacing a document and version history

When your message house changes, click **Replace** and upload the new file. Hi, Moose compares it with the previous version and only re-reads the sections that changed. The document shows how many sections were added, changed and removed.

The last five versions of each document stay listed under **Versions**. Uploading an identical file does nothing.

Click **Remove** to delete a document with all of its versions and sections. Briefs and drafts you already wrote keep their content.

## See what Moose will use

Before you write, you can check which sections a piece of work would pull in. Under **See what Moose will use**, type a topic or the kind of piece you plan to write (for example, "LinkedIn post about AI code security for security engineers") and click **Show sections**.

Hi, Moose lists the sections it would pull in. Click **Show the exact text Moose receives** to see the full text it would get. If nothing matches closely enough, your always-on rules still apply.

## Fill Brand Voice and Brand Truth from your documents

If your documents already describe your voice, audience, offerings and competitors, you don't need to retype them into [Brand Voice](brand-voice.md) and the [Brand Truth Profile](brand-truth-profile.md).

1. On the Brand documents screen, click **Fill profiles from documents**.
2. Hi, Moose reads your documents and suggests values for Brand Voice and Brand Truth Profile fields.
3. Review the suggestions. Each one shows the quote from your document that backs it up.
4. Choose the fields you want and click **Apply**.

Nothing is saved until you apply it. How suggestions are checked:

- Fields that are **empty today** are checked by default.
- Fields that **differ from current** are unchecked, so your own wording wins unless you choose otherwise. The current value is shown next to the suggestion.
- A suggestion is dropped if the quoted text doesn't appear word for word in your document. The dialog tells you how many were dropped.

Fields Hi, Moose can fill:

- **Brand Voice:** brand name, summary, audience, tone, writing style, brand values, secondary brand terms, preferred and avoided terminology, and proof points.
- **Brand Truth Profile:** how AI should describe the company, ideal customer segments and notes, products and services, key capabilities, common misrepresentations, outdated narratives, preferred vocabulary and vocabulary to avoid, competitors, sensitive claims, and the most damaging mistakes.

Filling profiles needs a model: an OpenRouter key, a local model, or a paid plan.

## Where your documents are used

Once a project has brand documents, Hi, Moose uses them in:

- [Content Briefs](../../features/content-briefs.md), [blog post drafts](../../features/blog-post-draft.md), [Key Points](../../features/key-points.md) and the [FAQ Generator](../../features/faq-generator.md). Each gets your always-on rules plus the sections that best match the topic.
- [Chat](../../chat/overview.md). Your rules are part of every chat, and chat can search your documents when a question needs product, persona or proof detail.
- [Send Moose](../../send-moose/overview.md) research and the final polish pass on generated content, which both get your rules.

Brand Documents work alongside Brand Voice and the Brand Truth Profile. Those profiles stay the short summary of who you are. Your documents add the full detail behind it.

## Storage and sync

Brand documents are stored locally for the current project. On a paid plan they sync with the rest of your project, so everyone on your team gets the same documents and they're backed up. While a teammate's changes are coming in, the screen shows **Syncing from your team...**.

Removing a project removes its brand documents too.
