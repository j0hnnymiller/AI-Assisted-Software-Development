---
marp: true
theme: default
paginate: true
ai_generated: true
model: "openai/gpt-5.4"
operator: "johnmillerATcodemag-com"
chat_id: "effective-prompts-technical-debt-20260322"
prompt: |
  create a marp deck explaining the following content:

  ## Section 9: Effective Prompts for Technical Debt (Duration: ~00:08:30)

  **Time Range**: 01:22:35 - 01:31:05

  ### Key Topics

  - Crafting effective technical debt prompts
  - GitHub issue management
  - Copilot integration with GitHub
  - Issue creation and assignment

  ### Subsection 9.1: Prompt Components

  #### Required Elements

  - **Clear description of debt**: What problem exists
  - **Constraints and architectural rules**: Beyond instruction files
  - **Expected outcomes**: What success looks like
  - **Required test updates**: Testing strategy
  - **Documentation updates**: Required documentation
  - **Provenance requirements**: Not in instruction files

  #### Benefits

  - Faster remediation
  - Consistent application of fixes
  - Reduced manual effort
  - Standardized approach

  ### Subsection 9.2: GitHub Integration

  #### Issue Management via Copilot

  **Method 1: Direct Issue Creation**

  - Command: "Post issue #6 to the GitHub [repo]"
  - Copilot creates issue in GitHub
  - Can specify labels, assignees, etc.

  **Challenges Encountered**:

  - Wrong repository selected initially
  - Required full repository name format: `owner/repository`
  - Need to enable issues in repository settings

  **Resolution**:

  - Provide explicit repository path
  - Verify settings in GitHub
  - Use format: `owner/repository-name`

  #### Assigning Issues to Copilot

  **Paid Subscription Feature**:

  1. Create issue in GitHub
  2. Assign to @copilot
  3. Copilot creates work-in-progress branch
  4. Implements solution autonomously
  5. Sends notifications on progress
  6. Creates pull request when complete

  **Requirements**:

  - Enterprise license OR
  - Pro Plus subscription
  - Repository in appropriate organization (for Enterprise)

  **Student Discussion**:

  - Free plan users cannot access this feature
  - Enterprise repos must be in enterprise org
  - Chris Bishop confirmed org requirement

  ### Subsection 9.3: Live Demonstration

  **Example Workflow**:

  1. Created issue from file content
  2. Attempted to post to GitHub
  3. Encountered repository selection issue
  4. Corrected repository reference
  5. Issue successfully created
  6. Assigned to @copilot
  7. Copilot began autonomous implementation

  **Observations**:

  - Parallel execution: Issue #5 implementation running simultaneously
  - Notifications received as work progresses
  - WIP (work-in-progress) branch created automatically
started: "2026-03-22T03:53:23Z"
ended: "2026-03-22T04:05:00Z"
task_durations:
  - task: "slide authoring"
    duration: "00:09:00"
  - task: "provenance and README updates"
    duration: "00:03:00"
total_duration: "00:12:00"
ai_log: "ai-logs/2026/03/22/effective-prompts-technical-debt-20260322/conversation.md"
source: "johnmillerATcodemag-com"
---

# Effective Prompts for Technical Debt || The Art of Complaining Productively to Your AI

---

## Effective Prompts for Technical Debt

- Focus: prompts, issues, and Copilot workflow
- Goal: turn vague cleanup into executable work

::: notes
Duration ~00:09

Open by explaining that technical debt work often fails because requests are too vague. This section shows how to convert cleanup ideas into structured prompts that can be executed, tracked, and reviewed. Emphasize that the topic is not just prompt wording; it is also about how prompts connect to GitHub issues and Copilot workflows. Set expectations that the audience will leave with a repeatable pattern they can apply immediately. (~1 minute)
:::

---

## What a Strong Technical Debt Prompt Includes

Every prompt should define the work clearly

