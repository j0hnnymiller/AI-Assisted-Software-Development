---
ai_generated: true
model: "anthropic/claude-sonnet-4-5@2025-02-19"
operator: "johnmillerATcodemag-com"
chat_id: "slide-pipeline-spec-20260313"
prompt: |
  create a specification for the marp slide merge and the marp deck conversion to a pptx
started: "2026-03-13T00:00:00Z"
ended: "2026-03-13T00:15:00Z"
task_durations:
  - task: "codebase exploration"
    duration: "00:05:00"
  - task: "specification authoring"
    duration: "00:10:00"
total_duration: "00:15:00"
ai_log: "ai-logs/2026/03/13/slide-pipeline-spec-20260313/conversation.md"
source: "johnmillerATcodemag-com"
applyTo: "Slides/**"
---

# Slide Pipeline Specification

This document specifies the authoring, assembling, and exporting of course slide decks
using the Copilot agent prompt pipeline.

The single pipeline entry point is `.github/copilot/Promptfiles/merge-marp-decks.prompt.md`, a
Copilot agent-mode prompt that reads the YAML manifest, merges individual slide files
into a single Marp deck, and generates an editable PPTX using python-pptx — all in one
AI-driven run.

**🔒 CRITICAL INVARIANTS**: Any modifications to `scripts/generate_pptx.py` MUST preserve:

1. **First Section Exception**: The first section (idx=0) MUST NOT receive injected slides (module list and agenda). These slides are only added for idx > 0.
2. **Slide Notes (MANDATORY)**: ALL slides (injected and content) MUST have comprehensive speaker notes:
   - **Injected slides**: Notes explaining they were auto-generated and their purpose
   - **Content slides**: Notes showing source file path AND speaker delivery guidance
   - **Every slide MUST have at least 3-4 sentences of speaker notes**
   - **Notes MUST include: delivery guidance, timing, key points, examples, and transitions**
   - **NO slides without speaker notes are acceptable**

**⚠️ REGRESSION PREVENTION**: When modifying `generate_pptx.py`:

- Always reference this specification
- Test with a manifest where first section has content slides
- Verify first section has NO injected slides in the output PPTX (no "Course Modules" or agenda)
- **VERIFY ALL slides (including injected) have comprehensive speaker notes in the output PPTX**
- **VERIFY speaker notes contain substantive delivery guidance (not just placeholders)**

---

## Table of Contents

