---
name: design-ownership-and-support-model
description: "Design or review a product or service ownership and support model covering roles, escalation, handoff, documentation, coverage, and resourcing."
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
source: "Messer/.github/prompts/ownership-support-model-guidance.prompt.md"
revisions:
  - chat_id: "skill-naming-convention-20261018"
    model: "unknown/unknown@unknown"
    date: "2026-10-18"
    change: "Applied approved skill naming decisions and updated active references; preserved workflow behavior and historical provenance."
    ai_log: "ai-logs/2026/10/18/skill-naming-convention-20261018/conversation.md"
---

# Ownership and Support Model Guidance

Use this skill to define accountable ownership and operational support for a service, product, or initiative.

## Procedure

1. Establish service scope, users, criticality, dependencies, deployment model, and existing support commitments.
2. Identify lifecycle responsibilities: product decisions, engineering, operations, security, vendor management, and customer communication.
3. Define ownership boundaries, primary/backup contacts or roles, decision rights, and handoff conditions.
4. Specify support channels, hours, severity/impact categories, escalation path, response expectations, and incident coordination only when agreed.
5. Document onboarding, runbooks, access, knowledge transfer, service changes, end-of-life, and continuity arrangements.
6. Assess staffing, skills, coverage gaps, vendor dependencies, and single-person risks. Mark capacity assumptions explicitly.
7. Review the model with accountable stakeholders and record unresolved decisions and review cadence.

## Output

Provide a responsibility matrix, escalation and handoff flow, support coverage model, documentation checklist, resourcing risks, and decisions needed. Use role names unless real owners are confirmed.

## Guardrails

- Do not invent named owners, support hours, SLAs, staffing levels, or escalation contacts.
- Distinguish proposed service levels from approved commitments.
- Apply least privilege to support access and protect personal/contact data.
