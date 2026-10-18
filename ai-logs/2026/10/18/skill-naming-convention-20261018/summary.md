---
ai_generated: true
model: "unknown/unknown@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "skill-naming-convention-20261018"
prompt: |
  go ahead with the plan
started: "2026-10-18T15:17:01+00:00"
ended: "2026-10-18T15:23:01+00:00"
task_durations:
  - task: "Approved skill renaming and active reference verification"
    duration: "00:06:00"
total_duration: "00:06:00"
ai_log: "ai-logs/2026/10/18/skill-naming-convention-20261018/conversation.md"
source: "user"
---

# Chat Summary

## Objective

Apply the user's naming decisions for all 80 repository skills: rename 50, keep 30 names, and repair current references without changing workflows.

## Decisions and Boundaries

- A skill's folder and its entry point's YAML `name` must match.
- Use the user's exact selected names, including custom spelling and singular/plural choices.
- The `deprecate-` prefix is a naming label only. Do not disable, delete, or change those workflows.
- Do not consolidate overlapping skills, rename the artifacts that skills generate, rewrite historical provenance, or distribute changes to other repositories.
- Preserve pre-existing worktree changes. Do not stage or commit.

## Renamed Skills

New-name links point to the current skill entry points.

| Previous name | Selected name |
| --- | --- |
| `ai-assisted-development-process` | [design-ai-assisted-development-process](../../../../../.github/skills/design-ai-assisted-development-process/SKILL.md) |
| `ai-practitioner-resource-catalog` | [curate-ai-practitioner-resources](../../../../../.github/skills/curate-ai-practitioner-resources/SKILL.md) |
| `architecture-design` | [design-system-architecture](../../../../../.github/skills/design-system-architecture/SKILL.md) |
| `blog-section-authoring` | [author-blog-section](../../../../../.github/skills/author-blog-section/SKILL.md) |
| `bug-hunt-issues` | [find-bugs-for-issue-drafts](../../../../../.github/skills/find-bugs-for-issue-drafts/SKILL.md) |
| `chatmode-authoring` | [deprecate-chatmode-authoring](../../../../../.github/skills/deprecate-chatmode-authoring/SKILL.md) |
| `cloud-readiness-checklists` | [cloud-readiness-checklist-authoring](../../../../../.github/skills/cloud-readiness-checklist-authoring/SKILL.md) |
| `codebase-review` | [review-codebase-instruction-compliance](../../../../../.github/skills/review-codebase-instruction-compliance/SKILL.md) |
| `commit-workspace-changes-logical-groups` | [commit-changes-in-logical-groups](../../../../../.github/skills/commit-changes-in-logical-groups/SKILL.md) |
| `compliance-check` | [assess-compliance](../../../../../.github/skills/assess-compliance/SKILL.md) |
| `cqrs-event-sourcing-guidance` | [cqrs-and-event-sourcing-guidance](../../../../../.github/skills/cqrs-and-event-sourcing-guidance/SKILL.md) |
| `create-agent-instructions-file` | [create-agent-authoring-instructions](../../../../../.github/skills/create-agent-authoring-instructions/SKILL.md) |
| `create-ai-assisted-output-instructions` | [create-ai-assisted-output-policy](../../../../../.github/skills/create-ai-assisted-output-policy/SKILL.md) |
| `create-codebase-explorer` | [create-codebase-explorer-agent](../../../../../.github/skills/create-codebase-explorer-agent/SKILL.md) |
| `create-instruction-file-instructions` | [create-instruction-file-policy](../../../../../.github/skills/create-instruction-file-policy/SKILL.md) |
| `create-instruction-files-instructions` | [create-instruction-file-authoring-instructions](../../../../../.github/skills/create-instruction-file-authoring-instructions/SKILL.md) |
| `create-issues-for-dead-code` | [create-dead-code-issues](../../../../../.github/skills/create-dead-code-issues/SKILL.md) |
| `create-issues-for-found-bugs` | [create-bug-issues](../../../../../.github/skills/create-bug-issues/SKILL.md) |
| `create-prompt-file-instructions-file` | [deprecate-create-prompt-file-instructions-file](../../../../../.github/skills/deprecate-create-prompt-file-instructions-file/SKILL.md) |
| `create-prompt-instructions` | [deprecate-create-prompt-instructions](../../../../../.github/skills/deprecate-create-prompt-instructions/SKILL.md) |
| `create-use-case-instruction-prompt` | [deprecate-create-use-case-instructions-prompt](../../../../../.github/skills/deprecate-create-use-case-instructions-prompt/SKILL.md) |
| `create-use-case-instructions` | [create-use-case-authoring-instructions](../../../../../.github/skills/create-use-case-authoring-instructions/SKILL.md) |
| `create-use-case-instructions-file-prompt-file` | [deprecate-create-use-case-instruction-file-prompt-file](../../../../../.github/skills/deprecate-create-use-case-instruction-file-prompt-file/SKILL.md) |
| `derive-use-cases-from-conceptual-model` | [use-cases-from-conceptual-model](../../../../../.github/skills/use-cases-from-conceptual-model/SKILL.md) |
| `finalize-pptx-local` | [finalize-pptx-locally](../../../../../.github/skills/finalize-pptx-locally/SKILL.md) |
| `github-config-canonical` | [github-config-select-canonical](../../../../../.github/skills/github-config-select-canonical/SKILL.md) |
| `instructions-bestpractices-issues` | [create-instruction-review-issue-drafts](../../../../../.github/skills/create-instruction-review-issue-drafts/SKILL.md) |
| `integration-design` | [design-system-integrations](../../../../../.github/skills/design-system-integrations/SKILL.md) |
| `issue-readiness-review` | [review-issue-readiness](../../../../../.github/skills/review-issue-readiness/SKILL.md) |
| `meeting-briefs-from-transcripts` | [create-meeting-brief-from-transcript](../../../../../.github/skills/create-meeting-brief-from-transcript/SKILL.md) |
| `mermaid-markdown-to-docx` | [convert-mermaid-markdown-to-docx](../../../../../.github/skills/convert-mermaid-markdown-to-docx/SKILL.md) |
| `meta-ai-validate-and-improve-instructions` | [orchestrate-instruction-improvement](../../../../../.github/skills/orchestrate-instruction-improvement/SKILL.md) |
| `migration-strategy` | [plan-system-migration](../../../../../.github/skills/plan-system-migration/SKILL.md) |
| `ownership-support-model-guidance` | [design-ownership-and-support-model](../../../../../.github/skills/design-ownership-and-support-model/SKILL.md) |
| `pattern-analysis` | [analyze-architecture-patterns](../../../../../.github/skills/analyze-architecture-patterns/SKILL.md) |
| `performance-analysis` | [analyze-system-performance](../../../../../.github/skills/analyze-system-performance/SKILL.md) |
| `prd-authoring` | [author-product-requirements](../../../../../.github/skills/author-product-requirements/SKILL.md) |
| `refactor-analysis` | [analyze-refactoring-opportunities](../../../../../.github/skills/analyze-refactoring-opportunities/SKILL.md) |
| `risk-assessment` | [assess-architecture-risks](../../../../../.github/skills/assess-architecture-risks/SKILL.md) |
| `scalability-planning` | [plan-system-scalability](../../../../../.github/skills/plan-system-scalability/SKILL.md) |
| `sdlc-stabilization-guidance` | [plan-sdlc-stabilization](../../../../../.github/skills/plan-sdlc-stabilization/SKILL.md) |
| `security-architecture` | [design-security-architecture](../../../../../.github/skills/design-security-architecture/SKILL.md) |
| `security-audit-issues` | [create-security-audit-issues](../../../../../.github/skills/create-security-audit-issues/SKILL.md) |
| `sme-intro-scheduling` | [schedule-sme-introductions](../../../../../.github/skills/schedule-sme-introductions/SKILL.md) |
| `summarize-vti-content` | [summarize-transcript-content](../../../../../.github/skills/summarize-transcript-content/SKILL.md) |
| `technical-debt-remediation` | [remediate-technical-debt](../../../../../.github/skills/remediate-technical-debt/SKILL.md) |
| `technology-evaluation` | [evaluate-technology-options](../../../../../.github/skills/evaluate-technology-options/SKILL.md) |
| `tests-gap-analysis` | [analyze-test-gaps](../../../../../.github/skills/analyze-test-gaps/SKILL.md) |
| `vue-migration-testing` | [vue-migration-test-coverage](../../../../../.github/skills/vue-migration-test-coverage/SKILL.md) |
| `workflow-path-counting` | [count-workflow-paths](../../../../../.github/skills/count-workflow-paths/SKILL.md) |

