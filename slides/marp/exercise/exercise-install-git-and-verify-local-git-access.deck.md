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
## Exercise: Install Git and Verify Local Git Access

**Setup and Objectives**

Prerequisites

- Local admin rights or permission to install software
- A terminal you can reopen after installs
- Internet access for downloads or package managers

Objectives

- Install Git using the method that fits your platform
- Confirm Git is available from the terminal
- Understand why Git is the dependency for later course steps

::: column

**Activities and Success Criteria**

Activities

1. Choose one install path for your platform: direct download, package manager, or Homebrew.
2. Install Git and close the installer completely.
3. Reopen your terminal so PATH changes are picked up.
4. Run a version check and confirm Git responds.
5. If Git is still missing, switch terminals or restart the shell before troubleshooting further.

```bash
git --version
```

Success Criteria

- `git --version` returns a version string
- You can explain why Git must be installed before GitHub CLI and repository labs
- You know which install path you used on your machine

::: notes
Duration ~00:10

Start by framing Git as the first hard dependency in the toolchain, not just a nice-to-have utility. Encourage students to pick one install method only so they do not create PATH confusion by mixing direct installers and package managers on the same machine. When learners hit `command not found`, have them fully restart the terminal first because that resolves many setup issues without deeper debugging. Close by asking for a quick verbal check that everyone can see a Git version before moving to account and GitHub work.
:::