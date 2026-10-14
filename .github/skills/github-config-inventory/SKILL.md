---
name: github-config-inventory
description: "Inventory and drift report of .github files, AGENTS.md, CLAUDE.md, and .vscode/mcp.json across every git repo under c:\\git. Use when asked to find differences between repos, audit config drift, list which repos have which agents/instructions/prompts/skills, or start a cross-repo consolidation."
argument-hint: "Optional repo filter, e.g. AIASD/*"
metadata:
  ai_generated: true
  model: "anthropic/claude-opus-4.5"
  operator: "johnmillerATcodemag-com"
  chat_id: "create-github-config-sync-agent-20261014"
  ai_log: "ai-logs/2026/10/14/create-github-config-sync-agent-20261014/conversation.md"
  source: "johnmillerATcodemag-com"
---

# GitHub Config Inventory

Read-only scan that compares every in-scope file across repos and classifies drift against this (canonical) repo.

## When to Use

- First step of any cross-repo review, consolidation, or sync
- "Which repos have a different copy of X?", "what's missing here?", "report drift"

## Scope

Defined in the manifest [.github/github-config-sync.json](../../github-config-sync.json): `root`, `maxDepth`, `include`/`exclude` globs, `skipDirs`, per-repo `mode` (`sync` | `report` | `ignore`). Defaults: `.github/**`, `AGENTS.md`, `CLAUDE.md`, `.vscode/mcp.json`. Repo discovery stops at the first folder with a `.git` directory, skipping `*.worktrees`, dot folders, and `skipDirs`.

## Procedure

1. From the canonical repo root run:
   ```powershell
   ./.github/skills/github-config-inventory/scripts/Get-GithubConfigInventory.ps1            # all repos
   ./.github/skills/github-config-inventory/scripts/Get-GithubConfigInventory.ps1 -Repo 'AIASD/*'
   ```
   Writes `%TEMP%/github-config-inventory.json` (override with `-OutFile`). Add `-ShowIdentical` to list everything.
2. Read the console summary; load the JSON for details. Per file: `Status`, `Variants` (grouped by normalized content hash), `Entries` (per repo: blob, last commit date/sha/author/message, commit count, working-tree state, secret hits), `Recommended`, `Confidence`, `Reason`.
3. Report using the format below. Do not modify any files.

## Status values

| Status            | Meaning                                          |
| ----------------- | ------------------------------------------------ |
| `identical`       | Same bytes everywhere                            |
| `whitespace-only` | Differs only in line endings/trailing whitespace |
| `canonical-only`  | Only in this repo                                |
| `missing-here`    | In other repos, not here (import candidate)      |
| `diverged`        | Different content; see recommendation            |

## Report Format

1. Repos scanned: key, branch, HEAD, dirty, mode, file count
2. Status counts
3. Table of `diverged` + `missing-here`: path, variants, repos, recommended repo(s), confidence
4. Flags: `SecretHits > 0` (never print values), uncommitted copies, repos on non-default branches
5. Next step: hand diverged files to the `github-config-canonical` skill

## Implementation

- [Get-GithubConfigInventory.ps1](./scripts/Get-GithubConfigInventory.ps1)
- [GithubConfigSync.psm1](./scripts/GithubConfigSync.psm1) — shared module used by all `github-config-*` skills
