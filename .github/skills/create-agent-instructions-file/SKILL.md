---
name: create-agent-instructions-file
description: "Generate comprehensive authoring guidelines for custom GitHub Copilot agents"

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
source: ".github/prompts/create-agent-instructions-file.prompt.md"
---
# Generate Custom Agent Instructions

Create comprehensive guidelines for authoring custom GitHub Copilot agents.

## Context

Instructions for creating specialized AI assistants with specific expertise, personality, and commands.
Must comply with `.github/instructions/ai-assisted-output.instructions.md` and `copilot-instructions.md`.

## Output: `.github/instructions/agent-file.instructions.md`

### Structure:

1. **Overview**: Purpose, benefits, when to create vs use default, integration
2. **File Structure**:
   - Naming: `<agent-name>.agent.md` (kebab-case) in `.github/agents/`
   - Header: Name, Focus, Temperature (0.0-1.0), Style
   - Sections: Mission, Core Expertise, Methodology, Commands, Response Format, Principles, Examples
3. **Header Fields**:
   - **Name**: Display name, Title Case, 2-4 words
   - **Focus**: Primary domain, specific capabilities
   - **Temperature**: 0.3 (security/compliance), 0.4-0.5 (docs/analysis), 0.6-0.7 (brainstorming)
   - **Style**: 2-4 descriptive adjectives (tone, approach, focus)
4. **Content Structure**:
   - Mission: 1-2 sentences, role + value + approach
   - Core Expertise: 5-10 specific areas (bold + description)
   - Methodology: Multi-phase workflow (if applicable)
   - Commands: `@kebab-case` format, clear descriptions
   - Response Format: Structured output template
   - Principles: Behavioral guidelines
   - Examples: Realistic usage demonstrations
5. **Best Practices**: Clarity, consistency, scope definition, intuitive commands
6. **Quality Assurance**: Validation checklist, testing, review process
7. **Examples**: Simple template, advanced template, domain-specific (security, docs, code exploration, architecture)
8. **Common Patterns**: Command-driven interaction, phased methodology, clear response format
9. **Anti-Patterns**: Overly broad scope, unclear commands, missing examples, vague mission
10. **Integration**: Activation (`@modename`), switching, combining with Copilot features
11. **Maintenance**: Versioning, feedback loop, iteration, deprecation

### Templates to Include:

- Security analyzer pattern
- Documentation assistant pattern
- Code exploration pattern
- Architecture review pattern

### Quality Checklist:

- kebab-case filename with `.agent.md`
- All header fields present
- Mission clear, expertise listed (5-10)
- Commands use `@kebab-case`
- Temperature appropriate
- Style aligns with domain

## Deliverable

Complete file with YAML front matter per ai-assisted-output policy, all sections, templates, checklists, examples.





