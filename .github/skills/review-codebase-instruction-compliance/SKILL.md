---
name: review-codebase-instruction-compliance
description: "Audit codebase against .github/instructions and report deviations"

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
source: ".github/prompts/codebase-review.prompt.md"
revisions:
  - chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
    model: "unknown/unknown@unknown"
    date: "2026-10-17"
    change: "Added explicit audit scope, rule mapping, missing-instructions fallback, and read-only/report-save boundaries.; Added scoped instruction drift, provenance, broad quality, and evergreen review dimensions."
    ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
  - chat_id: "skill-naming-convention-20261018"
    model: "unknown/unknown@unknown"
    date: "2026-10-18"
    change: "Applied approved skill naming decisions and updated active references; preserved workflow behavior and historical provenance."
    ai_log: "ai-logs/2026/10/18/skill-naming-convention-20261018/conversation.md"
---
# Codebase vs. Instructions Audit

Audit the repository against `.github/instructions` and report evidence-backed deviations without modifying files by default.

## Inputs
- Instructions: `.github/instructions/**/*` (md, mdx, yml, yaml, json)
- Codebase: all source files (excluding build/output/deps)

## Exclusions
`.git/`, `.github/` (except instructions), `node_modules/`, `dist/`, `build/`, `.venv/`, `.env/`, `.cache/`, `coverage/`, `out/`

## Procedure
1. **Discover instructions.** Extract explicit MUST/SHOULD/SHALL/REQUIRED/RECOMMENDED/MAY/OPTIONAL rules and assign stable Rule IDs for this review.
2. **Map rules to checks.** Define a concrete verification question or pattern for each rule.
3. **Analyze relevant files.** Inspect only in-scope files and cite evidence with file paths and line references.
4. **Classify deviations.** Record rule ID, instruction source, evidence, severity (Critical/High/Medium/Low), impact, remediation, and effort (S/M/L).
5. **Summarize.** Include the executive summary, deviations table, quick wins, larger initiatives, instruction gaps, and sources scanned.
6. **Save only if requested.** If the user explicitly asks for a report file, use the destination they provide or approve and ask before overwriting an existing file.

## Output (Markdown)

### Executive summary
2–3 sentences on alignment, gaps, risk

### Deviations table
| Rule ID | Rule | Instruction source | Evidence | Severity | Impact | Fix | Effort |
|---------|------|-------------------|----------|----------|--------|-----|--------|
| RULE-001 | Summary | `path#Section` | `file:lines` | High | Risk | Steps | M |

### Quick wins
Small, high-impact fixes

### Larger initiatives
Medium/large efforts with milestones

### Missing/ambiguous instructions
Gaps vs. best practices, suggest updates

### Sources scanned
Instruction files + key configs

### Durations
Report per-step and total elapsed time only when measured; do not estimate or fabricate durations.

## Missing Instructions Fallback
If no instructions found:
- State that no repository instructions were found.
- If the user still wants an audit, use generic best practices and label them as such.
- Keep the same output structure and include a limitations note.
- Recommend creating initial instruction documents.

## Check Examples
- **Security**: No secrets in repo, `.env` in `.gitignore`, dep audit, parameterized queries, input validation
- **Testing**: Unit/integration tests, coverage targets, test commands, CI test steps
- **CI/CD**: Workflows/pipelines, required checks, lint/format steps
- **Standards**: Linters/formatters, consistent versions, directory structure
- **Observability**: Structured logging, error handling, trace/metrics
- **Documentation**: README, contribution guidelines, ADRs

## Supplemental Review Dimensions

- Compare implementation with applicable instructions at the requested repository/folder scope. Map each finding to the exact instruction and code evidence; report ambiguity or conflicts in the instruction itself separately from implementation drift.
- Validate applicable instruction metadata and provenance against the repository policy when requested; distinguish a missing/invalid instruction from code nonconformance, and report provenance gaps without copying sensitive prompt or log content.
- For a broad code review, consider architecture, correctness, maintainability, testability, security, performance, error handling, operations, and documentation. Report only material findings supported by evidence.
- Use an evergreen-code lens where relevant: adaptability to likely change, clear extension points, testability, operability, dependency sustainability, and maintainability. Avoid predicting future needs without evidence.
- When discussing issue independence or remediation sequencing, identify shared files, APIs, data contracts, and prerequisites rather than asserting conflict-free parallel work.

## Boundaries
- Keep the audit read-only; do not edit code, instructions, or configuration unless the user explicitly requests remediation.
- Do not make network calls or run commands that write to the workspace.
- Distinguish verified facts from recommendations and unknowns; avoid generic findings without repository evidence.
- Respect the exclusions above.


