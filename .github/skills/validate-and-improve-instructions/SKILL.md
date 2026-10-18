---
name: validate-and-improve-instructions
description: "Validate a bounded set of repository instructions and related skills for conflicts, stale guidance, and unsupported claims; propose and apply approved improvements with evidence and a capped review cycle."

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
source: ".github/prompts/validate-and-improve-instructions.prompt.md"
revisions:
  - chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
    model: "unknown/unknown@unknown"
    date: "2026-10-17"
    change: "Replaced retired prompt-generation cycles with evidence-based instruction and skill validation, approval gates, and bounded iteration.; Added bounded legacy prompt-to-skill migration and validation procedure.; Clarified spoke prompts remain untouched unless separately authorized and are not imported or distributed."
    ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
---
# Validate and Improve Instructions

Review a defined set of repository instruction files and related skills for conflicts, unsupported requirements, stale paths, and unclear scope. Use current repository evidence and applicable policy; legacy prompt files are migration inputs only, never generation sources.

## Procedure

1. **Bound the scope.** Confirm the target files or directories. Inspect applicable policies and directly related skills, agents, and references only.
2. **Establish current behavior.** Verify file paths, scripts, schemas, host features, and referenced workflows against the repository or authoritative documentation. Mark unverified claims as unknown; do not infer current behavior from legacy prompts.
3. **Find issues.** Identify conflicts, inaccuracies, duplication, stale paths, missing constraints, and unsupported mandatory rules. Record evidence and impact for each finding.
4. **Propose a focused change set.** Map each finding to its canonical owning instruction or skill. Prefer fixing the source rule and any tightly coupled references; avoid broad rewrites.
5. **Get approval before edits** unless the user has already explicitly authorized implementation. Preserve unrelated user changes and staged/unstaged distinctions.
6. **Validate each approved iteration.** Check front matter, links, examples, and consistency with affected files. Re-run the scoped conflict review after edits; stop after three iterations or when no material issues remain.
7. **Report results.** Summarize files reviewed, findings, changes, validation evidence, unresolved questions, assumptions, and iteration count.

## Legacy Prompt Migration

When the scope includes `.github/prompts/**`, treat each file as a migration input, not a source for regenerating prompts:

1. Compare its purpose, inputs, procedure, outputs, and constraints with canonical skills.
2. Map it to an existing skill to update, a new skill candidate, or a repo-specific/obsolete disposition.
3. Leave the source prompt in its owning repository unchanged unless a change to that repository is separately approved. Do not import or distribute spoke prompts. For retained hub prompt records, keep them marked/indexed as deprecated and preserve the sync manifest's no-distribution rule.
4. Obtain approval before changing skills or indexes. Never copy the prompt into an active workflow or create a replacement prompt file.
5. Validate skill coverage, migration links, provenance, and inventory/sync behavior after approved changes.

## Boundaries

- Do not generate or re-generate instruction files from prompts.
- Do not make edits, create branches, stage, commit, push, or create/update pull requests without explicit user authorization.
- Do not alter unrelated files or claim validation that was not performed.
- For conflict analysis, reuse [`check-context-conflicts`](../check-context-conflicts/SKILL.md).
- Follow [`ai-assisted-output.instructions.md`](../../instructions/ai-assisted-output.instructions.md) for provenance and logging requirements.

