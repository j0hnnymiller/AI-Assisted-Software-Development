---
name: cqrs-and-event-sourcing-guidance
description: "Design, review, or implement CQRS and event-sourcing approaches with explicit consistency, event contracts, projections, idempotency, and operational trade-offs."
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
source: "zeus/zeus.academia.3b/.github/prompts/generate-cqrs-eventsourcing-instructions.prompt.md"
revisions:
  - chat_id: "skill-naming-convention-20261018"
    model: "unknown/unknown@unknown"
    date: "2026-10-18"
    change: "Applied approved skill naming decisions and updated active references; preserved workflow behavior and historical provenance."
    ai_log: "ai-logs/2026/10/18/skill-naming-convention-20261018/conversation.md"
---

# CQRS and Event Sourcing Guidance

Use this workflow when evaluating command/query separation, event-driven domain state, event stores, projections, or migration to an event-sourced model.

## Procedure

1. Establish domain boundaries, actors, business invariants, workload, latency, consistency, audit, retention, and recovery requirements.
2. Decide whether CQRS or event sourcing is justified. Compare with a simpler transactional model and document the additional operational complexity.
3. Define commands, validation, authorization, aggregate boundaries, events, and state transitions. Events describe accepted facts and are versioned contracts.
4. Specify event identity, ordering assumptions, idempotency, concurrency control, duplicate delivery handling, schema evolution, and replay behavior.
5. Design read models/projections, rebuild and backfill strategy, eventual-consistency UX, failure isolation, and observability.
6. Address transactional outbox/inbox or equivalent delivery guarantees where database commits and message publication must remain consistent.
7. Define security, PII minimization, retention/deletion, encryption, access controls, and audit requirements for event data.
8. Test invariants, invalid commands, concurrency, duplicate/out-of-order events, projection lag, replay, upgrades, and recovery.

## Deliverables

Provide a context/event flow diagram, command and event examples, consistency guarantees, data lifecycle, failure/recovery model, alternatives considered, risks, and incremental implementation plan. Mark unavailable details as questions or assumptions.

## Guardrails

- Do not recommend event sourcing by default; justify it against simpler alternatives.
- Do not treat events as mutable records or assume global ordering.
- Do not promise exactly-once delivery without evidence of the complete system guarantee.
- Preserve backward compatibility and auditability when evolving event contracts.
