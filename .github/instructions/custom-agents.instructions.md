---
ai_generated: true
model: "anthropic/claude-3.5-sonnet@2024-10-22"
operator: "johnmillerATcodemag-com"
chat_id: "update-custom-agents-instructions-20260212"
prompt: |
  Compare agent-file.instructions.md with GitHub's official custom agents guidance
  and create new instructions file aligned with official implementation
started: "2026-02-12T00:00:00Z"
ended: "2026-02-12T00:30:00Z"
task_durations:
  - task: "analysis and comparison"
    duration: "00:10:00"
  - task: "instruction file creation"
    duration: "00:20:00"
total_duration: "00:30:00"
ai_log: "ai-logs/2026/02/12/update-custom-agents-instructions-20260212/conversation.md"
source: "johnmillerATcodemag-com"
description: "Use when authoring or revising `.agent.md` custom-agent profiles; covers host schema, scope, tools, and validation."
applyTo: "**/*.agent.md"
---

# Custom Agent Authoring

Create focused `.agent.md` files using the selected host's current, documented format.

## Location and Naming

- Use a descriptive kebab-case filename ending in `.agent.md`.
- Put repository/workspace agents in `.github/agents/`.
- Verify user, organization, and enterprise locations against the selected host; do not assume they share the same paths or capabilities.

## Front Matter

- Include a clear `description`; use other fields only when documented for the selected host.
- `name` and `tools` are common optional fields, but their behavior and accepted values are host-specific.
- Use `model`, `target`, MCP server configuration, and other optional properties only when the selected host documents them.
- Do not substitute legacy Markdown headers such as `# Name`, `# Focus`, `# Temperature`, or `# Style` for supported front matter.

```yaml
---
name: security-reviewer
description: Review code for security issues and report evidence-based findings.
---
```

## Agent Instructions

In the Markdown body:

- State one focused role or a closely related set of responsibilities.
- Describe the mission, relevant expertise, bounded workflow, expected output, and boundaries.
- Specify what the agent should defer, ask about, or avoid when requirements are unclear.
- Include examples or response structures only when they improve predictable behavior.
- Keep recommendations distinct from verified host requirements.

## Tool Scope

- Select the minimum host-supported tools needed for the workflow.
- Check whether omitting a tool list grants broader access in the selected host.
- Do not treat natural-language instructions as authorization, sandboxing, or security controls; use platform-enforced permissions for those requirements.

## Validation Checklist

- [ ] Filename is descriptive, kebab-case, and ends in `.agent.md`.
- [ ] File is in a location supported by the selected host.
- [ ] YAML front matter parses and uses documented properties.
- [ ] Description and body state a focused role, task, and useful output expectations.
- [ ] Tool access is limited to what the workflow needs.
- [ ] Links and examples are valid for the repository and host.
- [ ] Test representative in-scope and out-of-scope requests.
- [ ] Verify picker discovery separately from behavioral compliance.

## Anti-Patterns

Avoid broad personas, excessive tools, unsupported front matter, redundant templates, repository-specific values copied into shared guidance, and claims that prose alone enforces safe behavior.
