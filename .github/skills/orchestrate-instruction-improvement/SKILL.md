---
name: orchestrate-instruction-improvement
description: "Coordinate bounded, evidence-based instruction validation and approved authoring updates using canonical skills."

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
revisions:
  - chat_id: "skill-naming-convention-20261018"
    model: "unknown/unknown@unknown"
    date: "2026-10-18"
    change: "Applied approved skill naming decisions and updated active references; preserved workflow behavior and historical provenance."
    ai_log: "ai-logs/2026/10/18/skill-naming-convention-20261018/conversation.md"
  - chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
    model: "unknown/unknown@unknown"
    date: "2026-10-18"
    change: "Replaced obsolete prompt regeneration and automatic branch/commit/PR stages with the current bounded instruction-validation and authoring workflows."
    ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
---
# Orchestrate Instruction Improvement

Coordinate review and approved improvement of a bounded set of repository instructions.
Use current repository evidence; never regenerate instructions from legacy prompts.

## Inputs

- Target instruction files or a clearly bounded instruction directory.
- The intended behavior or change, if an update is requested.
- Relevant requirements and repository constraints.

If the target scope or expected behavior is unclear, ask before proceeding.

## Workflow

1. **Bound and baseline.** Identify the target files, applicable policies, and directly
   related skills or references. Preserve unrelated changes and staged/unstaged state.
2. **Validate.** Follow [`validate-and-improve-instructions`](../validate-and-improve-instructions/SKILL.md)
   to verify current behavior and identify conflicts, stale paths, unsupported rules,
   duplication, and unclear scope. Use
   [`check-context-conflicts`](../check-context-conflicts/SKILL.md) for conflict analysis.
3. **Decide ownership.** Map each accepted finding to the instruction or skill that
   owns the rule. Do not edit legacy prompt files or use them to regenerate artifacts.
4. **Author only approved changes.** When instruction content needs creation or revision,
   follow [`create-instruction-file-authoring-instructions`](../create-instruction-file-authoring-instructions/SKILL.md).
   Prefer focused edits and links to canonical rules over duplicated guidance.
5. **Revalidate.** Check YAML/front matter where applicable, links, examples, scope,
   and consistency with directly related guidance. Repeat validation only when an
   approved change warrants it; stop after three iterations or when no material issue
   remains.
6. **Report.** Summarize scope, evidence, accepted changes, validation results,
   unresolved issues, and iteration count.

## Approval and Side-Effect Boundaries

- Analysis and proposed changes may be reported without modifying files.
- Edit only when the user explicitly requests implementation or approves the proposed
  changes. An explicit request to update named targets is approval for those targets.
- Do not create branches, stage, commit, push, create or update pull requests, or make
  external changes unless separately requested.
- Do not create replacement prompt files. Legacy prompts are migration inputs only;
  do not import or distribute spoke prompts.
- Follow the repository's AI provenance and logging policy for durable AI-assisted
  artifacts.

## Completion Checklist

- [ ] Scope and evidence sources are explicit.
- [ ] Findings map to the canonical owner of each rule.
- [ ] No instructions were generated from prompts.
- [ ] Edits, if any, were approved and narrowly scoped.
- [ ] Relevant links, metadata, examples, and cross-file consistency were validated.
- [ ] Remaining uncertainty and unaddressed findings are reported.



