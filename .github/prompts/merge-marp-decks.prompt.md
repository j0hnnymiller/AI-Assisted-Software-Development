---
mode: agent
model: "anthropic/claude-sonnet-4-5@2025-02-19"
tools: ["read", "create", "edit", "search", "run_command"]
description: Merges Marp slide decks listed in a YAML file into a single Marp deck and generates a PPTX with named sections using python-pptx, or runs a validate-only pass on the manifest and source slides.
prompt_metadata:
  id: merge-marp-decks
  title: Merge Marp Slide Decks, Validate Sources, and Generate PPTX
  owner: johnmillerATcodemag-com
  version: 3.0.0
  created: 2026-03-12
  updated: 2026-03-21
  output_path: Slides/<manifest-stem>-draft.md
  output_format: markdown
  category: slides
  tags: [marp, slides, merge, presentation, markdown, pptx, python-pptx]
---

# Merge Marp Slide Decks, Validate Sources, and Generate PPTX

Merge the Marp slide decks defined in the runtime manifest path into a single Marp slide
deck, then generate a PPTX with named sections using `python-pptx`.

This prompt also supports a **validate-only** mode that validates the manifest and source
slides without generating or overwriting any output files.

## Runtime Inputs

Provide the manifest path in the prompt invocation using plain language. Do not edit this
prompt file to switch manifests.

Preferred invocation format:

```
Manifest: Slides/aiasd-311-<day>.yaml
```

Optional mode line:

```text
Mode: validate-only
```

Also accepted:

```text
Use manifest Slides/aiasd-311-tuesday.yaml
```

Also accepted for validation:

```text
Validate only using manifest Slides/aiasd-311-tuesday.yaml
```

The manifest path is mandatory for every run. The agent must not assume a default manifest,
infer a manifest from filenames, or build a deck from every file in `Slides/individual-slides/`.

### Input Resolution

Resolve the manifest path from the invocation text using this order:

1. A line starting with `Manifest:`
2. A plain-language instruction of the form `Use manifest <path>`
3. A single unambiguous repo-relative YAML path under `Slides/`

If none of the above yields exactly one manifest path, abort immediately.

### Mode Resolution

Resolve the execution mode from the invocation text using this order:

1. A line starting with `Mode:`
2. A plain-language instruction containing `validate only`
3. Default to `full`

Supported modes:

- `full` — validate, merge, and generate PPTX
- `validate-only` — validate the manifest and source slides only

If an explicit mode is provided but is not one of the supported values, abort immediately.

### Derived Runtime Paths

After resolving the manifest path, derive these runtime paths automatically:

- `Merged deck path`: strip `.yaml` and append `-draft.md`
  (e.g. `Slides/aiasd-311-tuesday.yaml` → `Slides/aiasd-311-tuesday-draft.md`)
- `PPTX output path`: strip `.yaml`, get basename, prepend `Slides/output/` and append `-draft.pptx`
  (e.g. `Slides/aiasd-311-tuesday.yaml` → `Slides/output/aiasd-311-tuesday-draft.pptx`)

Fixed path:

- `PPTX script path` = `scripts/generate_pptx.py`

This prompt must be reusable across manifests. Do not modify the prompt file, front matter,
or `prompt_metadata.output_path` when the caller wants a different manifest.

In `validate-only` mode, these derived output paths remain informational only and must not be
created, edited, overwritten, or otherwise touched.

Front matter note:

- `prompt_metadata.output_path` is a documentation pattern, not a fixed runtime destination.
- The actual merged deck path must always be derived from the manifest path supplied in the invocation.
- Example: `Manifest: Slides/aiasd-311-tuesday.yaml` produces `Slides/aiasd-311-tuesday-draft.md`.

> **⚠️ IMPORTANT**: The merged deck path is a **generated artifact**. Do not manually edit it.
> This pipeline is **output-only**: it may create or overwrite the derived merged deck path
> and PPTX output path, but it must **never modify** source Marp slides in
> `Slides/individual-slides/` or the manifest YAML file. If the manifest or any source slide
> is invalid, missing, malformed, or inconsistent with this prompt, report the issue and
> continue where the prompt allows. Do not auto-fix, normalize, rewrite, rename, or replace
> manifest entries or source slide files as part of this run.

## Manifest Requirement

Before doing any repository exploration or file generation, resolve and validate the manifest path.

- If the invocation does not provide exactly one manifest path, abort immediately.
- If the manifest path does not exist, abort immediately.
- If the manifest file cannot be parsed as YAML with a top-level `sections:` array, abort immediately.
- Do not guess the manifest path.
- Do not fall back to `Slides/aiasd-311-monday.yaml` or any other file.
- Do not scan `Slides/individual-slides/` to assemble a deck without a manifest.

Abort message format:

