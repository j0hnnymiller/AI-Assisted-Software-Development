---
name: convert-mermaid-markdown-to-docx
description: "Convert Markdown containing Mermaid diagrams into a template-based DOCX and verify that diagrams, styles, links, and document structure render correctly."
ai_generated: true
model: "unknown/unknown@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
prompt: |
  Merge useful gaps and create proposed new skills
started: "2026-10-17T19:33:05.9169653-07:00"
ended: "2026-10-17T19:52:32.094572-07:00"
task_durations:
  - task: "Approved cross-repository prompt-to-skill migration"
    duration: "00:19:26"
total_duration: "00:19:26"
ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
source: "Messer/.github/prompts/convert-mermaid-markdown-to-templated-docx.prompt.md"
revisions:
  - chat_id: "skill-naming-convention-20261018"
    model: "unknown/unknown@unknown"
    date: "2026-10-18"
    change: "Applied approved skill naming decisions and updated active references; preserved workflow behavior and historical provenance."
    ai_log: "ai-logs/2026/10/18/skill-naming-convention-20261018/conversation.md"
---

# Mermaid Markdown to Template-Based DOCX

Use this workflow when a user asks to render Markdown and Mermaid content into an existing Word template or a requested DOCX format.

## Inputs and Preconditions

- Source Markdown, referenced assets, target DOCX template, output path, and required rendering tools.
- Preserve source files. Confirm overwrite behavior before replacing an existing output.

## Procedure

1. Inspect the Markdown, Mermaid blocks, relative assets, headings, tables, links, and template styles.
2. Check that required local converters/renderers are installed. If a dependency is missing, report it rather than silently substituting an unverified renderer.
3. Render Mermaid diagrams using a supported renderer; validate syntax and keep a mapping from source blocks to rendered assets.
4. Convert content into the supplied template, preserving heading hierarchy, tables, captions, links, and diagram order.
5. Inspect the DOCX package and render pages when tooling allows. Check for missing diagrams, broken images, overflow, blank pages, and style drift.
6. Compare the output against source sections and report any unsupported elements or transformations.

## Output

Provide the DOCX at the approved path, retain or identify generated diagram assets as appropriate, and summarize conversion checks and limitations.

## Guardrails

- Do not overwrite source files or an existing DOCX without approval.
- Do not include hidden metadata or unrelated template content.
- Do not claim visual verification if the document was not rendered and inspected.
- Keep generated assets within the requested output scope and avoid temporary-file leakage.
