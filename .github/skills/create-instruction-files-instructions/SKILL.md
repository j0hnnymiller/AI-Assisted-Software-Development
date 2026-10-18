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
revisions:
  - chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
    model: "unknown/unknown@unknown"
    date: "2026-10-17"
    change: "Added current-repository verification, required-versus-recommended distinction, overwrite approval, and example/link validation; removed unsupported fixed metadata and length requirements."
    ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
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

## YAML Front Matter Fields:

Document the provenance fields required by the current AI-assisted output policy. Describe additional fields, such as `applyTo`, only when they are supported and relevant to the target harness. Do not prescribe generic fields such as `name`, `version`, `author`, `tags`, `owner`, or review dates unless current repository policy or host documentation requires them.

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
- Include security requirements appropriate to the instruction's scope.
- Put controls that must apply across tasks in repository-level instructions; task-specific instructions should reference canonical security guidance rather than duplicate it.

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

- Complete, self-contained guide without an arbitrary line-count target
- Examples that match current repository and host-supported metadata
- Clear section navigation with table of contents
- Actionable checklists throughout
- Cross-references to canonical requirements
- Optimized for AI agent consumption

## Authoring Workflow

1. Inspect current repository instructions, examples, and the applicable provenance policy before setting requirements.
2. Use `.github/instructions/<topic>.instructions.md` for repository instruction guides. Verify front matter and host fields against current repository conventions and supported schemas.
3. Separate mandatory repository rules from recommendations. Include a practical template and realistic example, but do not invent fixed sections, governance fields, or length requirements without a demonstrated need.
4. Ask before overwriting an existing guide or creating a competing canonical guide.
5. Validate structure, YAML examples, links, and example consistency before finalizing.

## Boundaries

- Do not create or edit unrelated instruction files.
- Do not treat a guide-generation skill as permission to overwrite its target.
- Do not claim host behavior or metadata support without current evidence.




