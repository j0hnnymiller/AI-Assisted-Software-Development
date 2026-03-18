---
ai_generated: true
model: "anthropic/claude-sonnet-4.6"
operator: "johnmillerATcodemag-com"
chat_id: "welcome-back-slide-20260314"
prompt: |
  create a marp deck containing a slide welcoming attendees back. include a point for questions
started: "2026-03-14T15:46:54Z"
ended: "2026-03-14T15:47:00Z"
task_durations:
  - task: "draft"
    duration: "00:00:06"
total_duration: "00:00:06"
ai_log: "ai-logs/2026/03/14/welcome-back-slide-20260314/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---

## AI-Assisted Software Development

- 🎯 Ready to continue where we left off
- 💡 Today's session builds on what we've covered
- 🤝 We're all in this together — participation welcome
- ❓ **Questions are always welcome — ask anytime!**

::: notes
Welcome everyone back to the session. Take a moment to let people settle in before diving into content. Acknowledge that it's great to see everyone back and express enthusiasm for the session ahead.

Key talking points:

- Remind attendees of the previous session's topics briefly
- Emphasize that questions are encouraged at any point — not just at the end
- Set a positive, inclusive tone for the session
- If this is after a break, give people 30 seconds to get re-focused

Timing: Spend about 1-2 minutes on this slide before moving on.
Transition: "Let's pick up right where we left off..."
:::

---

## GitHub Copilot Pricing & Licensing

### What you need to know for your organization

::: notes
Introduce the topic by framing it as a decision teams need to make. Most developers have heard of Copilot, but licensing details are often misunderstood. This session clarifies the tiers and what each unlocks.

Timing: ~30 seconds on this title slide.
Transition: "Let's start with an overview of what's available."
:::

---

## Copilot Plan Overview

| Feature               | **Individual** | **Business**    | **Enterprise** |
| --------------------- | -------------- | --------------- | -------------- |
| Price                 | $10/mo         | **$19/user/mo** | $39/user/mo    |
| Code completions      | ✅             | ✅              | ✅             |
| Copilot Chat          | ✅             | ✅              | ✅             |
| Policy management     | ❌             | ✅              | ✅             |
| Org instruction files | ❌             | ✅              | ✅             |
| Enterprise features   | ❌             | ❌              | ✅             |

::: notes
Walk through the table column by column, not row by row — it helps the audience track each tier's value proposition.

Key talking points:

- Individual is for solo developers; no organizational control
- Business at $19/user/month is the sweet spot for most teams
- Enterprise adds Copilot Knowledge Bases, fine-tuning, and advanced audit logs
- All paid plans include unlimited completions and chat

Emphasize: Business tier is where most organizations should start. Enterprise is for large orgs with compliance or custom knowledge needs.

Timing: ~2 minutes. Be prepared for questions on what "policy management" means.
:::

---

## Business License — $19/user/month

- 🏢 **Centralized management** via GitHub organization settings
- 🔒 **Policy controls** — enable/disable features per org or team
- 📋 **Audit logs** — track Copilot usage across the organization
- 🚫 **Content exclusions** — block Copilot from specific files or repos
- 🌐 **Works with GitHub.com** and GitHub Enterprise Server
- ✅ No seat minimum — pay only for active users

::: notes
This is the most common license tier for companies. Focus on the operational benefits for managers and security teams, not just developers.

Key talking points:

- $19/user/month billed monthly, or discounted annually
- Admins can assign/unassign seats at any time
- Content exclusions are critical for IP-sensitive codebases (e.g., exclude `/src/proprietary/`)
- Audit logs satisfy many compliance requirements without needing Enterprise

Common question: "What counts as an active user?" — A user who has Copilot enabled in their IDE at least once in the billing cycle.

Timing: ~2 minutes.
Transition: "Now let's look at what Business adds that Individual doesn't..."
:::

---

## Business vs. Enterprise

### Business ($19/user/mo)

- Organization-wide policy management
- Org-level instruction files (`.github/instructions/`)
- Content exclusions & audit logs
- Standard model access

### Enterprise ($39/user/mo) — adds:

- 🧠 **Copilot Knowledge Bases** — index your internal docs & repos
- 🎯 **Fine-tuned models** on your private codebase
- 📊 **Advanced audit & usage analytics**
- 💬 **Copilot in GitHub.com** (PR summaries, issue chat)
- 🔐 Enhanced compliance & data residency options

::: notes
Frame this as "Business is the foundation; Enterprise is the multiplier."

Key talking points:

