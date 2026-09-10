# Competitors & Share of Voice

## What this helps you do

Answer the question your own numbers can't: when an AI assistant recommends something in your category, how often is it you, and who's getting picked instead?

Find it under **Visibility → Competition**.

## Setting up competitors

Add competitors in **Visibility → Settings → Competitor tracking**. Each one takes a name and, optionally, a website.

This list is shared with your [Brand Truth Profile](../getting-started/context/brand-truth-profile.md), so competitors added in either place show up in both.

How many are tracked in visibility runs depends on your plan: **5 on Preview Mode and BYOK Free, 15 on every paid plan**. The settings screen shows the number and warns you if your list is longer, so you know only the first ones are being tracked.

Three to five real competitors works better than a long list. These are the brands you're genuinely compared against, not everyone in the category.

## Share of Voice

**Share of Voice** is each brand's slice of the attention in AI answers across the period — but not every mention counts the same.

Being named first in an answer is worth more than being named sixth, because that's the name a reader takes away. So each mention is weighted by where the brand lands in the answer:

| Position in the answer | Weight |
|---|---|
| 1st | 1.00 |
| 2nd | 0.70 |
| 3rd | 0.50 |
| 4th | 0.35 |
| 5th | 0.25 |
| 6th or later | 0.15 |

A mention where no clear position could be read counts as 0.50. On top of that, an answer that **cites the brand's own site** adds another 0.50, because a citation is a stronger signal than a name-drop.

Each brand's weighted score is then divided by the total across every tracked brand to give its share.

The Competition tab leads with your rank — "You are 3rd" — and the ranked list underneath shows every tracked brand with its share. **Mention share** and **citation share** sit beside it as the plain, unweighted counts, so you can see the raw picture alongside the weighted one.

!!! note "Why the weighted number can disagree with the raw count"
    You can be mentioned as often as a competitor and still trail them on Share of Voice, if they keep landing first in the answer and you keep landing fourth. That gap is the point of the metric — it's telling you the mentions are there but the prominence isn't, which is a different problem with a different fix.

!!! warning "Share of Voice is not Mention Rate"
    These are two different numbers and they move independently.

    **Share of Voice** is your weighted slice of the total brand attention. It's competitive: a competitor can push it down without anything changing on your side.

    **Mention Rate** (on the Overview tab) is the share of tracked prompts where your brand was mentioned at all. It's absolute, it's unweighted, and it ignores competitors entirely.

    Your Mention Rate can rise while your Share of Voice falls, if competitors gained faster than you did. Both are worth watching, for different reasons.

## Share of Voice trend

The trend chart plots either **Share of Voice** or **Mention Rate** over time, so you can see whether a shift was you gaining, a competitor gaining, or the whole category getting noisier.

## Top Competitor Citations

Which competitor pages AI engines are actually citing as sources. This is the most directly actionable panel on the tab — these are the specific URLs winning the citations you want, and they tell you what the answer engines currently consider the best source on those questions.

Compare it against **Top Cited Pages** on the Overview tab, which shows the same thing for your own domain.

## Competitor Gaps

Questions where a competitor showed up in an AI answer and your brand did not.

Each gap shows which competitors appeared and which engines it was seen in, with a badge:

- **No visibility** — your brand doesn't appear for this question in any engine.
- **Partial** — your brand does appear for this question, just not in every engine. The row lists which engines you do show up in.

Partial rows often need no action at all. A question where you appear in four engines out of five isn't the same problem as one where you appear in none, and the badge is there so you can tell them apart at a glance.

If the list is truncated, narrow the date range or filters to see the rest.

## Where competitor data comes from

Competitor mentions and citations are extracted from the same visibility run observations as your own. Nothing extra runs, and no separate crawl of competitor sites happens for these panels. If a run failed or a model was unavailable, those observations are excluded rather than counted as an absence.

## In the executive report

Share of Voice, top competitor citations, and competitor gaps are all included in the exported [executive report](overview.md#exporting), so the competitive picture goes to clients and stakeholders without you rebuilding it by hand.
