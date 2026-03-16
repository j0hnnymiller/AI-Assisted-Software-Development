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

## AI-Assisted GitHub Pull Requests

## Faster, Better PRs with GitHub Copilot

::: notes
Welcome to this session on using AI to improve the pull request workflow. GitHub Copilot and related AI tools can dramatically reduce the friction of creating, reviewing, and merging pull requests.

**Timing**: 1 minute for title slide

**Key Points**:

- PRs are a critical communication artifact in software development
- AI can help at every stage: drafting, describing, reviewing, and summarizing
- The goal is not to replace human judgment but to reduce toil

**Delivery**: Open by asking the audience how much time they spend writing PR descriptions or waiting for code review. Frame AI assistance as a way to reclaim that time.

**Transition**: "Let's look at where AI fits in the pull request lifecycle."
:::

---

## The Pull Request Lifecycle

```
Code Changes → PR Creation → Review → Merge
```

AI can assist at **every stage**:

| Stage               | AI Assistance                  |
| ------------------- | ------------------------------ |
| Writing code        | Copilot completions            |
| Drafting the PR     | Generated description          |
| Code review         | Inline suggestions & summaries |
| Addressing feedback | Guided fixes                   |
| Final merge         | Automated checks               |

::: notes
**Timing**: 2 minutes

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

> 💡 Use `gh pr create` with Copilot in the CLI, or the **GitHub web editor** with AI suggestions

::: notes
**Timing**: 3 minutes

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

## Writing Effective PR Prompts

Getting great AI output starts with **good context**:

```markdown
# Good PR Description Prompt Pattern

## What changed

- Brief bullet list of changes

## Why it changed

- Business context or issue reference

## How to test

- Step-by-step verification
```

Ask Copilot: _"Generate a PR description for these changes that explains the business impact"_

::: notes
**Timing**: 3 minutes

**Key Points**:

1. AI output quality is proportional to the context you provide
2. Referencing the issue number or user story helps Copilot add business context
3. Structuring the prompt mirrors the structure you want in the output

**Template to Share**:
Show the three-section template on screen. Encourage teams to add this as a PR template in `.github/pull_request_template.md` so Copilot has a consistent structure to fill.

**Pro Tip**: Commit messages also feed into the PR description. Good commit messages mean better AI-generated PRs.

**Transition**: "Let's look at how AI helps on the review side of the process."
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
**Timing**: 3 minutes

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
**Timing**: 2 minutes

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
**Timing**: 3 minutes

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

---

## Automated PR Checks with AI

Integrate AI into your **CI/CD pipeline**:

```yaml
# .github/workflows/pr-review.yml
- name: Copilot Code Review
  uses: github/copilot-code-review@v1

- name: AI Security Scan
  uses: github/advanced-security-action@v2
```

- Run AI review on **every PR automatically**
- Block merges on **critical AI-flagged issues**
- Post AI summary as a **PR comment**

::: notes
**Timing**: 3 minutes

**Key Points**:

1. Automating AI checks ensures consistency—every PR gets the same baseline review
2. This is not a replacement for human review but a first pass that catches common issues
3. Teams can configure severity thresholds to control which findings block merges

**Architecture Note**: These actions run in GitHub Actions and post results as PR check statuses, integrating with existing branch protection rules.

**Pro Tip**: Combine AI code review with conventional linting and testing so developers get a single, unified set of feedback.

**Caution**: Avoid too many automated checks that create noise. Focus on high-signal rules.

**Transition**: "Let's look at some real-world patterns teams are using today."
:::

---

## Real-World Patterns

### Teams using AI for PRs report:

- **40-60% reduction** in time-to-first-review
- **Clearer PR descriptions** leading to fewer questions
- **Faster onboarding** — new devs produce PR-ready code sooner
- **Higher review quality** — reviewers catch logic issues, not style issues

> Source: GitHub internal data, 2024–2025 Copilot usage studies

::: notes
**Timing**: 2 minutes

**Key Points**:

1. The biggest gains are in communication overhead, not code writing speed
2. New team members benefit most because AI helps them match team standards faster
3. Reviewers focus on what matters—architecture, correctness, maintainability—when AI handles style and common issues

**Story to Share**: A team at a large enterprise reduced PR cycle time from 3 days to less than 1 day by combining AI-generated descriptions, automated checks, and Copilot Autofix. The change was primarily in the communication and iteration loop, not the code itself.

**Transition**: "Before we wrap up, let's talk about best practices."
:::

---

## Best Practices

✅ **Do**

- Review and personalize AI-generated descriptions
- Use Copilot Chat to ask questions during review
- Enable Copilot Autofix for security alerts
- Add a PR template to guide AI output

❌ **Avoid**

- Merging AI-generated descriptions without reading them
- Treating AI review as a substitute for human judgment
- Over-automating to the point of alert fatigue

::: notes
**Timing**: 3 minutes

**Key Points**:

1. AI is a collaborator, not an autopilot. Human oversight remains essential.
2. The PR template acts as a contract between the author and the AI—providing structure improves output quality
3. Alert fatigue is real. Configure automated checks to surface only actionable findings.

**Common Mistakes**:

- Teams that enable every available check end up ignoring them all
- Developers who merge AI descriptions verbatim lose the "why" context that only they know
- Over-reliance on AI review can erode human review skills over time

**Audience Interaction**: "What guardrails does your team have around AI-generated content in PRs?"

**Transition**: "Let's summarize what we covered and talk about next steps."
:::

---

## Getting Started

### Start small, build habits:

1. **Today**: Use Copilot to draft your next PR description
2. **This week**: Try Copilot Chat during your next code review
3. **This sprint**: Add a PR template to guide AI descriptions
4. **This quarter**: Automate AI checks in your CI pipeline

> 📖 Resources:
>
> - [GitHub Copilot for PRs](https://docs.github.com/copilot)
> - [GitHub Advanced Security](https://docs.github.com/en/code-security)
> - [gh CLI](https://cli.github.com)

::: notes
**Timing**: 2 minutes

**Key Points**:

1. Gradual adoption works better than a big-bang rollout
2. Starting with PR descriptions has no risk and immediate value
3. As teams build confidence, they can layer in automated checks

**Call to Action**: Encourage each attendee to write their next PR description with Copilot's help and note the difference.

**Resources**: Point to the GitHub Copilot docs and the gh CLI documentation for hands-on exploration.

**Transition**: "Let's open it up for questions."
:::

---

## Summary

### AI transforms the PR workflow:

| Without AI             | With AI                                       |
| ---------------------- | --------------------------------------------- |
| Manual PR descriptions | Auto-generated, structured descriptions       |
| Line-by-line review    | AI-summarized highlights + human logic review |
| Slow feedback loops    | Inline fix suggestions from review comments   |
| Inconsistent standards | Automated checks on every PR                  |
| Slow onboarding        | New devs match team standards faster          |

**Pull requests become a collaboration between humans and AI**

::: notes
**Timing**: 2 minutes

**Key Points**:

1. The table reinforces the before/after contrast—anchor the value proposition
2. The key insight: PRs shift from a documentation burden to a collaborative artifact
3. The human role shifts from doing all the communication work to reviewing and approving AI-assisted communication

**Closing Message**: AI doesn't change what a good PR looks like—it reduces the effort required to create one. The standards, the review culture, and the human judgment remain essential.

**Final Question for Audience**: "What's one part of your PR workflow you'd like AI to help with first?"

**Thank the audience and open for Q&A.**
:::
