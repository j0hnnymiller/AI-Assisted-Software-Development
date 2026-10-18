---
ai_generated: true
model: "unknown/unknown@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
prompt: |
  Continue through the remaining prompt families, recording each path as reviewed,
  duplicate/variant, supporting artifact, or needs skill coverage. Only after the
  ledger is complete, summarize genuine skill gaps and propose changes.
started: "2026-10-18T11:54:18-07:00"
ended: "2026-10-18T12:01:07-07:00"
task_durations:
  - task: "Refresh inventory and reconcile all prompt paths"
    duration: "00:02:00"
  - task: "Review remaining families and assign dispositions"
    duration: "00:04:49"
total_duration: "00:06:49"
ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
source: "User request and refreshed GitHub configuration inventory"
---

# Prompt Review Ledger

This ledger accounts for every distinct `.github/prompts/**` and
`.github/promptfiles/**` path in the refreshed inventory generated
2026-10-18. Repository lists identify where the path occurs; multiple repositories
with the same bytes are recorded together. Divergent copies are called out in the
disposition note.

Disposition meanings:

- **Reviewed** - a distinct, bounded, or project-specific prompt was reviewed; it does
  not justify a new reusable canonical skill.
- **Duplicate/variant** - the reusable workflow is already covered by the named
  canonical skill or the path is a superseded/alternate prompt.
- **Supporting artifact** - index, schema, historical report, guide, execution map, or
  empty file that supports another workflow but is not an independent skill.
- **Needs skill coverage** - a reusable workflow has no suitable existing skill.

## `.github/promptfiles/` (4)

| Path | Repository | Disposition | Coverage or evidence |
|---|---|---|---|
| `.github/promptfiles/check-context.prompt.md` | `Teleflex/agentsolution` | Duplicate/variant | `check-context-conflicts`; read-only scope and evidence rules supersede legacy full-scan/edit guidance. |
| `.github/promptfiles/create_chatmode_guidance.md` | `Teleflex/agentsolution` | Supporting artifact | Empty (0 bytes); contains no workflow. |
| `.github/promptfiles/create-ai-assisted-dev-wi-20260209.prompt.md` | `Teleflex/agentsolution` | Duplicate/variant | `author-iec62304-work-instruction`; controlled QMS sources and qualified review remain prerequisites. |
| `.github/promptfiles/create-ai-assisted-output-instructions.prompt.md` | `Teleflex/agentsolution` | Duplicate/variant | `create-ai-assisted-output-policy`; canonical workflow verifies host capabilities and distinguishes policy from enforcement. |

## `.github/prompts/` root (97)

