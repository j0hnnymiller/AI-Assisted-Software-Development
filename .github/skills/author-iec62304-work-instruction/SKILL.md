---
name: author-iec62304-work-instruction
description: "Draft a controlled software-development work instruction using IEC 62304 and an approved QMS template"
argument-hint: "Applicable standard edition, approved template, and QMS procedures"
ai_generated: true
model: "unknown/unknown@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
prompt: |
  files in the .github/prompts folder should be campared with the canonical skills. If a skill does not exist for the prompt, create a new skill. Prompt files are being deprecated. update the instructions, skills, and agents, responsible for syncing .github files.
started: "2026-10-18T09:55:12.922-07:00"
ended: "2026-10-18T10:05:54.310-07:00"
task_durations:
  - task: "Prompt-gap review and regulated-instruction skill authoring"
    duration: "00:10:41"
total_duration: "00:10:41"
ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
source: "Teleflex/agentsolution/.github/promptfiles/create-ai-assisted-dev-wi-20260209.prompt.md (spoke migration input)"
---

# Author an IEC 62304 Work Instruction

Draft a software-development work instruction for a regulated medical-device context.
This is a controlled-document drafting workflow, not a compliance determination or
approval. Use the separate [IEC 62304 compliance-assessment skill](../iec62304-compliance-assessment/SKILL.md)
for an evidence assessment.

## Required Inputs

- Applicable IEC 62304 edition and the organization's approved QMS template.
- Current procedures, policies, role definitions, and document-control requirements.
- Intended device/software scope and applicable safety classification, supplied by an
  authorized domain owner.
- Applicable risk-management, quality, cybersecurity, and regulatory sources identified
  by the organization.

If an input is missing or unverified, ask for it or mark the related content unresolved.
Do not infer the organization's QMS, safety class, regulatory market, approval authority,
or mandatory controls from an unrelated repository or example.

## Procedure

1. Confirm the document purpose, scope, audience, applicable edition, template, and
   approval workflow. Keep requirements from the approved template and controlled
   procedures distinct from recommendations.
2. Build a clause-to-section coverage map from authoritative sources. Paraphrase
   requirements and cite clause identifiers; do not reproduce copyrighted standard text.
3. Draft lifecycle procedures only where the organization provides evidence for roles,
   inputs, activities, records, review gates, and outputs. For each lifecycle area,
   distinguish sourced baseline requirements from organization-defined AI controls.
   Address AI-tool use, tool qualification or validation, generated-content review,
   traceability, configuration control, risk management, verification, maintenance, and
   problem resolution only to the extent applicable and supported.
4. If controls vary by software safety class, use classifications and decision rules
   supplied by the organization. Do not invent class-specific requirements.
5. Mark unknowns and assumptions visibly. Do not claim that the draft is compliant,
   approved, effective, or ready for implementation. Identify required review by
   regulatory, quality, safety, cybersecurity, and legal stakeholders as applicable.
6. Validate the draft against the approved template, clause coverage map, source
   references, terminology, responsibilities, records, and document-control conventions.
   Ensure each mandatory statement has an authoritative basis.
7. Present the draft and open decisions. Write only to an approved target path; inspect
   existing content and obtain overwrite approval before replacing a controlled document.
   Do not approve, release, or publish the procedure.

## Suggested Coverage

Adapt to the approved template and applicable scope; do not treat this list as a
substitute for the standard or the organization's procedures. The source request calls
for coverage of IEC 62304 clauses 5.1-5.8, 6.1, 7, 8, and 9; verify applicability against
the supplied edition and document scope, and map each clause to a section or an explicit
open item.

- Purpose, scope, responsibilities, definitions, and cited/associated documents
- Planning, requirements, architecture, detailed design, implementation, integration,
  system testing, and release (including clauses 5.1-5.8 where applicable)
- Maintenance, risk management, configuration management, and problem resolution
- AI-tool governance, generated-content review, provenance, and record retention where
  approved policy requires them
- Approvals, revision history, and appendices required by document control

When the organization confirms that class-specific controls apply, evaluate the supplied
Class A, B, and C definitions and decision rules. Do not derive class-specific controls
from examples or create requirements absent from approved sources.

## Acceptance Criteria

- [ ] The approved template, applicable edition, scope, and governing procedures are named.
- [ ] Each applicable clause is mapped to draft controls or explicitly marked unresolved.
- [ ] Organization-specific roles, classifications, records, and approval rules are
      evidence-based, not inferred.
- [ ] Recommendations are distinguished from mandatory requirements.
- [ ] Copyrighted standard text is paraphrased rather than reproduced.
- [ ] The result is clearly marked as a draft requiring qualified review and approval.
- [ ] No controlled document was overwritten, approved, or released without authorization.
