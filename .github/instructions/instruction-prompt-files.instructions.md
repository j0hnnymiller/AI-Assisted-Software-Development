---
ai_generated: true
model: "anthropic/claude-3.5-sonnet@2024-10-22"
operator: "johnmillerATcodemag-com"
chat_id: "optimize-instructions-20251023"
prompt: |
  Create AI-optimized version of create-instruction-prompts.instructions.md with minimal tokens
started: "2025-10-23T04:38:00Z"
ended: "2025-10-23T04:38:00Z"
task_durations:
  - task: "optimization"
    duration: "00:01:00"
total_duration: "00:01:00"
ai_log: "ai-logs/2025/10/23/optimize-instructions-20251023/conversation.md"
source: "optimization-task"
revisions:
  - chat_id: "convert-prompt-files-to-skills-20261016"
    model: "OpenAI/GPT-6@Luna"
    date: "2026-10-16"
    change: "Updated the instruction-prompt workflow reference to the migrated workspace skill."
    ai_log: "ai-logs/2026/10/16/convert-prompt-files-to-skills-20261016/conversation.md"
  - chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
    model: "unknown/unknown@unknown"
    date: "2026-10-17"
    change: "Deprecated new instruction-generating prompts and documented skill-based migration."
    ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
applyTo: "**/*.instructions.prompt.md"
---

# Legacy Instruction-Prompt Reference (Deprecated)

> **Deprecated:** Do not create new `*.instructions.prompt.md` files or other prompt generators. Use the existing skill workflows under `.github/skills/` to create or update instruction files. This document is retained only for migrating existing instruction-generating prompts.

## Legacy Purpose

This legacy guidance describes prompt files that generated `*.instructions.md` files. It remains only to support safe review and migration of existing prompt files.

## Why This Exists

Instruction files (`*.instructions.md`) require strict AI provenance compliance and standardized structure. This file ensures that prompts generating such files automatically include all required metadata and compliance elements, preventing non-compliant instruction files.

## Legacy Scope & Application

- **Applies To**: Existing prompts matching pattern `**/*.instructions.prompt.md` during migration only
- **Purpose**: Preserve provenance and output requirements while replacing legacy prompt files with skills
- **Current workflow**: Use `.github/skills/create-instruction-files-instructions/SKILL.md`; do not create another prompt file

## Target Audience

- Developers creating instruction-generating prompts
- AI assistants tasked with generating instruction files
- Anyone building meta-prompts for documentation generation

## Legacy Output Requirements (Migration Only)

### 1. Context Section

Must include AI policy reference:

```markdown
## Context

<domain-specific context>

**CRITICAL**: All AI-generated artifacts MUST comply with
`.github/instructions/ai-assisted-output.instructions.md`. Generated
instruction file MUST include full AI provenance metadata.
```

### 2. Deliverable Section

Must include AI provenance template:

`````markdown
## Deliverable

Generate `.github/instructions/<domain>.instructions.md` with:

### Required AI Provenance Metadata (YAML Front Matter)

````yaml
ai_generated: true
model: "<model-name-and-version>"
operator: "<operator-username>"
chat_id: "<chat-identifier>"
prompt: |
  <exact-prompt-text>
started: "<ISO8601-timestamp>"
ended: "<ISO8601-timestamp>"
task_durations:
  - task: "<task-name>"
    duration: "<hh:mm:ss>"
total_duration: "<hh:mm:ss>"
ai_log: "ai-logs/<yyyy>/<mm>/<dd>/<chat-id>/conversation.md"
applyTo: "<pattern>" # Optional
---
\```

### Content Requirements
<specific requirements>
\```

### 3. Required Front Matter

```yaml
prompt_metadata:
  id: create-<domain>-instructions
  output_path: .github/instructions/<domain>.instructions.md
  category: documentation
  output_format: markdown
````
`````

````

## Complete Template

```markdown
---
mode: agent
model: Auto (copilot)
tools: ["create"]
description: Generates <domain> authoring guidelines
prompt_metadata:
  id: create-<domain>-instructions
  title: Generate <Domain> Instructions
  owner: <author-username>
  version: 1.0.0
  output_path: .github/instructions/<domain>.instructions.md
  category: documentation
  output_format: markdown
---

# Generate <Domain> Instructions

## Context

<domain-context>

**CRITICAL**: All AI-generated artifacts MUST comply with
`.github/instructions/ai-assisted-output.instructions.md`.

## Deliverable

[Include provenance template from above]
```

## Validation Checklist

- [ ] Context references AI policy
- [ ] Deliverable includes provenance template with all 10 fields
- [ ] Output path points to `.github/instructions/<name>.instructions.md`
- [ ] Category is 'documentation'
- [ ] Output format is 'markdown'
- [ ] ID follows `create-<domain>-instructions` pattern

## Common Mistakes

❌ Missing AI provenance section → Add complete YAML template
❌ Not referencing AI policy → Add CRITICAL statement
❌ Vague deliverable → Be explicit about metadata fields
❌ Forgetting applyTo field → Include when applicable

## Migrating an Existing Instruction-Generating Prompt

Do not create a new prompt. Compare an existing prompt with the instruction-authoring skill, migrate unique reusable guidance into that skill, and add a deprecation notice and replacement link to the legacy prompt.

## Reference

See `.github/instructions/ai-assisted-output.instructions.md` for complete provenance requirements.
````
