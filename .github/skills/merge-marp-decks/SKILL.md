---
name: merge-marp-decks
description: "Merge Marp slide decks into a single combined presentation, optionally driven by a manifest YAML file"
argument-hint: "Manifest YAML path; leave blank to discover source decks"
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
---
# Merge Marp Slide Decks

Merge Marp slide decks according to a manifest file into a single combined presentation.

## Usage

Invoke the skill with a manifest path:

```text
/merge-marp-decks
Manifest: slides/aiasd-311-tuesday.yaml
```

Omit the `Manifest:` line to use the fallback source discovery.

## Manifest File Format

The manifest YAML file controls all inputs and the output path. It must follow this schema:

```yaml
title: "Combined deck title"
output: "slides/marp/output-filename.deck.md"   # path to write the merged deck
theme: default                         # Marp theme (default: default)
paginate: true                         # Marp paginate (default: true)
sources:
  - file: "path/to/source.md"         # existing Marp slide file OR instruction file
    topic: "Section topic label"       # used on the section divider slide
```

When the skill invocation includes a manifest path, read that file to obtain the
`title`, `output`, `theme`, `paginate`, and `sources` list.

If no manifest is provided, fall back to discovering all `*.md` files in
`slides/marp/` that contain `marp: true` in their front matter and
write the output to `slides/marp/ai-assisted-dev-overview.deck.md`.

## Instructions

- Instructions for Marp slides: `.github/instructions/marp-slides.instructions.md`
- Provenance policy: `.github/instructions/ai-assisted-output.instructions.md`

## Steps

0. **Read manifest**: If a manifest path was provided with the skill invocation, read that YAML
   file and extract `title`, `output`, `theme`, `paginate`, and `sources`.
   Otherwise use the fallback defaults described above.

1. **Discover sources**: Collect the list of source files from the manifest `sources` field
   (or from `slides/marp/*.deck.md` in fallback mode). For each source entry, note
   the `file` path and `topic` label.

2. **Read each source file**: Read its content. If it is a Marp slide file (contains
   `marp: true` in front matter), strip the YAML front matter block and keep only the slide
   content. If it is an instruction file, convert its content into Marp slides following
   `.github/instructions/marp-slides.instructions.md`.

3. **Assemble the combined deck**:
   - Build a YAML front matter block with `marp: true`, `theme`, `paginate`, and full AI
     provenance fields (see provenance policy).
   - Add a title slide using the manifest `title` (or a sensible default).
   - For each source, insert a `---` section divider slide with the `topic` as a heading,
     then append that source's slide content.

4. **Determine the output path** from the manifest `output` field (or the fallback
   `slides/marp/ai-assisted-dev-overview.deck.md`).

5. **Write the output file** — **IMPORTANT: check file existence first**:
   - Use a file-read tool to check whether the output path already exists in the repository.
   - **If the file exists**: use `edit` (or an update/replace operation) to overwrite its
     content. Do **not** use `create` on an existing file.
   - **If the file does not exist**: use `create` to create it.

6. **Create ai-logs**: Write `ai-logs/<yyyy>/<mm>/<dd>/<chat-id>/conversation.md` and
   `summary.md`. Apply the same exist-check rule: edit if present, create if absent.

7. **Update README.md**: Add or update an entry for the new combined slide deck.
   Check README.md for an existing entry for the output file; update it in place rather
   than appending a duplicate.

## Output Requirements

- Every slide in the combined deck must have speaker notes using pandoc `:::notes` syntax.
- The file must include complete AI provenance YAML front matter.

## Acceptance Criteria

- [ ] Manifest file (if provided) was read and used for configuration.
- [ ] All sources listed in the manifest (or discovered fallback) are represented.
- [ ] Section divider slides separate each source deck.
- [ ] Every slide has speaker notes.
- [ ] Combined file has valid Marp front matter.
- [ ] AI provenance metadata is complete.
- [ ] Output file was edited (not re-created) if it already existed.
- [ ] README updated with new or corrected entry — no duplicates added.

## Changelog

- **1.1.0** — Added `manifest` argument and manifest-driven workflow; added explicit file-existence
  check (edit vs. create) to fix cloud Copilot overwrite bug; retained fallback discovery mode.
- **1.0.0** — Initial version: discover `slides/marp/*.deck.md` and write to
  `slides/marp/ai-assisted-dev-overview.deck.md`.



