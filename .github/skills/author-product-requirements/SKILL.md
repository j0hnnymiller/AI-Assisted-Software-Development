---
name: author-product-requirements
description: "Create or refine a product requirements document (PRD) from a product idea, stakeholder input, or validated discovery."
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
source: "zeus/zeus.academia.3b/.github/prompts/create-prd.prompt.md"
revisions:
  - chat_id: "skill-naming-convention-20261018"
    model: "unknown/unknown@unknown"
    date: "2026-10-18"
    change: "Applied approved skill naming decisions and updated active references; preserved workflow behavior and historical provenance."
    ai_log: "ai-logs/2026/10/18/skill-naming-convention-20261018/conversation.md"
---

# Product Requirements Document Authoring

Create a decision-ready PRD grounded in supplied evidence. Use when shaping a product idea, defining a feature, or reviewing requirements before delivery planning.

## Inputs

- Problem statement, users, business context, research, constraints, existing products, and decision-makers.
- Mark unknowns and conflicting sources; do not silently convert assumptions into requirements.

## Procedure

1. State the problem, affected users, evidence, and why it matters now.
2. Define outcomes and measurable success indicators. Separate product outcomes from implementation tasks.
3. Describe target users, key scenarios, user journeys, and accessibility or operational needs where relevant.
4. Specify functional requirements and testable acceptance criteria. Label each requirement with its source or rationale when available.
5. Define non-goals, scope boundaries, dependencies, constraints, risks, and open questions.
6. Cover security, privacy, reliability, performance, accessibility, and compliance requirements only to the extent justified by context.
7. Review for ambiguity, contradictions, feasibility assumptions, and untestable wording; propose questions rather than invent answers.

## Output

Use a concise structure: summary, problem/evidence, goals and metrics, users/scenarios, requirements and acceptance criteria, non-goals, dependencies/constraints, risks, open questions, and decision history. Adapt to an existing team template when provided.

## Guardrails

- Do not prescribe architecture or implementation unless explicitly requested.
- Do not fabricate research, metrics, stakeholder decisions, dates, estimates, or market facts.
- Keep requirements independently understandable and verifiable; identify unresolved trade-offs.
