---
name: review-marp-course-materials
description: "Review Marp source decks, one course manifest, or a related multi-manifest sequence for evidence-based instructional, structural, accessibility, traceability, and delivery risks. Use when asked to review a slide deck, validate course flow, or assess a multi-day Marp course."
argument-hint: "Deck: <path> | Manifest: <path> | Manifests: <paths>"
ai_generated: true
model: "unknown/unknown@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "c16f927f-91c4-4a30-aada-8f74b099e547"
prompt: |
  Prioritize a canonical Marp review workflow covering the three review modes.
started: "2026-10-18T12:35:07.776-07:00"
ended: "2026-10-18T12:36:51.715-07:00"
task_durations:
  - task: "Workflow design and repository integration"
    duration: "00:01:43"
total_duration: "00:01:43"
ai_log: "ai-logs/2026/10/18/c16f927f-91c4-4a30-aada-8f74b099e547/conversation.md"
source: "user request"
---

# Review Marp Course Materials

Use one workflow with three explicit modes. Select a mode from the supplied input; do not guess which deck or manifest the user intends.

## Modes and inputs

1. **Source-deck review**: require one existing source deck under `slides/marp/`. Optionally accept explicit related manifest(s) for sequence context. Never treat generated files under `slides/merged/` or `slides/output/` as source decks.
2. **Single-manifest review**: require one existing course manifest and review its ordered source decks as one course unit.
3. **Related multi-manifest review**: require multiple unique manifests, a stable review-set identifier, and evidence they belong to one course sequence. Review each manifest independently and assess the combined progression. If relationship or grouping is unclear, ask rather than assume.

Resolve paths from the repository root. Read the repository's current Marp, manifest, and slide-pipeline guidance and inspect the applicable manifest schema and validation tools before relying on them. Do not assume a manifest schema, validator path, or output behavior from another repository. Stop for missing, malformed, duplicate, ambiguous, or out-of-scope inputs.

## Review procedure

1. Read each source deck in full, including front matter, slide order, diagrams, code, links, image references, and speaker notes. For manifest modes, read all referenced decks. For deck mode with manifest context, inspect the relevant section and adjacent decks.
2. Validate manifest structure and paths against the current repository's schema and implementation. Check required fields, supported deck-entry shapes, path existence and extensions, duplicates after separator normalization, likely case-insensitive collisions, unresolved variables, and empty sections where applicable.
3. Run the narrowest available source validator for each explicit deck or manifest. If no suitable validator exists, state that validation was unavailable; do not create a new validator or run merge/PPTX generation as a substitute. Record exact commands and results.
4. Assess relevant dimensions using the supplied objectives, audience, course documents, repository conventions, and source evidence:
   - factual accuracy and currency;
   - completeness and instructional quality;
   - narrative, prerequisites, transitions, progression, repetition, and coverage;
   - accessibility and delivery;
   - Marp/PPTX source risks, including front matter, separators, notes, syntax, variables, assets, diagrams, and layout;
   - traceability and consistency between manifest and source decks.
5. In manifest reviews, compare deck purpose and sequence using content, not filenames alone. In multi-manifest mode, retain separate validation evidence and per-manifest findings; assess cross-day progression only where the sequence relationship is evidenced.
6. Check change-sensitive claims against authoritative current sources when available; cite the source and access date. Do not claim currentness from memory or search snippets. Separate confirmed defects, likely risks, recommendations, and open questions. Ground omissions in stated objectives, prerequisites, dependencies, learner actions, or explicit course intent.
7. Include exercise alignment or slide/deck timing only when requested or required by the supplied objectives or repository policy. Estimate rather than present unmeasured timing as fact. Do not impose a fixed exercise count, duration, or course structure unless an applicable requirement explicitly sets it.
8. Produce one evidence-backed report for the selected mode. Use stable finding IDs, severity, confidence, location, evidence, impact, recommendation, and verification. State `None found` for reviewed dimensions without findings. Ask before overwriting an existing report.

## Report destinations and contents

- **Source-deck review**: `outlines/reviews/<deck-stem>-review.md`. Include executive summary and validation, findings, coverage/narrative assessment, Keep/Change/Add/Remove-or-Combine update proposal, validation plan, open questions, sources, and review limits.
- **Single-manifest review**: `outlines/reviews/<manifest-stem>-manifest-review.md`. Include executive summary, manifest validation, findings, cohesion/coverage and sequence recommendations, validation plan, open questions, sources, and review limits.
- **Related multi-manifest review**: `outlines/reviews/<review-set-id>-multi-day-marp-manifest-review.md`. Include per-manifest validation and findings, cross-day progression, combined recommendations, open questions, sources, and review limits.

If destinations collide or the intended report path is ambiguous, ask before writing. Include required AI provenance and follow repository logging and README requirements for durable artifacts.

## Boundaries

- Keep decks, manifests, images, scripts, and generated slide artifacts read-only during review.
- Apply source changes only when the user explicitly requests them; make only the approved changes and validate every changed source.
- Do not merge decks, generate PPTX, or run local PowerPoint finalization unless separately requested.
- Do not invent requirements, citations, learner context, or defects. Label unsupported concerns as questions or possible risks.
- Do not include secrets or private learner information in reports or logs.
