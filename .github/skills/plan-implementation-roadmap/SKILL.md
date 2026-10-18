---
name: plan-implementation-roadmap
description: "Turn approved requirements and dependency maps into a phased, verifiable implementation roadmap"
argument-hint: "Requirements and implementation-plan paths"
ai_generated: true
model: "unknown/unknown@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
prompt: |
  files in the .github/prompts folder should be campared with the canonical skills. If a skill does not exist for the prompt, create a new skill. Prompt files are being deprecated. update the instructions, skills, and agents, responsible for syncing .github files.
started: "2026-10-18T09:55:12.922-07:00"
ended: "2026-10-18T10:05:54.310-07:00"
task_durations:
  - task: "Prompt-gap review and roadmap skill authoring"
    duration: "00:10:41"
total_duration: "00:10:41"
ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
source: "zeus/zeus.academia.3b/.github/prompts/create-academia-execution-plan.prompt.md (spoke migration input)"
---

# Plan an Implementation Roadmap

Create a dependency-aware execution roadmap from approved requirements and implementation
planning inputs. This skill produces a plan only; it does not implement work or create
external work items.

## Inputs

- Authoritative requirements, business rules, and architecture or project overview.
- An implementation plan, dependency map, backlog, or equivalent source of slice-level work.
- Optional: a target output path and a requested planning horizon or release boundary.

If the authority of an input is unclear, requirements conflict, or a material ordering or
scope decision is missing, ask before producing the roadmap. Do not treat examples from a
project-specific source as universal planning rules.

## Procedure

1. Read the supplied sources and applicable repository instructions. Record scope,
   constraints, explicit dependencies, business rules, test obligations, and exclusions.
2. Build a traceable inventory of every in-scope deliverable. Map each item to its source
   and preserve its acceptance criteria. Do not add, rename, or drop work without approval.
3. Derive ordering from explicit prerequisites and technical or business constraints.
   Identify parallel work only when the sources establish independence and shared-resource
   conflicts have been considered. Mark unresolved dependencies instead of guessing.
4. Group the ordered work into phases with clear objectives and exit gates. Put foundational
   work before dependent slices, required sequential gates before their dependents, and
   reporting or operational work after its data-producing prerequisites where applicable.
   Do not impose fixed phase numbers or project-specific slice rules.
5. For each phase, state:
   - Objective and included deliverables
   - Dependencies, blockers, and verified parallel opportunities
   - Acceptance criteria and validation/test gates
   - Risks, mitigations, and any unverified assumptions
   - Exit criteria that determine whether the next phase can begin
6. Cross-check the plan against the input inventory: every in-scope item appears exactly
   once, all stated dependencies are respected, and all required business-rule checks have
   a verification point.
7. Present the draft for review. Write it only to a user-approved target path; check for
   existing files and obtain overwrite approval before replacing one. Do not create issues,
   project-board items, commits, or other external state unless separately requested.

## Output Structure

1. Scope and source inputs
2. Planning assumptions and unresolved decisions
3. Dependency-driven phase plan
4. Phase backlog with deliverables and measurable acceptance criteria
5. Validation and quality gates
6. Risks and mitigations
7. Exit criteria and next decisions

## Acceptance Criteria

- [ ] Every in-scope deliverable maps to an authoritative input and appears once.
- [ ] Explicit dependencies and sequencing constraints are preserved.
- [ ] Parallel work is justified by verified independence; unknown dependencies are flagged.
- [ ] Each phase has measurable acceptance and validation gates.
- [ ] Assumptions, missing information, risks, and unresolved decisions are visible.
- [ ] The skill has not implemented work or performed external writes.
