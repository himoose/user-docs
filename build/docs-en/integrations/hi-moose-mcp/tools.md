# Tool reference

Every tool Hi, Moose MCP offers a connected app, with what it takes and what comes back. You do not call tools yourself: the app picks the tool from what you ask. This page tells you what to ask for and what to expect.

Every tool except `list_projects` and `get_result` takes a **project**, by the name shown in Hi, Moose. Say the project name in your request when you have more than one, for example "for the Acme project".

## How long things take

| Tool | Typical time |
|---|---|
| List projects, briefs, drafts | A few seconds |
| Check site coverage | Under a minute |
| Visibility check, read an answer | A few seconds |
| Opportunities list | A few seconds to a minute |
| Content brief, draft, FAQs, key points, featured image | One to three minutes |
| AEO audit | Two to four minutes |
| Content refresh | Three to six minutes |
| Internal links | About a minute |
| Audio episode | 5 minutes for short, 9 for standard, 15 for deep |

When a tool takes longer than the app will wait, it answers "still working" with a job id. The app then uses `get_result` to pick the finished work up; ask it to check again if it does not.

## Projects and Library

### list_projects

Lists the Hi, Moose projects you can work on. Every other tool needs a project, so the app usually calls this first.

Ask: "List my Hi, Moose projects."

### list_briefs

Lists the content briefs saved in the Library for a project, newest first, up to 50. Use it when you refer to a brief made earlier.

Ask: "Show the briefs saved for Acme."

### list_drafts

Lists the drafts saved in the Library for a project, newest first, up to 50.

Ask: "Which drafts do I have in Acme?"

### get_result

Picks up work started by another tool, by job id. Waits up to a minute for it to finish. The app calls this on its own; you only need it when the app says the work is still running and you want it to check again.

## Site coverage

### check_site_coverage

Checks the latest crawl of your site for pages that already cover one or more topics.

| Input | Required | Meaning |
|---|---|---|
| topics | yes | One to fifteen short phrases, such as "SBOM generation for Python" |
| parentTopic | no | The wider subject the topics belong to, used to judge partial coverage |

For each topic it answers **covered**, **partial**, **uncovered** or **unknown**, with the closest page URLs as evidence and the date of the crawl it checked. Unknown means the check could not run for that topic, not that the site lacks it.

Ask: "Does our site already cover SCA vs SAST?"

## Content

### create_content_brief

Creates a search-informed content brief: objective, audience, rationale, keyword buckets, recommended structure and constraints, grounded in live search results, your site crawl, brand guidelines and Brand Truth.

| Input | Required | Meaning |
|---|---|---|
| topic | yes | The topic, question or working title, up to 400 characters |
| targetUrl | no | The page on your site the brief is for |
| templateType | no | The kind of content: "Blog post", "Landing page", "Comparison page", "Guide" |
| guidance | no | Requirements decided elsewhere: angle, must-include points, tone. Up to 4,000 characters. |

Returns the brief as text plus a brief id the draft tool uses. Saved in the Library.

Ask: "Write a content brief for a guide to SBOM generation for Python teams."

### create_draft

Writes a publishable first draft from a brief, in your brand's voice, grounded in the brief, Brand Truth and brand guidelines, with internal links chosen from your site crawl and a polish pass.

| Input | Required | Meaning |
|---|---|---|
| briefId | one of the two | A brief made in Hi, Moose |
| brief | one of the two | A brief written elsewhere, as text, up to 60,000 characters |
| briefTitle | no | The working title, when passing a brief as text |
| templateType | no | The kind of content, when passing a brief as text |
| guidance | no | Extra requirements, up to 4,000 characters |

Returns the draft as text plus a draft id. Saved in the Library.

Ask: "Draft the article from that brief." or "Here is a brief I wrote, draft it for Acme: ..."

### refresh_content

Refreshes content you already have. Hi, Moose reads the current content, works out the search query it targets (or uses the one you give), runs the same live research as a content brief for that query, and compares the two: what still works, what reads as stale, facts to update, what ranking and cited pages cover that your content does not, and the questions searchers ask that it does not answer.

