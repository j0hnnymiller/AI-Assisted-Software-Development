---
marp: true
theme: default
paginate: true
---

# Adding AI Guardrails || Teaching Your AI to Color Inside the Lines

---

## Adding AI Guardrails

- What are instructions, prompts, and Agents
- Creating instruction, prompt, and Agent files
- Meta prompts that generate these files
- Instructions for generating artifacts
- Enforcing provenance for AI-assisted artifacts

::: notes
Introduce this module as the foundation for safe, predictable AI-assisted development.

Guardrails ensure that AI output is intentional, reviewable, and aligned with architectural and organizational standards.

These practices turn AI from a novelty into a disciplined engineering tool.
:::

---

## Instructions for Generating Artifacts

- Best practices
  - Define the artifact type
  - Specify required sections
  - Provide examples or templates
  - Include acceptance criteria
  - Require the model to restate constraints

::: notes
When asking AI to generate an artifact, be explicit about structure and constraints.

This prevents drift and ensures the output is usable without heavy editing.
:::

---

## Enforcing Provenance for AI Artifacts

- AI involvement
- Model used
- Date generated
- Human reviewer
  - Store provenance in headers, footers, or side cars
  - Track revisions in version control

::: notes
Provenance is essential for conformance, auditability, and long-term maintainability.

It ensures teams know which artifacts were AI-generated, which were human-generated, and which were hybrid.
:::

---

## Instructions for AI Generated Artifacts

The one instruction file that rules them all

::: notes
Provenance is essential for conformance, auditability, and long-term maintainability.

It ensures teams know which artifacts were AI-generated, which were human-generated, and which were hybrid.
:::

---

## AI-Assisted Output Instructions

- Ensures provenance and logging for all AI-assisted outputs
- Defines required metadata, logging workflow, and quality gates
- Protects code quality and enables audits

::: notes
This slide introduces the purpose of the AI-Assisted Output Instructions file: to enforce traceability, quality, and compliance for all AI-generated artifacts in the repository.
:::

---

## Required Provenance Metadata

Every AI-assisted artifact must include:

```yaml
ai_generated: true
model: provider/model@version
operator: username
chat_id: unique chat identifier
prompt: exact prompt text
started/ended: timestamps
task_durations & total_duration
ai_log: path to conversation log
source: who/what created the file
```

::: notes
This slide lists the mandatory metadata fields that must be embedded in every AI-generated file.

These fields ensure each artifact can be traced back to its origin, model, and operator.
:::

---

## Metadata Placement Policy

- Use YAML front matter for Markdown and similar formats
- For binaries/images, use a sidecar <artifact>.meta.md
- Never use sidecars for Markdown

::: notes
This slide explains where and how to place provenance metadata.

Markdown files must use embedded YAML front matter; only non-embeddable formats use sidecar files.

Note: Instructions files have limited support for metadata and must use sidecar files
:::

---

## AI Chat Logging Workflow

- Each chat creates a unique log folder: `ai-logs/yyyy/mm/dd/<chat-id>/`
- Required files:
  - `conversation.md` (full transcript)
  - `summary.md` (objectives, decisions, outcomes)
  - `artifacts/` (optional)
- Never reuse chat logs between sessions

::: notes
This slide describes the logging structure for AI chats.

Each session gets its own folder, transcript, and summary, ensuring clear separation and traceability.
:::

---

## Quality & PR Checklist

- Metadata complete and correct
- Conversation and summary logs exist
- `README.md` updated for notable artifacts
- No sensitive data in outputs
- All AI-generated content traces to a chat log

::: notes
This slide summarizes the quality gates and PR requirements.

Artifacts must be fully documented, logs must exist, and sensitive data must be avoided.
:::

---

## Copilot Integration Requirements

- Copilot must auto-manage chat IDs and logs
- Metadata injected automatically
- Block artifact creation if chat context is missing
- Enforce provenance before file creation

::: notes
This slide highlights the requirements for GitHub Copilot integration.

Copilot should automate chat management, metadata injection, and enforce compliance before generating files.
:::

---

## Enforcement & Remediation

- PRs blocked if provenance is incomplete
- Missing logs or metadata must be added before merge
- Orphaned artifacts require reconstruction of logs and metadata

::: notes
This slide explains enforcement:

PRs are blocked if requirements are not met.

Any missing provenance must be remediated before merging.
:::

---

## Core Instruction files

`agent-file.instructions.md`
  - Defines the structure and contents of agents

`instruction-files.instructions.md`
  - Defines the structure and contents of instruction files

`prompt-file.instructions.md`
  - Defines the structure and contents of prompts

`instruction-prompt-files.instructions.md`
  - Defines the structure and contents of prompts that create instruction files
