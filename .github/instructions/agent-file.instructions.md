---
ai_generated: true
model: "anthropic/claude-3.5-sonnet@2024-10-22"
operator: "johnmillerATcodemag-com"
chat_id: "optimize-instructions-20251023"
prompt: |
  Create AI-optimized version of agent-file.instructions.md with minimal tokens
started: "2025-10-23T04:40:00Z"
ended: "2025-10-23T04:40:00Z"
task_durations:
  - task: "optimization"
    duration: "00:01:00"
total_duration: "00:01:00"
ai_log: "ai-logs/2025/10/23/optimize-instructions-20251023/conversation.md"
source: "optimization-task"
revisions:
  - chat_id: "reconcile-diverged-files-20261016"
    model: "OpenAI/GHT-6@Luna"
    date: "2026-10-16"
    change: "Replaced obsolete header-based guidance with current YAML front matter and scoped tool guidance."
    ai_log: "ai-logs/2026/10/16/reconcile-diverged-files-20261016/conversation.md"
applyTo: "**/*.agent.md"
---

# VS Code Custom Agent Authoring

Create focused custom agents as `.agent.md` files. Use the selected harness's supported locations and current front matter schema; see [Custom agents in VS Code](https://code.visualstudio.com/docs/agent-customization/custom-agents) for authoritative, harness-specific details.

## Location and Naming

- Use a descriptive kebab-case filename ending in `.agent.md`.
- Put repository/workspace agents in `.github/agents/`.
- Do not assume workspace, user-level, organization, and enterprise agents share the same locations or capabilities.

## YAML Front Matter

Use YAML front matter for supported agent configuration. `description` is required by the repository's agent format; `name` and `tools` are common fields. Verify any additional properties against the selected harness's current schema.

```yaml
---
name: security-reviewer
description: Review code for security issues and report evidence-based findings.
tools: ["search", "read"]
---
```

- Omit `name` when the filename is a suitable display name.
- Set the minimum `tools` needed. Omission may grant broader tool access, depending on the harness.
- Use `model`, `target`, MCP server configuration, and other optional fields only where the selected harness documents them.
- Do not use legacy Markdown headers such as `# Name`, `# Focus`, `# Temperature`, or `# Style` as substitutes for YAML front matter.

## Agent Instructions

In the Markdown body:

- State one focused role or a closely related set of responsibilities.
- Describe the mission, relevant expertise, workflow, expected output, and boundaries.
- Include examples or response structure only when they improve predictable results.
- State what the agent should defer, ask about, or avoid when requirements are unclear.

The prose guides behavior but does not enforce authorization, sandboxing, or security boundaries. Use platform permissions and enforced controls for those requirements.

## Validation Checklist

- [ ] Filename is descriptive, kebab-case, and ends in `.agent.md`.
- [ ] File is in a location supported by the selected harness.
- [ ] YAML front matter parses and uses documented properties.
- [ ] Description and body state a focused role, task, and useful output expectations.
- [ ] Tools are limited to those needed for the workflow.
- [ ] Instructions are tested with representative in-scope and out-of-scope requests.
- [ ] Tool availability and behavioral compliance are evaluated separately.
- [ ] Agent appears in the picker for its intended harness and scope.

## Anti-Patterns

Avoid broad or vague roles, unnecessary tools, unsupported front matter, redundant templates, and claims that natural-language instructions guarantee safe or compliant behavior.
