---
name: commit-changes-in-logical-groups
description: "Analyze current workspace changes, group them into logical commit sets, and create clear commits with focused messages"

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
source: ".github/prompts/commit-workspace-changes-logical-groups.prompt.md"
revisions:
  - chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
    model: "unknown/unknown@unknown"
    date: "2026-10-17"
    change: "Added explicit approval gates, staged/unstaged preservation, and staged-diff review before committing."
    ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
  - chat_id: "skill-naming-convention-20261018"
    model: "unknown/unknown@unknown"
    date: "2026-10-18"
    change: "Applied approved skill naming decisions and updated active references; preserved workflow behavior and historical provenance."
    ai_log: "ai-logs/2026/10/18/skill-naming-convention-20261018/conversation.md"
---
# Commit Workspace Changes In Logical Groups

Commit the current `@workspace` changes as a clean, reviewable sequence of focused commits.

## Objective

Produce a set of commits that:

- groups related files together by intent
- keeps unrelated changes separate
- uses clear, scoped commit messages
- preserves all existing work without destructive resets

## Required Workflow

1. Inspect current repository state:
   - Run `git status --short`.
   - Run `git diff --name-status`.
   - Run `git diff --cached --name-status`.
   - Preserve staged and unstaged distinctions; do not reset, unstage, or otherwise alter existing user work.
2. Build and present a grouping plan before staging:
   - Identify coherent change groups (feature, fix, docs, refactor, generated assets, formatting).
   - Keep generated output files with the source changes that produced them.
   - Keep unrelated cleanup in a separate commit.
   - List the proposed files and commit message for each group, then ask for approval.
3. For each approved group:
   - Stage only files for one group.
   - Inspect `git diff --cached --name-only` and the staged diff.
   - Request explicit approval for that commit; commit only after approval.
4. Validate completion:
   - Run `git status -sb`.
   - Report commit SHAs, titles, and grouped files.

## Commit Message Guidance

Use focused, imperative messages. Prefer one of these prefixes:

- `feat:` new functionality
- `fix:` bug fix
- `docs:` documentation-only changes
- `refactor:` code restructuring without behavior change
- `chore:` maintenance, formatting, generated artifacts not user-facing
- `test:` test additions or updates

Examples:

- `feat: add onboarding exercise slide deck`
- `fix: correct Tuesday manifest malformed entry`
- `docs: normalize formatting in session summary`

## Guardrails

- Do not rewrite history.
- Do not use destructive commands (`git reset --hard`, `git checkout --`, force push) unless explicitly requested.
- Do not combine unrelated edits into one commit.
- If a file has mixed changes for different intents, use partial staging (`git add -p`) or ask for guidance when safe splitting is ambiguous.
- Do not stage or commit unrelated work without specific approval.
- Invocation of this skill is not permission to alter Git state or create commits.

## Expected Output

At the end, provide:

1. Total number of commits created.
2. For each commit:
   - SHA
   - commit message
   - short rationale
   - files included
3. Final repository state from `git status -sb`.




