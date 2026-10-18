# Chat Summary

- Chat ID: c16f927f-91c4-4a30-aada-8f74b099e547
- Date: 2026-10-18
- Operator: johnmillerATcodemag-com
- Model: unknown/unknown@unknown
- Duration: 00:03:14 (active work across two updates)

## Objective

Prioritize and establish one canonical Marp review workflow that supports the three review modes identified during the cross-repository skill review.
Extend the existing transcript summarizer with VTI training-index hierarchy and duration-marker support.

## Completed

- `.github/skills/review-marp-course-materials/SKILL.md` - Added unified evidence-based review guidance for one source deck, one course manifest, and related multi-manifest sequences.
- `README.md` - Added the canonical review skill to the Agent Skills overview.
- `.github/skills/summarize-transcript-content/SKILL.md` - Added VTI detection, hierarchy preservation, explicit duration parsing, missing/conflicting timing handling, and non-overlapping statistics without removing VTT or response aggregation.
- `README.md` - Documented VTI support in the existing summarizer.

## Key decisions

- The three modes share review and evidence standards but retain distinct validation scopes, report destinations, and report contents.
- Source files remain read-only unless the user explicitly requests changes.
- Fixed exercise-count and duration requirements are not generalized; apply them only when supplied requirements or repository policy require them.
- VTI indices retain source structure; no universal VTI schema or invented timeline is assumed.
- Source duration uses `source_duration`, separate from provenance `total_duration`. Parent/child times are not double-counted; incomplete coverage yields a labeled subtotal.

## Validation

- Summarizer YAML, discovery metadata, folder/name agreement, provenance-policy link, retained VTT/aggregation sections, and whitespace checks passed.
- Repository VTI sample arithmetic verified: five top-level sections total 45:00, average 9:00, longest 12:15, shortest 4:10; timed subsection sums match parents.
- No automated VTI parser or end-to-end summarization was executed; this is a skill documentation update.

## Next steps

- Use the skill to conduct a Marp review when requested.