```text
ERROR: Missing or invalid manifest path. Provide an explicit manifest path such as
Slides/aiasd-311-tuesday.yaml. This prompt must not run without a valid manifest.
```

## Execution Rule

- Resolve the manifest path first. Abort on any manifest error before reading slide files.
- Resolve the execution mode before starting Phase 0.
- Perform **Phase 0** directly in this agent run using the prompt logic in all modes.
- Perform **Phase 1** and **Phase 2** only in `full` mode.
- Do **not** call or rely on any script for Phase 0/1.
- In `full` mode, read source files, validate them, build merged markdown in memory, and write the merged deck path.
- In `validate-only` mode, stop after Phase 0 and report validation results only.
- Treat the manifest YAML and all source slide files as **read-only inputs**.
- Only the derived merged deck path and derived PPTX output path are writable outputs, and only in `full` mode.

### Validate-Only Mode Contract

When mode is `validate-only`:

- Validate the manifest path, YAML structure, and manifest slide entries
- Run Phase 0 for every resolvable source slide
- Report manifest issues, source warnings, and the validation summary
- Do **not** run Phase 1 or Phase 2
- Do **not** create, edit, or overwrite the merged deck path
- Do **not** create, edit, or overwrite the PPTX output path
- Do **not** modify the manifest or any source file

## File Write Strategy

> **⚠️ CRITICAL (cloud compatibility)**: Output files (merged deck path and PPTX output path) may
> already exist from a previous run. **Always overwrite** — never create a new file with a
> modified name or leave the old content in place.
>
> - If the file **does not exist**: create it.
> - If the file **already exists**: replace its entire content using the `edit` tool
>   (full-file replacement), **not** the `create` tool. The `create` tool must never be
>   used on a file that already exists.

In `validate-only` mode, this entire file write strategy is disabled because no output files
may be written.

> **Agent verification (Issue 3)**: After computing the merged deck path, confirm its filename
> matches the pattern `<course>-<format>-<day>-draft.md` derived from the manifest stem.

## YAML Structure

The manifest uses a sectioned structure:

```yaml
sections:
  - name: <Section Name>
    slides:
      - Slides\individual-slides\<file>.md
      - Slides\individual-slides\<file>.md
  - name: <Empty Section>
    slides:
      # no slide files listed — still creates an empty PPTX section
```

Each section has a `name` and an optional `slides` list. Sections with no slide files
(null, empty, or comment-only) are still present in the final PPTX as **empty sections**.

### Manifest entry constraints

- Every `sections[].slides[]` entry must resolve to a repo-relative Markdown source file.
- Supported source slide extensions are `.md` and `.markdown` only.
- Any slide entry that is missing, malformed, uses a non-Markdown extension, contains a
  label instead of a path, or cannot be resolved exactly as written is a **manifest issue**.
- Manifest issues must be reported with the exact raw entry and section name.
- Do **not** rewrite manifest entries to alternative filenames, `.pptx` files, inferred
  Markdown files, or guessed paths.

---

## Phase 0 — Validate Manifest and Source Files

Collect the complete list of unique source file paths from the manifest, then **validate
each source file using a subagent**. Launch one subagent per source file — all subagents
may run concurrently. Each subagent must read the file it is assigned and apply the six
validation rules listed below, returning a structured result (file path, pass/fail per
rule, and any warning messages).

If the manifest path is missing or invalid, Phase 0 must not start.

### Subagent task

For each source file, invoke a subagent with a prompt that instructs it to:

1. Read the entire file content
2. Apply the six validation rules below
3. Extract the first `## H2` heading text from the body (after stripping front matter)
4. Return a JSON-style result containing:
   - `file`: the source file path
   - `rules`: an object with keys `1`–`6`, each `true` (pass) or `false` (fail)
   - `warnings`: a list of human-readable warning strings (empty if all rules pass)
   - `content`: the full file content (used by Phase 1 — avoids re-reading files)
   - `first_h2`: the text of the first `## H2` heading, or `null` if none found

> **Why return content?** Phase 1 needs every source file's content for merging.
> By capturing it here, each file is read exactly once across the entire pipeline.

> **Read-only rule**: Validation subagents must not edit the manifest or any source slide file.
> They may only read, validate, and report issues.

### Validation rules

| #   | Rule                      | Check                                                                 |
| --- | ------------------------- | --------------------------------------------------------------------- |
| 1   | **Front matter**          | File begins with a valid Marp YAML front-matter block (`---` … `---`) |
| 2   | **No H1 in body**         | No `# H1` headings appear after the front-matter block                |
| 3   | **H2 present**            | At least one `## H2` heading exists in the body                       |
| 4   | **Image paths**           | No `../images/` references (must use `images/` prefix)                |
| 5   | **No trailing separator** | File does not end with a bare `---` line                              |
| 6   | **Encoding**              | No vertical-tab (`\x0b`) characters                                   |

