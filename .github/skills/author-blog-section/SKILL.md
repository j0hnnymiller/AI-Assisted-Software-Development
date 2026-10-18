---
name: author-blog-section
description: "Draft or revise a focused technical blog section from supplied sources while preserving the author's style, factual accuracy, and requested edit boundaries."
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
source: "ai-practitioner-blog/.github/prompts/create-blog-section.prompt.md"
revisions:
  - chat_id: "skill-naming-convention-20261018"
    model: "unknown/unknown@unknown"
    date: "2026-10-18"
    change: "Applied approved skill naming decisions and updated active references; preserved workflow behavior and historical provenance."
    ai_log: "ai-logs/2026/10/18/skill-naming-convention-20261018/conversation.md"
---

# Technical Blog Section Authoring

Use this skill when asked to create or revise one bounded section of a technical blog post.

## Inputs

- Section purpose, audience, surrounding text, source material, style guidance, and permitted edit scope.
- Identify unsupported claims and source gaps before drafting.

## Procedure

1. Read the section and adjacent context to preserve terminology, voice, and narrative flow.
2. Extract claims and supporting evidence from supplied or approved sources; distinguish facts, interpretation, and opinion.
3. Draft only within the requested section boundary. Preserve citations, code, links, and technical meaning unless asked to change them.
4. Check clarity, sequence, examples, and consistency with surrounding content. Verify links and code examples when tools and source are available.
5. Report material assumptions, unresolved factual questions, and any edits outside the requested scope.

## Output

Return the revised section or apply a narrow edit when explicitly requested. Summarize sources used and identify claims requiring author verification.

## Guardrails

- Do not fabricate quotations, citations, research, benchmarks, or author experience.
- Do not rewrite unrelated sections or change the author's meaning.
- Avoid generic filler, repetition, vague claims, and canned conclusions.
