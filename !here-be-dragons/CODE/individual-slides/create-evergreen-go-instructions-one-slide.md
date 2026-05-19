---
marp: true
ai_generated: true
model: "anthropic/claude-3.5-sonnet@2024-10-22"
operator: "<github-username>"
chat_id: "<chat-id>"
prompt: |
  Create one marp slide for the Go evergreen instructions prompt file.
started: "<ISO8601-started>"
ended: "<ISO8601-ended>"
task_durations:
  - task: "slide-creation"
    duration: "00:00:00"
total_duration: "00:00:00"
ai_log: "ai-logs/<yyyy>/<mm>/<dd>/<chat-id>/conversation.md"
source: ".github/copilot/Promptfiles/create-evergreen-go-instructions.prompt.md"
---

<!-- _class: lead -->

# Evergreen Go Instructions — Prompt

## Generate Golang-specific evergreen development guidance

- **`go.mod` & `go.sum`** — dependency pinning, module versioning
- **Toolchain Management** — version pinning, reproducible builds
- **Static Analysis** — `go vet`, `golangci-lint`, `staticcheck`
- **Security Scanning** — `govulncheck`, `nancy`
- **Dependency Updates** — `go get -u`, `go list -m -u all`, Dependabot
- **Testing Matrix** — multi-version, cross-platform builds
- **Performance** — benchmarks, regression detection

---

_Generates: `.github/instructions/evergreen-software-development-go.instructions.md`_

<!--
Speaker Notes:

This prompt generates comprehensive Golang-specific evergreen development instructions. Key areas covered:

1. **Dependency Management**: Focus on go.mod and go.sum for reproducible builds, including semantic versioning and module management best practices.

2. **Toolchain Consistency**: Pin Go versions to ensure consistent builds across environments and teams.

3. **Code Quality**: Integrate static analysis tools like go vet, golangci-lint, and staticcheck into CI pipelines for early issue detection.

4. **Security**: Use govulncheck and nancy for vulnerability scanning of Go dependencies, essential for maintaining secure codebases.

5. **Automation**: Leverage go get -u and go list -m -u all for dependency updates, plus Dependabot for automated PR creation.

6. **Testing Strategy**: Multi-version testing matrices ensure compatibility across Go versions and platforms (Linux, macOS, Windows).

7. **Performance Monitoring**: Include benchmark regression detection to catch performance issues early in development.

The generated instruction file provides actionable checklists and complete GitHub Actions workflows that Go teams can immediately implement. This ensures consistent evergreen practices across all Go projects in the repository.
-->
