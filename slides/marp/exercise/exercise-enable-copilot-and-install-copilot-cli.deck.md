---
ai_generated: true
model: "openai/gpt-5.4@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "exercise-tool-installation-deck-20260329"
prompt: |
  create an marp deck of exercise slides from the content in #file:AIASD-tool-installation.md
started: "2026-03-29T00:00:00Z"
ended: "2026-03-29T00:15:00Z"
task_durations:
  - task: "exercise deck authoring"
    duration: "00:15:00"
total_duration: "00:15:00"
ai_log: "ai-logs/2026/03/29/exercise-tool-installation-deck-20260329/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---
## Exercise: Enable Copilot and Install Copilot CLI

**Setup and Objectives**

Prerequisites

- VS Code installed with GitHub Copilot extensions
- GitHub account with Copilot access or trial enabled
- GitHub CLI authenticated on the local machine

Objectives

- Sign in to Copilot inside VS Code
- Verify inline suggestions or chat access work
- Install the `gh-copilot` extension for terminal assistance

::: column

**Activities and Success Criteria**

Activities

1. Sign in to GitHub from VS Code and authorize Copilot.
2. Create a small test file and verify suggestions or Copilot Chat respond.
3. Install the GitHub Copilot CLI extension.
4. Run one `suggest` command and one `explain` command to validate the terminal workflow.

```bash
gh extension install github/gh-copilot
gh copilot suggest "create a new git branch"
gh copilot explain "git rebase -i HEAD~3"
```

Success Criteria

- Copilot works inside VS Code for chat or inline assistance
- `gh copilot suggest` returns a usable command suggestion
- `gh copilot explain` returns a readable explanation of a CLI command

::: notes
Duration ~00:10

This slide is where students first see the course AI workflow become tangible, so keep the validation lightweight and immediate. Encourage them to test Copilot with a tiny prompt or comment instead of jumping into a large coding task, because fast feedback here builds confidence and exposes account or licensing issues early. If they do not see suggestions, check sign-in state and subscription status before debugging editor behavior. Close by contrasting editor-based Copilot help with terminal-based Copilot CLI help so both modes are clearly understood.
:::