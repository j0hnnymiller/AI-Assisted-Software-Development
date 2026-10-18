---
name: databricks-hosting-decisions
description: "Compare Databricks and alternative cloud hosting options through decision-relevant questions and evidence about workload, integration, security, operations, delivery, roadmap, and cost."
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
source: "Messer/.github/prompts/databricks-app-hosting-decision-factors.prompt.md"
revisions:
  - chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
    model: "unknown/unknown@unknown"
    date: "2026-10-17"
    change: "Added decision-relevant clarification and comparable cost screening without a fixed region default."
    ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
---

# Databricks and Cloud Hosting Decisions

Use this skill when comparing hosting options for an application or workload, including Databricks-hosted application capabilities and general cloud services.

## Procedure

1. Clarify workload shape, users, data location/sensitivity, integration needs, latency, availability, scale, team skills, and deployment constraints. If material information is missing, ask plain-language questions one at a time and skip questions that cannot change the viable-host set or recommendation.
2. Identify viable alternatives and confirm the specific product capabilities and limitations from current official sources.
3. Establish functional fit before comparing cost. Compare viable options against agreed criteria: fit, identity/security, data movement, integration, operations, resilience, delivery, portability, support, and roadmap.
4. Separate facts, assumptions, estimates, and unknowns. Cite evidence and dates for vendor-specific claims.
5. Include cost only after viable hosts are identified. Use current official pricing sources and user-provided usage/budget priorities; compare with consistent workload, sizing, and region assumptions, show ranges when inputs are incomplete, and do not invent a precise total. Use the user's target region or verified deployment context rather than a fixed default.
6. Score only with an agreed scale and weights. Show sensitivity to uncertain or high-impact assumptions.
7. Recommend an option only when evidence supports it; otherwise present a short list and the decisions needed to choose.

## Output

Provide a decision summary, comparison matrix, assumptions and evidence, material risks/mitigations, cost variables (not fabricated totals), and next validation steps.

## Guardrails

- Do not assume Databricks is the default host because data or analytics use it.
- Do not invent pricing, service limits, compliance status, or product support.
- Do not select an unsuitable host only because it is cheaper, or use a default pricing region without evidence.
- Do not use a numeric score without explaining the criteria and weighting.
