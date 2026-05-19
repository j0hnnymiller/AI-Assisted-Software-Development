---
mode: agent
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["codebase", "edit"]
description: "Create a GitHub Copilot agent for reviewing unfamiliar codebases"
prompt_metadata:
  id: create-codebase-explorer
  title: Generate Codebase Explorer Agent
  owner: johnmillerATcodemag-com
  version: "1.0.0"
  created: "2025-02-05"
  updated: "2025-02-05"
  output_path: .github/agents/codebase-explorer.agent.md
  category: generation
  tags: [agent, codebase-exploration, documentation, github-copilot]
  output_format: markdown
---

# Create Codebase Explorer Agent

Create a github copilot agent for reviewing an unfamiliar codebase.

Place the agent file in `.github/agents/` directory.