- Most teams won't need Knowledge Bases until they have significant internal documentation
- Fine-tuned models are a game-changer for teams with large proprietary codebases
- PR summaries (Enterprise) save meaningful time in code review workflows
- Data residency matters for EU/regulated industries

Help the audience self-select: "If you have a team under 500 and no compliance requirements, Business is probably right for you today."

Timing: ~2-3 minutes. This slide often generates the most discussion.
:::

---

## Organization-Level Instruction Files

### Business & Enterprise unlock `.github/instructions/`

```
your-org/
└── .github/
    └── instructions/
        ├── coding-standards.instructions.md   ← all repos
        ├── security-policy.instructions.md    ← all repos
        └── api-guidelines.instructions.md     ← all repos
```

- 📌 Instructions apply **automatically** to all org repositories
- 🤖 Copilot follows them in every chat and code suggestion
- ✍️ Teams can still add **repo-level** instructions that extend org rules
- 🔄 Changes propagate instantly — no developer action needed

::: notes
This feature is one of the biggest unlocks of the Business tier and often underappreciated.

Key talking points:

- Org-level instructions are like a style guide that Copilot reads before every suggestion
- Examples: "Always use our internal logger, never console.log", "Follow OWASP guidelines", "Use our DTO pattern"
- Repo-level instructions inherit from org-level; they don't replace them
- This is how you scale coding standards without code reviews catching every deviation

Demo opportunity: Show a `.github/instructions/` file with a coding standard rule, then show Copilot following it in the IDE.

Timing: ~2-3 minutes.
Transition: "Let's talk about how to get started..."
:::

---

## Getting Started

1. **Assign seats** in GitHub Org Settings → Copilot → Access
2. **Set policies** — choose which features to enable org-wide
3. **Add content exclusions** for sensitive paths
4. **Create org instruction files** in `.github/instructions/`
5. **Developers install** the Copilot extension in their IDE
6. **Monitor usage** via Audit Log or Copilot usage dashboard

> 💡 **Tip**: Start with a pilot group, gather feedback, then roll out broadly.

::: notes
Give attendees a concrete action plan to leave with.

Key talking points:

- Seat assignment is instant; developers can start using Copilot within minutes
- Recommend starting with 5-10 power users as a pilot cohort
- The usage dashboard (Enterprise) or audit log (Business) helps justify ROI
- Instruction files should be a collaborative effort — involve senior devs and architects

Common concern: "What about IP and training data?" — Reassure that Business/Enterprise plans opt out of using your code to train GitHub's models by default.

Timing: ~2 minutes.
Transition: "Any questions on licensing, pricing, or rollout?"
:::

---

## Key Takeaways

- 💰 **Business** = $19/user/month — right for most organizations
- 🏢 **Enterprise** = $39/user/month — adds Knowledge Bases & fine-tuning
- 📋 **Org instruction files** available on Business & above
- 🔒 Both plans offer policy controls and content exclusions
- 🚀 You can start small and scale — no minimum seat count

### ❓ Questions?

::: notes
Summarize the session and open the floor for questions.

Key points to reinforce:

- Business tier is the most common starting point
- Org instruction files are a high-value, low-effort win on day one
- Enterprise is worth evaluating once the team is comfortable with Business features

For questions, be ready to address:

- Billing and seat management specifics
- How instruction files interact with repo-level settings
- Data privacy and training opt-out policies
- GitHub Enterprise Server (on-prem) compatibility

Timing: Spend remaining session time on Q&A. Don't rush this slide.
:::

---

## VS Code Configuration Tips

### Custom Keyboard Shortcuts & the Multi-command Extension

::: notes
Welcome the audience and frame the session. VS Code is infinitely configurable, but most developers use only default settings. Today we'll look at two high-leverage customizations: custom keyboard shortcuts and the Multi-command extension—especially useful for Marp slide authors.

Timing: ~30 seconds on the title slide.
Transition: "Let's start with why keyboard shortcuts matter."
:::

---

## Why Customize VS Code?

- Default shortcuts cover **common tasks** — not YOUR workflow
- Every repeated action you automate = less context switching
- Shortcuts + extensions compound over time into **significant productivity gains**
- Marp authors especially benefit: build, preview, export all from the keyboard

::: notes
Set the "why" before diving into the "how." Emphasize that configuration investment pays dividends every single day.

Key talking points:

- Most developers use VS Code for years without ever opening keybindings.json
- Even one well-chosen shortcut can save minutes per hour
- For Marp workflows specifically, running pandoc or opening side-by-side preview are prime candidates

