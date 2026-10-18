---
name: github-config-canonical
description: "Choose the canonical (main) version of a .github file, AGENTS.md, CLAUDE.md, or .vscode/mcp.json that differs between repos, using git history lineage and file content. Use when asked which version is newest or correct, to recommend a main version, compare variants, or decide what to merge."
argument-hint: "File path(s) relative to repo root, e.g. .github/instructions/x.instructions.md"
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
    change: "Added semantic prompt-to-skill comparison instead of importing legacy prompts."
    ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
---

# Choose the Canonical Version

Recommends one version per diverged file using git history first, then content. Read-only.

## When to Use

- After `github-config-inventory` reports `diverged` or `missing-here` files
- "Which copy of X should be the main one?", "diff the versions of X"

## Procedure

1. Ensure a fresh inventory exists (run `github-config-inventory` if older than the last change).
   - For `.github/prompts/**`, compare the full prompt's purpose, workflow, inputs, and outputs with potentially related canonical skills; same-path git history is not enough. Recommend an existing skill to update or a new skill to create; do not recommend importing or distributing the prompt file.
2. Show evidence and diffs:
   ```powershell
   ./.github/skills/github-config-canonical/scripts/Compare-GithubConfigVariant.ps1 -Path <rel-path>[, ...]        # --stat
   ./.github/skills/github-config-canonical/scripts/Compare-GithubConfigVariant.ps1 -Path <rel-path> -Full         # full diff
   ```
3. Apply the decision rules below; verify the script's recommendation by reading the full diff.
4. For ordinary config files, output a decision per file: `keep-canonical`, `import <repo>`, or `merge <variants>`, with one-line rationale. For legacy prompts, report `migrate to <skill>` or `new skill required` and get approval before writing.

## Decision Rules (in order)

1. **Lineage (strongest).** A variant is _stale_ when another repo's git history contains that exact blob and the repo has since moved on (`StaleIn`). If exactly one variant is not stale, it is canonical (`Confidence: high`). Variants listed in the manifest `files.<path>.supersedes` are also stale.
2. **Forks.** If 2+ variants are not stale (`Confidence: low`, "forked"), compare content:
   - One is a superset of the others' rules/sections → choose it.
   - Each has unique improvements → `merge`; base on the newest, port the unique parts of the others.
3. **Recency.** Prefer the newest commit date, then the most repos sharing it, then more lines, then this repo.
4. **Content quality overrides.** Do not choose a version that has repo-specific values (paths, org/repo names, environment names), literal secrets (`SecretHits`), broken front matter, or an obviously truncated body. Flag the issue instead.
5. **Uncommitted copies** (`Uncommitted`) are evidence only; tell the user to commit them before choosing them.

## Limits

- Lineage is matched per path; renames are not followed. Suspected renames (same name in another folder, or near-identical content) must be flagged for the user.
- `.vscode/mcp.json` often differs legitimately per repo; prefer `keep-canonical` + per-repo exclude unless servers are clearly shared.

## Output Format

| File | Variants | Decision | Source | Confidence | Rationale |
| ---- | -------- | -------- | ------ | ---------- | --------- |

Then list `merge` files with the specific sections to port from each variant.
