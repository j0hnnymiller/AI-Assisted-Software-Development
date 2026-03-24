---
name: commit-workspace-changes-logical-groups
description: Analyze current workspace changes, group them into logical commit sets, and create clear commits with focused messages
tags: [git, commits, workflow, code-review, repository-hygiene]
ai_generated: true
model: "openai/gpt-5.3-codex@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "commit-workspace-changes-logical-groups-20260324"
prompt: |
  commit these @workspace changes in logical groups
started: "2026-03-24T00:00:00Z"
ended: "2026-03-24T00:12:00Z"
task_durations:
  - task: "prompt file creation"
    duration: "00:06:00"
  - task: "provenance logging"
    duration: "00:04:00"
  - task: "readme update"
    duration: "00:02:00"
total_duration: "00:12:00"
ai_log: "ai-logs/2026/03/24/commit-workspace-changes-logical-groups-20260324/conversation.md"
source: "johnmillerATcodemag-com"
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
2. Build a grouping plan before committing:
   - Identify coherent change groups (feature, fix, docs, refactor, generated assets, formatting).
   - Keep generated output files with the source changes that produced them.
   - Keep unrelated cleanup in a separate commit.
3. Stage and commit each group in order:
   - Stage only files for one group.
   - Confirm staged set with `git diff --cached --name-only`.
   - Commit with a concise message.
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

## Expected Output

At the end, provide:

1. Total number of commits created.
2. For each commit:
   - SHA
   - commit message
   - short rationale
   - files included
3. Final repository state from `git status -sb`.
