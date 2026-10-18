---
name: transfer-blog-publication
description: "Create a publication-format blog copy or restore a publication copy while preserving its source"
argument-hint: "Direction, source path, and confirmed transformation rules"
ai_generated: true
model: "unknown/unknown@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
prompt: |
  files in the .github/prompts folder should be campared with the canonical skills. If a skill does not exist for the prompt, create a new skill. Prompt files are being deprecated. update the instructions, skills, and agents, responsible for syncing .github files.
started: "2026-10-18T09:55:12.922-07:00"
ended: "2026-10-18T10:05:54.310-07:00"
task_durations:
  - task: "Prompt-gap review and publication-transfer skill authoring"
    duration: "00:10:41"
total_duration: "00:10:41"
ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
source: "ai-practitioner/ai-practitioner-blog/.github/prompts/prepare-code-publication.prompt.md, restore-blog-publication.prompt.md, and movePost.prompt.md (spoke migration inputs)"
revisions:
  - chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
    model: "unknown/unknown@unknown"
    date: "2026-10-18"
    change: "Added confirmed custom filename and media-asset copy handling for publication migrations; mapped the legacy movePost workflow to this skill."
    ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
---

# Transfer Blog Publication Format

Create a transformed copy of a blog post for a publication workflow or restore a
publication copy to its source-blog format. This skill changes only explicitly declared
metadata and content patterns; it does not edit the source file.

## Required Inputs

- Direction: `prepare-for-publication` or `restore-source-format`.
- Source file or explicitly approved batch of files.
- Destination directory and filename rule, including any confirmed date/slug metadata.
- Confirmed URL, email, image, heading, and metadata transformation rules for the
  repository and direction.
- If media assets are part of the request: confirmed source and destination asset roots,
  filename/path transformations, alt-text or caption rules, and copy/overwrite behavior.

Do not infer or silently resolve a transformation value from an old prompt, example, or
another repository. The legacy preparation and restoration prompts disagree on the
publication contact email; require the user or an authoritative repository source to
confirm the correct target before changing contact information.

## Procedure

1. Inspect the source, its front matter, heading structure, and candidate transformation
   matches. Show the source and destination paths and a concise transformation preview.
2. Preserve the original file. Make a copy in the approved destination using the
   confirmed filename rule; this may retain the original filename, add a confirmed
   suffix, or use supplied date/slug metadata. For restoration, append `-CODE` before
   the extension only when that naming rule is confirmed.
3. Apply only the confirmed replacements. Preserve URL paths, anchors, query strings,
   code blocks, tables, lists, and unrelated prose. Preserve front matter unless specific
   fields to add or change are confirmed. Convert image syntax only when the exact source
   pattern and target representation are supplied. Do not invent a reverse image
   conversion that is absent from the rules.
4. For a confirmed publication-preparation rule, remove only the designated main H1 from
   the body; for a confirmed restoration rule, add it only when absent and when its exact
   text is available from the source or approved metadata.
5. Copy media assets only when explicitly included in the approved scope. Verify the
   source assets exist, apply only confirmed path/name rules, and report missing assets
   or destination collisions. Do not copy unrelated files.
6. Do not overwrite an existing destination, alter repository-wide contact information,
   or process additional files without explicit approval. If the transformation could
   affect code samples or unrelated text, narrow it to the confirmed pattern and report
   ambiguous matches.
7. Validate front matter, expected replacement counts, filename, asset references, and
   content integrity. Review the diff against the source. Test link syntax and local
   references; do not claim remote links work unless they were actually checked.
8. Report the source and output paths, replacement counts by rule, heading changes,
   validation results, and any skipped or ambiguous matches. Preserve file timestamps or
   permissions only when the available copy operation can verify that behavior; otherwise
   report the limitation.

## Boundaries

- Do not publish, upload, email, commit, or otherwise distribute the transformed copy.
- Do not alter the original post.
- Do not guess contact details, target URLs, asset paths, front-matter fields, or H1 text.
- Treat destination collisions as an approval gate; never silently choose an overwrite or
  alternate filename.

## Acceptance Criteria

- [ ] Direction, source, destination, filename rule, and every transformation rule were
      confirmed.
- [ ] The source remains unchanged and the output is a separate copy.
- [ ] Only declared patterns changed; preserved content was checked against the source.
- [ ] Contact-email conflicts and ambiguous transformations were resolved before writing.
- [ ] Output path, filename, front matter, and transformation counts were validated.
- [ ] Any explicitly requested media assets were copied using the confirmed mappings and
      references were checked.
- [ ] No publication or external write occurred.