| Input | Required | Meaning |
|---|---|---|
| url | one of the three | The live page. Best, because the comparison then uses exactly what is published. |
| draftId | one of the three | A saved draft |
| content | one of the three | The current content as text, up to 60,000 characters |
| title | no | The title, when passing content as text |
| targetQuery | no | The question or search prompt the refreshed content should win, up to 200 characters. Without it Hi, Moose detects the main query from the content and names it in the result. |
| templateType | no | The kind of content, such as "Blog post" or "Landing page" |
| guidance | no | Requirements for the refresh: sections to keep, points to add, tone. Up to 4,000 characters. |

Returns two things, both saved in the Library: a refresh brief (the comparison, a change list, and a full content brief for the updated piece) and a revised draft that keeps the current structure, voice and links and applies the changes. Download the brief from the Library as PDF, Word or Markdown when you need to make the case for the refresh internally.

Ask: "Refresh https://acme.example/guides/sbom." or "This article is two years old, refresh it for 'SBOM generation tools': ..."

### create_featured_image

Creates a featured image for an article, 1200 by 630, in your saved image style when one is set.

| Input | Required | Meaning |
|---|---|---|
| draftId | one of the two | A draft made in Hi, Moose |
| title and summary | one of the two | The article title and a short summary, up to 6,000 characters, when there is no draft |
| styleIntent | no | A wish for this one image: mood, scene, colours. The saved style still applies. |

Returns the image and a link to the PNG. The file is also saved on the host device.

Ask: "Make a featured image for that draft, evening light, no people."

### create_faqs

Writes frequently asked questions with answers for one piece of content, in your brand's voice, plus FAQPage schema markup ready to paste into the page. On paid accounts the questions are researched from real search behaviour first.

| Input | Required | Meaning |
|---|---|---|
| draftId | one of the two | A saved draft |
| url | one of the two | A published page on your site |
| guidance | no | Audience, questions that must appear, tone. Up to 4,000 characters. |

Ask: "Write FAQs for https://acme.example/guides/sbom."

### create_key_points

Writes the key points of one piece of content: short, quotable statements in your brand's voice that answer engines can lift.

| Input | Required | Meaning |
|---|---|---|
| draftId | one of the two | A saved draft |
| url | one of the two | A published page on your site |
| guidance | no | Audience, points that must appear, tone. Up to 4,000 characters. |

Ask: "Give me key points for the SBOM guide draft."

## Audits and links

### run_aeo_audit

Runs an answer engine optimization audit on one piece of content: a score out of 100, category scores (structure, extractability, citation potential, trust signals, freshness, answer readiness and more), the issues found, and concrete changes with proposed text.

| Input | Required | Meaning |
|---|---|---|
| url | one of the three | A live page. Best, because technical checks such as AI crawler access and page dates run only on a live page. |
| draftId | one of the three | A saved draft |
| content | one of the three | The content as text, for a page that is not live yet. Up to 50,000 characters. |
| targetQuery | no | The question or search prompt the content should win, up to 200 characters. Without it Hi, Moose infers one. |

On paid accounts live search evidence is included.

Ask: "Audit https://acme.example/guides/sbom for the query 'SBOM generation tools'."

### find_internal_links

Plans internal links for one piece of content using the crawl of your own site. Returns two lists: pages this content should link out to, each with the anchor text to use, and existing pages that should add a link pointing to this content, each with the anchor text to use on that page. Pages already linked either way are left out.

| Input | Required | Meaning |
|---|---|---|
| url | one of the three | A page on your site, live |
| draftId | one of the three | A saved draft |
| content | one of the three | The content as text, up to 50,000 characters |
| title | no | The title, when passing content as text |

Results cover the pages crawled so far and name the crawl date. Pages published since the last crawl are not included.

Ask: "Plan internal links for the SBOM guide draft."

## AI search visibility

### visibility_check_topic

Answers "are we showing up in AI search for X" from the visibility results Hi, Moose has stored. Pass the question in your own words; Hi, Moose matches it to the tracked prompts, in any language.

| Input | Required | Meaning |
|---|---|---|
| question | yes | The topic or question, up to 400 characters |
| lookbackDays | no | How many days of stored results to read. Default 90. |
| engine | no | Only this engine, by name, such as "ChatGPT" |

