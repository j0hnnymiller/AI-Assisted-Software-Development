---
marp: true
paginate: true
title: "Copilot Instruction File Constraints: Folders, Filenames, and the Chat Modes → Agents Rename"
---

# Copilot Instruction File Constraints

### Folders, Filenames, and the Chat Modes → Agents Transition

::: notes
This deck summarizes all folder and filename constraints for Copilot's instruction system and incorporates the ongoing rename of “chat modes” to “agents.”
:::

---

# Why Constraints Matter

### Predictability • Auditability • Determinism

- Copilot loads files only from **specific folders**
- Filenames must match **exact expected patterns**
- No recursion, no aliases, no alternative casing
- Misplaced files are silently ignored
- The rename to **agents** does not change folder rules (yet)

::: notes
The rename is conceptual and UI-level for now. The underlying filesystem rules remain unchanged.
:::

---

# High-Level Overview

### What Copilot Looks For

| Artifact Type                    | Required Location              | Required Format           | Notes                       |
| -------------------------------- | ------------------------------ | ------------------------- | --------------------------- |
| Org guardrails                   | Org settings                   | UI-managed                | Always included             |
| Repo guardrails                  | `.github/instructions/`        | `.md`                     | Always included             |
| Path-scoped guardrails           | Any folder                     | `copilot-instructions.md` | Applies to subtree          |
| **Agents (formerly chat modes)** | `.github/copilot/chat_modes/`  | `.json` or `.yaml`        | Folder name has NOT changed |
| Promptfiles                      | `.github/copilot/promptfiles/` | `.md`                     | Only when invoked           |

::: notes
Even though “chat modes” are being renamed to “agents,” the folder name remains `.github/copilot/chat_modes/` for now.
:::

---

# The Rename: Chat Modes → Agents

### What's Changing and What Isn't

**Changing:**

- Terminology in UI and documentation
- Conceptual framing (agents = more powerful, structured roles)
- Schema will expand over time

**Not changing (yet):**

- Folder name: `.github/copilot/chat_modes/`
- File discovery rules
- Filename requirements
- Promptfile behavior
- Instruction stack mechanics

::: notes
Teams can safely start using the term “agent” in training and inside the file's `name:` field, but must keep the existing folder structure.
:::

---

# Agents (Formerly Chat Modes)

### Folder and Filename Constraints

**Required folder:**
