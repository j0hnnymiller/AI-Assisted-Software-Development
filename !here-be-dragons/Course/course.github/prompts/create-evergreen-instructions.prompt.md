---
mode: chat
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["create", "edit", "read"]
description: "Generate an instruction file for Evergreen Software Development guidance used by contributors and Copilot to produce consistent deliverables."
prompt_metadata:
  id: create-evergreen-instructions
  title: Create Evergreen Instructions
  owner: johnmillerATcodemag-com
  repository: AI-Assisted-Software-Development-Course
  version: 1.0.0
  created: 2025-10-19
  updated: 2025-10-19
  output_path: .github/instructions/evergreen-software-development.instructions.md
  category: guidance
  tags: [evergreen, instructions, copilot, development]
  output_format: markdown
---

# Create Evergreen Software Development Instructions

## Context

This prompt generates an instruction file describing Evergreen Software Development practices for this repository. The produced instruction file should be suitable for use by contributors and by automated agents (e.g., GitHub Copilot) to guide code changes, CI, and maintenance workflows.

Follow the repository conventions in `.github/instructions/ai-assisted-output.instructions.md` and `.github/instructions/copilot-instructions.md` when producing the instruction file. Ensure the instruction file includes required provenance front matter if it is AI-generated.

## Requirements

- Produce a Markdown instruction file at `.github/instructions/evergreen-software-development.instructions.md`.
- Include YAML front matter at the top with the following fields: `ai_generated` (boolean), `model` (provider/model@version), `operator` (github-username or operator id), `chat_id`, `prompt` (verbatim prompt used), `started`, `ended`, `task_durations`, `total_duration`, `ai_log`, and `source`.
- The instruction file should cover: definition of evergreen software development, goals, recommended practices (branching, CI, dependency management, releases, security, observability), checklist for contributors, example CI jobs, and minimal enforcement guidance (how to verify compliance).
- Keep the instruction file actionable and concise (2-6 sections, with checklists and examples). Provide examples in repository-native tooling (prefer GitHub Actions where relevant).
- Output must be valid Markdown and suitable for inclusion in `.github/instructions/`.

## Deliverable

Return only the complete content of the instruction file as the assistant response (no surrounding commentary). The instruction file should be ready to write to `.github/instructions/evergreen-software-development.instructions.md` and include the required YAML front matter populated with placeholders for `chat_id`, `started`, `ended`, durations, and `ai_log` (these can be left as tokens to be filled by Copilot integration).

Be concise, use clear headings, short lists, and include a small example GitHub Actions job that checks dependency freshness and runs tests.

## Notes for the generator

- Use the repository's default model field format from `.github/instructions/copilot-instructions.md` if you need a model value. If unknown, use `anthropic/claude-3.5-sonnet@2024-10-22` as default.
- Do not include sidecar metadata files for Markdown outputs — embed YAML front matter.
