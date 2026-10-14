---
name: github-config-distribute
description: "Keep all repos under c:\\git in sync with the canonical .github files, AGENTS.md, CLAUDE.md, and .vscode/mcp.json from this repository. Plans or applies safe updates on a branch in each target repo, detects target-ahead or forked copies, and explains the sync strategy. Use when asked to push, propagate, sync back, roll out, or keep repos in sync."
argument-hint: "Optional repo filter (e.g. AIASD/*) and plan | apply | apply+commit"
metadata:
  ai_generated: true
  model: "anthropic/claude-opus-4.5"
  operator: "johnmillerATcodemag-com"
  chat_id: "create-github-config-sync-agent-20261014"
  ai_log: "ai-logs/2026/10/14/create-github-config-sync-agent-20261014/conversation.md"
  source: "johnmillerATcodemag-com"
---

# Distribute Canonical Config to Other Repos

Hub-and-spoke sync: this repo is the hub. Spokes only receive updates that are provably safe. Strategy and manifest details: [sync-strategy.md](./references/sync-strategy.md).

## When to Use

- After consolidation, to roll canonical versions out to other repos
- Periodic drift check ("are all repos in sync?")

## Procedure

1. Commit consolidation changes in this repo first (uncommitted canonical files are skipped).
2. Plan (dry run, read-only):
   ```powershell
   ./.github/skills/github-config-distribute/scripts/Sync-GithubConfig.ps1 [-Repo 'AIASD/*']
   ```
   Writes `%TEMP%/github-config-sync-plan.json`.
3. Present the plan per repo. Explain non-write actions:
   - `target-ahead` / `forked` → run `github-config-canonical` + `github-config-consolidate` for those files first
   - `target-only` → candidates to import here, or leave as repo-specific
   - `uncommitted` / dirty repo → owner must commit or stash
   - `blocked-secret` → fix the canonical `mcp.json`
4. With user approval, apply:
   ```powershell
   Sync-GithubConfig.ps1 -Repo <filter> -Apply            # creates branch, writes files
   Sync-GithubConfig.ps1 -Repo <filter> -Apply -Commit    # also commits
   ```
   Default branch: `chore/sync-github-config-<yyyyMMdd>` (`-Branch` to override). Repos with dirty working trees, `mode` other than `sync`, or an existing branch of the same name are skipped.
5. Never push. List the pushes and PRs the user needs to make (for example `git -C <repo> push -u origin <branch>` then open a PR).
6. Re-run the plan; applied repos should show no `update`/`add`.

## Safety Rules

- Overwrite only when the target's content is in canonical history or listed in `supersedes`
- Never delete files; never touch files outside the manifest scope
- Add new files only when the manifest says `distribute: "all"` or lists the repo
- Only the user pushes or merges

## Implementation

- [Sync-GithubConfig.ps1](./scripts/Sync-GithubConfig.ps1)
- [sync-strategy.md](./references/sync-strategy.md)
