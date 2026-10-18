---
name: create-bug-issues
description: "Identify bugs in codebase and generate GitHub issues with fixes"

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
source: ".github/prompts/create-issues-for-found-bugs.prompt.md"
revisions:
  - chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
    model: "unknown/unknown@unknown"
    date: "2026-10-17"
    change: "Added evidence-based issue independence and dependency assessment."
    ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
  - chat_id: "skill-naming-convention-20261018"
    model: "unknown/unknown@unknown"
    date: "2026-10-18"
    change: "Applied approved skill naming decisions and updated active references; preserved workflow behavior and historical provenance."
    ai_log: "ai-logs/2026/10/18/skill-naming-convention-20261018/conversation.md"
---
# Bug Hunt — Findings to GitHub Issues

Perform static analysis to surface bugs with evidence and create GitHub issue drafts with remediation.

## Heuristics
- Null/undefined handling, unchecked optionals
- Incorrect async/await, missing `await`, unhandled promises
- Off-by-one, boundary errors, unsafe indexing
- Resource leaks: timers, subscriptions, handles
- Data races/concurrency issues
- API contract mismatches
- Error handling gaps: swallowed errors, missing context
- Security: unvalidated input
- UI: stale state, missing deps, controlled/uncontrolled mix

## Process
1. Map key modules/APIs/flows
2. Scan for bug patterns (file:line evidence)
3. Classify (Critical/High/Medium/Low severity + impact)
4. Create GitHub issue drafts (title, evidence, impact, fix, labels)
5. Summarize + durations

For related findings, assess whether proposed issues can be implemented independently. Cite shared files, APIs, data contracts, or prerequisite fixes that create coordination or sequencing needs. Recommend splitting or linking issues only when that improves independent verification; mark parallel-safety as conditional rather than guaranteed.

## Output (Markdown)

### Executive summary
2–3 sentences on bug posture and highest risks

### Findings table
| ID | Category | File:Lines | Severity | Impact | Fix | 
|----|----------|------------|----------|--------|-----|
| BUG-001 | Unhandled promise | `file.ts:72-84` | High | Silent failure | Add await/catch |

### GitHub issue drafts per finding
**[BUG-001] Title**
- Severity: High
- Category: Type
- Affected: `file:lines`
- Description: Details
- Impact: Consequences
- Remediation: Steps
- Labels: bug, severity, area

### Sources scanned
Key files/dirs consulted

### Durations
Per-step + total

## Constraints
- Evidence-based with file:line refs
- Conservative classification
- No external calls/edits




