---
name: databricks-apps-cicd-advisory
description: "Assess or design CI/CD for Databricks Apps, including source control, validation, deployment promotion, secrets, permissions, rollback, and operational checks."
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
source: "Messer/.github/prompts/cicd-advisory-databricks-apps.prompt.md"
revisions:
  - chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
    model: "unknown/unknown@unknown"
    date: "2026-10-18"
    change: "Added evidence-based promotion gates, decision rights, exception handling, release traceability, and leadership/platform views from the retired advisory prompt."
    ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
---

# Databricks Apps CI/CD Advisory

Use this skill to advise on a Databricks Apps delivery pipeline. Verify platform capabilities and commands against the team's current Databricks product version and approved documentation.

## Inputs

- App framework and repository layout, workspaces/environments, deployment identity, existing pipeline, approval model, secrets handling, and release constraints.
- Confirmed repository and stakeholder evidence, applicable Databricks Apps product version, platform documentation, and open decisions.
- Separate confirmed platform configuration from assumptions. Use a clear confirmation placeholder for unknown workspace names, owners, deployment mechanisms, approvers, thresholds, dependencies, or support routes.

## Procedure

1. Inventory app code, configuration, dependencies, tests, infrastructure definitions, data integrations, generated artifacts, environments, current pipeline, and operational ownership.
2. Validate Databricks Apps capabilities, commands, APIs, permissions, and deployment mechanisms against current official documentation and the target product version. Treat product-page capabilities as options to verify, not proof of the team's configured design.
3. Map an end-to-end path from change intake and pull request through build/package, validation, lower-environment deployment, evidence capture, approval, production promotion, post-deployment verification, and rollback or recovery. Distinguish automated checks from human approvals.
4. Define objective promotion gates for each environment transition. For every gate, state the decision question, required evidence, evidence owner, reviewer/approver role (or confirmation placeholder), pass criteria, and exception path.
5. Cover source/change traceability; reproducible builds and versioned packages; unit, integration, smoke, and health checks; dependency, secret, security, identity, permission, and policy checks; workspace target/configuration validation; data access and compatibility; rollback readiness; monitoring, runbooks, support, and production approval.
6. Promote the same validated artifact across environments where feasible. Document any exception, the reason, associated risk, and compensating validation; do not silently rebuild different production bits.
7. Design least-privilege CI identities and supported authentication. Separate secrets and environment configuration from source and build artifacts. Address app identity, user authentication/authorization, Unity Catalog and other data permissions, auditability, and network controls only as applicable and evidenced.
8. Define stop, rollback, or rework conditions, failure notification, post-deployment verification, and a tested rollback or forward-fix path. Include out-of-band workspace/app changes in the traceability and drift-control design.
9. Define exceptions with rationale, named risk owner only when confirmed, compensating controls, expiry or review date, and leadership visibility. The customer organization owns exception acceptance and go/no-go decisions.
10. Provide a prioritized adoption sequence, assumptions, dependencies, open decisions, and an evidence-based readiness view for both implementers and leadership.

## Output

Deliver an advisory with scope and decision rights; confirmed versus unconfirmed context; pipeline structure; environment and promotion flow; a gate/evidence matrix; identity, security, data, and operational considerations; traceability, exceptions, rollback, and post-deployment checks; a leadership go/no-go view; adoption sequence; open decisions; and out-of-scope items. Provide sample configuration only when the runner and supported interfaces are known.

## Guardrails

- Do not assume a particular CI provider, workspace topology, deployment command, or feature availability.
- Never include credentials, tokens, workspace secrets, or sensitive deployment identifiers in examples.
- Distinguish recommendations from confirmed implementation facts. Do not invent approver names, service targets, recovery objectives, support coverage, thresholds, or compliance claims.
- Do not imply that an advisory author owns implementation, configuration, approvals, remediation, operations, or final go/no-go decisions.
- Do not create pipeline files, deploy, or modify a live workspace unless explicitly authorized.
- Do not define contractual SLAs or on-call coverage without confirmed requirements and decision authority.