### Collecting results

After all subagents complete, the orchestrating agent collects their results, aggregates
warnings, and prints the validation summary.

Log a warning for each violation and continue — do not abort. Print a validation summary
before writing the merged deck path:

```
Validation complete: N file(s) checked, M warning(s) found.
```

Also report any **manifest issues** discovered before subagent dispatch or while resolving
slide paths. Manifest issues are input problems, not output-generation tasks. Report them;
do not repair them in-place.

If mode is `validate-only`, stop here after printing the validation summary and issue report.
Do not continue to merge or PPTX generation.

> **Agent verification (Issue 1)**: After running Phase 0, confirm the validation summary
> is printed. For a file known to violate a rule (e.g. ends with `---`), verify the warning
> appears and the merge still completes successfully.

---

## Phase 1 — Merge Markdown

Run Phase 1 only in `full` mode. Skip it entirely in `validate-only` mode.

### Steps

1. Read the manifest; collect all sections (names + slide file lists) in manifest order
2. Collect all section names into a list — used to build every module list slide
3. Build a lookup map from Phase 0 subagent results, keyed by file path, containing
   each file's `content` — do **not** re-read source files from disk
4. For each section, build the section block following the rules below
5. Concatenate all section blocks (each injected module list slide and each merged source block
   separated by exactly one `\n\n---\n\n`)
6. Write the result to the merged deck path — check if the file exists first:

- **Exists**: overwrite its entire contents using the `edit` tool (full replacement).
- **Does not exist**: create it with the `create` tool.
- Never rename or append a suffix to the file. The output path is fixed.

The manifest is the sole source of truth for slide selection and ordering. Never merge
all files in `Slides/individual-slides/` unless every one of those files is explicitly
listed in the manifest.

### Injected module list slide

Insert one auto-generated module list slide at the start of each section after the
first, before any source content slides. It is produced entirely from manifest data.

**Exception**: For the **first section** in the manifest, **suppress the
injected module list slide**. Start the first section directly
with the first source content slide. This prevents navigation-heavy opening that would
precede the welcome slide.

#### Module list slide (always, first in every non-first section)

```markdown
<!-- _class: lead -->

## Course Modules

- Section A
- **▶ Current Section**
- Section C
```

Rules:

- One bullet per section in manifest order, using the exact `name` from YAML
- The section being introduced: `**▶ Section Name**` (bold, arrow prefix)
- All other sections: plain `Section Name`

#### Full slide order per section

**For the first section in the manifest**:

```
1. Content slides from file 1     (injected module list slide suppressed)
2. Content slides from file 2 …
```

**For all other sections**:

```
1. Module list slide              (always)
2. Content slides from file 1     (only when section has source files)
3. Content slides from file 2 …
```

### Merge rules for source content files

#### Front matter

- Use the YAML front matter from the **first source file across all sections**
- Place it at the very top of the merged deck path, before the first section block
- Strip front matter from all subsequent source files
- The first file's front matter provides `title:` and `subtitle:` — do not remove them

#### Level-1 headings (`# H1`)

- Strip **all** `# H1` headings from every source file
- Also strip any immediately-following provenance lines like `_Merged from: ..._`

#### Slide separators (`---`)

