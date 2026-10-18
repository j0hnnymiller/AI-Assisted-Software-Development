---
ai_generated: true
model: "unknown/unknown@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "c16f927f-91c4-4a30-aada-8f74b099e547"
prompt: |
  go ahead
started: "2026-10-18T20:32:37.5132862Z"
ended: "2026-10-18T20:36:28.2314286Z"
task_durations:
  - task: "Approved guidance adaptation"
    duration: "00:03:50"
total_duration: "00:03:50"
ai_log: "ai-logs/2026/10/18/c16f927f-91c4-4a30-aada-8f74b099e547/conversation.md"
source: "Approved remaining-config review; adapted Course agent-skills.instructions.md and verified Agent Skills specification"
name: agent-skills
description: "Use when creating, reviewing, or updating Agent Skills and SKILL.md entry points; covers names, discovery descriptions, resources, permissions, and validation."
applyTo: ".github/skills/**/SKILL.md"
version: "1.0.0"
author: "johnmillerATcodemag-com"
tags: ["skills", "authoring", "validation"]
owner: "johnmillerATcodemag-com"
reviewedDate: "2026-10-18"
nextReview: "2027-01-18"
---

# Agent Skill Authoring

## Overview

Apply these rules when authoring repository skills. For domain-specific implementation
workflows, also use [create-implementation-skills](../skills/create-implementation-skills/SKILL.md).
Reuse an existing skill when its inputs, behavior, and outputs already cover the task.
Keep one-off requests out of the skill catalog.

## Table of Contents

- [Format and discovery](#format-and-discovery)
- [Procedure and resources](#procedure-and-resources)
- [Validation checklist](#validation-checklist)
- [Summary](#summary)

## Format and discovery

- Store each skill in `.github/skills/<skill-name>/SKILL.md`.
- Require YAML `name` and `description`. Use a name of 1-64 lowercase ASCII
  letters, digits, or hyphens; match the folder name, with no leading, trailing,
  or consecutive hyphens.
- Keep `description` non-empty and at most 1024 characters. State both the
  capability and concrete use cases. Do not rely on body text or an invented
  `keywords` property for discovery.
- Verify optional properties against the selected harness and current specification.
  Do not invent tool names, model identifiers, or compatibility guarantees.
- Follow [provenance policy](ai-assisted-output.instructions.md). Distinguish
  repository provenance from host configuration; do not claim every harness accepts
  all repository metadata or rewrite historical model identity to select a model.

```yaml
---
name: review-test-gaps
description: "Identify untested behavior and prioritize regression cases. Use when assessing test coverage before a migration or release."
---
```

`description: "Helps with code"` is too vague: it names neither a bounded capability
nor a useful trigger.

## Procedure and resources

- State required inputs, scope, prerequisites, ordered steps, outputs, validation,
  and stop/clarification conditions. Identify write effects and required approval.
- Reference bundled scripts, examples, and assets using relative Markdown links
  from the entry point; load resources only when needed. Do not copy shared logic
  into multiple skills merely to make each directory self-contained.
- Inspect adopted instructions and scripts before execution. A linked script is
  not trusted or authorized merely because it is bundled with a skill.
- Use platform-enforced permissions and approval controls. Prose and experimental
  tool-list metadata do not create a security boundary.
- Preserve existing behavior outside the approved change. Use bounded checks;
  report missing dependencies or unsupported capabilities instead of claiming success.

## Validation checklist

- [ ] YAML parses; `name` matches its folder and the naming limits.
- [ ] Description states the capability and concrete use cases within 1024 characters.
- [ ] Inputs, outputs, failure conditions, and write/approval boundaries are explicit.
- [ ] Referenced local resources exist; script interfaces match the documented commands.
- [ ] Provenance, logs, and README entries follow repository policy.
- [ ] Check discovery and direct invocation in the selected harness when available.
- [ ] Test representative in-scope and out-of-scope requests separately from discovery;
      finding a skill does not prove it was invoked or behaved correctly.
- [ ] Report unavailable host checks rather than treating YAML parsing as behavioral validation.

## Summary

Keep skills discoverable, bounded, and resource-linked. Validate format and behavior
separately; do not duplicate existing workflow ownership.

References: [Agent Skills specification](https://agentskills.io/specification);
[VS Code skills](https://code.visualstudio.com/docs/agent-customization/agent-skills).

---

**Document Version**: 1.0.0  
**Last Updated**: 2026-10-18  
**Maintainer**: johnmillerATcodemag-com  
**Related Instructions**: [Provenance](ai-assisted-output.instructions.md),
[instruction authoring](instruction-files.instructions.md)
