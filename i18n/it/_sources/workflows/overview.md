# Workflows

## What this helps you do

Workflows turn a recurring operator pattern into a background routine described in plain language, instead of you re-running the same manual steps every time your AI visibility changes. Rather than a blank automation builder, each workflow is built from an opinionated, editable sentence — you fill in the blanks, Hi, Moose runs it.

!!! note "Availability"
    Workflows require a paid plan — BYOK Premium, BYOK Agency, or any managed plan. Preview Mode can monitor one project locally, but reusable workflows aren't included, and BYOK Free doesn't include them either. See [Account Types & Plans](../getting-started/account-modes.md).

## The first choice: what is this workflow for?

Every workflow starts with one decision: **"This workflow is for [ new / current ] content."**

- **Current content** runs the **[Recover Lost Visibility](recover-lost-visibility.md)** recipe — detect a drop in how your brand shows up, find the affected page, and stage a fix.
- **New content** runs the **[Create New Content](create-new-content.md)** recipe — scan your tracked topics on a schedule and stage brand-new content for gaps it finds.

## Managing multiple workflows

You aren't limited to one workflow:

- Click **New Workflow** to create another, independently configured one.
- Switch between saved workflows from the workflow selector, which shows each one's name and whether it's **Enabled** or **Paused**.
- Rename a workflow by clicking its name.
- **Pause**/**Enable** a workflow without deleting its configuration.
- **Remove** a workflow entirely — this only removes it from this device and doesn't affect other members of your workspace, since workflow definitions are local and personal rather than shared team state.
- **Save** persists your changes; Hi, Moose also auto-saves once a workflow has everything it needs to run.

## Running a workflow

- **Create New Content** workflows can be triggered immediately with **Run now**, in addition to running on their configured schedule. Results land in your [Inbox](../inbox/overview.md) for review — Hi, Moose links you straight there when a run finds something.
- **Recover Lost Visibility** workflows don't have a manual run button; they evaluate automatically every time a new [visibility](../visibility/overview.md) run completes, comparing it against the previous run.

## Before you can build a workflow

Workflows need at least one tracked visibility topic before they can watch for changes. If your project doesn't have one yet, Hi, Moose prompts you to set up [Visibility](../visibility/overview.md) tracking first, then return to Workflows.
