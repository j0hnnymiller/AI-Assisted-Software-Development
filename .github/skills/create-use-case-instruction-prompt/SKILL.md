---
name: create-use-case-instruction-prompt
description: "Creates a comprehensive prompt that generates Markdown authoring guidelines for creating effective repository prompts"

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
source: ".github/prompts/create-use-case-instruction-prompt.prompt.md"
---
# Meta Prompt — Generate Prompt Authoring Instructions

This meta-prompt creates a comprehensive prompt for generating Markdown authoring guidelines that help users create effective, well-structured repository prompts.

## Context

This prompt generates instructions for creating prompts that follow repository standards, ensuring consistency, clarity, and effectiveness across all prompt files in the project.

## Output Requirements

- **Target File**: Create or overwrite `.github/copilot/Promptfiles/prompt-file.instructions.prompt.md`
- **Format**: Valid Markdown with proper YAML frontmatter
- **Standards Compliance**: Must conform to Repository Prompt File Standards
- **Completeness**: Include comprehensive guidance for all prompt authoring aspects

## Generated Prompt Specifications

The generated prompt must instruct users to create `.github/instructions/create-prompt.instructions.md` and include these sections:

### Required Metadata Configuration

The generated prompt must include these top-level YAML frontmatter fields:

- `mode: ` ('agent' if the generated prompt creates a file, otherwise 'chat')
- `model: ` ('Auto (copilot)' if unspecified)
- `tools: [<comma delimited list of tools]` (tools needed to execute the generated prompt)
- `description:` Describe what the generated prompt does

Additional prompt_metadata structure:

- `prompt_metadata.id: prompt-file.instructions-prompt`
- `output_path: .github/instructions/create-prompt.instructions.md`
- Title: "Generate Prompt Authoring Instructions (Markdown)"
- Appropriate version, tags, and category fields

### Content Structure Requirements

1. **Audience and Scope Definition**
   - Target audience (developers, prompt authors)
   - Skill level expectations

2. **Prompt File Structure Guide**
   - YAML frontmatter requirements with mandatory top-level fields (mode, model, tools, description)
   - Section organization standards
   - Metadata field specifications for both top-level and prompt_metadata sections

3. **Field-by-Field Documentation**
   - Required top-level fields: mode ('agent' for file-creating prompts), model ('Auto (copilot)' if unspecified), tools (array of required tools), description (moved from prompt_metadata)
   - Optional prompt_metadata fields (excluding description)
   - Field validation rules
   - Example values and formats

4. **Best Practices Guidelines**
   - Metadata structure: Top-level fields (mode, model, tools, description) + prompt_metadata section
   - Tool selection: Analyze prompt requirements to determine needed tools (create, edit, search, etc.)
   - Mode specification: 'agent' for file-creating prompts, 'chat' for interactive prompts
   - Clarity and specificity requirements
   - Context provision techniques
   - Output format specifications
   - Version control considerations

5. **Quality Assurance Elements**
   - Metadata validation checklist (mode, model, tools, description present at top level)
   - Tool array verification (matches prompt execution requirements)
   - Description placement verification (not in prompt_metadata)
   - Authoring checklist
   - File naming conventions (kebab-case)
   - Validation criteria
   - Testing recommendations

6. **Acceptance Criteria**
   - Completeness verification
   - Clarity assessment
   - Markdown rendering validation
   - Standards compliance check

### Technical Requirements

- **Output Directive**: Include explicit instruction to output only final Markdown content
- **Self-Contained**: Instructions must be complete and standalone
- **Preview Compatible**: Must render correctly in Markdown preview
- **Actionable**: Provide specific, implementable guidance

## Quality Standards

The generated prompt must ensure the instruction file will:

- Be immediately usable by prompt authors
- Maintain consistency across the repository
- Follow established documentation patterns
- Enable efficient prompt creation workflows

## Deliverable

Output only the complete `.github/copilot/Promptfiles/prompt-file.instructions.prompt.md` file content as Markdown. No additional commentary, explanations, or wrapper text.





