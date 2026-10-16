---
name: meta-ai-validate-and-improve-instructions
description: "Orchestrate iterative validation and improvement of instruction files through automated cycles"

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
source: ".github/prompts/meta/ai/validate-and-improve-instructions.prompt.md"
---
# Validate and Improve Instruction Files

Automate quality improvement workflow for instruction files through iterative generation, validation, refinement.

## Context

Ensure quality/consistency through automated workflow:

1. Generate all instruction files from source prompts
2. Analyze for conflicts, inconsistencies, redundancy
3. Fix root causes in source prompts (not generated files)
4. Validate improvements via re-generation
5. Iterate until resolved or max attempts (3)

Must comply with `.github/instructions/ai-assisted-output.instructions.md` and `copilot-instructions.md`.

## Workflow Steps

### Phase 1: Branch Creation

```bash
git checkout -b feature/validate-improve-instructions-$(date +%Y%m%d-%H%M%S)
```

Record initial state (file count, baseline), initialize iteration counter (max: 3)

### Phase 2: Generation Cycle

Execute prompts in sequence:

1. `.github/copilot/Promptfiles/create-ai-assisted-output-instructions.prompt.md` → `ai-assisted-output.instructions.md`
2. `.github/copilot/Promptfiles/meta/create-instruction-file-instructions.prompt.md` → `instruction-standards.instruction.md`
3. `.github/copilot/Promptfiles/prompt-file.instructions.prompt.md` → `create-prompt.instructions.md`
4. `.github/copilot/Promptfiles/create-use-case-instructions.prompt.md` → `create-use-case.instructions.md`

Wait for completion, verify each created successfully.

### Phase 3: Validation & Analysis

Submit `.github/copilot/Promptfiles/check-context.prompt.md` targeting `.github/instructions/`
Analyze output for:

- Conflicting instructions
- Factual inconsistencies
- Logical contradictions
- Scope/priority conflicts
- Duplication/redundancy
- Communication gaps

### Phase 4: Root Cause Analysis

If issues found:

- Categorize by severity (Critical/High/Medium/Low)
- Trace to source prompts
- Document specific conflicts
- Propose prompt fixes (NOT instruction fixes)

### Phase 5: Iterative Improvement

For each issue:

1. Edit source prompt to address root cause
2. Re-run affected prompts
3. Re-validate
4. Track improvements
5. Repeat if needed (max 3 iterations)

### Phase 6: Finalization

- Commit all changes with detailed message
- Create/update PR with validation summary
- Document remaining issues (if any)
- Tag for review

## Output Format

Report per iteration:

- Issues found (count by severity)
- Prompts modified
- Files re-generated
- Improvements validated
- Remaining issues

Final report:

- Initial vs final state
- All modifications made
- Validation results
- Recommendations for remaining issues

## Constraints

- Max 3 iterations
- Fix prompts, not generated files
- Preserve functionality while improving quality
- Document all changes





