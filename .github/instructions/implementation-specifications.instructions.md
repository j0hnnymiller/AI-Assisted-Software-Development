---
description: "Use when creating, reviewing, or updating implementation specifications in specs/**/*.spec.md, or preparing a slice for the implement-vertical-slice skill."
applyTo: "specs/**/*.spec.md"
ai_generated: true
model: "unknown/unknown@unknown"
operator: "j0hnnymiller"
chat_id: "implementation-specifications-20261029-0acb8bc1"
prompt: |
  with the deprecation of prompt files, implementation prompts are replace with an implementation specification and a generic skill that implements a slice using the implementation specification.

  Verify that the generic skill exists.
  create an instruction file for implementation specifications. implementation specifications are stoored in the specs folder. implementation specifications have a .spec.md extension
started: "2026-10-29T08:33:53-07:00"
ended: "2026-10-29T08:36:16-07:00"
task_durations:
  - task: "repository review and specification guidance design"
    duration: "00:00:40"
  - task: "authoring and validation"
    duration: "00:01:43"
total_duration: "00:02:23"
ai_log: "ai-logs/2026/10/29/implementation-specifications-20261029-0acb8bc1/conversation.md"
source: "user"
---

# Implementation Specification Instructions

## Overview

**Audience:** Specification authors, reviewers, and implementation agents.
**Scope:** Create and maintain implementation specifications under the repository-root `specs/` folder with the `.spec.md` extension. Subfolders are allowed.

Separate the durable description of **what to implement** from the reusable workflow describing **how to implement it**. Replace per-slice implementation prompt files with specifications consumed by the existing [implement-vertical-slice skill](../skills/implement-vertical-slice/SKILL.md). Do not embed a copy of that skill or prompt-file execution metadata in a specification.

## Contents

