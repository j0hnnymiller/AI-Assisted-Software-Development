---
ai_generated: true
model: "unknown/unknown@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "c16f927f-91c4-4a30-aada-8f74b099e547"
prompt: |
  proceed
started: "2026-10-18T21:39:23.8698502Z"
ended: "2026-10-18T21:40:31.4195000Z"
task_durations:
  - task: "Vision and Scope guidance adaptation"
    duration: "00:01:07"
total_duration: "00:01:07"
ai_log: "ai-logs/2026/10/18/c16f927f-91c4-4a30-aada-8f74b099e547/conversation.md"
source: "Approved V&S authoring/review recommendation; adapted V&S vision-and-scope.instructions.md"
description: "Use when drafting, reviewing, or revising a Vision and Scope document for a system assessment, target direction, project scope, requirements, architecture options, or delivery roadmap."
applyTo: "**/*.VnS.md"
---

# Vision and Scope Documents

## Purpose and boundaries

Create or review a decision-oriented document explaining the business need,
assessment boundary, current state, intended outcomes, target direction, and
practical path to decisions and delivery.

- For **review**, report prioritized, evidence-linked findings and recommendations;
  do not edit the source unless asked.
- For **drafting or revision**, preserve approved decisions and unaffected content.
  Do not silently broaden an engagement, commit implementation work, or substitute
  a preferred architecture.
- Separate the scope of discovery/assessment from the scope of future implementation.
  A roadmap recommendation is not, by itself, authorization or a delivery commitment.
- Tailor detail to audience, decisions, risk, and evidence. Keep decision-relevant
  material in the main narrative; put large inventories in referenced appendices.
- Use [PRD authoring](../skills/author-product-requirements/SKILL.md) for a product
  or feature requirements document. A Vision and Scope may inform a PRD, but is
  broader when it assesses a current system, alternatives, transition, and delivery
  direction. Do not duplicate detailed feature requirements unnecessarily.

## Evidence and decisions

1. Review the available scope agreements, kickoff records, stakeholder inputs,
   existing documentation, system context, code/schema evidence, and approved
   decisions. Identify missing or inaccessible sources.
2. Distinguish:
   - verified facts and dated observations;
   - stakeholder-reported statements;
   - assumptions and estimates;
   - approved decisions and their authority;
   - recommendations and rationale;
   - open questions and validation needed.
3. For material claims, record source, date or observation period, validation
   status, and confidence/limitations. Use an evidence register when it improves
   traceability. Do not claim measurements, code review, interviews, approvals,
   or completed discovery without evidence.
4. Reconcile conflicting sources explicitly. Identify the accountable decision
   owner; recency alone does not supersede an approved scope, policy, or decision.
5. Where a written engagement scope or stakeholder commitment exists, check that
   planned discovery, deliverables, audience, review, and acceptance reflect it.
   Distinguish commitments, estimates, preferences, conditional work, and inferred
   expectations. Track owner, condition, status, and evidence of completion or
   approved disposition where relevant. Do not impose a commitment checklist on
   engagements that have no such agreement.
6. Record access limits, missing artifacts, coverage gaps, and their impact on
   confidence and sequencing. Do not fill gaps with invented facts.
7. Validate hosting, privacy, security, regulatory, AI-use, staffing, licensing,
   vendor, and data-sharing constraints for the specific organization. Do not
   carry another client's assumptions into the document.
8. Protect confidential information. Describe relevant risks without reproducing
   credentials, personal data, or sensitive source records. Follow applicable
   repository-level security and privacy instructions.

## Content and analysis

Adapt the structure to an approved template and the decisions required; no single
heading order or fixed document length is mandatory. Include relevant topics:

- Executive decision summary: business need, recommended direction, benefits,
  material risks, decisions requested, and immediate next action.
- Context and scope: purpose, audience, systems/processes/departments included,
  exclusions, limitations, and evidence coverage.
- Current state: capabilities, ownership, applications, data, reporting, documents,
  integrations, infrastructure, operations, and known limitations.
- Objectives and outcomes: business outcomes and measurable indicators where
  supported. Separate outcome measures from technology choices.
- Requirements: testable functional and data needs, nonfunctional qualities,
  source/owner, priority, dependencies, and status where useful. Identify coverage
  gaps; do not imply an incomplete request list is a complete specification.
- Options and target direction: current, transition, and target states as needed;
  alternatives, boundaries, dependencies, and reasons for the preferred direction.
- Delivery and governance: plausible phases, capacity and skills, dependencies,
  decision rights, owners, acceptance/exit criteria, review and approval points.
