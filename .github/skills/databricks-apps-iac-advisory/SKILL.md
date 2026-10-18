---
name: databricks-apps-iac-advisory
description: "Plan infrastructure-as-code for Databricks Apps, including supported resources, state, identity, secrets, environment separation, drift, and deployment controls."
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
source: "Messer/.github/prompts/infrastructure-as-code-advisory-databricks-apps.prompt.md"
---

# Infrastructure as Code for Databricks Apps

Use this skill to assess whether and how to manage Databricks Apps infrastructure through code. Confirm provider and API support for the current target versions before proposing implementation.

## Procedure

1. Inventory app resources, workspace/account boundaries, environments, ownership, and existing IaC tooling.
2. Identify which resources are supported by the selected provider/API and which require an alternate, documented deployment step.
3. Define resource ownership, configuration inputs, dependency ordering, state backend/access/locking, and import/adoption strategy.
4. Design environment separation, least-privilege identities, secret references, network/data access, and approval gates.
5. Specify plan/review/apply stages, drift detection, policy checks, audit records, and safe handling of partial failures.
6. Document destroy/rollback protections, state recovery, upgrades, and break-glass procedures.
7. Verify provider versions, resource schemas, and platform limitations against current official documentation.

## Output

Provide a resource inventory and support matrix, state/security design, pipeline flow, known manual steps, risks, and open questions. Include examples only for verified provider interfaces.

## Guardrails

- Never place credentials, secret values, or state contents in logs or examples.
- Do not claim full declarative management when a resource is unsupported or only partially managed.
- Do not run apply/destroy operations or change live infrastructure without explicit authorization.