| Path | Repository | Disposition | Coverage or evidence |
|---|---|---|---|
| `.github/prompts/ai-practitioner-resources-json.prompt.md` | `ai-practitioner/ai-practitioner-resources` | Duplicate/variant | `curate-ai-practitioner-resources`; validates source quality, schema, score scope, and aggregate thresholds. |
| `.github/prompts/ai-practitioner-resources.prompt.md` | `ai-practitioner/ai-practitioner-resources` | Duplicate/variant | Superseded by the JSON prompt; same catalog workflow, replaced with risk-based schema-driven output. |
| `.github/prompts/analyze-testability.prompt.md` | `Teleflex/AI-SW-Dev` | Duplicate/variant | `analyze-test-gaps` now includes design-for-testability evidence, controlled scoring, and the testability scorecard. |
| `.github/prompts/architecture-design.prompt.md` | `Messer`, `MusicBot` | Duplicate/variant | `design-system-architecture`; same architecture design workflow. |
| `.github/prompts/assess-d0003329-clause4.4-legacy.prompt.md` | `Teleflex/AIASD-SOP` | Duplicate/variant | `iec62304-compliance-assessment`; organization-specific D0003329 procedure remains source evidence, not canonical rule text. |
| `.github/prompts/assess-d0003329-clause5-development.prompt.md` | `Teleflex/AIASD-SOP` | Duplicate/variant | `iec62304-compliance-assessment`; clause-specific assessment is covered without importing Teleflex procedure claims. |
| `.github/prompts/assess-d0003329-clause6-maintenance.prompt.md` | `Teleflex/AIASD-SOP` | Duplicate/variant | `iec62304-compliance-assessment`; clause-specific assessment is covered without importing Teleflex procedure claims. |
| `.github/prompts/assess-d0003329-clause7-risk.prompt.md` | `Teleflex/AIASD-SOP` | Duplicate/variant | `iec62304-compliance-assessment`; clause-specific assessment is covered without importing Teleflex procedure claims. |
| `.github/prompts/assess-d0003329-clause8-config.prompt.md` | `Teleflex/AIASD-SOP` | Duplicate/variant | `iec62304-compliance-assessment`; clause-specific assessment is covered without importing Teleflex procedure claims. |
| `.github/prompts/assess-d0003329-clause9-problems.prompt.md` | `Teleflex/AIASD-SOP` | Duplicate/variant | `iec62304-compliance-assessment`; clause-specific assessment is covered without importing Teleflex procedure claims. |
| `.github/prompts/assess-d0003329-executive-summary.prompt.md` | `Teleflex/AIASD-SOP` | Duplicate/variant | `iec62304-compliance-assessment`; executive summary remains an output variation, not a separate workflow. |
| `.github/prompts/assess-d0003329-iec62304-compliance.prompt.md` | `Teleflex/AIASD-SOP` | Duplicate/variant | `iec62304-compliance-assessment`; same standard assessment family. |
| `.github/prompts/bug-hunt-issues.prompt.md` | `MusicBot` | Duplicate/variant | `create-bug-issues`; findings-to-issue-drafts workflow is already covered. |
| `.github/prompts/check-context.prompt.md` | `Messer`, `MusicBot`, `Teleflex/AI-SW-Dev`, `V&S`, `ai-practitioner/ai-practitioner-blog`, `zeus/zeus.academia.3b` | Duplicate/variant | Five content variants map to `check-context-conflicts`; old copies vary in scope, output, and unsafe edit/full-scan directions. |
| `.github/prompts/cicd-advisory-databricks-apps.prompt.md` | `Messer` | Duplicate/variant | `databricks-apps-cicd-advisory`; deployment promotion and evidence workflow is covered. |
| `.github/prompts/cloud-readiness-build-checklist-variants.prompt.md` | `Messer` | Duplicate/variant | `cloud-readiness-checklist-authoring`; tiered checklist authoring and traceability are covered. |
| `.github/prompts/code-review.prompt.md` | `ai-practitioner/ai-practitioner-resources` | Reviewed | Bound to that application's architecture and unsupported local quality mandates; generic PR review is available through `github-pr-reviewer`, so it is not a reusable canonical gap. |
| `.github/prompts/codebase-review.prompt.md` | `Messer` | Duplicate/variant | `review-codebase-instruction-compliance`; repository instruction compliance review is covered. |
| `.github/prompts/commit-workspace-changes-logical-groups.prompt.md` | `Messer` | Duplicate/variant | `commit-changes-in-logical-groups`; approval gates and staged/unstaged safeguards are covered. |
| `.github/prompts/compare-workspace-to-instructions.prompt.md` | `AIASD/AIASD-Brownfield-Example` | Duplicate/variant | `review-codebase-instruction-compliance`; same instruction-compliance audit. |
| `.github/prompts/compliance-check.prompt.md` | `Messer`, `MusicBot` | Duplicate/variant | `assess-compliance`; applicability, evidence status, and unknowns are covered. |
| `.github/prompts/convert-mermaid-markdown-to-templated-docx.prompt.md` | `Messer` | Duplicate/variant | `convert-mermaid-markdown-to-docx`; Messer-specific sizing, styles, and scripts were not generalized. |
| `.github/prompts/count-workflow-paths.prompt.md` | `ai-practitioner/ai-practitioner-resources` | Duplicate/variant | `count-workflow-paths`; terminal, loop, and path-explosion rules are covered. |
| `.github/prompts/create_chatmode_guidance.md` | `Teleflex/AI-SW-Dev` | Supporting artifact | Empty file; no workflow to migrate. |
| `.github/prompts/create-academia-execution-plan.prompt.md` | `zeus/zeus.academia.3b` | Duplicate/variant | `plan-implementation-roadmap`; fixed Academia phase and domain rules remain requirements, not generic planning rules. |
| `.github/prompts/create-agent-instructions-file.prompt.md` | `Messer` | Duplicate/variant | `create-agent-authoring-instructions`; agent authoring workflow is covered. |
| `.github/prompts/create-agent-instructions.prompt.md` | `Messer` | Duplicate/variant | `create-agent-authoring-instructions`; variant of the same agent authoring workflow. |
| `.github/prompts/create-ai-assisted-dev-wi-20260209.prompt.md` | `Teleflex/AI-SW-Dev` | Duplicate/variant | `author-iec62304-work-instruction`; controlled work-instruction authoring is covered. |
| `.github/prompts/create-ai-assisted-output-instructions.prompt.md` | `Messer`, `Teleflex/AI-SW-Dev` | Duplicate/variant | Two divergent policy-generator variants map to `create-ai-assisted-output-policy`; the autonomy-heavy variant is not adopted. |
| `.github/prompts/create-ai-dev-process.prompt.md` | `zeus/zeus.academia.3b` | Duplicate/variant | `design-ai-assisted-development-process`; reusable process-design workflow is covered. |
| `.github/prompts/create-blog-section.prompt.md` | `ai-practitioner/ai-practitioner-blog` | Duplicate/variant | `author-blog-section`; bounded, source-grounded editing is covered. |
| `.github/prompts/create-custom-agents-instructions.prompt.md` | `zeus/zeus.academia.3b` | Duplicate/variant | `create-agent-authoring-instructions` and `custom-agents.instructions.md`; current host behavior supersedes legacy fields. |
| `.github/prompts/create-git-workflow-instructions.prompt.md` | `zeus/zeus.academia.3b` | Duplicate/variant | `generate-instructions` and `github-cli.instructions.md`; repo-specific policy must be evidence-based. |
| `.github/prompts/create-github-config-optimizer-agent.prompt.md` | `Messer` | Duplicate/variant | `create-agent-authoring-instructions` plus `github-config-inventory` optimization signals; generator embeds stale rules and a spoke-specific agent definition. |
| `.github/prompts/create-implementation-prompt-generation-instructions.prompt.md` | `zeus/zeus.academia.3b` | Duplicate/variant | `create-implementation-skills`; reusable component workflows belong in skills, not prompt generators. |
| `.github/prompts/create-implementation-prompt-instructions.prompt.md` | `zeus/zeus.academia.3b` | Duplicate/variant | `create-implementation-skills`; bounded implementation uses `implement-vertical-slice`. |
| `.github/prompts/create-instruction-file-instructions.prompt.md` | `AIASD/Fleetly`, `Messer` | Duplicate/variant | `create-instruction-file-authoring-instructions`; same-path copies are identical and the obsolete singular suffix is not canonical. |
| `.github/prompts/create-instruction-files-instructions.prompt.md` | `Messer` | Duplicate/variant | `create-instruction-file-authoring-instructions`; current templates and validation are already covered. |
| `.github/prompts/create-instruction-files-prompt-file.prompt.md` | `Messer` | Duplicate/variant | Retired prompt-authoring redirect plus `create-instruction-file-authoring-instructions`; new prompt generators are prohibited. |
| `.github/prompts/create-instruction-prompt.prompt.md` | `Messer` | Duplicate/variant | Retired instruction-prompt redirect plus `create-instruction-file-authoring-instructions`; prompt files are not the authoring target. |
| `.github/prompts/create-issues-for-dead-code.prompt.md` | `MusicBot` | Duplicate/variant | `create-dead-code-issues`; read-only analysis and issue drafts are covered. |
| `.github/prompts/create-issues-for-found-bugs.prompt.md` | `Messer`, `MusicBot` | Duplicate/variant | `create-bug-issues`; bug finding and issue drafting are covered. |
| `.github/prompts/create-prd.prompt.md` | `zeus/zeus.academia.3b` | Duplicate/variant | `author-product-requirements`; requirements structure is covered without fixed unsupported counts. |
| `.github/prompts/create-product-manager-agent.prompt.md` | `zeus/zeus.academia.3b` | Duplicate/variant | `create-agent-authoring-instructions` and the canonical Product Manager agent; no agent-generator skill gap. |
| `.github/prompts/create-project-overview.prompt.md` | `zeus/zeus.academia.3b` | Duplicate/variant | `generate-instructions`; project facts and constraints must be grounded in supplied evidence. |
| `.github/prompts/create-prompt-file-instructions-file.prompt.md` | `Messer` | Duplicate/variant | Retired prompt-authoring redirect; reusable task workflows map to skills. |
| `.github/prompts/create-prompt-instructions.prompt.md` | `Messer` | Duplicate/variant | Retired prompt-authoring redirect; no new prompt-file guidance is needed. |
| `.github/prompts/create-technology-instructions.prompt.md` | `zeus/zeus.academia.3b` | Duplicate/variant | `generate-instructions`; technology rules remain specific to verified repository requirements. |
| `.github/prompts/create-vertical-slice-implementation-instructions.prompt.md` | `zeus/zeus.academia.3b` | Duplicate/variant | `vertical-slice.instructions.md` and `implement-vertical-slice`; generic slice guidance is covered. |
| `.github/prompts/databricks-app-hosting-decision-factors.prompt.md` | `Messer` | Duplicate/variant | `databricks-hosting-decisions`; hosting trade-off evaluation is covered. |
| `.github/prompts/DGA-Status-Report-Generator.md` | `V&S` | Reviewed | One-off V&S report workflow depends on private repository data, dates, and output layout; not generalizable without importing private context. |
| `.github/prompts/ERROR_HANDLING_GUIDE.md` | `ai-practitioner/ai-practitioner-resources` | Supporting artifact | PM system implementation guide; tied to that repository's API retry and recovery code. |
| `.github/prompts/generate-cqrs-eventsourcing-instructions.prompt.md` | `zeus/zeus.academia.3b` | Duplicate/variant | `cqrs-and-event-sourcing-guidance`; architecture workflow is covered. |
| `.github/prompts/generate-csharp-instructions.prompt.md` | `zeus/zeus.academia.3b` | Duplicate/variant | `generate-instructions` and the applicable C# instruction policy; no universal C# rules imported. |
| `.github/prompts/generate-implementation-prompts-prompt.md` | `Messer` | Duplicate/variant | `create-implementation-skills`; slice specifications remain requirements, while reusable workflows are skills. |
| `.github/prompts/generate-instructions.prompt.md` | `Messer` | Duplicate/variant | `generate-instructions`; project and technology instruction generation is covered. |
| `.github/prompts/implement-slice1-tdd.prompt.md` | `Teleflex/AI-SW-Dev` | Reviewed | Teleflex slice-specific implementation input; `implement-vertical-slice` and TDD guidance cover the reusable execution method. |
| `.github/prompts/implement-slice2-tdd.prompt.md` | `Teleflex/AI-SW-Dev` | Reviewed | Teleflex slice-specific implementation input; project requirements stay in the spoke. |
| `.github/prompts/implement-slice3-tdd.prompt.md` | `Teleflex/AI-SW-Dev` | Reviewed | Teleflex slice-specific implementation input; project requirements stay in the spoke. |
| `.github/prompts/implement-slice4-tdd.prompt.md` | `Teleflex/AI-SW-Dev` | Reviewed | Teleflex slice-specific implementation input; project requirements stay in the spoke. |
| `.github/prompts/implement-slice5-tdd.prompt.md` | `Teleflex/AI-SW-Dev` | Reviewed | Teleflex slice-specific implementation input; project requirements stay in the spoke. |
| `.github/prompts/implement-slice6-tdd.prompt.md` | `Teleflex/AI-SW-Dev` | Reviewed | Teleflex slice-specific implementation input; project requirements stay in the spoke. |
| `.github/prompts/implement-slice7-tdd.prompt.md` | `Teleflex/AI-SW-Dev` | Reviewed | Teleflex slice-specific implementation input; project requirements stay in the spoke. |
| `.github/prompts/implement-slices-4-8-parallel.prompt.md` | `Teleflex/AI-SW-Dev` | Reviewed | Calculator-specific dependency graph and parallel plan; not a reusable orchestration skill. |
| `.github/prompts/INDEPENDENCE_GUIDE.md` | `ai-practitioner/ai-practitioner-resources` | Supporting artifact | PM-system guide tied to local criteria and scripts; general issue independence is covered by `review-issue-readiness`. |
| `.github/prompts/infrastructure-as-code-advisory-databricks-apps.prompt.md` | `Messer` | Duplicate/variant | `databricks-apps-iac-advisory`; Databricks Apps IaC design is covered. |
| `.github/prompts/instructions-bestpractices-issues.prompt.md` | `Messer` | Duplicate/variant | `create-instruction-review-issue-drafts`; issue drafting remains distinct from making external issue changes. |
| `.github/prompts/integration-design.prompt.md` | `Messer` | Duplicate/variant | `design-system-integrations`; integration planning is covered. |
| `.github/prompts/issue-intake-testing.md` | `ai-practitioner/ai-practitioner-resources` | Supporting artifact | Historical PM issue-intake test report, not an assistant workflow. |
| `.github/prompts/LABEL_VALIDATION_GUIDE.md` | `ai-practitioner/ai-practitioner-resources` | Supporting artifact | PM automation label contract and implementation guidance; taxonomy remains project-specific. |
| `.github/prompts/meeting-brief-from-transcript.prompt.md` | `Messer` | Duplicate/variant | `create-meeting-brief-from-transcript`; attribution and uncertainty are covered. |
| `.github/prompts/migration-strategy.prompt.md` | `Messer` | Duplicate/variant | `plan-system-migration`; migration planning workflow is covered. |
| `.github/prompts/movePost.prompt.md` | `ai-practitioner/ai-practitioner-blog` | Duplicate/variant | `transfer-blog-publication`; reversible publication-copy workflow covers filename, front matter, and approved assets. |
| `.github/prompts/ownership-support-model-guidance.prompt.md` | `Messer` | Duplicate/variant | `design-ownership-and-support-model`; role, escalation, handoff, and coverage design are covered. |
| `.github/prompts/pattern-analysis.prompt.md` | `Messer`, `MusicBot` | Duplicate/variant | `analyze-architecture-patterns`; the two repository copies share the same workflow. |
| `.github/prompts/performance-analysis.prompt.md` | `Messer`, `MusicBot` | Duplicate/variant | `analyze-system-performance`; .NET-specific performance analysis is separately available where applicable. |
| `.github/prompts/pm-review.md` | `ai-practitioner/ai-practitioner-resources` | Duplicate/variant | `review-issue-readiness`; write actions, forced estimates, assignment, and label rules are not imported as defaults. |
| `.github/prompts/pm-review.schema.json` | `ai-practitioner/ai-practitioner-resources` | Supporting artifact | JSON automation contract consumed by that PM workflow; not an independent assistant skill. |
| `.github/prompts/prepare-code-publication.prompt.md` | `ai-practitioner/ai-practitioner-blog` | Duplicate/variant | `transfer-blog-publication`; publication preparation is covered with confirmation for conflicting metadata. |
| `.github/prompts/PROMPT_ARCHITECTURE_MIGRATION_GUIDE.md` | `ai-practitioner/ai-practitioner-resources` | Supporting artifact | Historical repository migration guide; its prompt-as-business-logic model is not current canonical guidance. |
| `.github/prompts/README.md` | `Messer`, `ai-practitioner/ai-practitioner-resources` | Supporting artifact | Two divergent prompt indexes; both contain stale prompt references and are repository-local indexes, not workflows. |
| `.github/prompts/refactor-analysis.prompt.md` | `Messer`, `MusicBot` | Duplicate/variant | Two near-identical variants map to `analyze-refactoring-opportunities`; one has malformed metadata only. |
| `.github/prompts/response-summary.prompt.md` | `V&S` | Duplicate/variant | `summarize-transcript-content`; aggregation safeguards and attribution are covered. |
| `.github/prompts/restore-blog-publication.prompt.md` | `ai-practitioner/ai-practitioner-blog` | Duplicate/variant | `transfer-blog-publication`; restoration is covered, with conflicting contact/image rules requiring confirmation. |
| `.github/prompts/review-evergreen-code.prompt.md` | `AIASD/AIASD-Brownfield-Example` | Duplicate/variant | `analyze-refactoring-opportunities`; evergreen evaluation is grounded in the supplied repository baseline. |
| `.github/prompts/risk-assessment.prompt.md` | `Messer`, `MusicBot` | Duplicate/variant | `assess-architecture-risks`; risk analysis and mitigation planning are covered. |
| `.github/prompts/scalability-planning.prompt.md` | `Messer`, `MusicBot` | Duplicate/variant | `plan-system-scalability`; capacity and scale planning are covered. |
| `.github/prompts/sdlc-stabilization-guidance.prompt.md` | `Messer` | Duplicate/variant | `plan-sdlc-stabilization`; evidence-based SDLC risk prioritization is covered. |
| `.github/prompts/security-architecture.prompt.md` | `Messer`, `MusicBot` | Duplicate/variant | `design-security-architecture`; the copies map to the same security-design workflow. |
| `.github/prompts/security-audit-issues.prompt.md` | `Messer`, `MusicBot` | Duplicate/variant | `create-security-audit-issues`; issue drafting maps to the existing skill; no security audit is implied by this classification. |
| `.github/prompts/session-recap-2025-11-07.md` | `ai-practitioner/ai-practitioner-resources` | Supporting artifact | Historical chat/session report, not an assistant workflow. |
| `.github/prompts/sme-intro-invites.prompt.md` | `V&S` | Duplicate/variant | `schedule-sme-introductions`; proposal and authorization safeguards supersede automatic invite behavior. |
| `.github/prompts/technology-evaluation.prompt.md` | `Messer`, `MusicBot` | Duplicate/variant | `evaluate-technology-options`; comparative evaluation is covered. |
| `.github/prompts/tests-gap-analysis.prompt.md` | `Messer`, `MusicBot` | Duplicate/variant | `analyze-test-gaps`; test inventory, risk gaps, and evidence-based recommendations are covered. |
| `.github/prompts/update-application-c4-diagrams.md` | `Messer`, `MusicBot` | Duplicate/variant | `update-application-c4-diagrams`; current-state diagrams are evidence-based. |
| `.github/prompts/validate-and-improve-instructions.prompt.md` | `Messer` | Duplicate/variant | `validate-and-improve-instructions`; bounded instruction validation and approved remediation are covered. |
| `.github/prompts/vue-3.4-migration-tests.prompt.md` | `Messer` | Duplicate/variant | `vue-migration-test-coverage`; behavior-focused Vue migration regression testing is covered. |

