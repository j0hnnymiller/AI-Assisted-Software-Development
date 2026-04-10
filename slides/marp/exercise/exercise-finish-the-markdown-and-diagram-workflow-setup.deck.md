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
## Exercise: Finish the Markdown and Diagram Workflow Setup

**Setup and Objectives**

Prerequisites

- VS Code running with the required extensions installed
- A writable user settings file and keybindings file
- Basic familiarity with the Command Palette and Extensions view

Objectives

- Verify Mermaid Preview works in the editor
- Configure the multi-command workflow for markdown review
- Confirm the full environment is ready for course labs

::: column

**Activities and Success Criteria**

Activities

1. Create a small Mermaid file and preview it inside VS Code.
2. Add the `multiCommand.commands` configuration to your settings.
3. Add the markdown preview keybinding to `keybindings.json`.
4. Test the shortcut in a markdown or Marp file.
5. Run a final workstation verification pass.

```json
"multiCommand.commands": [
  {
    "command": "extension.multiCommand.execute",
    "sequence": [
      "markdown.showPreviewToSide",
      "workbench.action.copyEditorToNewWindow"
    ]
  }
]
```

```json
{
  "key": "ctrl+shift+alt+x",
  "command": "extension.multiCommand.execute",
  "args": {
    "sequence": [
      "markdown.showPreviewToSide",
      "workbench.action.copyEditorToNewWindow"
    ]
  },
  "when": "editorLangId == markdown || resourceExtname == .mdc"
}
```

Success Criteria

- Mermaid Preview renders a simple diagram successfully
- The multi-command shortcut works in a markdown or Marp file
- Your machine is ready for repository, Copilot, and slide-authoring labs

::: notes
Duration ~00:10

Use this as the capstone setup lab that turns a list of installed tools into a working authoring environment. Students often complete installs without validating workflows, so emphasize that previewing Mermaid and testing the multi-command shortcut are proof that the environment is actually usable. If the shortcut does not fire, inspect both settings and keybindings for JSON syntax issues before assuming the extension is broken. Wrap up by having learners self-assess whether they can now clone repos, open them in VS Code, use Copilot, and preview markdown-based assets without help.
:::