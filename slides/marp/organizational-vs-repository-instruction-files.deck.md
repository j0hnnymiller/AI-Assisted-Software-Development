---
ai_generated: true
model: "openai/gpt-5.3-codex@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "organizational-vs-repository-instruction-files-20260317"
prompt: |
  create a marp deck with the title "Organizational vs. Repository Instruction Files"

  That covers this material: Business/Enterprise tier capabilities; Path-scoped instruction files; Folder-level technology-specific rules
started: "2026-03-17T08:20:17.2570320-07:00"
ended: "2026-03-17T08:32:00.0000000-07:00"
task_durations:
  - task: "requirements and instruction review"
    duration: "00:06:00"
  - task: "deck authoring"
    duration: "00:05:00"
  - task: "provenance and README updates"
    duration: "00:01:00"
total_duration: "00:12:00"
ai_log: "ai-logs/2026/03/17/organizational-vs-repository-instruction-files-20260317/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---

# Organizational vs. Repository Instruction Files || Corporate Rules vs. Your Team's Rules

---

## Organizational vs. Repository Instruction Files

- Business/Enterprise tier capabilities
- Path-scoped instruction files
- Folder-level technology-specific rules

::: notes
Frame this as a layering strategy, not an either-or choice. The audience should leave with a practical model for deciding what belongs at enterprise scope versus repository scope. Keep this opening to about 60-90 seconds.
:::

---

## Why Two Instruction Layers Exist

- Enterprise instructions enforce baseline policy and governance
- Repository instructions optimize for project context and implementation detail
- Together they balance consistency and local autonomy

**Key Idea**

Define global guardrails once, then narrow behavior where code lives.

::: notes
Explain that teams usually fail by over-centralizing or over-fragmenting. Centralize non-negotiables, decentralize implementation guidance. Emphasize this prevents policy drift while keeping day-to-day delivery fast.
:::

---

## Business/Enterprise Tier Capabilities

- Organization-wide safety and compliance standards
- Approved model and tool usage policy
- Mandatory provenance and audit requirements
- Security and legal baselines (secret handling, license constraints)
- Shared quality gates for CI/CD

**Typical Scope**

All repositories, all teams, all environments.

::: notes
Call out that enterprise-tier files should be stable and short. They should define constraints, not feature behavior. Give examples: required metadata fields, approved hosts, restricted operations, and mandatory security checks.
:::