## `.github/prompts/academia-implementation/` (36)

| Path | Repository | Disposition | Coverage or evidence |
|---|---|---|---|
| `.github/prompts/academia-implementation/application-host-and-persistence-composition-implementation.prompt.md` | `zeus/zeus.academia.3b` | Reviewed | Project-specific application composition slice; reusable implementation is `implement-vertical-slice`. |
| `.github/prompts/academia-implementation/ep-0-1-shared-kernel-implementation.prompt.md` | `zeus/zeus.academia.3b` | Reviewed | Shared-kernel requirements are project-specific; `implement-vertical-slice` covers execution. |
| `.github/prompts/academia-implementation/ep-1-1-manage-ranks-implementation.prompt.md` | `zeus/zeus.academia.3b` | Reviewed | Slice-specific faculty/rank requirements; reusable domain capability is `academia-faculty-management`. |
| `.github/prompts/academia-implementation/ep-1-2-manage-degrees-implementation.prompt.md` | `zeus/zeus.academia.3b` | Reviewed | Slice-specific degree requirements; reusable domain capability is `academia-faculty-management`. |
| `.github/prompts/academia-implementation/ep-1-3-manage-universities-execution-map.md` | `zeus/zeus.academia.3b` | Supporting artifact | Slice execution/dependency map, not an assistant workflow. |
| `.github/prompts/academia-implementation/ep-1-3-manage-universities-implementation.prompt.md` | `zeus/zeus.academia.3b` | Reviewed | Slice-specific university requirements; `academia-faculty-management` covers the reusable domain. |
| `.github/prompts/academia-implementation/ep-1-4-provision-extension-execution-map.md` | `zeus/zeus.academia.3b` | Supporting artifact | Slice execution/dependency map, not an assistant workflow. |
| `.github/prompts/academia-implementation/ep-1-4-provision-extension-implementation.prompt.md` | `zeus/zeus.academia.3b` | Reviewed | Slice-specific extension requirements; `academia-faculty-management` covers the reusable domain. |
| `.github/prompts/academia-implementation/ep-2-1-register-academic-implementation.prompt.md` | `zeus/zeus.academia.3b` | Reviewed | Slice-specific registration requirements; `academia-faculty-management` and `implement-vertical-slice` cover reusable work. |
| `.github/prompts/academia-implementation/ep-3-1-view-academic-profile-implementation.prompt.md` | `zeus/zeus.academia.3b` | Reviewed | Slice-specific profile behavior; `academia-faculty-management` covers reusable domain work. |
| `.github/prompts/academia-implementation/ep-3-2-update-academic-name-implementation.prompt.md` | `zeus/zeus.academia.3b` | Reviewed | Slice-specific name-update requirements; `academia-faculty-management` covers reusable domain work. |
| `.github/prompts/academia-implementation/ep-3-3-search-list-academics-implementation.prompt.md` | `zeus/zeus.academia.3b` | Reviewed | Slice-specific search/list requirements; `academia-faculty-management` covers reusable domain work. |
| `.github/prompts/academia-implementation/ep-3-4-grant-tenure-implementation.prompt.md` | `zeus/zeus.academia.3b` | Reviewed | Slice-specific tenure requirements; `academia-faculty-management` covers reusable domain work. |
| `.github/prompts/academia-implementation/ep-3-5-assign-contract-implementation.prompt.md` | `zeus/zeus.academia.3b` | Reviewed | Slice-specific contract requirements; `academia-faculty-management` covers reusable domain work. |
| `.github/prompts/academia-implementation/ep-3-6-remove-employment-status-implementation.prompt.md` | `zeus/zeus.academia.3b` | Reviewed | Slice-specific employment-status requirements; `academia-faculty-management` covers reusable domain work. |
| `.github/prompts/academia-implementation/ep-3-7-change-rank-implementation.prompt.md` | `zeus/zeus.academia.3b` | Reviewed | Slice-specific rank-change requirements; `academia-faculty-management` covers reusable domain work. |
| `.github/prompts/academia-implementation/ep-3-8-record-degree-obtained-implementation.prompt.md` | `zeus/zeus.academia.3b` | Reviewed | Slice-specific degree requirements; `academia-faculty-management` covers reusable domain work. |
| `.github/prompts/academia-implementation/ep-3-9-assign-extension-implementation.prompt.md` | `zeus/zeus.academia.3b` | Reviewed | Slice-specific extension assignment requirements; `academia-faculty-management` covers reusable domain work. |
| `.github/prompts/academia-implementation/ep-4-1-renew-contract-implementation.prompt.md` | `zeus/zeus.academia.3b` | Reviewed | Slice-specific contract-renewal requirements; `academia-faculty-management` covers reusable domain work. |
| `.github/prompts/academia-implementation/ep-4-2-convert-contract-to-tenure-implementation.prompt.md` | `zeus/zeus.academia.3b` | Reviewed | Slice-specific tenure-conversion requirements; `academia-faculty-management` covers reusable domain work. |
| `.github/prompts/academia-implementation/ep-4-3-update-degree-university-implementation.prompt.md` | `zeus/zeus.academia.3b` | Reviewed | Slice-specific degree/university requirements; `academia-faculty-management` covers reusable domain work. |
| `.github/prompts/academia-implementation/ep-4-4-remove-degree-record-implementation.prompt.md` | `zeus/zeus.academia.3b` | Reviewed | Slice-specific degree-record requirements; `academia-faculty-management` covers reusable domain work. |
| `.github/prompts/academia-implementation/ep-4-5-list-qualifications-implementation.prompt.md` | `zeus/zeus.academia.3b` | Reviewed | Slice-specific qualification-list requirements; `academia-faculty-management` covers reusable domain work. |
| `.github/prompts/academia-implementation/ep-4-6-reassign-extension-implementation.prompt.md` | `zeus/zeus.academia.3b` | Reviewed | Slice-specific extension reassignment requirements; `academia-faculty-management` covers reusable domain work. |
| `.github/prompts/academia-implementation/ep-4-7-release-extension-implementation.prompt.md` | `zeus/zeus.academia.3b` | Reviewed | Slice-specific extension release requirements; `academia-faculty-management` covers reusable domain work. |
| `.github/prompts/academia-implementation/ep-4-8-list-available-extensions-implementation.prompt.md` | `zeus/zeus.academia.3b` | Reviewed | Slice-specific extension query requirements; `academia-faculty-management` covers reusable domain work. |
| `.github/prompts/academia-implementation/ep-5-1-deregister-academic-implementation.prompt.md` | `zeus/zeus.academia.3b` | Reviewed | Slice-specific deregistration requirements; `academia-faculty-management` covers reusable domain work. |
| `.github/prompts/academia-implementation/ep-6-1-academic-directory-implementation.prompt.md` | `zeus/zeus.academia.3b` | Reviewed | Slice-specific directory report; reusable reporting capability is `academia-reporting-analytics`. |
| `.github/prompts/academia-implementation/ep-6-2-by-rank-report-implementation.prompt.md` | `zeus/zeus.academia.3b` | Reviewed | Slice-specific rank report; reusable reporting capability is `academia-reporting-analytics`. |
| `.github/prompts/academia-implementation/ep-6-3-by-access-level-report-implementation.prompt.md` | `zeus/zeus.academia.3b` | Reviewed | Slice-specific access-level report; reusable reporting capability is `academia-reporting-analytics`. |
| `.github/prompts/academia-implementation/ep-6-4-tenured-academics-report-implementation.prompt.md` | `zeus/zeus.academia.3b` | Reviewed | Slice-specific tenure report; reusable reporting capability is `academia-reporting-analytics`. |
| `.github/prompts/academia-implementation/ep-6-5-contracted-academics-report-implementation.prompt.md` | `zeus/zeus.academia.3b` | Reviewed | Slice-specific contract report; reusable reporting capability is `academia-reporting-analytics`. |
| `.github/prompts/academia-implementation/ep-6-6-expiring-contracts-report-implementation.prompt.md` | `zeus/zeus.academia.3b` | Reviewed | Slice-specific expiring-contract report; reusable reporting capability is `academia-reporting-analytics`. |
| `.github/prompts/academia-implementation/ep-6-7-qualification-reports-implementation.prompt.md` | `zeus/zeus.academia.3b` | Reviewed | Slice-specific qualification reports; reusable reporting capability is `academia-reporting-analytics`. |
| `.github/prompts/academia-implementation/ep-6-8-access-level-distribution-report-implementation.prompt.md` | `zeus/zeus.academia.3b` | Reviewed | Slice-specific access distribution report; reusable reporting capability is `academia-reporting-analytics`. |
| `.github/prompts/academia-implementation/README.md` | `zeus/zeus.academia.3b` | Supporting artifact | Index for the 33 slice prompts and two execution maps; not a standalone workflow. |

## `.github/prompts/meta/` (1)

| Path | Repository | Disposition | Coverage or evidence |
|---|---|---|---|
| `.github/prompts/meta/create-technology-instructions.instructions.prompt.md` | `AIASD/AIASD-Brownfield-Example` | Duplicate/variant | Variant of `generate-instructions`; repository-specific technology rules require evidence. |

## Review result

All 138 inventory paths have a disposition. No entry is marked **Needs skill coverage**:
the reusable workflows map to existing skills, available generic PR review capability,
or are too repository-specific to justify promotion. The only substantial copy
divergence is recorded in the context-analysis, AI-output-policy, prompt-index, and
refactor-analysis entries above. This is a migration review, not authorization to copy
or distribute legacy prompts.
