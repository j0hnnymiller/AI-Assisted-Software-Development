---
name: build-course-slide-deck
description: "Build merged course-slide Markdown and an editable PPTX from a sections/decks manifest"
argument-hint: "Path to a repository course manifest"
ai_generated: true
model: "unknown/unknown@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
prompt: |
  go ahead with the recommendations
started: "2026-10-18T09:49:31.896-07:00"
ended: "2026-10-18T09:52:53.680-07:00"
task_durations:
  - task: "Course slide pipeline skill authoring"
    duration: "00:03:21"
total_duration: "00:03:21"
ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
source: "User approval and the repository's slide manifests and scripts"
---

# Build Course Slide Deck

Build the repository's merged Marp Markdown and editable PowerPoint outputs from a
course manifest. Run from the repository root and use the checked-in scripts; do not
manually recreate their merge or rendering logic.

## Usage

```text
/build-course-slide-deck
Manifest: slides/manifests/aiasd-311-monday.manifest.md
```

The manifest is raw YAML despite its `.md` extension. This course workflow uses the
`sections`/`decks` schema. For a standalone Marp `sources` manifest or explicit source
discovery, use the Course repository's standalone merge workflow.

The pipeline scripts and instructions are Course-repository dependencies, not hub
assets. Before execution, verify that the consuming repository provides
`.github/scripts/phase1_merge_marp_decks.py` and `.github/scripts/generate_pptx.py`.
If either is absent, stop and report the missing prerequisite; do not recreate or
import Course-specific scripts into the hub.

## Manifest Contract

```yaml
template: slides\jMM-CODE-Training-Slide-Template-clean.pptx
title: "AI-Assisted Software Development"
subtitle: "From Code to Copilot"
sections:
  - name: Intro
    decks:
      - slides\marp\welcome-to-aiasd.deck.md
  - name: Module 1
    decks:
      - slides\marp\topic.deck.md
```

- `sections` must be a non-empty list. Each section needs a non-empty `name`; `decks`
  may be omitted or empty.
- Deck entries must be repository-relative Markdown path strings (`.md` or `.markdown`).
  Every listed source must exist.
- `template`, `title`, and `subtitle` are optional. Verify the template exists when set.
- Do not use object deck entries. The PPTX generator accepts some object forms, but the
  Phase 1 merger does not. Layout selection belongs in source Markdown, not the manifest.
- Report malformed entries and missing sources as input failures; do not edit manifests
  or source slides as part of this output-only build.

## Workflow

1. **Validate before writing outputs.** Parse the manifest as YAML. Check the section
   structure, string deck paths, extensions, source existence, template path, and Marp
   source structure. Inspect every source slide's `:::notes` block: the pipeline
   instructions require at least 3-4 substantive sentences of delivery notes per slide.
   Do not invent or silently insert notes; report gaps for source-author follow-up.
   The generator also leaves template-provided cover and agenda slides in place and does
   not add notes to them. Verify their notes in the source template as well. Do not claim
   a conforming build when any source or template slide fails the notes requirement.
2. **Generate Phase 1 merged Markdown** from the repository root:

   ```powershell
   python .github\scripts\phase1_merge_marp_decks.py <manifest-path>
   ```

   The script derives `slides/merged/<manifest-stem>-draft.md`, preserving any
   subdirectory below `slides/manifests/`, and overwrites that generated output. It merges
   source files in section order, preserves the first available source front matter, and
   injects module-list slides before sections after the first.
3. **Generate the Phase 2 PPTX** from the same manifest and original sources:

   ```powershell
   python .github\scripts\generate_pptx.py <manifest-path> <pptx-output-path>
   ```

   Use `slides/output/<manifest-stem>-draft.pptx`, preserving manifest subdirectories.
   Phase 2 reads the manifest and source Markdown directly; it does not consume the
   Phase 1 merged file. The generator fills title/agenda placeholders when available,
   adds module-list slides after the first section, and creates named PowerPoint sections.
   It appends source paths to notes, but does not generate or validate substantive note
   content.
4. **Finalize when supported.** On Windows with PowerPoint installed, check for a
   `~$<filename>.pptx` lock file beside the output. If unlocked, run:

   ```powershell
   pwsh -File .github\scripts\finalize_pptx_local.ps1 -Path "<pptx-output-path>"
   ```

   If PowerPoint, the finalizer, or an unlocked output is unavailable, report the reason
   and state that finalization did not complete.
5. **Verify and report.** Confirm both generated files exist, report script warnings,
   verify PPTX section ordering and speaker notes, and identify note-quality gaps. Do not
   claim that Phase 2 was generated from the merged Markdown or that finalization succeeded
   unless verified.

## Acceptance Criteria

- [ ] The supported manifest and all source inputs were validated without modification.
- [ ] Phase 1 generated the derived merged Markdown.
- [ ] Phase 2 generated the derived PPTX from the same manifest and original source files.
- [ ] First-section behavior, subsequent navigation slides, and PowerPoint section grouping
      are preserved.
- [ ] Speaker-note presence and the substantive source-note requirement were verified;
      any gaps are reported.
- [ ] Finalization status and all warnings are reported accurately.
