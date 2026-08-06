# Brand Truth Profile

## What this helps you do

The Brand Truth Profile is a machine-readable source of truth for how AI should describe your company — what you sell, who you serve, and what you should never be confused with. Hi, Moose uses it during [Visibility](../../visibility/overview.md) runs to detect when an AI engine's answer misrepresents your brand or repeats an outdated narrative, instead of leaving that judgment to a generic sentiment score.

Like Brand Voice, the Brand Truth Profile is scoped to the current [project](../projects.md).

All fields are optional, but the more you fill in, the more precisely Hi, Moose can flag misrepresentation and recommend corrections.

## Fields you can fill in

### Core description

- **How should AI describe your company today?** — the canonical one-or-two sentence description you'd want to see in a ChatGPT, Perplexity, Gemini, or Google AI answer.
- **Who is your ideal customer today?** — selected from common segments (SMBs, mid-market, enterprise, agencies, ecommerce brands, and more), plus free-text notes.

### What you offer

- **Products, services, or product categories AI should know you offer** — the major things AI should know you provide; you don't need to list every feature.
- **Features or capabilities AI should mention** — one per line. Helps Hi, Moose detect when AI leaves out something important.

### Where descriptions go wrong

- **What does AI or the market often get wrong about your company?** — chosen from common misrepresentation patterns: wrong customer type, wrong product category, outdated positioning, missing new products or features, wrong competitors, overstating or understating capability, confusion with another brand, and more.
- **One example of something AI or the market gets wrong** — a concrete example to ground the pattern above.
- **Outdated descriptions we should flag** — old categories, target customers, or limitations that no longer apply.
- **Which AI mistakes would be most damaging?** — the highest-stakes categories of error (wrong company description, wrong target customer, incorrect pricing or availability, negative or misleading sentiment, brand confusion, and more).

### Vocabulary

- **Words or phrases AI should use** — preferred vocabulary, one per line.
- **Words or phrases AI should avoid** — vocabulary to avoid, one per line.

### Competitive context

- **Main competitors or alternatives** — 3–5 competitors, alternatives, or categories of tools, each with an optional note (e.g. "positioned as enterprise-only"). Used to test comparison prompts.
- **Comparisons worth monitoring** — specific comparison or alternative-category searches Hi, Moose should watch (e.g. "best AEO tools for small businesses").

### Trust and evidence

- **Customer questions AI should answer correctly** — diagnostic questions aligned with how prospects actually shop.
- **Claims AI should be careful with** — pricing, performance, certifications, or other claims that need careful, qualified language.
- **Pages or sources that prove your current positioning** — specific pages, docs, or case studies to treat as important proof, each with an optional note.
- **Sources already known to be outdated or inaccurate** — third-party pages, directories, or prior AI citations known to describe your company incorrectly, each with a note on what's wrong.

## How it's used

During a visibility run, Hi, Moose loads the project's Brand Truth Profile (when it has meaningful content) and uses it to evaluate each AI response for misrepresentation or drift — comparing the response against your canonical description, offerings, competitors, preferred/avoided vocabulary, and known misrepresentation patterns, rather than just checking whether your brand name shows up.

## How this differs from Brand Voice

[Brand Voice](brand-voice.md) is about **style** — how your brand should sound. The Brand Truth Profile is about **facts** — what's actually true about your company, and which incorrect narratives to watch for. Fill in Brand Voice to shape tone; fill in Brand Truth Profile to catch AI getting the facts about you wrong.

## Cloud sync

Like Brand Voice, the Brand Truth Profile is stored locally for the current project by default. Syncing it to the cloud — so it's backed up and shared with your team — requires a paid plan. See [Context](overview.md) for details.

## Competitor tracking

The competitor list here is shared with [Visibility Settings](../../visibility/settings.md). Competitors added in either place appear in both, and feed [Share of Voice, competitor citations, and gaps](../../visibility/competitors.md).
