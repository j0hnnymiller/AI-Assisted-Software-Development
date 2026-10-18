---
name: tests-gap-analysis
description: "Analyze codebase and identify missing tests with prioritized recommendations"

ai_generated: true
model: "OpenAI/GPT-6@Luna"
operator: "johnmillerATcodemag-com"
chat_id: "convert-prompt-files-to-skills-20261016"
prompt: |
  help me convert the prompt files in the prompts folder into skills.
started: "2026-10-16T21:25:07.811Z"
ended: "2026-10-16T21:43:11.234Z"
task_durations:
  - task: "Converting repository prompt files to skills"
    duration: "00:18:03"
total_duration: "00:18:03"
ai_log: "ai-logs/2026/10/16/convert-prompt-files-to-skills-20261016/conversation.md"
source: ".github/prompts/tests-gap-analysis.prompt.md"
revisions:
  - chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
    model: "unknown/unknown@unknown"
    date: "2026-10-17"
    change: "Added design-for-testability analysis and an explicitly heuristic optional score."
    ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
---
# Tests Gap Analysis

What tests are needed and missing?

## Inputs
Codebase (source + test files), signals (unit/integration/e2e tests, runners, CI steps, coverage reports, fixtures, mocks)

## Exclusions
`.git/`, `node_modules/`, `dist/`, `build/`, `.venv/`, `.env/`, `.cache/`, `coverage/` artifacts, binaries

## Process
1. **Discover testing setup**: Frameworks/runners (Jest, Vitest, pytest, etc.), test dirs, naming patterns, coverage config/thresholds, CI workflow steps
2. **Inventory existing tests**: Count by type (unit/integration/e2e/component/contract), critical modules/components with tests, flakiness indicators
3. **Map critical functionality**: Core domains, public APIs, services, critical UI flows, error handling paths (use naming, folders, entry points)
4. **Identify gaps/risks**: Per critical area, state if tests exist/adequate; flag untested error paths, boundaries, auth/security checks, integration seams, and design friction that makes behavior hard to isolate or verify
5. **Recommend tests**: Prioritized list with type, target, scenario outline (Given/When/Then or Arrange/Act/Assert), rationale (risk/regressions), effort (S/M/L)
6. **Coverage goals/plan**: Baseline targets (overall + critical areas), 2–3 phase plan with quick wins first
7. **Summarize**: Executive summary + durations

For testability analysis, inspect evidence of tight coupling, hidden dependencies, side effects, difficult-to-control state, complex conditionals, and missing seams. Explain how each issue affects reliable verification and propose the smallest test or design change that would improve it. Use a numeric testability score only when the user supplies or approves a defined rubric; otherwise provide a qualitative assessment with evidence.

If a simple default score is requested, use a clearly labeled heuristic from 1 (behavior is difficult to isolate and relies on uncontrolled dependencies/state) to 5 (behavior is deterministic and has clear seams for isolated tests). Explain the evidence and do not present this score as test coverage, defect risk, or an objective quality metric.

## Output (Markdown)

### Executive summary
Current test posture, biggest gaps, risk level (2–3 sentences)

### Detected testing setup
Frameworks, dirs, patterns, CI steps, coverage config

### Test inventory
Counts by type, notable files/components and their tests

### Gaps/risks table
| Area/Target | Missing type | Scenario | Risk/Impact | Effort |
|-------------|--------------|----------|-------------|--------|
| auth/login | e2e | Invalid creds show error | Auth regressions | M |

### Recommended tests (prioritized)
Grouped by High/Medium/Low priority with scenario outlines

### Coverage goals and plan
Baseline targets, phased plan with milestones

### Sources scanned
Key files/dirs consulted

### Durations
Per-step + total

## Constraints
- Concrete, evidence-based (file paths, components)
- Prefer small, high-signal tests early
- No network calls/code modifications



