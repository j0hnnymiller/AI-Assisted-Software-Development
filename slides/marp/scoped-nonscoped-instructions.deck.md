---
ai_generated: true
model: "claude-sonnet-4.6"
operator: "johnmillerATcodemag-com"
chat_id: "scoped-nonscoped-instructions-marp-20260331"
prompt: |
  convert the pptx !here-be-dragons\pptx\scoped-nonscoped-instructions.pptx into a marp deck
started: "2026-03-31T03:27:00Z"
ended: "2026-03-31T03:35:00Z"
task_durations:
  - task: "pptx content extraction and conversion"
    duration: "00:08:00"
total_duration: "00:08:00"
ai_log: "ai-logs/2026/03/31/scoped-nonscoped-instructions-marp-20260331/conversation.md"
source: "!here-be-dragons/pptx/scoped-nonscoped-instructions.pptx"
marp: true
paginate: false
---

# Scoped vs Non‑Scoped Instructions || Choosing the Right Instruction File Type

---

## Scoped `<name>.instructions.md` files

- Apply **only** when `applyTo` matches
- Can **exclude** paths
- For **language‑, framework‑, or domain‑specific rules**
- Ideal for precision control
- Best for **targeted, contextual guidance**

---

## Repo‑level `.md` files

- Apply **everywhere** in the repo
- Always included
- For **universal rules**: style, security, logging, architecture
- No `applyTo` / `exclude` support
- Best for **global, evergreen guidance**

---

## Decision Rule

- If it should apply **repo‑wide** → use `.md`
- If it should apply **only in certain paths** → use `.instructions.md`
- If you need **exclusions** → must use `.instructions.md`

::: notes
This slide summarizes the functional difference between the two instruction file types GitHub Copilot supports inside `.github/instructions/`.
Repo‑level `.md` files are unconditional and always included.
Scoped `.instructions.md` files are conditional, support `applyTo` and `exclude`, and only activate when relevant.
The decision rule gives teams a simple, auditable way to choose the correct mechanism.
:::

---

## `exclude:` in Practice

```yaml
applyTo:
  - "src/**"
exclude:
  - "src/experimental/**"
  - "src/legacy/*.js"
```

- Scope instructions to `src/` but carve out experimental and legacy paths
- Only available with `.instructions.md` files (not repo‑level `.md`)
