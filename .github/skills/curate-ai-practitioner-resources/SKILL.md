---
name: curate-ai-practitioner-resources
description: "Research and curate an evidence-backed catalog of resources about risks and practices in AI-assisted software development, using a supplied schema and scoring rubric."
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
source: "ai-practitioner-resources/.github/prompts/ai-practitioner-resources-json.prompt.md"
revisions:
  - chat_id: "skill-naming-convention-20261018"
    model: "unknown/unknown@unknown"
    date: "2026-10-18"
    change: "Applied approved skill naming decisions and updated active references; preserved workflow behavior and historical provenance."
    ai_log: "ai-logs/2026/10/18/skill-naming-convention-20261018/conversation.md"
---

# AI Practitioner Resource Catalog

Use this skill to create or update a structured catalog of books, articles, reports, blogs, podcasts, or other resources about AI-assisted software development.

## Procedure

1. Confirm the audience, catalog scope, allowed source types, date/freshness requirements, output schema, and scoring rubric.
2. Define risk/practice categories from supplied requirements. Do not invent a canonical taxonomy when none is provided.
3. Research from approved, authoritative sources. Record title, publisher/author, publication date, stable URL, access date, and evidence for each entry.
4. Assess relevance, credibility, recency, and usefulness using the supplied scale. Explain scores and flag uncertainty.
5. Deduplicate entries, validate links and schema, and distinguish primary sources from commentary.
6. Compare additions with the existing catalog; update only requested fields and preserve valid entries.
7. Summarize coverage gaps, outdated material, and items needing human review.

## Output

Return valid JSON or the requested format. Validate required fields, types, enums, escaping, URLs, and cross-entry consistency. Include a concise change summary separately when permitted.

## Guardrails

- Never fabricate a publication, author, quote, date, URL, or score rationale.
- Do not scrape or reproduce copyrighted content beyond brief factual descriptions.
- Do not treat a resource's presence in the catalog as endorsement or proof.
- If the schema or scoring rules are missing, request them rather than improvising a replacement contract.
