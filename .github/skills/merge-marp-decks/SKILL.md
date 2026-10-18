---
name: merge-marp-decks
description: "Merge standalone Marp decks using a sources manifest or explicit source discovery"
argument-hint: "Optional sources-manifest path"
ai_generated: true
model: "OpenAI/GPT-6@Luna"
operator: "johnmillerATcodemag-com"
chat_id: "convert-prompt-files-to-skills-20261016"
prompt: |
  help me convert the prompt files in the prompts folder into skills.
started: "2026-10-16T21:25:07.811Z"
ended: "2026-10-16T21:43:11.234Z"
task_durations:
  - task: "Converting repository prompt files to skills"
    duration: "00:18:03"
total_duration: "00:18:03"
ai_log: "ai-logs/2026/10/16/convert-prompt-files-to-skills-20261016/conversation.md"
source: ".github/prompts/merge-marp-decks.prompt.md"
revisions:
  - chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
    model: "unknown/unknown@unknown"
    date: "2026-10-18"
    change: "Separated the repository-specific course manifest/PPTX workflow into build-course-slide-deck."
    ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
---

# Merge Marp Decks

Create a standalone combined Marp Markdown deck from a `sources` manifest or an explicit
discovery request. This workflow does not produce a PPTX. For this repository's
`sections`/`decks` course manifests and PPTX pipeline, use
`.github/skills/build-course-slide-deck/SKILL.md`.

## Usage

```text
/merge-marp-decks
Manifest: path/to/standalone-sources.manifest.yaml
```

If no manifest is supplied, use the fallback discovery behavior only when the user
explicitly requests it. Do not confuse this format with the course pipeline's
`sections`/`decks` format.

For that explicit fallback, discover `*.md` files in `slides/marp/` with `marp: true`
in front matter and write `slides/marp/ai-assisted-dev-overview.deck.md`.

## Manifest Format

```yaml
title: "Combined deck title"
output: "slides/marp/output-filename.deck.md"
theme: default
paginate: true
sources:
  - file: "path/to/source.md"
    topic: "Section topic label"
```

Read `title`, `output`, `theme`, `paginate`, and `sources` from the manifest. Each source
must be an existing Marp slide file or an instruction file that can be converted using
`.github/instructions/marp-slides.instructions.md`.

## Workflow

1. Read and validate the manifest. If none was supplied, only discover source files after
   the user explicitly requests fallback discovery; do not silently include every deck.
2. Read each source. For Marp decks, remove source front matter and preserve slide content.
   For instruction files, create slides following
   `.github/instructions/marp-slides.instructions.md`.
3. Assemble a new Marp deck with `marp: true`, manifest theme and pagination values, and
   complete provenance metadata required by
   `.github/instructions/ai-assisted-output.instructions.md`.
4. Add a title slide from `title`, then a divider using each source's `topic` before its
   content. Preserve source order.
5. Every slide must include substantive presenter notes using `:::notes` syntax. Do not
   fabricate speaker guidance; flag source content that needs clarification.
6. Write to the manifest's `output` path, or the fallback
   `slides/marp/ai-assisted-dev-overview.deck.md`. Check the target first and overwrite
   existing output rather than creating a duplicate.
7. Create or update the chat's `conversation.md` and `summary.md`, then update README for
   a durable deck. Do not edit source decks.

## Acceptance Criteria

- [ ] The standalone `sources` manifest or explicitly requested discovery set was validated.
- [ ] All sources appear in manifest order with topic divider slides.
- [ ] Every slide has substantive presenter notes.
- [ ] The combined deck has valid Marp front matter and complete provenance.
- [ ] Existing generated output is replaced; sources remain unchanged.
- [ ] Required chat logs and README entry are present and links resolve.
