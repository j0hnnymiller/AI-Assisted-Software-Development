---
name: create-use-case-instructions
description: "Generate Markdown authoring guide for creating use cases with standard structure and Mermaid diagrams"

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
source: ".github/prompts/create-use-case-instructions.prompt.md"
---
# Generate Use Case Authoring Instructions

Create instruction file at `.github/instructions/create-use-case.instructions.md` teaching how to author use cases with standard format and Mermaid diagrams.

## Output
Single Markdown file, self-contained, renders correctly in preview.

## Structure
1. Title: "Use Case Authoring Instructions"
2. Introduction
3. Standard Template (copy-paste ready)
4. Field-by-field Guidance
5. Mermaid Diagram Guidance
6. Example Use Case (concise, realistic)
7. Authoring Checklist
8. Naming/File Conventions
9. Tips and Pitfalls

## Template (include verbatim)
```
# Use Case: <Title>
- Primary Actor: <Role>
- Supporting Actors: <Roles>
- Goal: <One sentence>
- Scope: <System>
- Level: <User-goal | Subfunction | Summary>
- Preconditions: 1. <Condition>
- Triggers: <Event>

## Main Success Scenario
1. <Actor> <action>.
2. <System> <response>.

## Alternate/Exception Flows
A1. <Condition>: 1. <Step>

## Postconditions
- Success Guarantees: <What's true>
- Minimal Guarantees: <What remains>

## Business Rules
- <Rule>

## Non-Functional Notes
- <Notes>

## Diagram
\`\`\`mermaid
flowchart TD
\`\`\`
```





