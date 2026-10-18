---
name: vue-migration-test-coverage
description: "Plan or implement behavior-focused regression tests for Vue migrations, including Vue 3.4 migrations; use when assessing migration readiness, coverage gaps, or requested test changes."
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
source: "Messer/.github/prompts/vue-3.4-migration-tests.prompt.md"
revisions:
  - chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
    model: "unknown/unknown@unknown"
    date: "2026-10-17"
    change: "Added Vue 3.4 migration-risk surfaces as evidence-driven checks, not assumed breaking changes."
    ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
  - chat_id: "skill-naming-convention-20261018"
    model: "unknown/unknown@unknown"
    date: "2026-10-18"
    change: "Applied approved skill naming decisions and updated active references; preserved workflow behavior and historical provenance."
    ai_log: "ai-logs/2026/10/18/skill-naming-convention-20261018/conversation.md"
---

# Vue Migration Testing

Use this skill to build a test strategy for a Vue version migration. Confirm the actual source and target versions, libraries, and build tools from the repository before relying on version-specific behavior.

## Procedure

1. Inventory framework versions, plugins, component libraries, router/state tools, build configuration, tests, and migration notes.
2. Identify changed APIs, removed/deprecated behavior, compatibility constraints, and third-party dependencies; verify against official release and migration documentation. For Vue 3.4 migrations, explicitly consider Composition/Options API interop, props/emits/`v-model`, slots/Teleport/Suspense, reactivity and watcher cleanup, router/state behavior, directives, async errors, and critical user flows; include only risks supported by the target code and current documentation.
3. Map affected components and user flows to risks, existing tests, and missing coverage.
4. Prioritize tests for critical workflows, routing/state, forms, rendering, accessibility, SSR/hydration if used, error states, and integration boundaries.
5. Propose focused unit/component/integration/e2e cases with setup, action, expected result, and risk rationale.
6. If asked to add tests, follow repository conventions and run the narrowest relevant test/build commands; report failures and environmental blockers.
7. Confirm the test plan covers migration regressions without duplicating equivalent coverage.

## Output

Provide a version/dependency inventory, migration risk matrix, prioritized test plan, suggested scaffolds (if requested), validation commands, and known gaps.

## Guardrails

- Do not assume a migration path, API change, or library compatibility from the target version alone.
- Do not claim a test passes unless it was executed successfully.
- Do not modify production code when the request is limited to test planning.