1. [Repository layout](#1-repository-layout)
2. [YAML manifest](#2-yaml-manifest)
3. [Individual slide file rules](#3-individual-slide-file-rules)
4. [Merge phase — injected slides](#4-merge-phase--injected-slides)
   - 4.1 [Module list slide](#41-module-list-slide)
   - 4.2 [Section agenda slide](#42-section-agenda-slide)
5. [Merge phase — content slides](#5-merge-phase--content-slides)
6. [Merge phase — full slide order per section](#6-merge-phase--full-slide-order-per-section)
7. [PPTX generation phase](#7-pptx-generation-phase)
8. [Agent prompt invocation](#8-agent-prompt-invocation)
9. [File naming conventions](#9-file-naming-conventions)
10. [Constraints and known limitations](#10-constraints-and-known-limitations)
11. [Extension points](#11-extension-points)

---

## 1. Repository layout

```
Slides/
├── individual-slides/          # Atomic per-topic slide files (one topic per .md)
│   ├── images/                 # Images referenced by individual slides
│   └── *.md
├── images/                     # Images referenced by the merged deck
├── output/                     # Generated artefacts (PPTX)
└── <course>-<format>-<day>-draft.md   # Merged Marp output (e.g. aiasd-311-monday-draft.md)

.github/copilot/Promptfiles/
└── merge-marp-decks.prompt.md  # Pipeline entry point: Copilot agent prompt
```

---

## 2. YAML manifest

The manifest is the single source of truth for the entire pipeline. It lists all sections
in order, and within each section the ordered set of individual slide files to include.

### 2.1 Location and naming

```
Slides/<course>-<format>-<day>.yaml      e.g.  Slides/aiasd-311-monday.yaml
```

### 2.2 Format

```yaml
sections:
  - name: "Intro"
    slides:
      - Slides\individual-slides\welcome-to-aiasd.md
      - Slides\individual-slides\john-michael-miller-intro.md

  - name: "Module 1 - AIASD"
    slides:
      - Slides\individual-slides\whats-the-big-deal.md
      - Slides\individual-slides\the-ai-revolution.md

  - name: "Module 2 - Intro to Copilot"
    slides:
      - Slides\individual-slides\repository-and-tool-setup.md
```

### 2.3 Rules

- `name` is required and non-empty for every section.
- `slides` is an ordered list of repo-root-relative paths (Windows or POSIX separators accepted).
- Sections are processed in declaration order.
- A `slides:` list may be empty or absent; the section still produces a module list slide
  and an empty section grouping in the PPTX.
- All section names are used to build the module list that appears on every module list slide.
- **Exercise slides** (slides whose extracted title starts with `Exercise`, case-insensitive) may be
  included in the `slides` list and will be merged into the deck, but they are **excluded from the
  section agenda slide** — attendees discover exercises as they progress through the section rather
  than seeing them previewed up front.

---

## 3. Individual slide file rules

Each `.md` file under `Slides/individual-slides/` must conform to these rules.
The agent validates and reports violations, but does not abort — it logs a warning and
continues.

| Rule               | Requirement                                                                                                                                                                                                          |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Front matter       | Must begin with a valid Marp YAML front-matter block (`---` … `---`)                                                                                                                                                 |
| H1 headings        | No `# H1` headings in the body                                                                                                                                                                                       |
| Slide title        | Must contain at least one `## H2` heading in the body; the **first** `## H2` is used as the slide title for the section agenda slide (slides with titles starting with `Exercise` are excluded from the agenda list) |
| Image paths        | Use `images/` (not `../images/`); individual slide previews use `../images/` but the merged deck lives one level up                                                                                                  |
| Trailing separator | Must not end with a bare `---`                                                                                                                                                                                       |
| Encoding           | No vertical-tab (`\x0b`) characters                                                                                                                                                                                  |

---

## 4. Merge phase — injected slides

During the merge the agent inserts two auto-generated slides at the start of each
section, **before** any of that section's source content slides. They are produced
entirely from the manifest data and the source file titles — no content is invented.

**Exception**: For the **first section** in the manifest, **both injected
slides are suppressed** (module list and agenda). The first section starts
directly with the first source content slide. This prevents navigation-heavy opening
that would precede the welcome slide.

### 4.1 Module list slide

**One module list slide is inserted at the very start of every section.**

Its purpose is course-progress navigation: attendees can see all course modules at a
glance, and the module that is about to begin is visually highlighted.

#### Content

- **Title**: `Course Modules`
- **Body**: one bullet per section, in manifest order
  - The section whose content **immediately follows** this slide (i.e., the current section
    being introduced) is rendered as **`**▶ Section Name**`** (bold + arrow prefix)
  - All other sections are rendered as plain text: `Section Name`

#### Marp markdown template

```markdown
<!-- _class: lead -->

## Course Modules

- Section Name A
- **▶ Section Name B** ← this section (about to start)
- Section Name C
- Section Name D
```

#### Rules

- The arrow `▶` and bold markers are part of the Marp source; Marp renders bold text
  in the theme's accent colour or with heavier weight.
- Every section in the manifest is listed, including "Intro" and empty sections.
- Sections before the current one are plain (already covered).
- Sections after the current one are plain (upcoming).
- Only the section immediately being introduced is highlighted.

#### Example

Given a manifest with sections `Intro`, `Module 1 - AIASD`, `Module 2 - Intro to Copilot`,
the module list slide inserted before `Module 2 - Intro to Copilot` content looks like:

```markdown
<!-- _class: lead -->

## Course Modules

- Intro
- Module 1 - AIASD
- **▶ Module 2 - Intro to Copilot**
```

---

### 4.2 Section agenda slide

**One section agenda slide is inserted after the module list slide for every section
that has at least one source content slide.**

Its purpose is to preview the topics covered in the section so attendees know what's
coming before the content starts.

#### Slide title extraction

The agent extracts slide titles from source files as follows:

1. Strip the YAML front-matter block (`---` … `---`) from the file content.
2. Scan the remaining lines for the **first `## H2` heading**.
3. The text of that heading (without the `## ` prefix) is the slide title.
4. If no `## H2` heading is found, the file's stem (filename without extension) is used
   as a fallback title.

#### Content

- **Title**: same as the section name (rendered as a `##` heading to produce a
  Title-and-Content layout in the PPTX)
- **Body**: numbered or bulleted list of slide titles, one per source file in the order
  they appear in the manifest
  - **Exercise slides are excluded**: any slide whose extracted title starts with `Exercise`
    (case-insensitive) is skipped when building the agenda list. These slides are still merged
    into the deck in their manifest order, but attendees discover them naturally as they
    progress through the section rather than seeing them previewed in the agenda.

#### Marp markdown template

```markdown
## Section Name

- Slide Title From File 1
- Slide Title From File 2
- Slide Title From File 3
```

#### Example

For `Module 2 - Intro to Copilot` with two source files whose first `## H2` headings are
`Repository and Tool Setup` and `Hands-On with GitHub Copilot (VS Code)`:

```markdown
## Module 2 - Intro to Copilot

- Repository and Tool Setup
- Hands-On with GitHub Copilot (VS Code)
```

#### Example with Exercise slides

For `Module 3 - Vibbing` with source files:

- `vibe-coding.md` (title: "Vibe Coding")
- `exercise-calculator-project.md` (title: "Exercise: Calculator Project")
- `multi-model-implementation-comparison.md` (title: "Multi-Model Implementation Comparison")
- `any-filename.md` (title: "Exercise: Test Coverage Improvement")

The section agenda slide shows only the non-exercise slides (slides whose title does not start with "Exercise"):

```markdown
## Module 3 - Vibbing

- Vibe Coding
- Multi-Model Implementation Comparison
```

All four slides are merged into the deck in manifest order, but the two slides with titles
starting with "Exercise" are omitted from the agenda preview. Note that the exclusion is
based on the **slide title** (the first `## H2` heading), not the filename.

---

## 5. Merge phase — content slides

After the two injected slides, the source files for the section are merged in order.

### 5.1 Transformations applied to each source file

| Transformation          | Rule                                                                                                 |
| ----------------------- | ---------------------------------------------------------------------------------------------------- |
| Front matter            | Kept from the **first file processed across all sections only**; stripped from every subsequent file |
| H1 headings             | Removed; any immediately-following italicised provenance line (`_Merged from: …_`) is also removed   |
| Image paths             | `../images/` rewritten to `images/`                                                                  |
| Trailing separator      | One trailing `---` (and surrounding blank lines) stripped from each file body                        |
| Leading separator       | One leading `---` (and surrounding blank lines) stripped from each file body                         |
| Separator between files | Exactly one `\n\n---\n\n` inserted between consecutive file blocks by the joiner                     |

### 5.2 Code-fence awareness

`---` lines that appear inside fenced code blocks (` ``` ` or `~~~`) are never treated
as slide separators — they are preserved verbatim.

### 5.3 Slide counting

```
slide_count_for_block = 1 + (number of bare --- lines outside code fences in the block)
```

Each injected slide (module list and section agenda) counts as 1 slide.

---

## 6. Merge phase — full slide order per section

**For the first section in the manifest**:

```
┌──────────────────────────────────────────────┐
│  1.  Content slides from source file 1               │
│      (injected slides suppressed)                   │
│  2.  Content slides from source file 2               │
│  …                                                   │
└──────────────────────────────────────────────┘
```

**For all other sections**, slides appear in this order in the merged deck:

```
┌──────────────────────────────────────────────────────┐
│  1.  Module list slide                                │
│      (all section names; current section highlighted) │
├──────────────────────────────────────────────────────┤
│  2.  Section agenda slide          ← omitted when    │
│      (## Section Name + bullet     ← section has     │
│       list of slide titles)        ← no source files │
├──────────────────────────────────────────────────────────┤
│  3.  Content slides from source file 1               │
│  4.  Content slides from source file 2               │
│  …                                                   │
└──────────────────────────────────────────────────────┘
```

This block repeats for every section. The merged deck begins with the first file's
front matter and then the first section's block.

> **⚠️ IMPORTANT**: The merged output file (e.g., `Slides/aiasd-311-monday-draft.md`)
> is a **generated artifact**. Do not manually edit this file. All changes must be made
> to individual source slide files in `Slides/individual-slides/` or to the manifest YAML
> structure. Re-run `.github/copilot/Promptfiles/merge-marp-decks.prompt.md` to regenerate the deck.

---

## 7. PPTX generation phase

After the merged Marp deck is written the agent generates and executes a python-pptx
build script to produce the final editable PPTX.

### 7.1 Script location

```
scripts/generate_pptx.py            (existing script invoked by the agent)
```

### 7.2 What the script produces

- One PPTX slide per Marp slide in the merged deck.
- For each section in the manifest: a named `<p14:section>` XML group in the PPTX
  covering all slides belonging to that section (module list + agenda + content).
- **Empty sections** (no source files) receive a section group containing only the
  module list slide.
- **🔒 CRITICAL**: Speaker notes on EVERY slide:
  - **Injected slides**: Notes explaining auto-generation and purpose
    - Module list: "Auto-generated course navigation slide showing all modules with current section highlighted"
    - Section agenda: "Auto-generated section agenda slide listing slide titles from manifest"
  - **Content slides**: Notes showing source file path (e.g., "Source: Slides\\individual-slides\\welcome.md")

### 7.3 Slide layout mapping

| Marp source                            | python-pptx layout used  |
| -------------------------------------- | ------------------------ |
| `<!-- _class: lead -->` + `## heading` | Section Header layout    |
| `<!-- _class: lead -->` + `# heading`  | Section Header layout    |
| `## heading` + body bullets            | Title and Content layout |
| `## heading` (no body)                 | Title Only layout        |

### 7.4 First Section Exception (🔒 CRITICAL)

**REQUIRED BEHAVIOR**: The first section in the YAML manifest (index 0) MUST NOT receive the two injected slides. This is implemented in `generate_pptx.py` with:

```python
for idx, section in enumerate(sections_cfg):
    # ...
    if idx > 0:  # Skip injected slides for first section
        add_module_list_slide(...)
        add_section_agenda_slide(...)
```

**Rationale**: The first section typically contains the welcome/title slide. Adding navigation slides before it creates an awkward opening that frontloads course structure before the course begins.

**Testing verification**: When testing modifications, confirm that:

1. The first section in the PPTX starts with its first content slide (no "Course Modules" slide)
2. Subsequent sections DO have the two injected slides (module list and agenda)
3. ALL slides (including injected) have speaker notes

### 7.4.5 Markdown Formatting Support

**REQUIRED FEATURE**: The PPTX generator MUST parse and render markdown bold syntax (`**text**`) as actual bold formatting in PowerPoint slides.

**Implementation**: The `apply_markdown_formatting()` function in `generate_pptx.py` parses markdown bold syntax and creates separate text runs with appropriate formatting:

```python
def apply_markdown_formatting(text_frame, line_text: str) -> None:
    """
    Parse markdown bold syntax and add formatted runs to the text frame paragraph.
    Supports **bold text** syntax. Text outside bold markers is added as normal runs.
    """
```

**Behavior**:

- Text wrapped in `**double asterisks**` is rendered with `run.font.bold = True`
- Text outside bold markers is rendered as normal text
- Multiple bold sections on one line are supported
- Works with bulleted lists (the bullet prefix `- ` is handled correctly)

**Example transformations**:

| Markdown Source                           | PowerPoint Rendering                           |
| ----------------------------------------- | ---------------------------------------------- |
| `**Principal Software Engineer at CODE**` | **Principal Software Engineer at CODE** (bold) |
| `This is **important text** and normal`   | This is **important text** (bold) and normal   |
| `- **Key Point**: explanation text`       | • **Key Point** (bold): explanation text       |

**Testing verification**: When testing modifications:

1. Create a slide with markdown bold syntax in the source markdown
2. Generate the PPTX using `generate_pptx.py`
3. Open the PPTX and verify bold text appears with actual bold formatting (not literal asterisks)

### 7.5 Execution

```bash
pip install python-pptx pyyaml --quiet
python $PPTX_SCRIPT $MANIFEST $PPTX_OUTPUT
```

The agent runs both commands, reports any missing-file warnings, and confirms
`$PPTX_OUTPUT` on success.

### 7.5 Outputs

| File           | Description                                            |
| -------------- | ------------------------------------------------------ |
| `$OUTPUT_FILE` | Merged Marp deck (valid for Marp preview)              |
| `$PPTX_SCRIPT` | Existing python-pptx build script invoked by the agent |
| `$PPTX_OUTPUT` | Editable PPTX with named section groupings             |

Default values:

| Variable       | Default                                     |
| -------------- | ------------------------------------------- |
| `$OUTPUT_FILE` | `Slides/aiasd-311-monday-draft.md`          |
| `$PPTX_SCRIPT` | `scripts/generate_pptx.py`                  |
| `$PPTX_OUTPUT` | `Slides/output/aiasd-311-monday-draft.pptx` |

---

## 8. Agent prompt invocation

```
1. Open .github/copilot/Promptfiles/merge-marp-decks.prompt.md in VS Code
2. Click "Run Prompt" in the Copilot chat panel (agent mode)
   — or —
   Type in Copilot chat:  /merge-marp-decks
3. Optionally override $MANIFEST, $OUTPUT_FILE, $PPTX_SCRIPT, $PPTX_OUTPUT
   by editing the Default Values section of the prompt before running
```

### End-to-end flow

```
┌──────────────────────────────────────────────────────────────┐
│ 1. Author Slides/individual-slides/<topic>.md                 │
│    - One topic per file                                        │
│    - Valid Marp front matter                                   │
│    - First ## H2 heading = slide title                         │
│    - No H1 headings; no trailing ---                           │
└─────────────────────────────┬────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│ 2. Edit Slides/aiasd-311-monday.yaml                          │
│    - List sections with names in course order                  │
│    - List slide files under each section                       │
└─────────────────────────────┬────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│ 3. Run merge-marp-decks.prompt.md in Copilot agent mode       │
│                                                                │
│    Agent merge phase — for each section emits:                 │
│      a. Module list slide (all modules; current highlighted)   │
│      b. Section agenda slide  (## Section Name + slide titles) │
│      c. Content slides from source files (merged verbatim)     │
│                                                                │
│    → Slides/aiasd-311-monday-draft.md                         │
└─────────────────────────────┬────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│    Agent PPTX phase                                            │
│      Runs scripts/generate_pptx.py                            │
│      - Agenda and content slides                               │
│      - <p14:section> XML groups per section                    │
│                                                                │
│    → Slides/output/aiasd-311-monday-draft.pptx                │
│        Editable text boxes, bullets, presenter notes           │
│        Named section groupings visible in PowerPoint           │
└──────────────────────────────────────────────────────────────┘
```

---

## 9. File naming conventions

| Pattern                              | Example                       | Description                |
| ------------------------------------ | ----------------------------- | -------------------------- |
| `<course>-<format>-<day>.yaml`       | `aiasd-311-monday.yaml`       | Manifest file              |
| `<course>-<format>-<day>-draft.md`   | `aiasd-311-monday-draft.md`   | Merged Marp deck           |
| `generate_pptx.py`                   | `scripts/generate_pptx.py`    | Existing PPTX build script |
| `<course>-<format>-<day>-draft.pptx` | `aiasd-311-monday-draft.pptx` | Editable PPTX output       |

`course` = identifier prefix (e.g. `aiasd`)
`format` = numeric format code (e.g. `311` = 3-day, 1st delivery)
`day` = day of week (e.g. `monday`)

---

## 10. Constraints and known limitations

| Area                  | Constraint                                                                                                                                                                                                                         |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Background images     | `![bg ...]` tags in source files are stripped during merge. Add background images manually in PowerPoint after export.                                                                                                             |
| Marp CSS themes       | Custom CSS in front matter is not transferred to the PPTX. Apply visual identity via a python-pptx slide master or reference template.                                                                                             |
| Module list highlight | Marp renders `**bold**` text using the theme's default bold style, not a custom colour. To use a custom highlight colour, apply a Marp theme with a styled `.highlight` span or adjust the reference PPTX master after generation. |
| Slide title fallback  | If a source file has no `## H2` heading, the file stem is used as the agenda bullet. Ensure every content file has at least one `## H2` heading.                                                                                   |
| Empty sections        | Sections with no source files produce only a module list slide and an empty PPTX section group — no agenda slide.                                                                                                                  |
| Image paths           | Images referenced in individual slides must exist at `Slides/images/` (not only at `Slides/individual-slides/images/`) for the merged deck to render correctly.                                                                    |
| Working directory     | Run the agent prompt from the repo root: `C:\git\AIASD\AI-Assisted-Software-Development-Course`.                                                                                                                                   |

---

## 11. Verification Checklist

**⚠️ USE THIS CHECKLIST** when modifying `scripts/generate_pptx.py` or the merge logic to prevent regressions:

### Before Committing Changes

- [ ] **First Section Test**: Generate PPTX from a manifest where the first section has at least 2 content slides
  - [ ] Open the PPTX in PowerPoint
  - [ ] Verify the **first slide** is a content slide from the manifest (NOT "Course Modules")
  - [ ] Verify NO "Course Modules" slide appears before the first content slide
  - [ ] Verify NO section agenda slide appears before the first content slide

- [ ] **Subsequent Sections Test**: Verify sections after the first
  - [ ] Each section DOES start with "Course Modules" slide
  - [ ] "Course Modules" slide highlights the current section with ▶ and bold
  - [ ] Section agenda slide appears after "Course Modules" (if section has content slides)

- [ ] **Speaker Notes Test**: Open PPTX and verify EVERY slide has speaker notes
  - [ ] Module list slides: Note says "Auto-generated course navigation slide..."
  - [ ] Section agenda slides: Note says "Auto-generated section agenda slide..."
  - [ ] Content slides: Note says "Source: Slides\\individual-slides\\<filename>.md"

- [ ] **Code Verification**: Confirm the following patterns exist in `generate_pptx.py`
  - [ ] Loop uses `enumerate(sections_cfg)` to get section index
  - [ ] Injected slides wrapped in `if idx > 0:` check
  - [ ] All `add_*_slide()` functions accept `note` parameter
  - [ ] All calls to injected slide functions pass appropriate note text
  - [ ] `set_slide_notes(slide, note)` called in each add function when note is present

### Test Manifest Example

Use this minimal manifest for regression testing:

```yaml
sections:
  - name: "Intro"
    slides:
      - Slides\individual-slides\welcome-to-aiasd.md
      - Slides\individual-slides\john-michael-miller-intro.md

  - name: "Module 1 - Test"
    slides:
      - Slides\individual-slides\whats-the-big-deal.md
```

Expected PPTX slide order:

1. Welcome to AI Assisted Software Development (content slide, has note "Source: ...")
2. John Michael Miller (content slide, has note "Source: ...")
3. Course Modules (injected, has note "Auto-generated course...")
4. Module 1 - Test (section agenda, has note "Auto-generated section...")
5. What's the Big Deal (content slide, has note "Source: ...")

---

## 12. Extension points

| Scenario                                        | Approach                                                                                                                                      |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Add a new slide file                            | Create `Slides/individual-slides/<topic>.md`; add its path to the YAML manifest under the appropriate section                                 |
| Add a new section                               | Append a `- name: … slides: …` block to the YAML manifest; all module list slides update automatically on next run                            |
| Reorder sections                                | Change the order in the YAML manifest; module list slides re-generate in the new order                                                        |
| Skip module list or agenda slides for a section | Add a manifest flag (e.g. `no_injected_slides: true`) and update the prompt to honour it                                                      |
| Use a branded PPTX template                     | Extend `generate_pptx.py` to load a reference `.pptx` and copy its slide master before adding slides                                          |
| Automate on push                                | Add a GitHub Actions step that runs the agent prompt via `gh copilot suggest` or invokes the python-pptx script directly after a manual merge |
