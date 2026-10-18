---
name: create-instruction-file-authoring-instructions
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
    change: "Added current-repository verification, required-versus-recommended distinction, overwrite approval, and example/link validation; removed unsupported fixed metadata and length requirements.; Added AI-assisted development, Git workflow, vertical-slice, and language-specific guide structures."
    ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
  - chat_id: "skill-naming-convention-20261018"
    model: "unknown/unknown@unknown"
    date: "2026-10-18"
    change: "Applied approved skill naming decisions and updated active references; preserved workflow behavior and historical provenance."
    ai_log: "ai-logs/2026/10/18/skill-naming-convention-20261018/conversation.md"
---
# Generate Instruction-File Creation Guide

Create comprehensive Markdown guidance for creating or revising `.instructions.md` files in the repository.

## Output

File: `.github/instructions/instruction-files.instructions.md`
Follow the canonical guide and current AI provenance policy. Do not prescribe unsupported host metadata or legacy prompt workflows.

## Recommended Guide Structure

Tailor the guide to the task. Cover relevant items from this list rather than requiring every section:

1. Purpose, audience, scope, and when to create an instruction file
2. Supported location, naming, and host-specific front matter
3. Content organization, actionable rules, and examples
4. Authoring, review, and update workflow
5. Security, privacy, or compliance requirements relevant to the domain
6. Validation checklist, references, and maintenance

## YAML Front Matter Fields

Document the provenance fields required by the current AI-assisted output policy. Describe additional fields, such as `applyTo`, only when they are supported and relevant to the target harness. Do not prescribe generic fields such as `name`, `version`, `author`, `tags`, `owner`, or review dates unless current repository policy or host documentation requires them.

## Content Guidelines to Document

### Writing Principles
- Use clear, actionable language; reserve MUST/NEVER for actual requirements
- Provide concrete examples
- Structure: Overview → Rules → Examples → Quality checklist

### AI Optimization
- Keep instructions focused and use structured formats when they improve clarity
- If a guide grows substantially, consider splitting only when scopes and workflows remain distinct
- Use YAML/JSON schemas over verbose examples
- Target audience: AI agents

### Security
- Include security requirements appropriate to the instruction's scope.
- Put controls that must apply across tasks in repository-level instructions; task-specific instructions should reference canonical security guidance rather than duplicate it.

## Authoring Workflow

1. Review the canonical [instruction-file guide](../../instructions/instruction-files.instructions.md), related guidance, and existing skills.
2. Verify required fields and supported front matter against repository policy and the selected host.
3. Draft or revise only the necessary scope; prefer linking to canonical rules over duplicating them.
4. Validate YAML, links, examples, applicability, and consistency with existing instructions.
5. Update indexes and related files when needed. Follow repository provenance requirements for the resulting artifact.

Do not create prompt generators. For migration of an existing prompt, compare its purpose, inputs, workflow, and outputs with skills; use the [retired prompt-authoring workflow](../create-instruction-files-prompt-file/SKILL.md) when needed.

## Common Patterns to Include

### Pattern 1: Process Instructions
```markdown
## Process Overview
1. **Step 1**: [Action]
   - Requirement A
   - Requirement B
```

### Pattern 2: Standard Templates
Include a complete template skeleton only when the workflow needs reusable structure; identify required fields from current policy.

### Pattern 3: Validation Rules
```markdown
### Rule 1: [Category]
- **Requirement**: Specific requirement
- **Validation**: How to check
- **Examples**: ✅ Good / ❌ Bad
```

## Examples to Include

Include a concise example only when it demonstrates a pattern that prose cannot explain clearly.

## Quality Checklist Items

### Content Quality
- Clear purpose, actionable guidance, complete coverage
- Consistent structure, concrete examples, quality criteria

### Technical Quality
- Complete metadata (all 11 AI provenance fields)
- Correct format, valid links, proper location

### Process Quality
- Provenance and logging follow repository policy
- README or index updated for durable guidance where required
- Commit changes only when requested or part of the approved workflow

## Common Mistakes Section:

Document these anti-patterns:
- ❌ Vague requirements vs ✅ Specific requirements
- ❌ Missing examples vs ✅ Concrete examples
- ❌ Incomplete metadata vs ✅ Complete metadata
- ❌ Wrong location vs ✅ Correct location
- ❌ Unsupported host metadata vs ✅ Verified host-supported fields
- ❌ No documentation vs ✅ Relevant post-creation requirements
- ❌ Reused chat logs vs ✅ Unique chat logs

## References:

Link to related documentation:
- `.github/instructions/ai-assisted-output.instructions.md` (canonical post-creation requirements)
- `.github/instructions/copilot-instructions.md`

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

## Cross-Cutting Development Workflow Guides

When a guide covers AI-assisted development, Git practices, vertical slices, or a language such as C#:

- Derive requirements from the repository's actual workflow, tools, configuration, and representative code; identify unsupported details as questions.
- Separate required controls from recommendations and optional examples.
- For AI-assisted development, cover lifecycle stages, human review, privacy, verification, and provenance without asserting unapproved organizational policy.
- A work instruction for AI-assisted development should make purpose/scope, roles, permitted tasks and data, human decision gates, stage-by-stage workflow, verification/release controls, exception escalation, provenance/logging, and review ownership explicit. Tailor gates to the organization's approved policies.
- For Git workflow guidance, distinguish observed branch/commit/review practice from proposed conventions; never invent required branch names or approval gates.
- A Git workflow guide can cover branch creation/naming, keeping work isolated, commit scope/messages, pull-request review, required checks, merge/release practices, conflict recovery, and safe rollback. Include only practices evidenced in the repository or explicitly approved by maintainers.
- For vertical-slice guidance, explain feature boundaries, end-to-end behavior, cross-cutting dependencies, and test evidence without prescribing an unsupported architecture.
- For language-specific instructions, verify versions and analyzers and keep examples compatible with the repository's target framework.
- Include a focused validation checklist and identify the source evidence used.

## Boundaries

- Do not create or edit unrelated instruction files.
- Do not treat a guide-generation skill as permission to overwrite its target.
- Do not claim host behavior or metadata support without current evidence.