Ask the audience: "How many of you have a custom keyboard shortcut right now?" — gauge the room.

Timing: ~1 minute.
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
Walk through the three-field structure of a keybinding entry. The `when` clause is the most powerful and least-used feature — it scopes shortcuts to contexts like "only when a Markdown file is open."

Demo tip: Open the Keyboard Shortcuts editor live, search for a command, and show how clicking the pencil icon edits keybindings.json directly.

Timing: ~2 minutes.
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
This is the practical "lookup" step developers skip, then wonder why they can't write shortcuts. Stress that every command in the palette has an ID — including extension commands.

Demo: Open the command palette, type "Marp", right-click "Open Preview", and copy its ID. Then show adding it to keybindings.json.

Timing: ~1.5 minutes.
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
Go through each shortcut and explain the Marp use case:

- Side-by-side preview is essential when authoring slides — you want to see layout changes immediately
- File explorer toggle helps when switching between slide files and assets
- Terminal toggle is needed to run pandoc or Marp CLI commands
- Copy path is handy when referencing images or linking between files
- The custom task shortcut is a preview of what we'll build with Multi-command

Timing: ~2 minutes.
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
Introduce the extension and explain the core problem it solves: VS Code shortcuts fire exactly one command. Multi-command lets you chain many into a single keystroke — like a macro system.

Install tip: Show `Ctrl+Shift+X`, search "multi-command", install ryuta46.multi-command.

Timing: ~1.5 minutes.
Transition: "Let's see what the configuration looks like."
:::

---

## Multi-command: Configuration Structure

`settings.json`:

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

Then bind it in `keybindings.json`:

```json
{
  "key": "ctrl+shift+m",
  "command": "multiCommand.marpBuildAndPreview"
}
```

::: notes
Walk through the structure carefully:

1. `command` — a unique ID you choose; must start with `multiCommand.`
2. `label` — shown in the command palette
3. `sequence` — array of commands fired in order; can be strings (command IDs) or objects with args

Point out the "save first" pattern — always save before building so the exported file reflects current edits.

Demo: Paste this into settings.json and fire the shortcut live.

Timing: ~2.5 minutes.
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
Paint the before/after picture:

- BEFORE: Save manually → open terminal → type marp command → switch to Finder/Explorer → open PDF
- AFTER: Press `Ctrl+Shift+M`, everything happens in sequence

This is the kind of workflow automation that pays for the time you spent configuring it within the first session.

Timing: ~2 minutes.
Transition: "Let's also set up the VS Code task that runs Marp CLI."
:::

---

## VS Code Task: Marp Export PDF

`.vscode/tasks.json`:

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

::: notes
Walk through the task definition:

- `${file}` — the currently open file (your active .md slide deck)
- `--pdf` — export to PDF format; can swap for `--pptx` for PowerPoint
- `${fileDirname}/${fileBasenameNoExtension}.pdf` — output file next to source with same name
- `"reveal": "silent"` — terminal doesn't pop up visually, keeps focus on slides

Prerequisite: Marp CLI must be installed (`npm install -g @marp-team/marp-cli`).

Timing: ~2 minutes.
Transition: "Before we wrap up, let me share a few more power-user tips."
:::

---

## Power-User Tips

**Keyboard shortcut tips:**

- Use `when: "editorLangId == markdown"` to scope Marp shortcuts
- Chain `Ctrl+K` as a leader key for shortcut groups
- View all active shortcuts: `Ctrl+K Ctrl+S`

**Multi-command tips:**

- Add `{ "command": "vscode.delay", "args": 500 }` between steps if a command is async
- Use `label` to find your macros in the Command Palette
- Keep sequences short — 3–5 steps is the sweet spot

**Sync your config:**

- Enable **Settings Sync** (`Ctrl+Shift+P` → "Settings Sync: Turn On")
- Keybindings and settings sync automatically across machines

::: notes
These are the tips that separate power users from casual users. Call out the `when` clause again — it's underused but prevents shortcut conflicts across file types.

The delay tip is important for Multi-command: if a task launches a process, subsequent commands may fire before it finishes. A small delay solves this.

Settings Sync is a quality-of-life tip that resonates well — many developers maintain multiple machines or reinstall VS Code periodically.

Timing: ~2 minutes.
Transition: "Let's look at where to find these settings in your own VS Code."
:::

---

## Where to Find These Files

