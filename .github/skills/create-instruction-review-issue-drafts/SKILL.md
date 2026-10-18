---
name: create-instruction-review-issue-drafts
description: "Review .github/instructions for deviations from best practices and generate GitHub issue drafts"

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
source: ".github/prompts/instructions-bestpractices-issues.prompt.md"
revisions:
  - chat_id: "skill-naming-convention-20261018"
    model: "unknown/unknown@unknown"
    date: "2026-10-18"
    change: "Applied approved skill naming decisions and updated active references; preserved workflow behavior and historical provenance."
    ai_log: "ai-logs/2026/10/18/skill-naming-convention-20261018/conversation.md"
---
# Instruction Files — Best Practices Review to GitHub Issues

Analyze `.github/instructions` files and report where they no longer represent best practices. Create GitHub issues for updates.

## Inputs
Instructions (`.github/instructions/**/*` md, mdx, yml, yaml, json), signals (MUST/SHOULD, version pins, tooling refs, security/testing/coding/CI policies)

## Exclusions
Non-instruction folders, no file modifications, no external calls

## Best-practices Lenses
- **Security**: Secret management, SBOM/dependency policy, secure defaults, headers, least privilege
- **Testing**: Coverage targets, CI enforcement, flaky test policy, test types
- **Code quality**: Formatting/linters, code review guidelines, naming conventions, ADRs
- **DevEx/Tooling**: Modern toolchain versions, deprecations, recommended alternatives
- **Observability**: Logging standards, error handling, tracing/metrics guidance
- **Cloud/Infra**: Environment config patterns, IaC references

## Process
1. **Inventory**: Map files to topics, note version/tool refs
2. **Detect outdated**: Deprecated tools, weak security stances, unclear/conflicting rules, missing critical sections
3. **Propose updates**: Concrete wording/structural changes, exact file/section
4. **Create issue drafts**: Title, context, suggested update, acceptance criteria, labels
5. **Summarize**: Executive summary + durations

## Output (Markdown)

### Executive summary
2–3 sentences summarizing gaps and urgency

### Findings table
| ID | Topic | File/Section | Finding | Impact | Suggested update |
|----|-------|--------------|---------|--------|------------------|
| INST-001 | Security | `path#Section` | Issue | High | Update details |

### GitHub issue drafts per finding
**[INST-001] Update security instructions: topic**
- Topic: Security
- File/Section: `path#Section`
- Problem: Current guidance issue
- Suggested update: New policy with examples
- Acceptance: File updated, add refs to tooling
- Labels: documentation, best-practices, security

### Sources scanned
List of instruction files/sections

### Durations
Per-step + total

## Constraints
- Evidence-based, cite exact files/sections
- Conservative suggestions, align with modern practices
- No edits/external calls





