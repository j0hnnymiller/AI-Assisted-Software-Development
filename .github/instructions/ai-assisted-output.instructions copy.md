---
ai_generated: true
model: "anthropic/claude-3.5-sonnet@2024-10-22"
operator: "johnmillerATcodemag-com"
chat_id: "generate-ai-output-policy-20260120"
prompt: |
  Generate comprehensive AI provenance and logging policy for all AI-assisted outputs
started: "2026-01-20T16:45:00Z"
ended: "2026-01-20T17:15:00Z"
task_durations:
  - task: "policy design"
    duration: "00:15:00"
  - task: "workflow specification"
    duration: "00:10:00"
  - task: "template creation"
    duration: "00:05:00"
total_duration: "00:30:00"
ai_log: "ai-logs/2026/01/20/generate-ai-output-policy-20260120/conversation.md"
source: ".github/prompts/create-ai-assisted-output-instructions.prompt.md"
applyTo: "**/*"
---

# AI-Assisted Output Instructions

## Overview

This repository requires provenance and chat linkage for AI-assisted artifacts. Keep metadata complete, logs traceable, and instructions concise for both humans and AI agents.

## Audience

Contributors generating or curating AI-assisted content (code, docs, diagrams, tests, data).

## Scope

- Define required provenance metadata.
- Define required chat logging artifacts and layout.
- Define post-creation checks before PR/merge.
- Require README updates for durable artifacts.
- Prefer concise, AI-readable outputs that minimize token use (except files in `docs/`, all README files, and files in the project root, which target human technical readers).

## Terminology

- Use “chat ID” in prose.
- Use `chat_id` in embedded metadata/front matter.
- Do not use “session” or “session-id” in paths or labels.
- Standardize placeholder paths on `<chat-id>`.
- Do not output `U+2011`; use `-` instead.
- Do not output `U+2019`; use `'` instead.

## Metadata placement policy

- For file formats that support embedded front matter (e.g., Markdown), provenance MUST be embedded as YAML front matter at the top of the artifact.
- For formats that do not support embedded front matter (images, binaries, etc.), create a sidecar file named `<artifact>.meta.md` containing the required metadata.
- Sidecars for Markdown (or any format supporting embedded front matter) are prohibited. Use embedded YAML front matter.

## Required provenance metadata

All AI-assisted artifacts must include:

- `ai_generated: true`
- `model`: `<provider>/<model>@<version>`
- `operator`: username or full name
- `chat_id`: unique chat identifier
- `prompt`: exact prompt text used
- `started`: ISO8601 timestamp
- `ended`: ISO8601 timestamp
- `task_durations`: list of task labels and durations
- `total_duration`: overall duration
- `ai_log`: path to `conversation.md`
- `source`: prompt file, user, or tool origin

## Standard front matter template

```yaml
---
ai_generated: true
model: "<provider>/<model>@<version>"
operator: "<username>"
chat_id: "<chat-id>"
prompt: |
  <exact prompt>
started: "<ISO8601>"
ended: "<ISO8601>"
task_durations:
  - task: "<task>"
    duration: "<hh:mm:ss>"
total_duration: "<hh:mm:ss>"
ai_log: "ai-logs/<yyyy>/<mm>/<dd>/<chat-id>/conversation.md"
source: "<creator or prompt path>"
---
```

## AI chat logging workflow

### Required path layout

- Base folder: `ai-logs/`
- Per-chat folder: `ai-logs/yyyy/mm/dd/<chat-id>/`
- Required files:
  - `conversation.md`
  - `summary.md`
- Optional folder:
  - `artifacts/`

### Required post-creation steps

1. Create or update `conversation.md` for this chat.
2. Create or update `summary.md` with objectives, decisions, artifacts, and next steps.
3. Ensure each generated artifact includes `chat_id` and `ai_log` metadata.
4. Update `README.md` for durable artifacts with a short description and link.
5. Validate links and metadata completeness.

### Minimal `conversation.md` template

````markdown
# AI Conversation Log

- Chat ID: <chat-id>
- Operator: <operator>
- Model: <provider>/<model>@<version>
- Started: <ISO8601>
- Ended: <ISO8601>

## Context

- Inputs: <files/requirements>
- Targets: <output artifacts>
- Constraints: <key policies>

## Exchanges

### 1

[<timestamp>] User

```text
<prompt>
```
````

[<timestamp>] Assistant

```text
<response>
```

````

### Minimal `summary.md` template

```markdown
# Session Summary

- Chat ID: <chat-id>
- Date: <YYYY-MM-DD>
- Operator: <operator>
- Model: <provider>/<model>@<version>
- Duration: <hh:mm:ss>

## Objective

<what this chat intended to deliver>

## Completed

- <artifact path> - <purpose>

## Key decisions

- <decision> - <rationale>

## Next steps

- <follow-up work>
````

## Placement and naming

- Place this file at `.github/instructions/ai-assisted-output.instructions.md`.
- Place logs in `ai-logs/yyyy/mm/dd/<chat-id>/`.
- Prefer lowercase descriptive artifact filenames.
- README entries are required for durable artifacts; optional for temporary drafts.
- Files in `docs/`, all README files (e.g., `README.md`, `docs/README.md`), and files in the project root are exempt from token optimization requirements and should target human technical readers with full detail and explanation.

## Quality checklist

- [ ] `ai_generated: true` present
- [ ] `model` has provider/model@version format
- [ ] `chat_id` and `ai_log` present
- [ ] Prompt and timestamps present
- [ ] `conversation.md` exists at referenced path
- [ ] `summary.md` exists for the chat
- [ ] README updated for durable artifacts
- [ ] No secrets/credentials in logs or prompts
- [ ] Embedded metadata used for Markdown (no sidecar)
- [ ] Content is concise and token-optimized (except `docs/` files, README files, and project root files, which prioritize human readability)

## PR checklist

- [ ] All AI-generated artifacts trace to exactly one chat folder
- [ ] Provenance metadata is complete and valid
- [ ] Required log files exist and links resolve
- [ ] README updates included where required

## Non-compliance remediation

- Missing logs: create `ai-logs/yyyy/mm/dd/<chat-id>/` with `conversation.md` and `summary.md`.
- Missing metadata: add required fields and validate formats.
- Orphaned artifacts: reconstruct chat log from available history and backfill metadata.
- Sidecar misuse: move metadata into embedded front matter when format supports it.
