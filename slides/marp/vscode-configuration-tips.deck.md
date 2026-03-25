---
ai_generated: true
model: "anthropic/claude-sonnet-4.6"
operator: "johnmillerATcodemag-com"
chat_id: "vscode-configuration-tips-20260314"
prompt: |
  create a marp deck describing VS Code Configuration Tips. Custom keyboard shortcuts;
  Multi-command extension for Marp slides
started: "2026-03-14T15:54:58Z"
ended: "2026-03-14T15:55:30Z"
task_durations:
  - task: "draft"
    duration: "00:00:32"
total_duration: "00:00:32"
ai_log: "ai-logs/2026/03/14/vscode-configuration-tips-20260314/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---

## Why Customize VS Code?

- Default shortcuts cover **common tasks** — not YOUR workflow
- Every repeated action you automate = less context switching
- Shortcuts + extensions compound over time into **significant productivity gains**
- Marp authors especially benefit: build, preview, export all from the keyboard

::: notes
Duration ~00:01

Set the "why" before diving into the "how." Emphasize that configuration investment pays dividends every single day.

Key talking points:

- Most developers use VS Code for years without ever opening keybindings.json
- Even one well-chosen shortcut can
- For Marp workflows specifically, running pandoc or opening side-by-side preview are prime candidates

Ask the audience: "How many of you have a custom keyboard shortcut right now?" — gauge the room.

Transition: "Let's look at how VS Code's shortcut system actually works."
:::

---

## How VS Code Keyboard Shortcuts Work

- **GUI**: `File → Preferences → Keyboard Shortcuts` (`Ctrl+K Ctrl+S`)
- **JSON**: `keybindings.json` — full control, version-controllable
- Each binding has three fields:
  - `key` — the chord or combination
  - `command` — VS Code command ID
  - `when` — optional context condition

```json
{
  "key": "ctrl+shift+b",
  "command": "workbench.action.tasks.runTask",
  "args": "Build Slides",
  "when": "editorLangId == markdown"
}
```

::: notes
Duration ~00:02

Walk through the three-field structure of a keybinding entry. The `when` clause is the most powerful and least-used feature — it scopes shortcuts to contexts like "only when a Markdown file is open."

Demo tip: Open the Keyboard Shortcuts editor live, search for a command, and show how clicking the pencil icon edits keybindings.json directly.

Transition: "Now let's see how to discover command IDs — the key to writing your own shortcuts."
:::

---

## Discovering Command IDs

- Open the **Command Palette** (`Ctrl+Shift+P`)
- Right-click any command → **Copy Command ID**
- Or check **Keyboard Shortcuts** list (right-click → Copy Command ID)
- Built-in commands: `workbench.*`, `editor.*`, `terminal.*`
- Extension commands: shown in the same list after install

```
workbench.action.terminal.new
editor.action.formatDocument
markdown.showPreviewToSide
```

::: notes
Duration ~00:02

This is the practical "lookup" step developers skip, then wonder why they can't write shortcuts. Stress that every command in the palette has an ID — including extension commands.

Demo: Open the command palette, type "Marp", right-click "Open Preview", and copy its ID. Then show adding it to keybindings.json.

Transition: "Let's look at some concrete shortcut recipes for Marp authors."
:::

---

## Useful Shortcuts for Marp Authors

| Shortcut       | Command                                       | Purpose                   |
| -------------- | --------------------------------------------- | ------------------------- |
| `Ctrl+Shift+V` | `markdown.showPreviewToSide`                  | Side-by-side Marp preview |
| `Ctrl+Shift+E` | `workbench.view.explorer`                     | Toggle file explorer      |
| `Ctrl+\``      | `workbench.action.terminal.toggleTerminal`    | Toggle terminal           |
| `Ctrl+K P`     | `workbench.action.files.copyPathOfActiveFile` | Copy file path            |
| Custom         | `tasks.runTask` → `Export PDF`                | One-key PDF export        |

::: notes
Duration ~00:02

Go through each shortcut and explain the Marp use case:

- Side-by-side preview is essential when authoring slides — you want to see layout changes immediately
- File explorer toggle helps when switching between slide files and assets
- Terminal toggle is needed to run pandoc or Marp CLI commands
- Copy path is handy when referencing images or linking between files
- The custom task shortcut is a preview of what we'll build with Multi-command

Transition: "Now let's explore the Multi-command extension, which lets us chain commands together."
:::

---

## Introducing the Multi-command Extension

- **Extension ID**: `ryuta46.multi-command`
- Lets you **bind a single key to a sequence of commands**
- Configured in `settings.json` under `multiCommand.commands`
- Each sequence can include:
  - Built-in VS Code commands
  - Extension commands
  - Terminal commands (via tasks)
  - Delays between steps

::: notes
Duration ~00:02

Introduce the extension and explain the core problem it solves: VS Code shortcuts fire exactly one command. Multi-command lets you chain many into a single keystroke — like a macro system.

Install tip: Show `Ctrl+Shift+X`, search "multi-command", install ryuta46.multi-command.

Transition: "Let's see what the configuration looks like."
:::

---

<!-- layout: Two Content -->

## Multi-command: Configuration Structure

**`settings.json`**

```json
"multiCommand.commands": [
  {
    "command": "multiCommand.marpBuildAndPreview",
    "label": "Marp: Build & Open Preview",
    "sequence": [
      "workbench.action.files.save",
      "markdown.showPreviewToSide",
      {
        "command": "workbench.action.tasks.runTask",
        "args": "Marp Export PDF"
      }
    ]
  }
]
```

::: column

**`keybindings.json`**

```json
{
  "key": "ctrl+shift+m",
  "command": "multiCommand.marpBuildAndPreview"
}
```

**Mental model**

