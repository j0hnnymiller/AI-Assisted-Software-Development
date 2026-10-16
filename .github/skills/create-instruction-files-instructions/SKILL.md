---
name: create-instruction-files-instructions
description: "Generate comprehensive guide for creating instruction files"

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
source: ".github/prompts/create-instruction-files-instructions.prompt.md"
---
# Generate Instruction-File Creation Guide

Create comprehensive Markdown guide for creating new `.instructions.md` files in the repository.

## Output

File: `.github/instructions/instruction-files.instructions.md`
Complete, self-contained guide optimized for both AI assistants and to minimize token consumption

## Complete Structure Required:

1. **Title**: "Creating New Instruction Files"
2. **Overview**: Purpose, target audience, related documentation
3. **Table of Contents**: Full navigation structure
4. **When to Create Instruction Files**: Use cases, examples of good instruction files
5. **File Structure Requirements**:
   - Location and naming: `.github/instructions/`
   - Required YAML front matter: Complete AI provenance + Copilot metadata + governance fields
   - Required content structure: Template with all standard sections
6. **Content Guidelines**:
   - Writing principles: Imperative language, examples, structure
   - Content organization: Standard sections breakdown
   - Target audience: AI agents (primary), token optimization strategies
7. **Creation Process**:
   - Using meta-prompt
8. **Quality Standards**:
   - Content quality checklist
   - Technical quality checklist
   - Process quality checklist
9. **Common Patterns**:
   - Process instructions pattern
   - Standard templates pattern
   - Validation rules pattern
10. **AI-Specific Considerations**:
    - Critical safety rule ("When uncertain, ask")
    - Rules format for AI consumption
    - Validation checklists
    - Token optimization techniques
11. **Known Limitations and Constraints**: Document constraints affecting instruction effectiveness
12. **Security and Compliance (NON-NEGOTIABLE)**: Mandatory security rules for code generation
13. **Integration Requirements**:
    - README updates (reference canonical post-creation requirements)
    - Related file updates
    - Prompt file creation
14. **Validation Checklist**:
    - Process validation
    - Content validation
    - Technical validation
    - Compliance validation
15. **Common Mistakes to Avoid**:
    - Content mistakes (vague requirements, missing examples)
    - Technical mistakes (incomplete metadata, wrong location)
    - Process mistakes (no documentation, reused chat logs)
16. **Examples**:
    - Example 1: Code Review Instructions (complete with metadata)
    - Example 2: API Documentation Instructions (complete with metadata)
17. **Maintenance and Updates**:
    - When to update
    - Update process
    - Version control
18. **File Length Management**: Guidelines for when files exceed 300-500 line limit
19. **Summary**: Key requirements checklist
20. **Document Footer**: Version, last updated, maintainer, related instructions

## Required YAML Front Matter Fields:

Document these required metadata fields:
- AI Provenance: `ai_generated`, `model`, `operator`, `chat_id`, `prompt`, `started`, `ended`, `task_durations`, `total_duration`, `ai_log`, `source`
- Copilot Metadata: `name`, `description`, `appliesTo`, `version`, `author`, `tags`
- Governance: `owner`, `reviewedDate`, `nextReview`

## Content Guidelines to Document:

### Writing Principles:
- Use imperative, declarative language (ALWAYS/NEVER/MUST)
- Provide concrete examples
- Avoid tentative language ("please try", "consider")
- Structure: Overview → Rules → Examples → Quality checklist

### AI Optimization:
- Token efficiency: imperative commands, structured formats, minimal prose
- Keep files under 300-500 lines
- Use YAML/JSON schemas over verbose examples
- Target audience: AI agents

### Security:
- All instruction files involving code generation MUST include NON-NEGOTIABLE security rules
- Security rules go in repo-level guardrails, NOT optional promptfiles

## Creation Methods to Document:

1. **Meta-Prompt Method**: Use `.github/skills/create-instruction-files-prompt-file/SKILL.md`

## Common Patterns to Include:

### Pattern 1: Process Instructions
```markdown
## Process Overview
1. **Step 1**: [Action]
   - Requirement A
   - Requirement B
```

### Pattern 2: Standard Templates
Include complete template skeleton with all required sections

### Pattern 3: Validation Rules
```markdown
### Rule 1: [Category]
- **Requirement**: Specific requirement
- **Validation**: How to check
- **Examples**: ✅ Good / ❌ Bad
```

## Examples to Include:

### Example 1: Code Review Instructions
- Complete YAML front matter
- Review criteria (functional, code quality, testing)
- Review process steps
- Security requirements (NON-NEGOTIABLE)

### Example 2: API Documentation Instructions
- Complete YAML front matter
- Required fields for each endpoint
- Example format with code blocks
- Security requirements (NON-NEGOTIABLE)

## Quality Checklist Items:

### Content Quality:
- Clear purpose, actionable guidance, complete coverage
- Consistent structure, concrete examples, quality criteria

### Technical Quality:
- Complete metadata (all 11 AI provenance fields)
- Correct format, valid links, proper location

### Process Quality:
- Conversation log created and linked
- Summary created, README updated
- Git integration with semantic commit

## Common Mistakes Section:

Document these anti-patterns:
- ❌ Vague requirements vs ✅ Specific requirements
- ❌ Missing examples vs ✅ Concrete examples
- ❌ Incomplete metadata vs ✅ Complete metadata
- ❌ Wrong location vs ✅ Correct location
- ❌ Interface as model (`"github/copilot"`) vs ✅ Actual model
- ❌ No documentation vs ✅ Complete post-creation requirements
- ❌ Reused chat logs vs ✅ Unique chat logs

## References:

Link to related documentation:
- `.github/instructions/ai-assisted-output.instructions.md` (canonical post-creation requirements)
- `.github/instructions/copilot-instructions.md`
- `.github/instructions/instruction-prompt-files.instructions.md`

## Output Requirements:

- Comprehensive guide (600-700 lines)
- Complete working examples with full metadata
- Clear section navigation with table of contents
- Actionable checklists throughout
- Cross-references to canonical requirements
- Optimized for AI agent consumption