- Risks, open questions, glossary, appendices, and next steps where they support
  decisions or traceability.

### Requirements and architecture recommendations

- Define assessment findings separately from future implementation scope.
- For material requirements, capture enough context to trace the need to its
  source and verify fulfillment. Use identifiers only when the project has an
  established scheme or traceability requires one; follow that scheme rather than
  imposing a universal ID format.
- Include reporting, documents, scheduled jobs, external exchanges, data ownership,
  quality, reconciliation, audit, retention, security, accessibility, reliability,
  observability, recovery, and supportability when relevant to evidence and scope.
- Define baseline/target pairs and workload assumptions for performance, availability,
  synchronization, or recovery only when supported. Mark proposed targets and
  assign validation/approval owners; never invent quantitative requirements.
- Treat deployment topology, module boundaries, data ownership, read/write separation,
  persistence, messaging, and hosting as related but distinct choices.
- Do not prescribe microservices, CQRS, event sourcing, separate databases,
  asynchronous messaging, cloud migration, or AI without an evidenced problem,
  bounded benefit, and applicable policy approval.
- For each material recommendation, explain the problem and where it applies;
  compare change with retaining the status quo; state expected benefits,
  trade-offs, dependencies, and adoption/operating costs. Support estimates with
  evidence or mark them unknown with an owner and validation step.
- Where a decision remains open, name the needed evidence, decision owner, and
  approval point. Keep summary, options, requirements, and roadmap consistent
  about what is recommended, conditional, or undecided.

### Delivery and transition

- Separate completed discovery from proposed activities and future milestones.
  Label estimates, dependencies, and uncertainty.
- Select initial work using stated business value, risk, dependency, measurability,
  and feasibility criteria; show the evidence behind the selection.
- Plan against available delivery capacity after support and maintenance needs;
  identify specialist dependencies and knowledge-concentration risks where evidenced.
- For each material phase, identify deliverables, owner, prerequisites, acceptance
  or exit evidence, and decision/approval responsibility.
- Address testing, data verification, user acceptance, pilot, cutover, rollback,
  and coexistence only to the extent required by the transition. Make data/write
  ownership, synchronization, reconciliation, compatibility, and failure handling
  explicit when parallel operation is proposed.
- If retirement is in scope, define evidence and approvals for replacement,
  data reconciliation, dependent consumers, retention, support, and safe
  decommissioning. Do not imply a system is safe to retire based on a text search
  or incomplete inventory.
- Assign material risks an impact, mitigation, owner, and escalation/decision
  trigger. Identify external work as a dependency unless it is explicitly in scope.

## Writing and review

- Use plain, decision-focused language and define acronyms on first use.
- Use past tense for completed activity, present tense for observed current state,
  and future/conditional language for proposals.
- Avoid marketing claims, unsupported certainty, first-person author instructions,
  and duplicated narrative. Keep source, date, and approval status for planning
  clarifications that affect decisions.
- Preserve useful existing structures and terminology. Use stable identifiers and
  Markdown links when the project requires traceability; ensure links resolve.
- A polished draft is not an approved scope, architecture baseline, or authorization
  to implement. Mark draft/approval state accurately.

## Validation checklist

- [ ] Audience, purpose, assessment scope, implementation scope, exclusions, and
      evidence limits are clear.
- [ ] Claims, assumptions, estimates, approvals, and recommendations are distinct
      and traceable to sources or explicitly labeled as open.
- [ ] Applicable commitments and discovery coverage are reflected, with gaps and
      dispositions visible; no commitments were invented.
- [ ] Outcomes and requirements are verifiable without unsupported metrics.
- [ ] Current, transition, and target states are consistent; alternatives and
      status-quo trade-offs are considered for material recommendations.
- [ ] Costs, capacity, dependencies, risks, owners, and decision/approval points
      are evidence-based or marked unresolved.
- [ ] Roadmap milestones are proposals unless authorized; transition, acceptance,
      rollback, and retirement gates fit the stated scope.
- [ ] Privacy, security, compliance, licensing, AI use, and data sharing follow
      applicable organization-specific policy.
- [ ] Summary, requirements, architecture, and next steps do not contradict each
      other. Dates, terms, tables, contents, and Markdown links are checked.
- [ ] Review findings are prioritized and located; requested edits preserve
      approved decisions and unaffected material.

## Related guidance

- [Product requirements](../skills/author-product-requirements/SKILL.md)
- [Instruction authoring](instruction-files.instructions.md)
- [Repository-wide constraints](copilot-instructions.md)
- [Provenance and logging](ai-assisted-output.instructions.md)
