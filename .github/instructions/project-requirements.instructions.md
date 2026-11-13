---
ai_generated: true
model: "unknown/unknown@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "5d5e4cc3-6034-4b17-aa97-f9c4df116620"
prompt: |
  create an instruction file for creating project requirement specifications
started: "2026-11-12T19:01:16.0366403-08:00"
ended: "2026-11-12T19:04:10.2792167-08:00"
task_durations:
  - task: "Drafting and validating project requirements guidance"
    duration: "00:02:54"
total_duration: "00:02:54"
ai_log: "ai-logs/2026/11/12/5d5e4cc3-6034-4b17-aa97-f9c4df116620/conversation.md"
source: "user request"
description: "Use when drafting, reviewing, or revising a project requirements specification; covers scope, evidence, verifiable requirements, traceability, and approval status."
applyTo: "**/*requirement*.md"
---

# Project Requirements Specifications

## Purpose and boundaries

Create or revise a project requirements specification (PRS) that gives stakeholders and delivery teams a shared, reviewable statement of the need, scope, constraints, requirements, and evidence for acceptance.

- Tailor the specification to the project, its decisions, risks, and intended readers. Do not require a fixed document length, lifecycle, notation, or approval process unless the project or governing policy requires it.
- Use [PRD authoring](../skills/author-product-requirements/SKILL.md) for product or feature requirements. Use [Vision and Scope guidance](vision-and-scope.instructions.md) when the work assesses a system, compares target directions, or proposes a delivery roadmap. A PRS may link to these documents rather than duplicate them.
- Treat a draft as unapproved until the authorized decision-maker has approved it. A specification does not, by itself, authorize implementation, procurement, or scope changes.
- Keep requirements distinct from design choices, implementation tasks, recommendations, assumptions, and decisions. Include a solution constraint only when it is required by evidence, policy, or an approved decision.

## Evidence and discovery

1. Identify the request, intended decision, audience, project context, and available source material.
2. Record material needs with their source, stakeholder or owner, and rationale when known. Distinguish verified facts, stakeholder statements, assumptions, estimates, recommendations, decisions, and unresolved questions.
3. Reconcile conflicting input explicitly. Record the conflict, its impact, the decision owner, and what evidence or decision is still needed.
4. Mark missing sources, access limits, and discovery gaps. Do not present an incomplete list as a complete set of requirements.
5. Do not invent stakeholder decisions, legal obligations, metrics, dates, budgets, estimates, or approval. Label proposals and obtain confirmation from the accountable owner.
6. Protect confidential information and personal data. Summarize only the information needed to explain a requirement, and follow applicable privacy, security, and compliance policies.

## Recommended content

Adapt this structure to the project and any approved template. Omit irrelevant sections and explain material omissions or unresolved topics when readers could otherwise mistake them for settled scope.

- **Document control**: title, status, version, date, author or owner, reviewers, approver, and change history as required by the project.
- **Purpose and context**: the problem or opportunity, intended outcomes, affected users or stakeholders, and evidence for the need.
- **Scope**: included capabilities, processes, systems, interfaces, data, and user groups; explicit exclusions; and boundaries with dependent projects or services.
- **Stakeholders and decisions**: affected parties, requirement owners, decision rights, and the people responsible for review and approval.
- **Requirements**: functional behavior, data, interfaces, operational needs, and relevant quality attributes. Group them so they are easy to review and trace.
- **Constraints, assumptions, dependencies, and risks**: state their source, owner, impact, and validation status where known.
- **Acceptance and verification**: observable conditions and appropriate evidence for determining whether the requirements are satisfied.
- **Open questions and decisions**: unresolved issues, options where useful, decision owner, and the evidence or date needed to resolve them.
- **Traceability**: links among source needs, requirements, acceptance evidence, and downstream design or delivery work when traceability is needed.

## Writing requirements

