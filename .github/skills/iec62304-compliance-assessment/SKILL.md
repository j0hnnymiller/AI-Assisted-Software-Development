---
name: iec62304-compliance-assessment
description: "Assess software lifecycle evidence against a specified IEC 62304 edition and applicable organizational procedure, including clause-level gaps, risks, and remediation."
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
source: "AIASD-SOP/.github/prompts/assess-d0003329-iec62304-compliance.prompt.md"
---

# IEC 62304 Software Lifecycle Assessment

Use this skill for a bounded, evidence-based assessment of software lifecycle processes against the exact IEC 62304 edition, amendments, jurisdiction, and organizational procedures identified by the user.

## Preconditions

- Confirm the standard edition/amendments, device/software scope, safety classification, lifecycle boundary, applicable procedures, and intended assessment use.
- Obtain controlled requirement text or an approved clause checklist. Do not reproduce copyrighted standard text.

## Procedure

1. Define scope, exclusions, software items, interfaces, and relevant risk-management/configuration processes.
2. Build a clause/subclause traceability matrix from the supplied or licensed requirements source.
3. For each applicable requirement, classify evidence as demonstrated, partial, not demonstrated, not applicable (with rationale), or unknown.
4. Cite objective evidence precisely: document/process identifier, version, section, record, and responsible role when supplied.
5. Assess gaps and dependencies across planning, development, maintenance, risk management, configuration management, and problem resolution.
6. Prioritize remediation by safety/operational impact, applicability, evidence strength, and dependency. Separate observations from formal nonconformities.
7. Synthesize an executive summary with material risks, highest-priority gaps, phased actions, owners only when confirmed, and evidence limitations.
8. Have qualified regulatory/quality personnel review the assessment before it is used for formal audit, submission, or conformity claims.

## Output

Provide scope and edition, assessment method, traceability matrix, evidence status, gap/risk register, prioritized remediation plan, assumptions, and review questions. Include a clause-specific appendix only when supported by the approved requirement source.

## Guardrails

- This workflow is not legal advice, certification, notified-body review, or a guarantee of conformity.
- Do not claim compliance from policy text alone or infer missing evidence.
- Do not reproduce substantial portions of the copyrighted standard.
- Protect confidential medical-device, patient, and quality-system information.
