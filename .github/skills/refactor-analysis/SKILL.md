---
name: refactor-analysis
description: "Analyze codebase for refactoring opportunities with evidence, impact, and prioritized plan"

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
source: ".github/prompts/refactor-analysis.prompt.md"
revisions:
  - chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
    model: "unknown/unknown@unknown"
    date: "2026-10-17"
    change: "Added evidence-grounded adaptability, testability, operability, and dependency-sustainability lens."
    ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
---
# Refactoring Opportunities Analysis

What needs refactoring in the codebase?

## Inputs
Repo (source, tests, configs, build/CI), signals (file size, complexity, duplication, deprecated APIs, TODOs, lint configs)

## Exclusions
`.git/`, `node_modules/`, `dist/`, `build/`, `.venv/`, `.env/`, `.cache/`, binaries

## Smell Catalog
- **Size/complexity**: Long functions, large classes/modules, deep nesting, god objects
- **Coupling**: High fan-in/out, cross-module imports, circular deps, tight UI/logic coupling
- **Duplication**: Repeated logic, copy-paste, near-duplicates
- **Naming**: Ambiguous names, mixed responsibilities, unclear boundaries
- **Error handling**: Inconsistent patterns, swallow-catch, missing context, unstructured logs
- **Testing friction**: Untestable design, static singletons, side effects in constructors
- **Performance**: N+1 calls, unnecessary re-renders, blocking I/O on hot paths
- **Deprecated/legacy**: Obsolete APIs, version straddles, pre-migration shims
- **Config drift**: Hardcoded constants, scattered env handling

## Process
1. **Inventory**: Largest files/functions, high-change areas, TODOs, key entry points/boundaries
2. **Detect smells**: Scan catalog, record evidence (file:line), note dependencies
3. **Propose refactors**: Type (extract, interface, inversion, composition, rename, dedupe, move, add tests), targets, outcome (readability/testability/reliability/performance), effort (S/M/L), risk (Low/Med/High)
4. **Prioritize**: Quick wins (S, low risk), Phase 1 (test enablers), Phase 2 (structural), Phase 3 (nice-to-have), safety net strategy
5. **Summarize**: Executive summary + durations

When requested, assess whether the design is likely to remain maintainable as requirements evolve: adaptability, extension points, testability, operability, and sustainability of dependencies. Tie each observation to current evidence and an explicit change scenario; do not predict unspecified future requirements or equate novelty with maintainability.

## Output (Markdown)

### Executive summary
2–3 sentences on maintainability and top refactor themes

### Hotspots inventory
Largest/most complex modules and risks

### Findings table
| Category | File/Target | Evidence | Impact | Refactor | Effort | Risk |
|----------|-------------|----------|--------|----------|--------|------|
| Duplication | `path:lines` | Similar in `path:lines` | Bug risk, cost | Extract shared util | S | Low |

### Refactor proposals (prioritized)
Grouped by Quick wins, Phase 1, Phase 2, Phase 3 with rationale

### Safety net and test strategy
Tests to add first for de-risking

### Sources scanned
Key files/dirs consulted

### Durations
Per-step + total

## Constraints
- Evidence-based, concrete file refs
- Prefer incremental, reversible refactors
- No code edits/network calls




