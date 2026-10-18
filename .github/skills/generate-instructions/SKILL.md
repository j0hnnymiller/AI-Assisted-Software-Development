---
name: generate-instructions
description: "Analyze codebase and generate comprehensive instruction files following GitHub Copilot format"

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
source: ".github/prompts/generate-instructions.prompt.md"
revisions:
  - chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
    model: "unknown/unknown@unknown"
    date: "2026-10-17"
    change: "Added evidence-based Git workflow and C# instruction-generation guidance."
    ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
---
# Generate Project Instruction Files

Analyze codebase and generate comprehensive instruction files.

**IMPORTANT**: Only create NEW files. Never overwrite existing.

## Analysis Phase
1. **Project Structure/Technologies**: Languages, frameworks, libraries, architecture, DB, cloud (Azure/AWS/GCP), frontend (React/Vue/Angular), backend (.NET/Node/Python/Java)
2. **Existing Patterns**: Naming, organization, error handling, testing, docs
3. **Stack Assessment**: Versions, integrations, security, performance

## Instruction Files to Generate in `.github/instructions`:

### 1. README.md
```markdown
---
applyTo: "**"
---
# Development Instructions
Coding guidelines, templates, best practices
## AI Assistant Integration
## Project Overview
## Quick Reference
```

### 2. project-instructions.md
```markdown
---
applyTo: "**"
triggers: ["project structure", "architecture overview", "technology stack"]
---
# Project Structure and Architecture
- Project overview, detected details
- Technology Stack (authoritative versions: frontend, backend, build/test, cloud/DevOps)
- File structure with organization principles
- Architecture patterns: cross-tech integration, API communication, config management
- Data flow, auth/authz, error handling
```

### 3. Technology-Specific Files
Based on detected technologies, generate:
- `<language>-instructions.md` (e.g., csharp-instructions.md, python-instructions.md)
- `<framework>-instructions.md` (e.g., react-instructions.md, dotnet-instructions.md)

Each with:
- `applyTo: "**/*.{ext}"` pattern
- AI guidelines for style, naming, patterns
- Language/framework specific conventions
- Common patterns/anti-patterns
- Testing approach
- Documentation standards

### 4. Cross-Cutting Concerns
Generate if patterns detected:
- `error-handling-instructions.md`: Unified error handling strategy
- `logging-instructions.md`: Structured logging standards
- `testing-instructions.md`: Testing philosophy and conventions
- `security-instructions.md`: Security best practices
- `api-design-instructions.md`: API conventions
- `database-instructions.md`: DB access patterns
- `configuration-instructions.md`: Config management
- `ci-cd-instructions.md`: Build/deployment

## Instruction File Template
```markdown
---
applyTo: "<pattern>"
triggers: ["<keyword1>", "<keyword2>"]
---
# <Title> Instructions
## AI Assistant Guidelines
[3-5 key directives for AI]
## <Topic> Overview
[Context and purpose]
## Conventions
### Naming
### Organization
### Patterns
## Common Patterns
[Code examples with ✅/❌]
## Anti-Patterns
[What to avoid]
## Testing
[Testing approach]
## Examples
[Real examples from codebase]
```

## Generation Process
1. **Scan existing**: List `.github/instructions/*.md`, skip existing
2. **Analyze codebase**: Detect languages, frameworks, patterns (file counts, extensions, imports)
3. **Generate priority order**:
   - README.md (overview)
   - project-instructions.md (central reference)
   - Language-specific (most used languages first)
   - Framework-specific
   - Cross-cutting concerns (if patterns detected)
4. **Per file**:
   - Extract conventions from codebase examples
   - Document detected patterns
   - Provide concrete examples
   - Include AI-specific guidance
5. **Report**: List generated files with brief summary per file

When documenting Git workflows, inspect repository evidence such as branch conventions, commit history, contribution guidance, hooks, and CI policy. Distinguish current enforced rules from suggested conventions; do not invent branch names, approval requirements, merge strategies, or release procedures. Include safe examples only when supported by the repo.

For language-specific guidance such as C#, verify the target framework/SDK, compiler settings, analyzers, formatters, project conventions, and representative code. Explain which rules are repository requirements versus recommendations, and include focused validation commands only when confirmed.

For C# projects, consider documenting nullable-reference settings, async/cancellation patterns, dependency injection, exception/logging conventions, API and persistence boundaries, test conventions, analyzers/formatting, and target-framework compatibility when those topics apply. Treat them as evidence-gathering categories, not mandatory rules; derive each rule from repository configuration, approved standards, or verified platform documentation.

## Quality Standards
- Evidence-based (reference actual codebase patterns)
- Specific and actionable (not generic advice)
- Include code examples from codebase
- Follow GitHub Copilot instruction format
- Clear AI assistant directives
- Cross-reference related instruction files

## Output Format
List generated files with:
- Filename
- ApplyTo pattern
- Key conventions documented
- Example patterns included
- Integration points with other instructions