Returns, per engine, whether the brand was mentioned or cited in the latest run and in an earlier run, the mention and citation rates over the window, a short excerpt from the latest answer where the brand appeared, the prompts matched, and other brands seen. Each excerpt carries an answer id for the next tool. Results cover the tracked prompts on the tracked engines only, never the whole of AI search. It reads stored results and never runs new checks.

Ask: "Are we showing up in AI search for SBOM generation?"

### visibility_get_answer

Fetches one stored answer by its answer id: the prompt, engine, date, whether the brand was mentioned or cited, the sources the engine listed, the scorer's notes, and the full answer text. The text is what the engine wrote at the time.

Ask: "Show me the full ChatGPT answer from that result."

### visibility_list_opportunities

Returns the ranked work queue Hi, Moose builds from stored visibility results, the same rows as the Opportunities tab. Each row names the exact gap, the one-sentence next step, the priority with its reasons, how consistently the gap held across runs, the effort, the status the team set, and an opportunity id.

| Input | Required | Meaning |
|---|---|---|
| lookbackDays | no | Days of stored results to read. Default 7, the same as the Opportunities tab. At most 90. |
| limit | no | Rows to return, best first. Default 10, at most 25. |
| action | no | Only one kind of row: `create-coverage`, `improve-page`, `earn-inclusion`, `correct-description` or `investigate-change` |
| priority | no | `high`, `medium` or `low` |
| includeClosed | no | Also return rows marked done, dismissed or snoozed. Default false. |
| opportunityId | no | An id from an earlier result. Returns the full evidence for that one row instead of the list. |

The five kinds of row: **create-coverage** (no page of yours answers a prompt competitors win), **improve-page** (a page of yours is cited or is the closest match but the brand is left out or ranked behind), **earn-inclusion** (a third-party page the engines cite names competitors but not you), **correct-description** (answers repeat a claim about the brand that needs checking) and **investigate-change** (the brand was named or cited before and is not any more).

Ask: "What should we work on for AI search this week?" then "Show me the evidence for the first one."

## Audio

### create_audio

Creates a "listen to this article" episode: a two-voice spoken conversation about the content, rendered as an MP3 and hosted by Hi, Moose, plus the HTML snippet for the embeddable player.

| Input | Required | Meaning |
|---|---|---|
| url | one of the three | A live page |
| draftId | one of the three | A saved draft |
| content and title | one of the three | The article as text, 1,200 to 200,000 characters, with its title |
| length | no | `short` (about 4 minutes), `standard` or `deep`. Default short. |
| hostVoice, guestVoice | no | Two different voices. Default Sulafat and Fenrir. |
| language | no | Narration language. Default: the language of the content. |
| focus | no | What the conversation should focus on, up to 500 characters |
| theme, layout, color, showTitle, customTitle, showTranscript, hideAttribution | no | The player look, see below |

The [audio settings page](https://himoose.com/hi-moose-mcp/audio/) lets you hear every voice, pick the length, language and player look, and copy a settings line to paste into the chat. While the episode renders the host device works on nothing else. If the result says the episode is still rendering, the next tool picks it up a few minutes later.

Ask: "Turn https://acme.example/guides/sbom into audio, short, with Zephyr and Charon."

### get_audio_embed

Returns the player snippet for an existing episode, with a new look when player fields are passed. The audio is not re-rendered. Also the way to pick up an episode that was still rendering.

| Input | Required | Meaning |
|---|---|---|
| audioId | yes | The id from the episode |
| theme | no | `dark`, `light` or `auto`. Default dark. |
| layout | no | `full` or `compact`. Default full. |
| color | no | Accent colour as hex, for example `#5688b0` |
| showTitle, customTitle | no | Show a title line, or set your own |
| showTranscript | no | Show the transcript button. Default true. |
| hideAttribution | no | Hide the "Audio by Hi, Moose" line. Paid plans only. |

Ask: "Give me the compact light player for that episode."

## What the tools cannot do

They cannot change settings or team members, change what Hi, Moose tracks, start visibility runs, or delete anything. For dashboards and automation, use the [Hi, Moose API](../developer-api.md).