## Names Retained

```text
academia-api-gateway-routing
academia-course-scheduling
academia-data-import-export
academia-database-migrations
academia-faculty-management
academia-grades-transcripts
academia-identity-and-permissions
academia-integration-deployment
academia-logging-monitoring
academia-mobile-apps
academia-reporting-analytics
academia-student-enrollment
academia-system-configuration
academia-web-portals
check-context-conflicts
create-instruction-files-prompt-file
create-instruction-prompt
databricks-apps-cicd-advisory
databricks-apps-iac-advisory
databricks-hosting-decisions
generate-instructions
github-config-consolidate
github-config-distribute
github-config-inventory
iec62304-compliance-assessment
implement-vertical-slice
merge-marp-decks
run-aiasd-weekly-slide-pipeline
update-application-c4-diagrams
validate-and-improve-instructions
```

Retaining a name does not prevent updating that skill's references to other renamed skills.

## Verification

- All 80 skill entry points parse as YAML and have nonempty descriptions.
- All folder names match front matter names; selected names are unique lowercase kebab-case and no longer than 64 characters.
- The 50 former skill directories are absent, and all 50 replacements exist.
- Current links and command references use the selected names; historical source paths and artifact filenames retain their original spelling.
- Original creation metadata and previous revision records remain unchanged.
- Supporting scripts moved with their skill retain their original bytes.
- Workflow bodies match the expected naming substitutions, apart from the related documentation and heading updates.
- Checked 285 local links across affected artifacts and the new logs: no newly broken links. Twenty pre-existing broken README links remain unchanged and are outside this task's scope.
- All five supporting PowerShell scripts parse successfully, including the canonical-comparison script at its new path.
- `git diff --check` passed.
- All nine pre-existing staged files were verified as preserved in a commit made independently during this work; the index was not changed by this task.
- No commit or cross-repository rollout was performed.

## Next Steps

Review and commit the changes when ready. If the current host caches skill discovery, refresh it before invoking the renamed slash commands. A cross-repository rollout requires separate approval and must account for old paths in target repositories.
