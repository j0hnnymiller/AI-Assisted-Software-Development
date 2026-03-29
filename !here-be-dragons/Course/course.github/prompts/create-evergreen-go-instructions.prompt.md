---
mode: chat
model: "anthropic/claude-3.5-sonnet@2024-10-22"
tools: ["create", "edit", "read"]
description: "Generate a Golang-specific instruction file for Evergreen Software Development guidance used by contributors and Copilot to produce consistent Go deliverables."
prompt_metadata:
  id: create-evergreen-go-instructions
  title: Create Evergreen Go Instructions
  owner: johnmillerATcodemag-com
  repository: AI-Assisted-Software-Development-Course
  version: 1.0.0
  created: 2025-10-19
  updated: 2025-10-19
  output_path: .github/instructions/evergreen-software-development-go.instructions.md
  category: guidance
  tags: [evergreen, go, golang, instructions, copilot, development]
  output_format: markdown
---

# Create Evergreen Software Development Instructions — Go

## Context

This prompt generates an instruction file tailored to Go projects in this repository. The resulting instruction file should be suitable for contributors and automated agents (e.g., GitHub Copilot) and must follow the repository's AI provenance conventions.

Follow `.github/instructions/ai-assisted-output.instructions.md` and `.github/instructions/copilot-instructions.md` when producing the instruction file.

## Requirements

- Produce a Markdown instruction file at `.github/instructions/evergreen-software-development-go.instructions.md`.
- Include YAML front matter with: `ai_generated` (boolean), `model` (provider/model@version), `operator`, `chat_id`, `prompt` (verbatim), `started`, `ended`, `task_durations`, `total_duration`, `ai_log`, and `source`.
- The instruction file should cover Go-specific best practices:
  - `go.mod` and `go.sum` management (dependency pinning, module versioning)
  - Go toolchain version pinning and reproducible builds
  - Static analysis tools (`go vet`, `golangci-lint`, `staticcheck`)
  - Dependency update workflows (`go get -u`, `go list -m -u all`, Dependabot configuration)
  - Build and test matrix (multiple Go versions, cross-platform builds)
  - Security scanning for Go modules (govulncheck, nancy)
  - Release tagging and semantic versioning for Go modules
  - Performance regression detection (benchmarks, profiling)
- Include a contributor checklist specific to Go projects and an example GitHub Actions workflow that runs `go test`, `go vet`, `golangci-lint`, `govulncheck`, and checks for outdated dependencies.
- Keep the instruction file actionable and concise (2-6 sections, with checklists and examples). Provide examples using Go-native tooling and GitHub Actions.

## Deliverable

Return only the complete content of the instruction file as the assistant response (no surrounding commentary). The instruction file should be ready to write to `.github/instructions/evergreen-software-development-go.instructions.md` and include the required YAML front matter populated with placeholders for `chat_id`, `started`, `ended`, durations, and `ai_log` (these can be left as tokens to be filled by Copilot integration).

Be concise, use clear headings, short lists, and include a complete example GitHub Actions job that demonstrates Go-specific evergreen practices including dependency checks, security scanning, and multi-version testing.

## Notes for the generator

- Use the repository's default model field format from `.github/instructions/copilot-instructions.md` if you need a model value. If unknown, use `anthropic/claude-3.5-sonnet@2024-10-22` as default.
- Focus on Go-specific tools and practices rather than generic software development guidance.
- Include concrete command examples that Go developers can copy and adapt.
- Do not include sidecar metadata files for Markdown outputs — embed YAML front matter.