- **Debt description** - the concrete problem to fix
- **Constraints** - architecture, guardrails, and non-negotiables
- **Expected outcome** - what success looks like
- **Test updates** - how validation must change
- **Documentation updates** - what artifacts must be refreshed
- **Provenance requirements** - what must be logged beyond instructions

::: notes
Walk through each component as part of a checklist, not as optional advice. The key message is that a good prompt reduces ambiguity before implementation starts. Highlight that provenance and documentation are easy to forget when teams focus only on code, so they need to be called out explicitly in the request. Frame this slide as the minimum contract between the requester and the AI assistant. (~1.5 minutes)
:::

---

## Why Structured Prompts Matter

Better prompts create better remediation workflows

- Faster remediation because the target is explicit
- More consistent fixes across contributors and sessions
- Less manual follow-up after the first prompt
- A standardized approach for recurring debt categories

> Better prompt quality means less cleanup after the cleanup work

::: notes
This is the business-value slide. Explain that structured prompts reduce rework because they front-load clarity on tests, docs, and guardrails. Connect this to team scalability: if multiple people or multiple models work on similar debt items, consistent prompt structure produces more predictable outputs. Use the quote as the memorable takeaway for why investing in the prompt upfront saves time later. (~1 minute)
:::

---

## GitHub Integration - Direct Issue Creation

Copilot can help move prompt content into GitHub issues

- Example command: `"Post issue #6 to the GitHub owner/repository-name"`
- Copilot can create the issue directly in GitHub
- Labels, assignees, and metadata can be included

::: notes
Present this as the first automation step after prompt authoring. The audience should understand that Copilot can bridge from local artifact or prompt text into the GitHub issue system, but repository targeting must be explicit. Stress the practical lesson from the demo: natural language is often not enough when multiple repositories are in play. Encourage attendees to always state the full repository name to avoid misrouting work. (~1.25 minutes)
:::

---

## Assigning an Issue to @copilot

Paid plan workflow for autonomous implementation
  1. Create the issue in GitHub
  2. Assign the issue to `@copilot`
  3. Copilot creates a work-in-progress branch
  4. Copilot implements the requested solution
  5. Notifications report ongoing progress
  6. Copilot opens a pull request when complete

**Requirements**
  - Enterprise license or Pro Plus subscription
  - Enterprise workflow requires the repository in the correct org

::: notes
Describe this as the jump from assisted drafting to autonomous execution. The value is not just code generation; it is the full workflow of branch creation, progress updates, and PR delivery. Be clear that this is a paid capability and that organizational placement matters for enterprise scenarios. This helps the audience distinguish between what everyone can do and what requires higher-tier licensing. (~1.25 minutes)
:::

---

## Reusable Prompt Template for Technical Debt

Use a structure like this for repeatable results

```text
Fix the following technical debt: [describe the problem].
Constraints: [architecture rules, guardrails, scope limits].
Expected outcome: [what should be true when done].
Tests to update: [unit, integration, regression, CI expectations].
Documentation to update: [README, docs, comments, diagrams].
Provenance required: [logs, metadata, linked artifacts].
```

- Treat this as a starting template, then specialize by debt type

::: notes
Give the audience a concrete artifact they can copy into their own workflow. Explain that the template is intentionally simple because its power comes from completeness, not clever phrasing. Encourage them to tailor the constraints and validation sections based on the type of debt item, such as refactoring, security cleanup, or test hardening. Close by connecting the template back to the earlier benefits: clarity, consistency, and reduced manual follow-up. (~1 minute)
:::

---

## Key Takeaways

- Strong prompts define the debt, constraints, outcomes, tests, docs, and provenance
- Assigning to `@copilot` can automate branch, progress, and PR creation
- Technical debt becomes easier to manage when prompts and issues work together

::: notes
Close by tying prompt quality to execution quality. The audience should leave with the idea that technical debt management is not just about identifying problems; it is about packaging them so AI and GitHub workflows can act on them reliably. Re-emphasize the two most practical habits: always include validation and always specify the exact repository. End with a suggested next step: take one existing debt item and rewrite it using the template from the previous slide. (~1 minute)
:::
