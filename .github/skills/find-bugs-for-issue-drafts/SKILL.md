---
name: find-bugs-for-issue-drafts
description: "Identify likely bugs via static analysis heuristics and generate GitHub-issue-ready findings with remediation"

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
source: ".github/prompts/bug-hunt-issues.prompt.md"
revisions:
  - chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
    model: "unknown/unknown@unknown"
    date: "2026-10-17"
    change: "Resolved the issue-creation/read-only conflict and clarified requested report saving and overwrite behavior."
    ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
  - chat_id: "skill-naming-convention-20261018"
    model: "unknown/unknown@unknown"
    date: "2026-10-18"
    change: "Applied approved skill naming decisions and updated active references; preserved workflow behavior and historical provenance."
    ai_log: "ai-logs/2026/10/18/skill-naming-convention-20261018/conversation.md"
---
# Bug Hunt — Findings to GitHub Issues

Review the current codebase for likely bugs using static analysis heuristics. Produce evidence-backed findings and GitHub issue drafts; do not create issues automatically.

## Objective

Perform a read-only, static analysis to surface likely bugs with concrete evidence and produce ready-to-post GitHub issue drafts including remediation suggestions.

## Heuristics (non-exhaustive)

- Null/undefined handling mistakes, unchecked optionals
- Incorrect async/await usage, missing `await`, unhandled promise rejections
- Off-by-one and boundary errors, unsafe indexing
- Resource leaks: timers, subscriptions, file/socket handles not disposed
- Data races/concurrency issues (where applicable)
- API contract mismatches: wrong types/shape, missing fields, misused enums
- Error handling/logging gaps: swallowed errors, broad catches, missing context
- Security-adjacent bugs: input not validated where required
- UI logic pitfalls: stale state, missing dependency arrays, uncontrolled/controlled mismatches (web)

## Procedure

1. Map key modules and contracts
   - Identify public APIs, core services, critical flows

2. Scan for bug heuristics
   - Record evidence with file paths and line ranges; avoid speculation

3. Validate and classify
   - Assign severity (Critical/High/Medium/Low) and impact description

4. Draft GitHub issues
   - Provide issue titles, descriptions (evidence, impact), remediation steps, and labels; do not submit them

5. Summarize and durations
   - Provide an executive summary and report per-step/total time only when measured

6. Save only if requested
   - Write a report only when the user explicitly asks and provides or approves a destination path
   - Ask before overwriting an existing report

## Output format (Markdown)

### Executive summary

- 2–3 sentences on overall bug posture and highest risks

### Findings

Provide a table. One row per finding.

| ID      | Category          | File:Lines                   | Severity | Impact                                        | Suggested fix                             |
| ------- | ----------------- | ---------------------------- | -------- | --------------------------------------------- | ----------------------------------------- |
| BUG-001 | Unhandled promise | `src/services/user.ts:72-84` | High     | User save may silently fail and corrupt state | Add missing await and catch; bubble error |

### GitHub issue drafts

Provide a section per finding with an issue-ready body.

#### [BUG-001] Unhandled promise in src/services/user.ts

- Severity: High
- Category: Async error handling
- Affected: `src/services/user.ts:72-84`

Description:

- Promise returned by service call isn't awaited or handled; errors are swallowed.

Impact:

- Can cause silent data loss or inconsistent UI state.

Remediation:

- Add `await` and proper error handling; propagate or show user-facing error as appropriate.

Labels:

- bug, severity:high, area:services

### Sources scanned

- Key files and directories consulted

### Durations

- Report measured per-step and total durations; do not estimate or fabricate elapsed time.

## Boundaries

- Keep the review read-only. Do not create GitHub issues, make external calls, or modify code/infrastructure unless the user explicitly requests that action.
- Drafting an issue is not permission to submit or publish it.
- Do not write to the workspace unless a report is explicitly requested; use the user's requested path and ask before overwriting an existing report.
- Keep findings evidence-based with file/line references and conservative classifications; call out uncertainty when applicable.




