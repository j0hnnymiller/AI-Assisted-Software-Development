# Chat Summary

- Chat ID: ae2e29d6-183f-4dde-8453-6726cf6c42cd
- Date: 2026-11-12
- Operator: johnmillerATcodemag-com
- Model: unknown/unknown@unknown
- Duration: 00:04:05

## Objective

Create reusable guidance that makes human-facing communications and documentation easier to read.

## Completed

- `.github/instructions/human-facing-writing.instructions.md` - Added audience-aware writing, ASD-STE100-style clarity, one thought per sentence, concise code-documentation, and editing rules for obsolete history.
- `.github/instructions/ai-assisted-output.instructions.md` - Added a cross-reference to the new writing guidance.
- `.github/instructions/README.md` and `README.md` - Indexed the new instruction and linked its chat log.
- `conversation.md` - Recorded the request, refinement, and implementation outcome.

## Key decisions

- Keep writing standards in a separate instruction from provenance and logging rules.
- Preserve historical material only when needed for audit, compliance, provenance, or the document's stated purpose.
- Use `applyTo: "**/*"` because the guidance can apply to human-facing content across formats; limit its application in the instruction to prose and relevant code documentation.

## Next steps

- None.
