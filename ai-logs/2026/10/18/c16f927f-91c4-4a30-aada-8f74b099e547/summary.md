# Chat Summary

- Chat ID: c16f927f-91c4-4a30-aada-8f74b099e547
- Date: 2026-10-18
- Operator: johnmillerATcodemag-com
- Model: unknown/unknown@unknown
- Duration: 00:01:43

## Objective

Prioritize and establish one canonical Marp review workflow that supports the three review modes identified during the cross-repository skill review.

## Completed

- `.github/skills/review-marp-course-materials/SKILL.md` - Added unified evidence-based review guidance for one source deck, one course manifest, and related multi-manifest sequences.
- `README.md` - Added the canonical review skill to the Agent Skills overview.

## Key decisions

- The three modes share review and evidence standards but retain distinct validation scopes, report destinations, and report contents.
- Source files remain read-only unless the user explicitly requests changes.
- Fixed exercise-count and duration requirements are not generalized; apply them only when supplied requirements or repository policy require them.

## Next steps

- Use the skill to conduct a Marp review when requested.
