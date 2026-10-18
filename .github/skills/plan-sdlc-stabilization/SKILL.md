---
name: plan-sdlc-stabilization
description: "Assess and stabilize a software development lifecycle by prioritizing delivery risks, clarifying controls, and proposing a measurable improvement plan."
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
source: "Messer/.github/prompts/sdlc-stabilization-guidance.prompt.md"
revisions:
  - chat_id: "skill-naming-convention-20261018"
    model: "unknown/unknown@unknown"
    date: "2026-10-18"
    change: "Applied approved skill naming decisions and updated active references; preserved workflow behavior and historical provenance."
    ai_log: "ai-logs/2026/10/18/skill-naming-convention-20261018/conversation.md"
---

# SDLC Stabilization Guidance

Use this skill when a team needs to reduce delivery instability, improve release confidence, or establish a practical improvement roadmap.

## Procedure

1. Define the product/team boundary, current pain points, delivery objectives, and evidence available.
2. Map the actual flow from intake through release and support; note queues, handoffs, rework, incidents, and approval bottlenecks.
3. Assess risks across requirements, design, source control, testing, security, deployment, operations, and ownership.
4. Separate observed facts from hypotheses; identify the highest-impact failure modes and contributing causes.
5. Propose staged improvements with owner roles, prerequisites, effort ranges only when supported, measurable outcomes, and rollback/exception paths.
6. Define a small baseline of metrics, such as lead time, escaped defects, change failure rate, recovery time, test reliability, and work in progress, with precise definitions.
7. Sequence a pilot and review cadence; revise based on measured evidence.

## Output

Provide an executive summary, current-state evidence, prioritized risks, phased actions, proposed metrics with definitions, assumptions, and decisions needed. If a DOCX or other rendered deliverable is requested, use the user's template and verify the rendered output separately.

## Guardrails

- Do not prescribe process frameworks or tools without context.
- Do not invent baseline metrics, deadlines, owners, or staffing.
- Avoid large process redesign before validating root causes and stakeholder constraints.
