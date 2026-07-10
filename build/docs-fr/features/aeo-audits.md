!!! info "Not translated yet"
    This page is not available in your language yet, so it is shown in English.

# AEO Audits

## What this helps you do

An AEO (Answer Engine Optimization) audit scores how ready a page is to be understood, retrieved, and cited by AI systems like ChatGPT, Google AI Overviews, Perplexity, and Gemini — then gives you a prioritized, evidence-backed action plan to improve it.

This replaces one-off "AEO tips" with a durable, comparable artifact: every audit produces a scorecard and an action plan you can revisit, and later audits on the same page can verify whether your changes actually moved the score.

## What gets scored

The overall score is a weighted composite of eight categories, each scored 0–100:

1. **Freshness** — recency and update signals.
2. **Structure** — headings, lists, tables, and paragraphing an answer engine can parse.
3. **Semantic Clarity** — how tightly the content aligns to your target query and intent.
4. **Extractability** — how easily an answer engine can lift a definition, fact, or key point.
5. **Citation Potential** — attribution and sourcing signals, based on the page's external reference links.
6. **Comprehensiveness** — coverage of the subtopics people and answer engines expect for the query.
7. **Trust Signals** — consistency, specificity, and qualified claims in how the page presents attribution and sourcing. This category doesn't verify claims against outside sources — it measures how well-attributed and specific the page's own claims are.
8. **Answer Readiness** — direct-answer placement near the top, one idea per block, clear referential language (avoiding vague "this/it/they"), and consistent entity naming. Scoring is language-aware across English, German, Spanish, French, Italian, and Portuguese.

The audit also tracks Engagement, Entity Recognition, and Media Enrichment signals, though these don't factor into the overall score or appear on the scorecard.

## Infrastructure and retrieval checks

Alongside content scoring, every audit checks whether an answer engine can actually retrieve the page at all:

- **AI crawler access** — checks robots.txt rules for each of the specific AI crawler tokens used by OpenAI, Anthropic, Perplexity, Google, and Bing (covering their training, indexing, and live-fetch crawlers separately, since a site can block one and allow another). A blocked retrieval or indexing crawler is flagged as critical; a blocked live-fetch agent is medium priority; a training-only block is noted as a neutral, legitimate policy choice that doesn't affect citations.
- **Server-side rendering / client-rendered-shell detection** — most AI crawlers do not execute JavaScript. If a page's critical content only appears after client-side rendering, that's flagged as a critical, headline-level finding rather than a minor technical note, since it's a retrieval problem that comes before any content optimization matters.
- **Retrieval hygiene** — checks a sample of internal links for broken links and redirect chains.
- **Bing index presence** — checks whether the page appears to be indexed by Bing, since Microsoft Copilot and parts of ChatGPT search rely on Bing's index. Verdicts are deliberately conservative: an inconclusive result is reported as inconclusive rather than guessed, and a "not listed" verdict is only shown when the check has real signal to support it.

## Off-page and coverage context

- **Citation landscape** — when live research runs, the audit reports which domains an answer engine actually cited for the target query, whether the audited site is among them, and whether third-party sources (community sites, review sites, Wikipedia, YouTube) dominate the answer. This is disclosed as context you mostly can't fix by editing your own page, rather than folded into the score.
- **Fan-out coverage** — checks the page against related queries an answer engine might expand the original query into (People Also Ask questions, related searches, secondary keywords). When several of these aren't addressed on the page, that becomes a concrete "cover these related questions" recommendation.

## Evidence tiers on recommendations

Every issue and recommendation is labeled with how strong the evidence behind it is:

- **Proven** — retrieval preconditions with strong empirical support (crawler access, server-side rendering, working links, search-engine indexing).
- **Directional** — supported by large-scale observational research, but not a guarantee (answer-first placement, freshness, structural clarity).
- **Best-practice** — plausible and low-cost, but not proven to move AI citations (adding statistics, quotations, or additional sourcing polish).

The audit does not recommend schema/JSON-LD markup, `llms.txt` files, or keyword-stuffing style tactics as ways to improve AI citation, since current research doesn't support treating those as citation levers.

## How many recommendations you get

Recommendation count is based on how many real issues are found, weighted by the page's overall score — a page with real problems will see more recommendations, and a page that already scores well will see fewer, sometimes none at all. The count is never padded to hit a fixed target.

## Running an audit

1. Provide a live URL or paste a draft, along with the target query someone would use to find this content.
2. Hi, Moose captures a bounded snapshot of the page's content and structure, using the static (non-JavaScript-rendered) version of the page as the primary evidence, since that's closer to what most AI crawlers actually see.
3. When useful, it collects real answer-engine or citation evidence for the target query.
4. If your project has a connected [Google Search Console](../integrations/google-search-console.md) property for this URL, first-party search performance is factored into prioritization and recommendation safety — it does not change the underlying AEO score.
5. Hi, Moose scores the page, creates a baseline (or verifies against a prior baseline), and assembles the audit into a durable artifact with an explicit next-action plan.

## Verifying improvement

Because each audit is saved as a baseline, running a new audit on the same page after making changes produces a **verification result** — showing whether the score actually improved, not just whether you made edits.

## Integrity

AEO audits never fabricate evidence. If Hi, Moose can't collect the evidence or complete a scoring step for real, the audit fails explicitly and tells you why, rather than presenting a guess as a finished result. If live search and competitor research can't complete for a Paid Managed audit, the audit still finishes using the page evidence it has, with an explicit note that live research was unavailable for that run.

## Entitlements

- **Preview Mode (Free)** includes a small number of real audits per month using Hi, Moose's included AI usage.
- **BYOK Free and BYOK Premium** run audits locally using your own OpenRouter key.
- **Paid Managed** accounts use Hi, Moose's managed AI usage under your account's normal token balance — there's no separate "audit credit" currency to track.

## Next actions from an audit

An audit's action plan routes directly into other capabilities — generating a [content brief](content-briefs.md), staging an [edit and preview](drafts-and-publishing.md), or adding FAQs or key points — so the audit is a starting point for action, not just a report.

