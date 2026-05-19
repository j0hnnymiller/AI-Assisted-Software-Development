---
ai_generated: true
model: "anthropic/claude-sonnet-4.6"
operator: "johnmillerATcodemag-com"
chat_id: "ai-assisted-pr-marp-20260314"
prompt: |
  create a marp deck describing AI assistance in creating github pull requests
started: "2026-03-14T20:03:48Z"
ended: "2026-03-14T20:10:00Z"
task_durations:
  - task: "content structuring"
    duration: "00:02:00"
  - task: "slide creation"
    duration: "00:05:00"
  - task: "speaker notes"
    duration: "00:03:00"
total_duration: "00:10:00"
ai_log: "ai-logs/2026/03/14/ai-assisted-pr-marp-20260314/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---

# AI-Assisted Pull Request Workflows || Pull Requests That Actually Get Reviewed

::: notes
Duration ~00:01

Welcome to this session on using AI to improve the pull request workflow. GitHub Copilot and related AI tools can dramatically reduce the friction of creating, reviewing, and merging pull requests.

**Key Points**:

- PRs are a critical communication artifact in software development
- AI can help at every stage: drafting, describing, reviewing, and summarizing
- The goal is not to replace human judgment but to reduce toil

**Delivery**: Open by asking the audience how much time they spend writing PR descriptions or waiting for code review. Frame AI assistance as a way to reclaim that time.

**Transition**: "Let's look at where AI fits in the pull request lifecycle."
:::

---

## The Pull Request Lifecycle

| Stage               | AI Assistance                  |
| ------------------- | ------------------------------ |
| Writing code        | Copilot completions            |
| Drafting the PR     | Generated description          |
| Code review         | Inline suggestions & summaries |
| Addressing feedback | Guided fixes                   |
| Final merge         | Automated checks               |

::: notes
Duration ~00:02

**Key Points**:

1. The PR lifecycle is a feedback loop, not a one-way street
2. Most developers focus on the code-writing stage but spend significant time on communication tasks
3. AI assistance compresses the non-coding parts of the cycle

**Examples to Share**:

- A developer who writes great code but struggles with clear PR descriptions benefits from AI drafting
- A reviewer who is overwhelmed with large PRs benefits from AI summaries

**Audience Interaction**: "Which stage do you find most time-consuming or frustrating?"

**Transition**: "Let's start with where most of the AI value is—creating the PR itself."
:::

---

## AI-Generated PR Descriptions

GitHub Copilot can **draft your PR description** based on your diff:

- Summarizes **what changed** and **why**
- Suggests **testing instructions**
- Highlights **breaking changes**
- Links related **issues and tickets**

> Use `gh pr create` with Copilot in the CLI, or the **GitHub web editor** with AI suggestions

::: notes
Duration ~00:03

**Key Points**:

1. Copilot analyzes the diff and generates a structured description automatically
2. Good PR descriptions save reviewers time and reduce back-and-forth questions
3. The AI draft is a starting point—always review and personalize it

**Demo Tip**: If demoing live, show `gh pr create` in the terminal and trigger Copilot suggestions in the description field.

**Common Pitfall**: AI descriptions can be verbose. Encourage developers to trim and focus on the "why" rather than just the "what."

**Audience Interaction**: "How many of you write a detailed PR description every time? How many leave it mostly empty?"

**Transition**: "Once the PR is open, AI continues to help on the review side."
:::

---

## AI-Powered Code Review

GitHub Copilot assists reviewers with:

- **Inline explanations** of complex code
- **Suggested improvements** with rationale
- **Security vulnerability** detection
- **Test coverage** gap identification
- **Style and convention** enforcement

> Use `@workspace` in Copilot Chat to ask questions across the entire PR diff

::: notes
Duration ~00:03

**Key Points**:

1. AI doesn't replace human reviewers—it reduces the cognitive load so reviewers can focus on design and logic
2. Copilot Chat in the PR view lets reviewers ask questions like "What does this function do?" without leaving the review
3. Security scanning tools (GitHub Advanced Security + Copilot Autofix) can suggest fixes for flagged issues

**Examples to Share**:

- Reviewer asks: "Is there a simpler way to write this?" → Copilot suggests a refactored version
- Reviewer asks: "Does this handle null input?" → Copilot analyzes and flags a potential null reference

**Audience Interaction**: "Have you used Copilot Chat during a code review? What kinds of questions did you ask?"

**Transition**: "Beyond individual comments, AI can also summarize entire PRs."
:::

---

## Copilot PR Summaries

GitHub Copilot can **summarize large PRs** automatically:

- Condenses hundreds of lines of diff into a **paragraph**
- Categorizes changes: _features, fixes, refactors_
- Flags **high-risk areas** that need closer review
- Generates a **changelog entry** from the summary

```
GitHub.com → Pull Request → Copilot Summary button
```

::: notes
Duration ~00:02

**Key Points**:

1. This feature is particularly valuable for large PRs with many files changed
2. Summaries help async teams where reviewers may not have full context
3. The summary can be copied directly into release notes or changelogs

**Demo Tip**: Show the Copilot summary button on GitHub.com if doing a live demo. Highlight how it categorizes changes.

**Pro Tip**: Teams can require a Copilot summary as part of their PR checklist to ensure all PRs are self-documenting.

**Transition**: "Now let's look at how Copilot helps you respond to review feedback."
:::

---

## Responding to Review Feedback

AI accelerates **addressing reviewer comments**:

1. Copilot suggests **code fixes** inline from review comments
2. Ask Copilot Chat: _"How do I fix this review comment?"_
3. Copilot **Autofix** resolves flagged security issues
4. Batch-address similar comments across files

> 🔁 The feedback loop closes faster when AI drafts the fix and the human approves it

::: notes
Duration ~00:03

**Key Points**:

1. The most time-consuming part of PR iteration is addressing multiple review comments
2. Copilot can read a review comment and suggest the corresponding code change
3. Autofix is especially powerful for security alerts—it not only flags the issue but provides the patched code

**Workflow to Describe**:

1. Reviewer leaves a comment: "This should use a parameterized query"
2. Developer clicks Copilot suggestion next to the comment
3. Copilot generates the parameterized version
4. Developer reviews and commits

**Audience Interaction**: "How many review cycles does a typical PR go through on your team? Could AI reduce that?"

**Transition**: "Let's talk about automating the checks that run on every PR."
:::
