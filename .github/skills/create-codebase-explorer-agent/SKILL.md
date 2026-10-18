---
name: create-codebase-explorer-agent
description: "Create or adapt a focused codebase-explorer agent with read-only tools, bounded investigation, and evidence-linked output. Use when adding an unfamiliar-codebase investigation profile to a repository, not when performing the investigation itself."

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
source: ".github/prompts/create-codebase-explorer.prompt.md"
revisions:
  - chat_id: "c16f927f-91c4-4a30-aada-8f74b099e547"
    model: "unknown/unknown@unknown"
    date: "2026-10-18"
    change: "Linked the canonical combined explorer/investigator and replaced the empty generator body with bounded adaptation and validation steps."
    ai_log: "ai-logs/2026/10/18/c16f927f-91c4-4a30-aada-8f74b099e547/conversation.md"
  - chat_id: "skill-naming-convention-20261018"
    model: "unknown/unknown@unknown"
    date: "2026-10-18"
    change: "Applied approved skill naming decisions and updated active references; preserved workflow behavior and historical provenance."
    ai_log: "ai-logs/2026/10/18/skill-naming-convention-20261018/conversation.md"
---
# Create Codebase Explorer Agent

Create or adapt an investigation profile, not a second agent for each exploration
style. For an investigation itself, use the existing
[Codebase Explorer](../../agents/codebase-explorer.agent.md).

## Procedure

1. Confirm the target repository and selected host. Read its applicable instructions
   and existing agents; reuse an existing explorer when it covers the request.
2. Start from the canonical profile linked above. Preserve its explicit question,
   boundary, stop condition, fact/inference/question ledger, and read-only behavior.
   Adapt only evidenced repository conventions, not inferred stack assumptions.
3. Place the requested profile in `.github/agents/` using supported YAML and a
   discovery-focused description. Use the minimum read/search tools supported by
   the host; do not add shell or edit access just to obtain history.
4. Make history availability explicit. If authorized read-only history tools are
   unavailable, require supplied evidence or report the limitation rather than
   promising Git, PR, or operational access.
5. Do not overwrite a local profile or modify another repository without explicit
   approval. Follow its provenance/logging policy and update its durable-artifact
   index. Keep source examples and historical provenance intact.

## Validation

- Parse YAML and verify name, description, tool aliases, location, and links.
- Check that ordinary onboarding yields a bounded map, a behavior request follows
  a relevant path, missing history is disclosed, and fix/delete/run requests do not
  trigger writes or execution.
- Check picker discovery separately from representative behavior when the target
  host is available. Report unavailable checks; static inspection is not proof of
  invocation or enforcement.
- Follow [custom-agent guidance](../../instructions/custom-agents.instructions.md)
  and [skill-authoring rules](../../instructions/agent-skills.instructions.md).
