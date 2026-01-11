# AEO Scoring Methodology

This page explains how the Hi, Moose AEO (Answer Engine Optimization) score is calculated and how to improve it.

### What the AEO score represents

Your AEO score (0--100) estimates how likely a page is to be:

-   Understood correctly by modern answer engines (AI Overviews, chat-based search, assistants)
-   Extracted into concise answers (quotable snippets, definitions, step lists)
-   Selected as a trustworthy, citable source for answers

We compute an overall score plus a category breakdown, then generate targeted recommendations based on the lowest-scoring categories (the highest-opportunity areas).

### Inputs we analyze (high level)

Depending on how you run the audit, the analyzer may use:

-   The page's HTML / visible content (we ignore scripts/styles and focus on human-visible text)
-   The target query you care about (what you want the page to rank/answer for)
-   Lightweight "topic context" signals from external search/overview data (used for coverage/comprehensiveness and citation alignment)

### How the overall score is computed

The overall AEO score is a weighted composite of multiple category scores. The weights are tuned to reflect how answer engines behave in practice and may evolve over time as the ecosystem changes. You'll always see the category breakdown so you can improve the parts that matter most.

### Category scores (what we measure)

Each category is scored 0--100. Here's what each one means and how to improve it.

#### 1) Freshness

Checks whether the page communicates recency and maintenance (e.g., updated dates, recent statistics, "as of" language).

-   Improve it by adding clear "last updated" signals and refreshing old stats/examples.

#### 2) Structure

Measures whether the page is organized in a way machines can parse: headings, sections, lists, and sensible paragraphing.

-   Improve it by adding descriptive headings, breaking up long blocks, and using lists where appropriate.

#### 3) Semantic Clarity (Query Alignment)

Estimates how tightly the page content aligns to the target query and intent (not just keyword stuffing).

-   Improve it by answering the exact query directly, using related concepts naturally, and ensuring the H1/H2s reflect the query's intent.

#### 4) Extractability

Measures how easy it is for answer engines to "lift" correct answers: definitions, summaries, short declarative sentences, and well-formatted key points.

-   Improve it by adding a short TL;DR or Key Points block, writing crisp definitions ("X is..."), and making important claims standalone.

#### 5) Citation Potential

Estimates the likelihood your page will be cited as a source: attributed claims, specific facts/statistics, and source-quality signals.

-   Improve it by adding reputable citations, including concrete data points, and writing quotable definitions.

#### 6) Comprehensiveness (Topic Coverage)

Checks whether you cover the major subtopics people (and answer engines) expect for the query---without drifting off-topic.

-   Improve it by expanding missing subtopics, adding common FAQs, and ensuring each section is relevant to the query.

#### 7) Factual Accuracy Signals

Evaluates trust signals around correctness: consistency, specificity, attribution, qualified claims, and up-to-date references.

-   Improve it by citing primary/reputable sources, qualifying uncertain claims, and replacing vague/general statements with verifiable detail.

#### 8) Engagement (Low-weight helper signal)

Looks for basic readability and "human helpfulness" indicators (questions, direct address, examples). This is supportive, not the main driver.

-   Improve it by adding clear examples and making the content easier to follow.

#### 9) Entity Clarity

Checks whether key entities (products, organizations, concepts) are clearly named and consistently referenced.

-   Improve it by using full names on first mention, defining acronyms once, and keeping terminology consistent.

#### 10) Media Enrichment

Looks for supporting media that improves understanding (images, diagrams, embeds). If your page includes the Hi, Moose "Listen as a Podcast" player + transcript, that also contributes because it adds crawlable, structured, first-hand content.

-   Improve it by adding relevant visuals with descriptive alt text and (when appropriate) adding the Hi, Moose player + transcript.

#### 11) Answer Readiness (Direct-answer quality)

Measures how well your page supports "answer extraction," including:

-   Direct answer placement (answer early, near the top)
-   Atomicity (one main idea per paragraph/answer block)
-   Referential clarity (avoid vague "this/it/they" without nouns)
-   Entity consistency (stable naming across the page)
-   Improve it by adding a 1--2 sentence direct answer under the H1 and rewriting key sections into short, explicit, self-contained blocks.

### How to interpret scores

-   **90--100:** Strong AEO readiness; keep content updated and maintain citations.
-   **75--89:** Solid foundation; focus on the lowest category scores to break through.
-   **<75:** You likely have "answer extraction" blockers (missing direct answer, weak structure, thin coverage, or weak attribution).

### Recommendations: how we generate them

Recommendations are derived from:

-   The lowest category scores (highest opportunity)
-   Specific diagnostic flags (e.g., multi-claim paragraphs, missing direct answer, vague references)
-   Practical best practices that improve how answer engines extract and trust answers