| File                        | Location                | How to Open                              |
| --------------------------- | ----------------------- | ---------------------------------------- |
| `keybindings.json`          | `~/.config/Code/User/`  | `Ctrl+K Ctrl+S` → icon top-right         |
| `settings.json` (user)      | `~/.config/Code/User/`  | `Ctrl+,` → icon top-right                |
| `settings.json` (workspace) | `.vscode/settings.json` | Create manually                          |
| `tasks.json`                | `.vscode/tasks.json`    | `Ctrl+Shift+P` → "Tasks: Configure Task" |

> 💡 Workspace `.vscode/` settings are **version-controllable** — commit them with your slides repo!

::: notes
Clarify the difference between user-level and workspace-level settings:

- User settings apply globally across all projects
- Workspace settings apply only to the current folder and can be shared with teammates via Git

For slide authors, storing tasks.json and workspace settings.json in the slides repository is best practice — anyone who clones the repo gets the same Marp build workflow instantly.

Windows paths: `%APPDATA%\Code\User\` instead of the Linux/Mac paths shown.

Timing: ~1.5 minutes.
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
Reinforce the three takeaways clearly. The closing advice — "start with one shortcut" — combats the paralysis of trying to configure everything at once.

Call to action ideas:

- "Open keybindings.json right now and add one shortcut before you leave"
- "Install Multi-command and try the Marp build sequence this week"
- "Commit your .vscode/ folder to your next slide repo"

Thank the audience and open for questions.

Timing: ~1 minute.
:::

---

<!-- _class: lead -->

## Course Modules

- Intro
- **▶ Module 1 - LLM**
- Module 2 - Copilot for Teams
- Module 3 - Models and Context

---

<!-- _class: lead -->

# Module 1 - LLM

---

## Module 1 - LLM

- Large Language Models

---

## Large Language Models

### How they work — and why developers should care

::: notes
Set the stage: LLMs are the engine behind GitHub Copilot, ChatGPT, Claude, and every other AI coding tool. Understanding how they work helps developers use them more effectively and set realistic expectations.

No deep math required — focus on intuition and mental models. This is a conceptual overview, not a research lecture.

Timing: ~30 seconds on title slide.
Transition: "Let's start with the big picture of what an LLM actually is."
:::

---

## What Is a Large Language Model?

> A statistical model trained to **predict the next token** given all preceding tokens.

- Trained on **trillions of tokens** of text (code, books, web pages)
- Learns **patterns, relationships, and structure** in language
- Not a database — it doesn't store facts, it learns **weights**
- Generates output one token at a time, probabilistically

### Key insight

**LLMs don't "know" things — they learn what text tends to follow other text.**

::: notes
This is the most important conceptual slide. Many developers expect LLMs to behave like search engines or databases — they don't.

Key talking points:

- "Next token prediction" sounds simple but at scale it forces the model to learn grammar, logic, context, and even reasoning
- "Weights" are just numbers — billions of floating point values that encode everything the model learned
- Probabilistic output means the same prompt can produce different answers — this is by design, controlled by "temperature"
- Analogy: autocomplete on your phone, but trained on all of human writing

Common misconception to address: "Does Copilot look up my code in a database?" — No. It generates completions based on learned patterns.

Timing: ~2 minutes.
:::

---

## Tokenization — Breaking Text Apart

### Text → Numbers (before the model sees anything)

```
Input:  "Hello, world!"
Tokens: ["Hello", ",", " world", "!"]
IDs:    [15496, 11, 995, 0]
```

```
Input:  "def calculate_tax(income):"
Tokens: ["def", " calculate", "_tax", "(", "income", "):"]
```

- A **token** ≈ ~4 characters or ¾ of a word on average
- The model only ever sees **token IDs**, never raw text
- Tokenization affects **cost**, **context limits**, and **model behavior**
- Rare words split into multiple tokens → less efficient

::: notes
Tokenization is often overlooked but explains many "weird" LLM behaviors.

Key talking points:

- GPT-4 uses ~100,000 tokens in its vocabulary (tiktoken)
- Context window limits (e.g., "128k tokens") are token limits, not character limits
- Why does Copilot sometimes mishandle unusual variable names? Tokenization — rare strings get split awkwardly
- Code tokenization differs from prose — identifiers often split at underscores, camelCase boundaries

Practical implication for developers:

- Long variable names consume more tokens than short ones
- Copy-pasting large files into chat uses tokens fast
- Understanding tokens helps estimate cost when using API

Interactive moment: Ask "How many tokens do you think this slide is?" — good engagement exercise.

Timing: ~2-3 minutes.
:::

---

## The Transformer Architecture

### The breakthrough that made modern LLMs possible (2017)

```
Input Tokens
     ↓
