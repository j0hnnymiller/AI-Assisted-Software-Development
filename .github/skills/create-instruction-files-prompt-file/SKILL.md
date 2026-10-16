---
name: create-instruction-files-prompt-file
description: "Create prompt that generates Markdown authoring guidelines for effective repository prompts"

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
source: ".github/prompts/create-instruction-files-prompt-file.prompt.md"
---
# Meta Prompt — Generate Prompt Authoring Instructions

Create prompt for generating Markdown guidelines to help create effective, well-structured repository prompts.

## Output Target

`.github/skills/create-prompt-file-instructions-file/SKILL.md` → creates → `.github/instructions/prompt-file.instructions.md`

## Generated Prompt Must Include:

### Required Metadata (YAML Frontmatter)

- Top-level: `mode` (agent|chat), `model` (Auto or specific), `tools` (array), `description`
- `prompt_metadata`: `id: prompt-file.instructions-prompt`, `output_path`, title, version, tags, category

### Content Structure

1. **Audience & Scope**: Developers, prompt authors, skill expectations
2. **Prompt File Structure**: YAML frontmatter (mode, model, tools, description at top-level + prompt_metadata), organization standards
3. **Field-by-Field Docs**:
   - Top-level required: mode (agent for files), model (Auto default), tools (array), description (NOT in metadata)
   - prompt_metadata: id, title, owner, output_path, output_format, tags
   - Validation rules, examples
4. **Best Practices**: Metadata structure, tool selection methodology, mode specification, clarity/specificity
5. **Quality Assurance**: Validation checklist, authoring standards, testing
6. **Examples & Templates**: Code generator, docs generator, interactive assistant, domain-specific
7. **Common Patterns**: Effective patterns, anti-patterns
8. **Troubleshooting**: Common issues, solutions
9. **Quick Reference**: Minimal valid prompt, field reference, tool selection guide

### Key Requirements to Enforce

- Description at TOP-LEVEL (not in prompt_metadata)
- Tools array complete and minimal
- Mode: agent (file ops) or chat (interactive)
- Naming: kebab-case, unique IDs
- YAML syntax valid

## Deliverable

Complete prompt that generates comprehensive prompt authoring instructions following all standards.




