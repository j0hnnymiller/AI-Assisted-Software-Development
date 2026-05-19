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

# Exercise: AIASD Tool Installation || Workstation Setup

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