[Embedding Layer]      ← tokens → vectors
     ↓
[Attention Layers] ×N  ← "what matters given what came before?"
     ↓
[Feed-Forward Layers]  ← learn patterns and transformations
     ↓
[Output Layer]         ← probability over next token
```

- **Self-attention** lets every token "look at" every other token
- Processes the **entire context window at once** (not word-by-word)
- Stacked in **layers** — deeper = richer understanding
- GPT-4 has ~1.8 trillion parameters across hundreds of layers

::: notes
You don't need to explain the math — focus on the intuition of attention.

Key talking points:

- Before Transformers: RNNs processed text sequentially (slow, forgot early context)
- Transformers process everything in parallel — that's why they scale so well on GPUs
- Self-attention intuition: "When I see the word 'it' in a sentence, which earlier word does 'it' refer to?" Attention figures this out
- Layers build up from syntax → semantics → reasoning as you go deeper

Analogy for attention: Imagine reading a legal contract. When you hit a pronoun like "the aforementioned party," your brain jumps back to find who that is. That's attention.

Why this matters for developers: Larger context windows (more tokens processed at once) = Copilot can see more of your codebase at once = better suggestions.

Timing: ~3 minutes. This is the most technical slide — keep it high-level.
:::

---

## Self-Attention — The Core Idea

### How the model decides what to focus on

> **"The trophy didn't fit in the suitcase because it was too big."**
> What does "it" refer to?

- Each token computes **Query**, **Key**, and **Value** vectors
- Attention score = how much each token should influence the current one
- Model learns which relationships matter during training
- Multiple **attention heads** capture different relationship types simultaneously

### In code:

```
"def process(data):"  →  model attends to "def" when predicting
                          what comes after "(data):"
```

::: notes
Use the trophy/suitcase example — it's a classic from the research literature and immediately intuitive.

Key talking points:

- Q/K/V is just a learned lookup mechanism — don't get lost in the math
- Multiple heads: one head might learn syntax relationships, another semantic, another positional
- This is why LLMs understand that a closing brace `}` should match an opening one several lines earlier
- Attention is also why very long prompts can "distract" the model — it has finite attention capacity

Practical tip: When using Copilot, relevant context near your cursor gets higher attention weight. Keep related code nearby when you want better completions.

Timing: ~2-3 minutes.
:::

---

## The Training Process

### Phase 1: Pre-training

```
Raw text (internet, books, code, papers)
          ↓
    Tokenize everything
          ↓
    For each token: predict next token
          ↓
    Compare prediction to actual → compute loss
          ↓
    Backpropagation → update billions of weights
          ↓
    Repeat trillions of times on thousands of GPUs
```

- Months of training, millions of dollars in compute
- Produces a **base model** that completes text — but isn't yet "helpful"

::: notes
Pre-training is where the model learns language, code, and world knowledge.

Key talking points:

- The objective is deceptively simple: predict the next token. But at scale it forces the model to learn everything
- Training data quality matters enormously — garbage in, garbage out
- GitHub Copilot's base model was trained on public GitHub repos (billions of lines of code)
- A "base model" after pre-training will complete text but may write offensive content, refuse nothing, and ramble — it needs the next phase

Scale reference: GPT-3 used 45TB of text data. Training ran on ~10,000 A100 GPUs.

Why developers care: The pre-training corpus determines what languages, frameworks, and patterns the model knows well. Copilot knows React better than a niche internal framework.

Timing: ~2-3 minutes.
:::

---

## The Training Process

### Phase 2: Fine-tuning & Alignment

**Supervised Fine-Tuning (SFT)**

- Train on curated prompt → ideal response pairs
- Teaches the model to be helpful and follow instructions

**Reinforcement Learning from Human Feedback (RLHF)**

- Human raters rank model outputs
- A reward model learns human preferences
- The LLM is optimized to maximize reward score

**Result**: A model that is helpful, harmless, and honest

```
Base model: "The capital of France is Paris. The capital of Spain is..."
Aligned model: "The capital of France is Paris."  ← stops when done
```

::: notes
This phase is what separates "a model that generates text" from "an assistant you can actually use."

Key talking points:

- SFT teaches format and helpfulness; RLHF teaches judgment
- "Hallucinations" happen when the model optimizes for sounding helpful over being accurate
- Safety guardrails (content filters) are also applied at this stage
- GitHub Copilot has additional fine-tuning on high-quality code and developer feedback

Why alignment matters for developers: It's why Copilot suggests reasonable code instead of technically-valid-but-insane solutions. It's also why it refuses to help with malicious code.

Common question: "Can I fine-tune Copilot on my codebase?" — GitHub Enterprise Copilot offers custom fine-tuning on private repos.

Timing: ~2-3 minutes.
:::

---

## Context Window — The Model's Working Memory

| Model             | Context Window               |
| ----------------- | ---------------------------- |
| GPT-3.5           | 16k tokens (~12,000 words)   |
| GPT-4o            | 128k tokens (~96,000 words)  |
| Claude 3.5 Sonnet | 200k tokens (~150,000 words) |
| Gemini 1.5 Pro    | 1M tokens (~750,000 words)   |

- Everything the model "knows" during a conversation fits here
- Once exceeded, **earlier content is forgotten**
- GitHub Copilot uses the context window for: open files, cursor position, recent edits, instruction files
- Larger context = can see more code, but also slower & more expensive

::: notes
Context window is one of the most practically important LLM concepts for developers using Copilot.

Key talking points:

- The context window is not persistent memory — every new conversation starts fresh
- Copilot automatically fills the context window with relevant code from open tabs and recent edits
- This is why opening related files improves Copilot suggestions — they get included in context
- Instruction files (`.github/instructions/`) consume some of the context window — keep them concise

Practical tip: If Copilot seems to "forget" something you told it, it likely scrolled out of the context window. Repeat the key constraints.

Timing: ~2 minutes.
:::

---

## Temperature & Sampling

### How the model chooses its next token

```
Token probabilities after "def calculate_":
  "tax"      → 35%
  "total"    → 28%
  "price"    → 18%
  "discount" → 12%
  other...   → 7%