- Write each requirement as one independently understandable, necessary statement. Avoid combining unrelated outcomes with "and" or burying conditions in prose.
- State the actor or system, required behavior or quality, and relevant condition or boundary. Use consistent terms and define domain language or acronyms.
- Prefer observable, testable wording. Replace vague terms such as "fast", "easy", "robust", or "user-friendly" with an agreed measure or concrete behavior. If the measure is unknown, record it as an open question rather than inventing a target.
- Use "shall" only when the project adopts it to express a binding requirement. Otherwise use the project's established wording and distinguish requirements from preferences and proposals.
- Keep the rationale separate from the requirement statement. A rationale explains why the need exists; it does not add hidden acceptance conditions.
- Give requirements identifiers only when the project has an established scheme or traceability needs them. Preserve the project's naming and numbering conventions.
- Record priority, status, source, owner, and verification method when useful or required. Do not apply a prioritization scale unless its meaning and decision authority are agreed.
- Specify nonfunctional requirements as measurable conditions where possible. Include performance, availability, accessibility, security, privacy, reliability, recovery, supportability, audit, retention, or compliance only when relevant to the project and supported by applicable evidence or policy.
- Separate an external interface's required behavior and contract from a proposed implementation. Identify data ownership, formats, timing, error behavior, and compatibility needs where relevant.

## Requirement record template

Adapt these fields to the project. Do not leave a field that is not applicable as if it were agreed; mark it not applicable or unresolved where that distinction matters.

| Field                      | Content                                           |
| -------------------------- | ------------------------------------------------- |
| ID                         | Project-defined identifier, if needed             |
| Requirement                | One necessary, testable statement                 |
| Source and rationale       | Origin of the need and why it matters             |
| Owner                      | Person or role accountable for clarification      |
| Priority and status        | Use only the project's defined values             |
| Acceptance or verification | Observable result and evidence used to verify it  |
| Dependencies or notes      | Relevant conditions, links, or unresolved details |

Example:

> **Requirement:** An authorized user can view the profile fields approved for that user's role.
>
> **Acceptance:** Given an authorized user with a defined role, when the user requests their profile, the response contains the approved fields for that role and excludes fields not approved for it.
>
> Confirm the approved fields and role rules with the accountable data or product owner before treating this example as a project requirement.

## Review and change control

1. Review the specification with affected stakeholders and requirement owners. Confirm that each material need is represented or explicitly deferred, excluded, or unresolved.
2. Check that each requirement is necessary, unambiguous, feasible to verify, consistent with related requirements, and within stated scope.
3. Check that acceptance conditions do not introduce new, unapproved requirements and that every material requirement has a credible verification approach.
4. Confirm dependencies, assumptions, constraints, risks, open decisions, and approval status with their accountable owners.
5. Record material changes and their impact on scope, acceptance, cost, schedule, risk, and dependent decisions when those impacts can be assessed. Follow the project's approved change process; do not invent one.
6. Keep the summary, scope, requirements, acceptance criteria, and decision history consistent. Identify unresolved disagreements instead of silently choosing a side.

## Validation checklist

- [ ] Purpose, audience, context, outcomes, scope, exclusions, and document status are clear.
- [ ] Sources, stakeholder statements, assumptions, estimates, decisions, recommendations, and open questions are distinguishable.
- [ ] Requirements are in scope, independently understandable, necessary, and verifiable; unknown targets remain open questions.
- [ ] Functional, data, interface, and quality requirements address relevant needs without unsupported claims or solution prescriptions.
- [ ] Each material requirement can be traced to its source and to acceptance or verification evidence when required.
- [ ] Priorities, identifiers, terminology, and approval roles follow project conventions rather than invented standards.
- [ ] Dependencies, risks, constraints, and unresolved decisions have clear owners or next steps where known.
- [ ] Privacy, security, accessibility, compliance, and operational needs follow applicable evidence and policies.
- [ ] The document's summary, tables, links, cross-references, and approval status are consistent and checked.

## Related guidance

- [Product requirements authoring](../skills/author-product-requirements/SKILL.md)
- [Vision and Scope](vision-and-scope.instructions.md)
- [Human-facing writing](human-facing-writing.instructions.md)
- [AI provenance and logging](ai-assisted-output.instructions.md)