- [Placement and prerequisites](#placement-and-prerequisites)
- [Required specification content](#required-specification-content)
- [Authoring and implementation handoff](#authoring-and-implementation-handoff)
- [Copy-ready template](#copy-ready-template)
- [Example](#example)
- [Validation checklist](#validation-checklist)
- [Maintenance and safety](#maintenance-and-safety)

## Placement and prerequisites

- Use `specs/[<area>/]<slice-id>-<short-description>.spec.md`, for example `specs/catalog/SL-001-view-product.spec.md`. Keep IDs stable and use lowercase descriptive filename words.
- Define one bounded, end-to-end slice per specification. Reference shared plans and prerequisite specifications rather than duplicating them.
- Read the source requirements, applicable repository instructions, relevant code, and existing tests before specifying a solution. Link actual sources with paths relative to the specification.
- Identify the reviewing role or team and the specification's status: `Draft`, `Ready for review`, `Approved`, `Implemented`, or `Blocked`. Record unresolved decisions explicitly; do not present assumptions as approved requirements.
- Include the repository-required embedded provenance and logs for AI-assisted specifications; see [AI-assisted output instructions](ai-assisted-output.instructions.md). Do not invent model identities, timestamps, or validation results.

## Required specification content

1. **Identity and goal:** Stable slice ID, title, status, owner/reviewer role, user or stakeholder outcome, and links to source requirements, business rules, use cases, and any implementation plan.
2. **Scope and exclusions:** In-scope behavior and explicit non-goals. Include the relevant UI, API, domain, persistence, or integration surfaces; do not force layers the slice does not need.
3. **Context and dependencies:** Relevant existing paths and conventions, prerequisite slice IDs and relative links, required contracts, configuration, tooling, data, and test environment. State `None` when there are no dependencies. Separate verified facts, assumptions, and open questions.
4. **Behavior and contracts:** Inputs, outputs, validation, authorization, state changes, error responses, and boundary cases. Describe compatibility and existing behavior that must remain unchanged. Specify migrations, observability, and rollback needs when relevant; otherwise state why they are not applicable.
5. **Acceptance criteria:** Stable IDs such as `AC-001` with observable pass/fail outcomes. Cover the success path, relevant failures and boundaries, and regressions. Use Given/When/Then where helpful. Define units, thresholds, datasets, and measurement conditions for quantitative requirements; avoid unsupported coverage or performance targets.
6. **Verification:** Map every acceptance criterion to a planned test or manual check. Include focused unit, integration, and end-to-end checks as appropriate, exact repository-supported commands, working directories, prerequisites, and expected results. Label proposed tests and unverified commands honestly. Do not invent commands or substitute mocks for a required real integration check.
7. **Showcase and completion:** Reproducible human-facing demonstration steps and expected observations; the evidence required for acceptance, known risks, and the next dependency or handoff. Keep planned checks distinct from execution evidence.

Optional: Add diagrams, decision records, or supporting tables only when they clarify the slice. Do not prescribe an architecture, framework, or dependency without requirements and repository evidence.

## Authoring and implementation handoff

1. Inspect sources and existing implementation patterns; select a slice with independently verifiable user value.
2. Draft the required sections and resolve conflicts with the reviewer. Split overly broad work into linked specifications with explicit dependencies.
3. Review scope, contracts, acceptance criteria, and the criterion-to-check mapping. Mark blocking unknowns and obtain review before marking the specification `Approved`.
4. Make the reviewed specification available in version control before handing it to a separate worktree. Creating or approving a specification does not authorize committing, pushing, merging, or implementing it.
5. Invoke `implement-vertical-slice` with the explicit specification path, for example `/implement-vertical-slice specs/catalog/SL-001-view-product.spec.md` where skill slash invocation is supported; otherwise request that skill by name and supply the path.
6. The skill reads the specification and applicable instructions, inspects code and tests, proposes an implementation plan, and waits for user approval before editing. Specification approval is not a substitute for that implementation approval.
7. Implement only the selected, approved slice. If requirements change or a dependency is missing, stop for clarification and update the specification through review rather than silently expanding scope.
8. Record actual verification evidence and unresolved risks after implementation. Mark `Implemented` only after all acceptance criteria have evidence; identify the next slice without automatically starting it.

## Copy-ready template

Add complete embedded AI provenance above this body when applicable. Replace placeholders, expand the acceptance table for all required scenarios, and remove instructions to the author before review.

```markdown
# <SL-ID>: <Slice title>

- Status: Draft
- Owner/reviewer: <role or team>
- Sources: <relative links to requirements, rules, use cases, and plan>

## Goal
<Actor, action, and observable value.>

## Scope and exclusions
- In scope: <bounded end-to-end behavior and surfaces>
- Out of scope: <explicit non-goals>

## Context and dependencies
- Existing implementation and conventions: <verified paths and facts>
- Prerequisites: <slice IDs and relative links, or None>
- Environment: <configuration, tooling, and safe test data>
- Assumptions: <explicitly unconfirmed items, or None>
- Open questions/blockers: <decision and reviewing role, or None>

## Behavior and contracts
- Inputs and outputs: <shapes and observable results>
- Validation, authorization, and errors: <rules and failure behavior>
- State and integrations: <changes, boundaries, and dependencies>
- Compatibility: <behavior that must remain unchanged>
- Migration, observability, and rollback: <requirements or N/A with reason>

## Acceptance criteria
- AC-001: Given <context>, when <action>, then <observable result>.
- AC-002: Given <invalid or boundary input>, when <action>, then <result>.
- AC-003: <Existing behavior preserved and how it is observed>.

## Verification
| Criterion | Planned test/check | Command and working directory | Expected result |
|-----------|--------------------|-------------------------------|-----------------|
| AC-001 | <test path/name or manual steps> | <verified command, or manual> | <pass condition> |
| AC-002 | <test path/name or manual steps> | <verified command, or manual> | <pass condition> |
| AC-003 | <regression check> | <verified command, or manual> | <pass condition> |

## Showcase and completion
1. <Setup and action using safe test data.>
2. <Expected human-visible observation and cleanup.>

- Completion evidence: <required diffs, check results, and AC mapping>
- Execution evidence: Not run; specification only.
- Risks: <known risks or None identified, with limitations>
- Next dependency/handoff: <slice ID and link, or None>
```

## Example

Illustrative body excerpts for `specs/catalog/SL-001-view-product.spec.md`:

- **Goal:** A shopper can view an existing product's public name and price.
- **Scope:** Read-only product lookup and its existing detail screen. Exclude editing, purchasing, and schema changes.
- **Contract:** A known public product ID returns its name and price; an unknown ID shows the existing not-found state. Preserve the current authorization policy and price formatting.
- **AC-001:** Given a public product fixture, opening its detail screen displays that fixture's name and formatted price.
- **AC-002:** Given an unknown product ID, opening the detail screen shows not found and no stale product data.
- **AC-003:** Reading a product leaves its stored fields unchanged.
- **Verification:** Map AC-001 to a detail-screen integration check, AC-002 to the not-found check, and AC-003 to a before/after persistence comparison. Specify actual test paths, commands, working directories, and fixtures after inspecting the target application.
- **Showcase:** Open the seeded product, compare its displayed values to the fixture, then open an unknown ID and observe not found.

This example does not assert that this course repository contains a catalog application or executable catalog tests.

## Validation checklist

- [ ] File is under `specs/` and ends in `.spec.md`; its stable slice ID is unique.
- [ ] Sources, prerequisite links, and referenced existing paths resolve.
- [ ] Scope delivers bounded value; exclusions, dependencies, assumptions, and blockers are explicit.
- [ ] Contracts cover relevant failure and boundary behavior and preserve intended compatibility.
- [ ] Every acceptance criterion maps to a reproducible check with an expected result.
- [ ] Commands and prerequisites come from the target repository; unverified items are labeled.
- [ ] Showcase, completion evidence, and next handoff are specified.
- [ ] The implementation skill is referenced rather than duplicated; approval gates remain intact.
- [ ] Required provenance, logs, README linkage, and review status are complete.

## Maintenance and safety

The owning team reviews contract, scope, dependency, and acceptance changes in version control. Preserve slice and criterion IDs so implementation evidence remains traceable; record material requirement changes and obtain renewed approval before implementing them.

Never include credentials, production data, or sensitive conversation content. Reference secret names and safe configuration mechanisms instead. Do not authorize destructive operations, production access, or permission bypasses through a specification. Instructions and specifications guide behavior; they are not security controls.
