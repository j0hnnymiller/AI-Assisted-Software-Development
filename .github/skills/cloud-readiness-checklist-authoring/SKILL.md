---
name: cloud-readiness-checklist-authoring
description: "Build or validate tiered cloud-readiness checklists, such as foundational, expanded, and comprehensive assessments, with traceable requirements and controlled variants."
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
source: "Messer/.github/prompts/cloud-readiness-build-checklist-variants.prompt.md"
revisions:
  - chat_id: "skill-naming-convention-20261018"
    model: "unknown/unknown@unknown"
    date: "2026-10-18"
    change: "Applied approved skill naming decisions and updated active references; preserved workflow behavior and historical provenance."
    ai_log: "ai-logs/2026/10/18/skill-naming-convention-20261018/conversation.md"
---

# Cloud Readiness Checklist Design

Use this skill to create or adapt cloud-readiness checklists for an organization, workload, migration, or platform. The checklist tiers are configurable, not universal maturity ratings.

## Procedure

1. Confirm the target workload, cloud/provider scope, assessment audience, evidence sources, and intended decisions.
2. Define a shared baseline of essential controls and add clearly scoped extensions for each requested tier.
3. Organize checks into relevant domains such as governance, identity, networking, data, security, resilience, operations, cost, and delivery.
4. Make each check verifiable: state the question, expected evidence, owner (if supplied), applicability, and pass/partial/fail/unknown status.
5. Trace each requirement to an authoritative source or supplied policy. Record edition/date and avoid unsupported compliance claims.
6. Validate that higher tiers extend rather than contradict the baseline; identify duplicates, ambiguous terms, and non-applicable checks.
7. Record changes between variants and provide a review/approval process for future updates.

If the requester uses named tiers such as foundational, foundational-plus-intermediate, and comprehensive, preserve those boundaries and show exactly which checks are added at each level. Do not imply that a tier name maps to a universal certification or maturity level.

## Output

Provide the tier definitions, checklist, evidence/status fields, mapping to source requirements, variant change log, assumptions, and unresolved decisions. Keep requirements and recommendations distinct.

## Guardrails

- Do not label a workload "cloud ready" based only on checklist completion.
- Do not invent owners, thresholds, policy mandates, or provider-specific controls.
- Use an explicit "unknown/not assessed" state instead of treating missing evidence as a pass.
