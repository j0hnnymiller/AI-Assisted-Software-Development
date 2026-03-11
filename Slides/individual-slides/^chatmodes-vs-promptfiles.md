---
marp: true
theme: default
class: lead
paginate: false
---

# Chat Modes vs. Promptfiles
### How They Work Together in GitHub Copilot

---

## The Relationship

- **Chat Modes** define *how Copilot behaves*
  - Persona, guardrails, reasoning style
  - Safety, compliance, and workflow rules
  - Determines *when* a promptfile should be invoked

- **Promptfiles** define *what task Copilot performs*
  - Structured, reusable task templates
  - Output formats, constraints, and steps
  - Executed *inside* a chat mode

---

## Flow of Control

**User → Chat Mode → Promptfile → Output**

- Chat mode interprets intent
- Matches intent to an invocation rule
- Calls the appropriate promptfile
- Promptfile executes the task with structured output

---

## Why This Matters

- Clear separation of **behavior** (chat mode) and **task logic** (promptfile)
- Predictable, auditable, version‑controlled workflows
- Scalable across teams and repositories
- Perfect for brownfield modernization and safe AI‑assisted development

::: notes
This slide explains the architectural separation between chat modes and promptfiles.
Chat modes act as the behavioral and compliance layer, ensuring consistent reasoning and guardrails.
Promptfiles act as reusable task modules that define structured, repeatable operations.
The key takeaway is the flow: user intent is interpreted by the chat mode, which then delegates to a promptfile.
This separation enables safe, scalable, and auditable AI workflows across teams.
:::