```

| Temperature | Behavior                         | Use case           |
| ----------- | -------------------------------- | ------------------ |
| 0.0         | Always picks highest probability | Deterministic code |
| 0.3–0.5     | Mostly top tokens, some variety  | Code completion    |
| 0.7–1.0     | More creative, less predictable  | Brainstorming      |
| > 1.0       | Random / incoherent              | Rarely useful      |

::: notes
Temperature demystifies why LLMs give different answers to the same question.

Key talking points:

- Temperature = how "flat" or "peaked" the probability distribution is before sampling
- Copilot uses a low temperature (~0.2-0.4) for code — you want predictable, correct completions
- ChatGPT uses higher temperature for conversational responses — feels more natural
- When Copilot gives you alternates (Alt+] to cycle), it's sampling different tokens

Developer implication: If you're using the Copilot API or OpenAI API directly, lower temperature for code generation tasks, higher for creative tasks like writing test descriptions.

Timing: ~2 minutes.
:::

---

## Key Takeaways

- 🔤 **Tokenization** — text is broken into tokens; everything is numbers
- 🔍 **Transformers** — attention lets every token relate to every other
- 🎓 **Pre-training** — learns from trillions of tokens of text & code
- 🎯 **Fine-tuning** — makes the model helpful, safe, and task-specific
- 📏 **Context window** — the model's working memory; bigger = better
- 🌡️ **Temperature** — controls creativity vs. determinism

### The bottom line for developers:

> LLMs are powerful pattern matchers. Give them **clear context**, **good examples**, and **specific instructions** — and they'll surprise you.

### ❓ Questions?

::: notes
Wrap up by connecting the technical concepts back to practical developer behavior.

Key points to reinforce:

- You don't need to understand the math to use LLMs effectively
- Understanding tokens helps you write better prompts and manage costs
- Understanding context helps you structure your workspace for better Copilot suggestions
- Understanding temperature explains why results vary

For Q&A, be prepared for:

- "How does Copilot know about my private code?" — It doesn't unless you're using Enterprise Knowledge Bases
- "Why does it make things up?" — Hallucination: the model is optimized to produce plausible-sounding text, not verified facts
- "What's the difference between Copilot and ChatGPT?" — Same underlying technology; different fine-tuning, context, and integration

Timing: Spend remaining session time on Q&A.
:::

---

<!-- _class: lead -->

## Course Modules

- Intro
- Module 1 - LLM
- **▶ Module 2 - Copilot for Teams**
- Module 3 - Models and Context

---

<!-- _class: lead -->

# Module 2 - Copilot for Teams

---

## Module 2 - Copilot for Teams

- GitHub Copilot for Teams

---

## GitHub Copilot for Teams

Key Considerations for Adoption

Empowering developers with AI while protecting your codebase

::: notes
Outline governance, admin controls, and adoption factors (training, policy, developer onboarding).
:::

---

## What Prompted This Deck?

I want to know how GitHub Copilot protects the intellectual property in the code and documentation submitted to the model. Is this information isolated from other users? Is it incorporated into the model and leaked to other users? How can I protect my IP while using GitHub Copilot?

::: notes
Explain the motivating questions about IP, privacy, and safe use that led to this presentation.
:::

---

## Benefits for Organizations

Accelerated Development

- Faster prototyping, fewer boilerplate tasks
  Improved Documentation
- Auto-generates comments and README content
  Enhanced Testing
- Suggests unit tests and edge cases
  Team Productivity
- Reduces cognitive load, supports onboarding

::: notes
Highlight productivity, documentation, test generation, and onboarding benefits with brief examples.
:::

---

## Risks to Consider

IP Leakage Concerns

- Copilot may suggest code similar to public repositories
- Risk of inadvertently using copyrighted or licensed code
- Mitigation: Enable public code filters and review suggestions carefully
  Code Quality and Accuracy
- AI-generated code may contain bugs, inefficiencies, or security flaws
- Always validate and test before deployment
- Treat Copilot as a drafting tool, not a source of truth
  Developer Overreliance
- Risk of reduced understanding or critical thinking
- Encourage code reviews and pair programming to maintain rigor

::: notes
Cover IP leakage, code quality risks, and developer overreliance; suggest mitigations for each.
:::

---

## Governance and Compliance Risks

Regulatory Compliance

- Generated code may not meet industry-specific standards (e.g., HIPAA, PCI-DSS)
- Organizations must enforce coding policies and audits
  Data Privacy and Security
- Sensitive data should never be typed into prompts
- Use Copilot in secure environments with clear usage guidelines
  Licensing Ambiguity
- Copilot suggestions may resemble code under restrictive licenses
- Legal teams should define acceptable use policies and monitor compliance

::: notes
Discuss regulatory impacts, auditability, and how to enforce coding policies with automated checks.
:::

---

## IP and Data Protection

Your code is not used to retrain the model (with Copilot for Business/Enterprise)
Suggestions are generated locally — no code is shared unless feedback is submitted
No leakage between users: your private code is not exposed to others
Admins can disable suggestions matching public code for added safety

::: notes
Clarify data flows, model retraining policy for enterprise plans, and recommended org controls to protect IP.
:::

---

## Licensing and Legal Considerations

Copilot may suggest code similar to public repositories
GitHub provides a filter to block matching public code
Organizations should review Copilot's Terms of Service and Privacy Statement

::: notes
Explain risks of suggested code resembling public repos and recommend legal review and filter settings.
:::

---

## Deployment Options

| Plan                           | Key Features                       | IP Protection |
| ------------------------------ | ---------------------------------- | ------------- |
| Copilot Individual (Pro, Pro+) | Personal use, no admin controls    | Limited       |
| Copilot for Business           | Admin controls, policy enforcement | Strong        |
| Copilot for Enterprise         | Org-wide policy, audit tools       | Strongest     |

::: notes
Summarize plan differences and pick considerations (control, audit, scale) for each offering.
:::

---

## Best Practices for Safe Use

Enable public code filters
Establish a review process
Educate teams on responsible use and licensing awareness

::: notes
Practical checklist: avoid secrets in prompts, enable public-code filters, and establish review processes.
:::

---

## Resources

Copilot Documentation:

- https://docs.github.com/en/copilot
  Copilot for Business Overview
- https://github.com/features/copilot-for-business
  Security and Privacy FAQ
- https://docs.github.com/en/copilot/security

::: notes
Point attendees to official docs and FAQs; recommend follow-up reading links on the slide.
:::

---

<!-- _class: lead -->

## Course Modules

- Intro
- Module 1 - LLM
- Module 2 - Copilot for Teams
- **▶ Module 3 - Models and Context**

---

<!-- _class: lead -->

# Module 3 - Models and Context

---

## Module 3 - Models and Context

- Advanced Context Techniques

---

## Advanced Context Techniques

Modern AI tools rely heavily on context quality
Developers can shape context intentionally
Reduces hallucinations, drift, and rework
Strong context discipline is a core AI‑era skill

::: notes
This slide frames the idea that AI quality is directly tied to context quality.

Models don't "understand" your repo – they interpret whatever you give them.

Advanced context techniques let you control what the model sees and how reliably it stays aligned with your architecture.
:::

---

## File & Folder Mentions (# Syntax)

How it helps
Explicitly pull files into context
Ensures the model references real code, not guesses
Supports cross‑file refactoring and API consistency
Reduces drift in large repos
Examples
#src/utils/date.ts
#services/

::: notes
The # syntax is one of the most powerful ways to anchor Copilot.

It forces the model to load specific files or directories into its working memory.

This is essential when you want the model to follow existing patterns or avoid hallucinating APIs.
:::

---

## Spaces & Knowledge Bases Integration

Why they matter
Persistent, structured context containers
Store architectural rules, domain models, coding standards
Provide long‑term memory beyond a single prompt
Ideal for instruction files and evergreen boundaries
Use cases
Architecture constraints
Domain terminology
API contracts
Coding conventions

::: notes
Spaces and knowledge bases give you a stable context layer that doesn't depend on prompt length.

Instead of repeating instructions every session, you store them once and let Copilot reference them automatically.

This is especially valuable for brownfield systems with scattered tribal knowledge.
:::

---

## Premium Usage Monitoring

High‑end models = high reasoning cost
Monitor usage patterns to avoid unnecessary calls
Use a tiered strategy:

- Premium for architecture & refactoring
- Mid‑tier for implementation
- Lightweight for boilerplate
  Optimize prompts to reduce token consumption

::: notes
Premium models are incredible, but they're not free.

Monitoring usage helps teams understand where they're over‑relying on heavyweight models.

A tiered strategy ensures the right model is used for the right task, keeping costs predictable and output quality high.
:::

---

## Token Estimation & Overflow Detection

Models have strict token limits
Overflow causes silent failures:

- Missing requirements
- Contradictions
- Forgotten rules
  Techniques to stay within limits:
- Summaries
- Chunking
- Scoped prompts
- Instruction files

::: notes
Open by explaining that token limits are one of the most important but least visible constraints in AI-assisted development.

When a model exceeds its context window, it silently drops earlier content.

This leads to missing requirements, contradictions, or forgotten rules.

The goal of this section is to help developers recognize overflow symptoms and apply techniques to prevent them.
:::

---

## Why Token Limits Matter

Every model has a maximum context window
Prompts, code, examples, and instructions all consume tokens
Exceeding the limit forces the model to discard earlier content
The model never alerts you when this happens

::: notes
Token limits are a hard boundary.

Everything the model reads – your prompt, code snippets, examples, and even its own reasoning – counts toward the limit.

When the limit is exceeded, the model truncates the earliest content, which often contains critical instructions or architectural rules.
:::

---

## Silent Failure Modes

What Overflow Looks Like
Missing requirements
Contradictions
Forgotten rules
Inconsistent reasoning
Loss of architectural constraints

::: notes
Overflow is subtle.

The model behaves as if you never gave it the missing information.

Developers often misinterpret this as stubbornness or randomness, but it's simply the model losing context due to token pressure.

These symptoms are your early warning signs.
:::

---

## Technique: Summaries

How Summaries Help
Compress large files into short, high‑signal descriptions
Preserve intent without overwhelming the context window
Reuse summaries across prompts
Reduce noise and improve model alignment

::: notes
Summaries are your first line of defense.

Instead of pasting entire files, summarize their purpose, interfaces, and constraints.

Summaries dramatically reduce token usage while keeping the model aligned with the system's intent.

They also become reusable context anchors for future prompts.
:::

---

## Technique: Chunking

How Chunking Works
Break large tasks into smaller, self‑contained steps
Provide only the relevant portion of the code
Validate each chunk before moving on
Prevents the model from being overloaded

::: notes
Chunking keeps prompts small and manageable.

Instead of asking the model to refactor a huge file, break the task into sections.

This keeps each prompt within safe token limits and makes the output easier to review, test, and roll back if needed.
:::

---

## Technique: Scoped Prompts

Benefits
Limit the model's focus to a single module or function
Reduce irrelevant context
Improve accuracy and reduce hallucinations
Keep token usage predictable

::: notes
Scoped prompts are about intentionality.

Tell the model exactly what part of the system to focus on.

This reduces token usage and improves reliability because the model isn't trying to reason about the entire codebase at once.

It also reduces hallucinations by narrowing the reasoning space.
:::

---

## Technique: Instruction Files

Why They Matter
Move stable rules out of the active prompt
Provide persistent architectural and style guidance
Reduce repeated tokens across sessions
Keep prompts short and high‑signal

::: notes
Instruction files are a powerful way to reduce token load.

Instead of repeating architectural rules or coding standards in every prompt, store them in a persistent instruction file.

This frees up space for task‑specific context and keeps the model aligned with your evergreen architecture.
:::
