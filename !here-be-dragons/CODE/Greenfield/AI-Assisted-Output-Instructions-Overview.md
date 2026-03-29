---
marp: true
theme: default
title: "AI-Assisted Output Instructions Overview"
---

# **AI-Assisted Output Instructions**

- Ensures provenance and logging for all AI-assisted outputs
- Defines required metadata, logging workflow, and quality gates
- Protects code quality and enables audits

::: notes
This slide introduces the purpose of the AI-Assisted Output Instructions file: to enforce traceability, quality, and compliance for all AI-generated artifacts in the repository.
:::

---

# **Required Provenance Metadata**

- Every AI-assisted artifact must include:
  - ai_generated: true
  - model: provider/model@version
  - operator: username
  - chat_id: unique chat identifier
  - prompt: exact prompt text
  - started/ended: timestamps
  - task_durations & total_duration
  - ai_log: path to conversation log
  - source: who/what created the file

::: notes
This slide lists the mandatory metadata fields that must be embedded in every AI-generated file. These fields ensure each artifact can be traced back to its origin, model, and operator.
:::

---

# **Metadata Placement Policy**

- Use YAML front matter for Markdown and similar formats
- For binaries/images, use a sidecar `<artifact>.meta.md`
- Never use sidecars for Markdown

::: notes
This slide explains where and how to place provenance metadata. Markdown files must use embedded YAML front matter; only non-embeddable formats use sidecar files.
:::

---

# **AI Chat Logging Workflow**

- Each chat creates a unique log folder: `ai-logs/yyyy/mm/dd/<chat-id>/`
- Required files:
  - conversation.md (full transcript)
  - summary.md (objectives, decisions, outcomes)
  - artifacts/ (optional)
- Never reuse chat logs between sessions

::: notes
This slide describes the logging structure for AI chats. Each session gets its own folder, transcript, and summary, ensuring clear separation and traceability.
:::

---

# **Quality & PR Checklist**

- Metadata complete and correct
- Conversation and summary logs exist
- README.md updated for notable artifacts
- No sensitive data in outputs
- All AI-generated content traces to a chat log

::: notes
This slide summarizes the quality gates and PR requirements. Artifacts must be fully documented, logs must exist, and sensitive data must be avoided.
:::

---

# **Copilot Integration Requirements**

- Copilot must auto-manage chat IDs and logs
- Metadata injected automatically
- Block artifact creation if chat context is missing
- Enforce provenance before file creation

::: notes
This slide highlights the requirements for GitHub Copilot integration. Copilot should automate chat management, metadata injection, and enforce compliance before generating files.
:::

---

# **Enforcement & Remediation**

- PRs blocked if provenance is incomplete
- Missing logs or metadata must be added before merge
- Orphaned artifacts require reconstruction of logs and metadata

::: notes
This slide explains enforcement: PRs are blocked if requirements are not met. Any missing provenance must be remediated before merging.
:::

---

# **Summary: Why This Matters**

- Enables auditability and trust in AI outputs
- Protects against orphaned or unverifiable artifacts
- Supports team collaboration and compliance

::: notes
The final slide reinforces the value of these instructions: they ensure every AI-assisted artifact is trustworthy, auditable, and compliant with team and industry standards.
:::