- Preserve all `---` separators that appear within each source file's content
- `---` lines that appear inside fenced code blocks (` ``` ` or `~~~`) are **never** treated
  as slide separators — preserve them verbatim
- Strip one leading `---` (and surrounding blank lines) from each source file body
- Strip one trailing `---` (and surrounding blank lines) from each source file body
- Between the injected module list slide and source file blocks, and between source
  file blocks, use exactly one `\n\n---\n\n`
- Do not double-up separators

> **Agent verification (Issue 2)**: Open a source file containing a YAML code block with
> internal `---` lines. After merging, confirm those `---` lines are present verbatim in
> the merged deck path and do not create unexpected extra slides (slide count must match
> expectation).

#### All other content

- Include verbatim: `## H2` headings, body text, bullet lists, images, speaker notes
  (`::: notes` blocks), inline styles

#### Image paths

- Source files use `../images/` for their own Marp preview; the merged deck lives in
  `Slides/`, so rewrite `../images/` → `images/` in all image references
- All other content is preserved verbatim

### Output format

- Single YAML front matter block at top (from first source file, with `title:` and
  `subtitle:` fields)
- No `# H1` headings in the body
- `<!-- _class: lead -->` directives present on module list slides
- `## H2` headings on all content slides

### Slide counting

After writing the merged deck path, count and report the total number of slides produced:

```
slide_count = 1 + (number of bare --- lines outside fenced code blocks)
```

Each injected module list slide counts as 1 slide.
Report the count in the form: `Merged deck: N slide(s) across M section(s).`

> **Agent verification (Issue 7)**: Compare the reported slide count against a manual count
> of `---` separators in the merged deck path (excluding those inside code fences). The counts
> must match.

---

## Phase 2 — Generate PPTX with Sections

Run Phase 2 only in `full` mode. Skip it entirely in `validate-only` mode.

Run the PPTX script path (`scripts/generate_pptx.py`) to produce the PPTX output path.

### Markdown formatting support

**CRITICAL FEATURE**: The PPTX generator automatically parses markdown bold syntax (`**text**`) and renders it as actual bold formatting in PowerPoint slides (not literal asterisks).

**How it works**:

- The `apply_markdown_formatting()` function parses each line of slide content
- Text wrapped in `**double asterisks**` is rendered with `font.bold = True`
- Text outside bold markers appears as normal text
- Multiple bold sections per line are supported
- Works correctly with bulleted lists

**Example transformations**:

| Markdown Source                            | PPTX Rendering                                      |
| ------------------------------------------ | --------------------------------------------------- |
| `**Principal Software Engineer at CODE**`  | **Principal Software Engineer at CODE** (bold font) |
| `- **Key Point**: explanation text`        | • **Key Point** (bold): explanation text            |
| `Experience: **15+ years** in development` | Experience: **15+ years** (bold) in development     |

This ensures that markdown bold syntax in source slides (e.g., `Slides/individual-slides/*.md`) is properly rendered as visual bold formatting when viewed in PowerPoint, improving readability and emphasis.

### Execution

```bash
pip install python-pptx pyyaml --quiet
python scripts/generate_pptx.py <manifest-path> <pptx-output-path>
```

Report any warnings (missing slide files) and confirm the output path on success.

> **Agent verification (Issue 4)**: Run `python scripts/generate_pptx.py <manifest-path> <pptx-output-path>`
> and verify the PPTX is created at the PPTX output path.
>
> **Agent verification (Issue 5)**: Open the generated PPTX. For any source slide whose
> `## heading` had no body content, confirm that slide uses the `Title Only` layout
> (index `LAYOUT_TITLE_ONLY`), not `Title and Content`.

---

## Deliverables

### Full mode

1. Merged deck path — merged Marp markdown deck (with injected module list slides only)
2. PPTX output path — generated PPTX with named sections
3. Issue report — validation warnings and manifest/source issues found during the run

### Validate-only mode

1. Validation summary — number of files checked and warnings found
2. Manifest issue report — malformed, missing, or unresolved manifest entries
3. Source issue report — rule violations found in the source slide files

Validate-only mode must not emit merged markdown or PPTX artifacts.

## Section Handling Rules

- **Every** section in the YAML becomes a named section in the PPTX, regardless of whether
  it contains source slide files
- Every section gets a module list slide
- Sections with source files then continue directly into content slides
- Sections with no source files produce only the module list slide and an empty PPTX section group
- Section names in the PPTX match the `name` field in the YAML exactly
- Slide file paths are resolved relative to the repository root

> **Agent verification (Issue 6)**: Add a section to the manifest with no `slides:` entries.
> Run the PPTX phase and confirm `INFO: Section '...' is empty — only module list slide added`
> is printed, and the resulting PPTX contains a named section group with only the module
> list slide.

---

## Agent Verification Checklist

Run all checks below after the pipeline completes to confirm spec conformance.

| #   | Issue                         | Check                                                                    | Pass condition                                                                           |
| --- | ----------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| V1  | Source validation             | Phase 0 summary printed before the merged deck path is written           | `Validation complete: N file(s) checked, M warning(s) found.` appears in output          |
| V2  | Code-fence `---` preserved    | Merge a source file that contains `---` inside a fenced code block       | No unexpected extra slides; the embedded `---` appears verbatim in the merged deck path  |
| V3  | Output file named correctly   | Inspect the merged deck path                                             | Filename matches `<course>-<format>-<day>-draft.md` derived from the manifest stem       |
| V4  | PPTX generated                | Run `python scripts/generate_pptx.py <manifest-path> <pptx-output-path>` | PPTX file created at the PPTX output path without errors                                 |
| V5  | `Title Only` layout used      | Source file with `## heading` and no body content                        | PPTX slide uses `Title Only` layout (`LAYOUT_TITLE_ONLY` index), not `Title and Content` |
| V6  | Empty section logged          | YAML section with no `slides:` entries                                   | `INFO: Section '...' is empty — only module list slide added` printed during PPTX phase  |
| V7  | Slide count reported          | Any successful merge run                                                 | Output includes `Merged deck: N slide(s) across M section(s).`                           |
| V8  | Validate-only stays read-only | Run with `Mode: validate-only`                                           | Validation summary and issues are reported, and no merged deck or PPTX file is written   |
