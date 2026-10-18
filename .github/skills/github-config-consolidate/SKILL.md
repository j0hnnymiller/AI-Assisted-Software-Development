---
name: github-config-consolidate
description: "Consolidate the approved canonical version of .github files, AGENTS.md, CLAUDE.md, or .vscode/mcp.json into this repository from other repos, merge forked versions, and record superseded variants in the sync manifest. Use when asked to import, adopt, merge, or consolidate the main version of config files here."
argument-hint: "Approved decisions: file path + keep/import <repo>/merge"
metadata:
  ai_generated: true
  model: "anthropic/claude-opus-4.5"
  operator: "johnmillerATcodemag-com"
  chat_id: "create-github-config-sync-agent-20261014"
  ai_log: "ai-logs/2026/10/14/create-github-config-sync-agent-20261014/conversation.md"
  source: "johnmillerATcodemag-com"
revisions:
  - chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
    model: "unknown/unknown@unknown"
    date: "2026-10-17"
    change: "Prohibited importing prompt files and documented skill migration instead."
    ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
---

# Consolidate into the Canonical Repo

Writes approved versions into this repo and records which other versions they replace. Never commits.

## When to Use

- After decisions from `github-config-canonical` are approved by the user
- "Import X from repo Y", "adopt the newest version", "merge these copies"

## Preconditions

- Fresh inventory JSON (`github-config-inventory`)
- Explicit user approval per file or per approved batch
- Canonical copies of target files have no uncommitted changes (script refuses unless `-Force`)
- Prompt files are never imported: migrate approved prompt behavior into an existing or new skill, and keep the source prompt as a deprecated migration record.

## Procedure

1. For ordinary config files, preview: `./.github/skills/github-config-consolidate/scripts/Import-GithubConfigFile.ps1 -Path <paths> -WhatIf`. For `.github/prompts/**`, do not use the import script; update/create the approved skill and add the replacement link to the legacy prompt and README.
2. Apply by decision:
   | Decision | Command |
   |---|---|
   | import recommended | `Import-GithubConfigFile.ps1 -Path <paths>` |
   | import specific repo | `Import-GithubConfigFile.ps1 -Path <path> -FromRepo <repo-key>` |
   | keep canonical | `Import-GithubConfigFile.ps1 -Path <path> -RecordOnly` |
   | merge | edit the canonical file by hand, then `Import-GithubConfigFile.ps1 -Path <path> -RecordOnly` |
3. Every run updates `files.<path>.supersedes` in [.github/github-config-sync.json](../../github-config-sync.json) with all other variant hashes, so `github-config-distribute` can overwrite them safely.
4. For merged or AI-edited Markdown, update provenance front matter per `.github/instructions/ai-assisted-output.instructions.md`.
5. Validate: no editor errors in changed files, front matter parses, no secrets introduced. Re-run the inventory; consolidated files should show `Confidence: high` with the canonical repo recommended.
6. Leave changes uncommitted; suggest commit groups (for example via the `logical-git-commits` skill).

## Merge Guidance

- Start from the newest variant; port unique rules/sections from others; drop duplicates.
- Keep this repo's conventions (front matter fields, headings, file naming).
- Strip repo-specific values; never copy literal secrets.
- `.vscode/mcp.json`: use `${input:...}` / `${env:...}` for credentials.
- Keep legacy prompt paths visible in inventory but set their manifest `distribute` value to `none`; do not delete them or propagate them as active prompts.

## Implementation

- [Import-GithubConfigFile.ps1](./scripts/Import-GithubConfigFile.ps1)
