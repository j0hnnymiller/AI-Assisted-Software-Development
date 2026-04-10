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
## Exercise: Install VS Code and the Core Course Extensions

**Setup and Objectives**

Prerequisites

- GitHub account available for Copilot sign-in
- GitHub CLI already installed is helpful but not required
- VS Code not yet installed, or an existing install you can update

Objectives

- Install Visual Studio Code and confirm the `code` command works
- Add the extensions used throughout the course
- Prepare the editor for Copilot, Mermaid preview, and markdown workflows

::: column

**Activities and Success Criteria**

Activities

1. Install Visual Studio Code and ensure the `code` command is available in PATH.
2. Open VS Code and verify the integrated terminal works.
3. Install the following extensions from the Extensions view or the command line.
4. Restart VS Code if extension activation or sign-in prompts do not appear immediately.

```bash
code --version
code --install-extension GitHub.copilot
code --install-extension GitHub.copilot-chat
code --install-extension vstirbu.vscode-mermaid-preview
code --install-extension ryuta46.multi-command
```

Success Criteria

- `code --version` works from a terminal
- VS Code opens successfully and shows the installed extensions
- Copilot, Copilot Chat, Mermaid Preview, and multi-command are all present in the editor

::: notes
Duration ~00:15

Frame VS Code as the primary lab environment rather than just another editor choice. The main thing to validate here is not only installation, but that the `code` shell command works, because later workflows depend on opening repos and files from the terminal. If extension installation is slow, reassure learners that marketplace delays are normal and have them verify extension IDs carefully instead of repeatedly clicking install. Transition by noting that the next step is to make the AI features operational, not merely installed.
:::