- `settings.json` defines the macro.
- `keybindings.json` assigns the trigger.

::: notes
Duration ~00:03

Walk through the structure carefully:

1. `command` — a unique ID you choose; must start with `multiCommand.`
2. `label` — shown in the command palette
3. `sequence` — array of commands fired in order; can be strings (command IDs) or objects with args

Point out the "save first" pattern — always save before building so the exported file reflects current edits.

Demo: Paste this into settings.json and fire the shortcut live.

Transition: "Let's look at a complete Marp workflow using Multi-command."
:::

---

## Marp Slide Workflow with Multi-command

**One shortcut does all of this:**

1. 💾 Save the current file
2. 🔍 Open Marp preview side-by-side
3. 📄 Run `marp --pdf` via VS Code task
4. 📂 Reveal output file in Explorer

```json
"sequence": [
  "workbench.action.files.save",
  "markdown.showPreviewToSide",
  { "command": "workbench.action.tasks.runTask", "args": "Marp Export PDF" },
  "revealFileInOS"
]
```

::: notes
Duration ~00:02

Paint the before/after picture:

- BEFORE: Save manually → open terminal → type marp command → switch to Finder/Explorer → open PDF
- AFTER: Press `Ctrl+Shift+M`, everything happens in sequence

This is the kind of workflow automation that pays for the time you spent configuring it within the first session.

Transition: "Let's also set up the VS Code task that runs Marp CLI."
:::

---

<!-- layout: Two Content -->

## VS Code Task: Marp Export PDF

**`.vscode/tasks.json`**

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Marp Export PDF",
      "type": "shell",
      "command": "marp",
      "args": [
        "${file}",
        "--pdf",
        "--output",
        "${fileDirname}/${fileBasenameNoExtension}.pdf"
      ],
      "group": "build",
      "presentation": { "reveal": "silent" }
    }
  ]
}
```

::: column

**What matters**

- `${file}` targets the active deck
- `--pdf` can be replaced with `--pptx` when needed
- Output stays beside the source file
- `"reveal": "silent"` keeps focus on authoring

::: notes
Duration ~00:02

Walk through the task definition:

- `${file}` — the currently open file (your active .md slide deck)
- `--pdf` — export to PDF format; can swap for `--pptx` for PowerPoint
- `${fileDirname}/${fileBasenameNoExtension}.pdf` — output file next to source with same name
- `"reveal": "silent"` — terminal doesn't pop up visually, keeps focus on slides

Prerequisite: Marp CLI must be installed (`npm install -g @marp-team/marp-cli`).

Transition: "Before we wrap up, let me share a few more power-user tips."
:::

---

<!-- layout: Two Content -->

## Power-User Tips

**Keyboard shortcut tips**

- Use `when: "editorLangId == markdown"` to scope Marp shortcuts
- Chain `Ctrl+K` as a leader key for shortcut groups
- View all active shortcuts with `Ctrl+K Ctrl+S`

::: column

**Multi-command and sync tips**

- Add `{ "command": "vscode.delay", "args": 500 }` when a command is async
- Use `label` to find macros in the Command Palette
- Keep sequences short: 3 to 5 steps
- Turn on **Settings Sync** so keybindings and settings follow you across machines

::: notes
Duration ~00:02

These are the tips that separate power users from casual users. Call out the `when` clause again — it's underused but prevents shortcut conflicts across file types.

The delay tip is important for Multi-command: if a task launches a process, subsequent commands may fire before it finishes. A small delay solves this.

Settings Sync is a quality-of-life tip that resonates well — many developers maintain multiple machines or reinstall VS Code periodically.

Transition: "Let's look at where to find these settings in your own VS Code."
:::

---

<!-- layout: Two Content -->

## Where to Find These Files

**User-level files**

- `keybindings.json`
  `~/.config/Code/User/`
  Open via `Ctrl+K Ctrl+S` and the icon in the top-right.
- `settings.json` (user)
  `~/.config/Code/User/`
  Open via `Ctrl+,` and the icon in the top-right.

::: column

**Workspace-level files**

- `settings.json` (workspace)
  `.vscode/settings.json`
  Create manually.
- `tasks.json`
  `.vscode/tasks.json`
  Open via `Ctrl+Shift+P` and `Tasks: Configure Task`.

**Tip**

- Workspace `.vscode/` settings are version-controllable and should ship with the slides repo.

::: notes
Duration ~00:02

Clarify the difference between user-level and workspace-level settings:

- User settings apply globally across all projects
- Workspace settings apply only to the current folder and can be shared with teammates via Git

For slide authors, storing tasks.json and workspace settings.json in the slides repository is best practice — anyone who clones the repo gets the same Marp build workflow instantly.

Windows paths: `%APPDATA%\Code\User\` instead of the Linux/Mac paths shown.

Transition: "Let's wrap up with a quick summary."
:::

---

## Summary

✅ **Custom shortcuts** = less mouse, more flow

- Use `keybindings.json` for full control
- Scope with `when` to avoid conflicts

✅ **Multi-command** = keyboard macros for VS Code

- Chain save → preview → export in one keystroke
- Define sequences in `settings.json`, bind in `keybindings.json`

✅ **VS Code tasks** = repeatable Marp CLI builds

- Store in `.vscode/tasks.json` and commit with your repo

> Start with **one shortcut** you use every day. Build from there.

::: notes
Duration ~00:01

Reinforce the three takeaways clearly. The closing advice — "start with one shortcut" — combats the paralysis of trying to configure everything at once.

Call to action ideas:

- "Open keybindings.json right now and add one shortcut before you leave"
- "Install Multi-command and try the Marp build sequence this week"
- "Commit your .vscode/ folder to your next slide repo"

Thank the audience and open for questions.
:::
