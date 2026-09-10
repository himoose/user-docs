# Send Moose

## What this helps you do

Send Moose is where you hand over a job instead of running it yourself. You describe the work in plain language — "find out who's being recommended instead of us for project management software and why", "check whether our pricing page still matches what's on our competitors' comparison pages" — and Moose goes and does it, using the web and everything Hi, Moose already knows about your project.

It's the difference between a chat that answers you and an agent that goes to work. Chat is a conversation; Send Moose is a job you dispatch and come back to.

Find it in the sidebar under **Send Moose**.

!!! warning "Send Moose is experimental"
    It's in the app and it works, but it's the newest and least settled thing in Hi, Moose. Watch the quality of what comes back, and watch your token use on paid plans — Scout and Skeptic run in the cloud even when Moose himself runs locally.

## What Moose brings with him

A general web agent starts from nothing and has to be told everything. Moose starts already connected to your project:

| He can read | What that means |
|---|---|
| Your visibility data | Overview, Share of Voice, competitors, topics, prompts, and what changed |
| Your site index | Crawled pages, what changed on them, internal links, and your [entity graph](../features/entity-graph.md) |
| Your AEO history | Past audits and their detail, citation context, crawler access, topic coverage |
| [Google Search Console](../integrations/google-search-console.md) | Your real query and page data, queried iteratively |
| Your [Library](../library/overview.md) | Briefs, drafts, key points, FAQs and audits you've already made |
| Past jobs | What he found and decided on earlier runs in this project |

He can also run a live [visibility check](../visibility/overview.md) or an [AEO audit](../features/aeo-audits.md) mid-job when the answer needs one, rather than telling you to go and run it.

## Sending a job

Describe the work and press **Send Moose**. Two options shape how he runs it:

- **Deep work** — let the job take hours if it needs them: many more pages, many more searches, more check-ins. Use it when the question is genuinely broad, not for a quick lookup.
- **Attach files** — up to six files per job, as context he reads while working.

You can tick **Notify me when Moose is done** and leave. The job keeps running whether or not you're watching it, and whether or not you stay on the screen.

## Watching him work

**Watch browser** opens the browser instance Moose is using, so you can see the pages as he reads them. **Take control** hands the browser to you if he's stuck on something you can clear in a second — a cookie wall, a login — and **Back to the job** hands it back.

You can close that window whenever you like. Moose keeps working.

## Moose, Scout and Skeptic

On the free plan, Moose works alone.

Paid plans add two other agents to the job:

- **Scout** finds angles Moose didn't think to look for.
- **Skeptic** challenges the evidence before it reaches your result.

You can talk to any of them mid-job from the thread — tell Moose something, ask Scout for another angle, ask Skeptic to push harder on a claim. **Keep going** and **Check another five results** extend a run that stopped somewhere useful.

Scout and Skeptic always run in the cloud through OpenRouter, even when Moose himself is running on a local model, so they cost tokens.

## When Moose needs you

Two things stop a job and wait for you rather than guessing:

- **Needs your approval** — Moose is about to commit an action on a real website, like pressing a button on a form. He shows you the exact button and waits for **Approve and continue** or **Don't do it**.
- **Needs your help** — he's blocked on something only you can answer. Type an answer, or press **Let Moose decide** to have him make the call himself.

Nothing gets published, sent, or submitted anywhere without you approving it first. That holds on scheduled runs too.

## Reading the result

A finished job has four tabs:

- **Result** — what he found, written up.
- **Collaboration** — how it went, and who contributed what: notes Scout added, challenges Skeptic raised, times you steered.
- **Sources** — every page he opened, with the evidence he captured from each.
- **Activity** — the full run, filterable by tools or agents.

From there you can **Save to Library**, **Download report**, or ask a follow-up about the result in [chat](../chat/overview.md). Any files Moose saved during the job appear under **Files Moose saved** — open them, save a copy, or show them in their folder. He can save CSV, Markdown, plain text, PDF and Word files.

## Content Moose creates

Moose can produce real Hi, Moose artifacts as part of a job, not just a written answer: a **content brief**, a **draft**, **key points**, **FAQs**, or an **AEO audit**. These land in your [Library](../library/overview.md) like anything else, and the job's result links straight to them.

## Running a job on a schedule

**Run on a schedule** turns a one-off job into a standing one — every day, weekdays, weekly, or monthly, at one or more times of day.

Scheduled jobs appear under **Scheduled jobs** and can be paused, resumed, or deleted. They run unattended: Moose makes the small decisions himself, and still never publishes or sends anything without your approval.

## Past jobs

Every job is kept under **Past jobs**, searchable and filterable by **Done**, **Called back**, **Didn't finish** and **Blocked**, grouped into today, earlier this week, and earlier. Jobs are scoped to the project they were run in.

## Settings

**Send Moose settings** are saved per project:

- **Moose LLM** — Automatic uses the largest installed local model, or your plan's cloud model when local AI is off. You can pin a specific model instead.
- **Scout LLM** and **Skeptic LLM** — paid plans only, defaulting to Gemma 4 31B.
- **Content model** — which model writes the briefs, drafts and FAQs he creates. Defaults to the same one Moose is using.
- **Search engine** — which engine he searches with.

Anything marked **Uses tokens** runs in the cloud through OpenRouter rather than on your computer. Deep work jobs run longest, so they cost the most.

## What it needs

- **A local model, or a paid plan.** Moose thinks on a Gemma model that runs on your computer. Download it once from the prompt on the screen and jobs cost nothing to run. Paid plans can put him on a cloud model instead. If you've turned local AI off and you're on the free plan, Send Moose tells you and offers to turn it back on.
- **A website on the project**, for jobs about your own site, brand or competitors. General web jobs work fine without one.

## Where to go from here

- **[Chat](../chat/overview.md)** — for work you want to steer turn by turn instead of dispatching.
- **[Workflows](../workflows/overview.md)** — for a fixed recipe that runs on a trigger rather than an open-ended job.
- **[Library](../library/overview.md)** — where the reports and content from a job are kept.
