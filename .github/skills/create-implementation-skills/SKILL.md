---
name: create-implementation-skills
description: "Create or update focused implementation skills from validated requirements and repository evidence. Use when defining reusable, domain-specific coding workflows, including Academia System components."
argument-hint: "[system, component, or requirements source]"
ai_generated: true
model: "unknown/unknown@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "create-implementation-skills-20261018"
prompt: |
  convert this prompt file that creates implementation prompt files into a skill that creates implementation skills
started: "2026-10-18T08:39:16.635-07:00"
ended: "2026-10-18T08:43:12.603474-07:00"
task_durations:
  - task: "Implementation skill workflow design"
    duration: "00:03:56"
total_duration: "00:03:56"
ai_log: "ai-logs/2026/10/18/create-implementation-skills-20261018/conversation.md"
source: "user request"
revisions:
  - chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
    model: "unknown/unknown@unknown"
    date: "2026-10-18"
    change: "Removed a link to the deleted prompt migration index and clarified that legacy prompts are migration inputs, not implementation guidance."
    ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
---

# Create Implementation Skills

Create reusable workspace skills that guide implementation of a specific system component or cohesive feature. This skill authors implementation workflows; it does not implement the component itself.

## When to Use

- A system, domain, or feature needs a reusable implementation workflow.
- An existing implementation skill is missing verified requirements or needs a focused update.
- Academia System implementation work needs a component skill; use the current Academia skills and authoritative system requirements to establish component boundaries. Treat any legacy prompt as migration input, not active implementation guidance.

## Procedure

1. **Resolve the scope.** Identify the system, component, intended implementers, authoritative requirements, expected behavior, and desired skill path. If the component boundary or governing requirements are unclear, ask before drafting.
2. **Ground the workflow in evidence.** Read the relevant requirements, business rules, architecture, existing code and tests, applicable repository instructions, and neighboring skills. Separate verified facts from assumptions and open decisions.
3. **Check for existing coverage.** Search `.github/skills/` by purpose, workflow, inputs, outputs, and constraints, not just by name. Extend the canonical skill when appropriate; do not create a duplicate. For Academia System components, preserve the domain boundaries of the existing skills and verify scope against authoritative requirements; do not rely on deprecated prompt files as implementation specifications.
4. **Define a bounded skill.** Use one skill per cohesive implementation capability. Identify prerequisites and dependencies from evidence, and order multiple requested skills by those dependencies. Do not invent a fixed implementation sequence when the system requirements do not establish one.
5. **Write the skill** at `.github/skills/<kebab-case-name>/SKILL.md`. The folder name must match the frontmatter `name`. Include:
   - A discovery-focused `description` stating the capability and trigger phrases.
   - Scope and applicable prerequisites.
   - An implementation procedure with actionable, repository-grounded work and measurable acceptance criteria.
   - Focused verification for the component and integration/regression checks for affected existing workflows.
   - Relevant compatibility, migration/data integrity, security, performance, scalability, and documentation requirements, based on the component's actual risks.
   - Boundaries that prevent unrelated scope expansion and require unresolved business or architectural decisions to be surfaced.
6. **Apply repository policy.** Embed complete AI provenance in the skill's YAML frontmatter, following [AI-assisted output instructions](../../instructions/ai-assisted-output.instructions.md). Use real, consistent timestamps and durations; do not invent unavailable model details. Create or update `conversation.md` and `summary.md` under the referenced `ai-logs/yyyy/mm/dd/<chat-id>/` path. Never use a Markdown sidecar for metadata.
7. **Integrate and validate.** Update the relevant README or skill index for durable skills. Check YAML syntax, skill-name/folder agreement, link targets, referenced instructions, and whether each acceptance check is testable. Confirm that no existing workflow is contradicted or duplicated.
8. **Report the result.** List created or updated skills, their scope and dependency order, evidence used, index changes, validation performed, and unresolved questions. Do not claim tests or checks passed unless they were run.

## Quality Checks

- Each skill covers one coherent implementation capability and is grounded in authoritative requirements and repository patterns.
- Tasks have observable outcomes; verification is appropriate to the change and does not impose unsupported coverage thresholds.
- Existing behavior and API/data compatibility are preserved unless the requirements explicitly authorize a change.
- Security and privacy controls are included where relevant; do not expose credentials or sensitive data in skills or logs.
- Links resolve, provenance is complete, and all artifacts from the work trace to the same chat log.

## Boundaries

- Do not generate implementation prompt files. Reusable implementation workflows belong in skills.
- Do not create a skill merely to restate a requirement, nor create duplicates of existing skills.
- Do not silently decide unresolved product, domain, security, or architecture questions.
- Do not overwrite an existing skill unless the user requested an update or approves the proposed changes.
- Do not implement the system component as part of authoring its skill unless separately requested.
