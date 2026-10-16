---
name: create-use-case-instructions-file-prompt-file
description: "Create prompt that generates use case authoring guidelines"

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
source: ".github/prompts/create-use-case-instructions-file-prompt-file.prompt.md"
---
# Meta Prompt — Generate Use Case Authoring Instructions

Create prompt that generates use case authoring guidelines.

## Output Target

`.github/prompts/create-use-case-instructions.prompt.md` → creates → `.github/instructions/create-use-case.instructions.md`

## Generated Prompt Specs:

### Required Metadata

- `mode: agent`, `model: Auto (copilot)`, `tools: ["edit", "create"]`
- `description`: Generate use case authoring guide
- `prompt_metadata`: id, output_path, title, category, tags

### Content Structure

Generated instructions must include:

1. **Audience & Scope**: Contributors authoring use cases, standard format + Mermaid diagrams
2. **Standard Template** (copy-paste ready):

```markdown
# Use Case: <Title>

- Primary Actor: <Role>
- Goal: <One sentence>
- Preconditions: 1. <Condition>
- Triggers: <Event>

## Main Success Scenario

## Alternate/Exception Flows

## Postconditions

## Business Rules

## Non-Functional Notes

## Diagram

\`\`\`mermaid
flowchart TD
\`\`\`
```

3. **Field-by-field Guidance**: Purpose and examples for each template field
4. **Mermaid Diagram Guidance**: Flowchart vs sequence, when to use each, syntax
5. **Example Use Case**: Concise but realistic
6. **Authoring Checklist**: Validation criteria
7. **Naming/File Conventions**: `use-case-<kebab-case>.md` in appropriate folder
8. **Tips & Pitfalls**: Common mistakes, best practices

### Quality Standards

- Template is copy-paste ready
- Examples are realistic
- Mermaid diagrams are clear
- All standard sections explained

## Deliverable

Complete prompt that generates comprehensive use case authoring instructions.





