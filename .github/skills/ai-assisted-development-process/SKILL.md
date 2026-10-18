---
name: ai-assisted-development-process
description: "Design or improve an AI-assisted software development process, including governance, workflow stages, human review, privacy, verification, and provenance."
ai_generated: true
model: "unknown/unknown@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
prompt: |
  Merge useful gaps and create proposed new skills
started: "2026-10-17T19:33:05.9169653-07:00"
ended: "2026-10-17T19:52:32.094572-07:00"
task_durations:
  - task: "Approved cross-repository prompt-to-skill migration"
    duration: "00:19:26"
total_duration: "00:19:26"
ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
source: "zeus/zeus.academia.3b/.github/prompts/create-ai-dev-process.prompt.md"
---

# AI-Assisted Development Process

Use this skill to define a repeatable development lifecycle that uses AI tools while keeping engineering decisions, data handling, quality gates, and accountability explicit.

## Inputs

- Organization and project context, existing SDLC, applicable policies, tool/model constraints, risk tolerance, and intended users.
- Clearly distinguish supplied facts from assumptions; ask for missing decisions that materially affect controls.

## Procedure

1. Map the current lifecycle from intake and planning through design, implementation, verification, release, and maintenance.
2. For each stage, define appropriate AI-assisted tasks, required human decisions, inputs that may be shared, and outputs that must be reviewed.
3. Set controls for privacy, confidential data, access, generated code and content, licensing, prompt injection, external tools, and retention.
4. Define review gates proportionate to risk. Require accountable human approval for architecture, security, regulated, production, and user-impacting decisions.
5. Specify verification for generated changes: tests, static analysis, security checks, provenance, reproducibility, and rollback where applicable.
6. Assign owners for policy, tool approval, incidents, training, and periodic review. Define exception and escalation paths.
7. Pilot the process on a bounded workflow, gather evidence, identify friction and failure modes, and revise before wider adoption.

## Output

Provide a lifecycle diagram or stage table, roles and responsibilities, stage-specific controls, exception/escalation flow, adoption plan, measurable success indicators, and unresolved decisions. Tailor detail to the project's risk and regulatory context.

## Guardrails

- Do not treat AI output as verified, authoritative, or approved merely because it is fluent.
- Do not transmit secrets, personal data, or restricted material to an unapproved service.
- Do not invent organizational policy, legal requirements, owners, service levels, or model capabilities.
- Identify where legal, privacy, security, or compliance review is required; do not claim certification.
