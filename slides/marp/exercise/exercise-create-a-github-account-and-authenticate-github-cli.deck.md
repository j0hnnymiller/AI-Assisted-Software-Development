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
## Exercise: Create a GitHub Account and Authenticate GitHub CLI

**Setup and Objectives**

Prerequisites

- Git installed successfully
- Browser access and a working email account
- Permission to sign in through the browser on this machine

Objectives

- Create or verify a GitHub account for the course
- Install GitHub CLI locally
- Authenticate `gh` so later repository and PR exercises work from the terminal

::: column

**Activities and Success Criteria**

Activities

1. Sign in to GitHub or create a new account at `https://github.com/signup`.
2. Install GitHub CLI using direct download, Chocolatey, Winget, or Homebrew.
3. Run the CLI version check.
4. Authenticate with the browser flow and choose `GitHub.com` plus `HTTPS` when prompted.
5. Validate access by listing repositories from the terminal.

```bash
gh --version
gh auth login
gh repo list
```

Success Criteria

- `gh --version` returns installed version details
- `gh auth status` or `gh repo list` works without an authentication error
- Your GitHub account is ready for later fork, clone, issue, and PR workflows

::: notes
Duration ~00:15

Explain that this step converts GitHub from a browser-only experience into a workflow tool students can automate from the terminal. During the hands-on portion, watch for confusion between Git authentication and GitHub CLI authentication because learners often assume one automatically sets up the other. If anyone is blocked in the browser flow, have them retry with `gh auth logout` followed by `gh auth login` rather than improvising token storage mid-exercise. End by confirming that everyone can run a harmless `gh` command successfully before proceeding.
:::