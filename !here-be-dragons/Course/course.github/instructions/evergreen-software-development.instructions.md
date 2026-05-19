---
ai_generated: true
model: "anthropic/claude-3.5-sonnet@2024-10-22"
operator: "johnmillerATcodemag-com"
chat_id: "evergreen-instructions-20251019-153556"
prompt: |
  Generate an instruction file describing Evergreen Software Development practices for this repository. The produced file should include definition, goals, practices (branching, CI, dependency management, releases, security, observability), contributor checklist, and a sample GitHub Actions job that checks dependency freshness and runs tests.
started: "2025-10-19T15:35:56Z"
ended: "2025-10-19T15:40:00Z"
task_durations:
  - task: "authoring"
    duration: "00:03:30"
  - task: "provenance-setup"
    duration: "00:00:34"
total_duration: "00:04:04"
ai_log: "ai-logs/2025/10/19/evergreen-instructions-20251019-153556/conversation.md"
source: ".github/copilot/Promptfiles/create-evergreen-instructions.prompt.md"
---

# Evergreen Software Development — Instructions

Purpose: keep the repository continuously healthy and deployable by minimizing large batch upgrades, automating maintenance, and making small, frequent changes the norm.

## 1. Definition & Goals

- Definition: Evergreen development means continuously updating dependencies, CI, and infra so the main branch remains buildable, secure, and releasable at all times.
- Goals:
  - Reduce large, risky upgrades.
  - Keep security patches and dependency updates current.
  - Maintain fast, reliable CI and clear ownership for maintenance tasks.

## 2. Recommended Practices

- Branching: Keep `main` always green. Use short-lived feature branches and merge frequently.
- CI: Require CI to pass on all PRs; include unit tests, linting, and dependency checks.
- Dependency management:
  - Use automated dependency updates (Dependabot or similar) configured for minor/patch updates; schedule major upgrades for review windows.
  - Pin direct dependencies where appropriate and monitor transitive changes.
- Releases: Prefer continuous delivery for minor changes; gate major-version releases with review and compatibility testing.
- Security: Run SCA and vulnerability scans in CI; fail PRs on high/CVSS-critical regressions unless approved.
- Observability: Ensure test coverage targets and telemetry (where applicable) are maintained; PRs that reduce observability require strong justification.

## 3. Contributor Checklist (before merging)

- [ ] CI checks pass locally and on the PR.
- [ ] Dependency changes are explained and small (or linked to an issue for major changes).
- [ ] Security scan results reviewed; mitigations documented if any issues found.
- [ ] CHANGELOG or release notes updated if behavior or public APIs changed.
- [ ] Owner/maintainer sign-off for packages/modules with explicit owners.

## 4. Example: GitHub Actions job (dependency freshness + tests)

This is a minimal job to run dependency updates check and tests. Adapt to your language/tooling.

```yaml
name: Evergreen check
on:
  push:
    branches: [main]
  pull_request:
    paths: ["**/*"]

jobs:
  deps-and-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up environment
        run: |
          # install runtime, e.g., for Python/Node/Go
          echo "Set up runtime as needed"

      - name: Check dependency freshness
        run: |
          # Example checks (replace with repo-specific commands)
          # For Node: npm outdated --json
          # For Python: pip list --outdated --format=json
          echo "Checking outdated dependencies"

      - name: Run tests
        run: |
          # Replace with repo test command
          echo "Running tests"

      - name: Upload test results
        if: always()
        run: echo "Upload or store test artifacts"
```

## 5. Enforcement & Verification

- CI enforcement: PRs must pass the Evergreen check job before merge.
- Periodic maintenance: Schedule weekly or biweekly maintenance windows for major dependency PR triage.
- Audit: Review `dependabot` or update bot PRs weekly; maintain a small backlog for major-version upgrades with assigned owners.

## 6. Quick remediation steps (when CI fails due to deps)

1. Reproduce locally: run the failing job steps.
2. If a transitive upgrade broke tests, pin the immediate transitive dep or add a regression test and open a PR to fix.
3. For security-critical failures, open an urgent patch PR and notify maintainers.

## Notes

- Keep instructions short and actionable. Link to deeper playbooks or language-specific docs where necessary.
- Update this document when the repo's tooling or CI changes.
