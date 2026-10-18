---
name: summarize-transcript-content
description: "Summarize WebVTT transcripts or VTI training indices with source hierarchy, duration markers, and evidence-grounded timing statistics; also aggregate supplied structured response files."
argument-hint: "Path to a VTT transcript, VTI training index, or response-file set"
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
source: ".github/prompts/summarize-vti-content.prompt.md"
revisions:
  - chat_id: "0ee42cac-b369-4e34-9193-397eba0fac7a"
    model: "unknown/unknown@unknown"
    date: "2026-10-17"
    change: "Added optional multi-file response aggregation, attribution, traceability, and regeneration safeguards."
    ai_log: "ai-logs/2026/10/17/0ee42cac-b369-4e34-9193-397eba0fac7a/conversation.md"
  - chat_id: "skill-naming-convention-20261018"
    model: "unknown/unknown@unknown"
    date: "2026-10-18"
    change: "Applied approved skill naming decisions and updated active references; preserved workflow behavior and historical provenance."
    ai_log: "ai-logs/2026/10/18/skill-naming-convention-20261018/conversation.md"
  - chat_id: "c16f927f-91c4-4a30-aada-8f74b099e547"
    model: "unknown/unknown@unknown"
    date: "2026-10-18"
    change: "Added VTI structure and duration-marker analysis, non-overlapping timing statistics, and explicit handling of missing or conflicting durations while preserving VTT and response aggregation."
    ai_log: "ai-logs/2026/10/18/c16f927f-91c4-4a30-aada-8f74b099e547/conversation.md"
    prompt: "extend summarize-transcript-content to support VTI structure and duration markers."
    started: "2026-10-18T12:44:13.309-07:00"
    ended: "2026-10-18T12:45:44.678-07:00"
    task_durations:
      - task: "VTI workflow extension and validation"
        duration: "00:01:31"
    total_duration: "00:01:31"
---
# Transcript and Training Index Summarizer

Analyze one explicitly supplied VTT transcript or VTI training index and generate an outline with timing information. For a supplied response-file set, use the separate aggregation workflow below.

## Input and Format Detection

- Require an existing source path. Identify WebVTT by `WEBVTT` and timestamp cues; identify a VTI training index by its section/subsection headings and duration markers. Inspect content rather than relying only on the extension.
- VTI here means a structured text training index, not a universally standardized file format. Read the source's conventions before interpreting markers; stop and ask for clarification when the format or time notation cannot be identified reliably.
- Preserve the source and distinguish extracted structure and facts from inferred topic grouping.

## Analysis Requirements

1. **Parse VTT Structure**
   - Read the VTT file format (WebVTT)
   - Extract timestamps and associated text
   - Identify speaker changes (if indicated)
   - Note any cue identifiers or metadata

2. **Content Segmentation**
   - Group related content into logical sections
   - Identify topic transitions
   - Detect major themes or discussion points
   - Note any Q&A segments or breaks

3. **Timing Analysis**
   - Calculate duration of each section
   - Identify the total video length
   - Note significant pauses or gaps
   - Track pacing patterns

## VTI Structure and Duration Markers

1. Read the whole index. Preserve its title, overview, section/subsection hierarchy, source order, topics, and speaker names only when stated. Keep overview and conclusion metadata separate from timed teaching sections.
2. Extract explicit durations from `Duration: 45:00`, `Total Duration: 45:00`, heading suffixes such as `## Section 1: Introduction (8:30)` and `### File Structure (4:00)`, or equivalent unambiguous source labels. Interpret `MM:SS` and `HH:MM:SS` as elapsed durations, not clock times; normalize to seconds for arithmetic. Accept unit-labeled values such as `8 minutes 30 seconds` when unambiguous. Validate component ranges and reject negative or malformed values; do not treat arbitrary numbers or parenthetical text as durations.
3. Associate each marker with its actual scope (whole index, section, or subsection). Record declared values separately from calculated values. Repeated overview/conclusion totals are declarations of the same total, not additional timed sections.
4. Never add a parent duration to its children. Use complete, non-overlapping sibling sections for totals and statistics. A parent may be derived from children only when the source establishes complete coverage; label it calculated. If parent and child sums differ, report both and the discrepancy without changing the source or silently choosing one.
5. Mark absent, ambiguous, or invalid durations as `Not specified` and explain any invalid marker or uncertainty. Do not fill missing child durations from a parent's remainder. Do not invent start/end timestamps from durations alone; show duration-only entries unless the source supplies a timeline or explicitly establishes a contiguous sequence. Label any requested cumulative schedule as derived, not observed.
6. Report the declared total, calculated section total when complete, and any mismatch. For incomplete coverage, report a known-duration subtotal and its coverage, not a complete total. Calculate average, longest, and shortest only across reliable durations at one stated hierarchy level, with the count included and missing entries excluded. Label partial statistics; do not mix sections with their subsections or include overview/conclusion totals.

For example, a section declared as `12:15` with children `4:00`, `3:30`, and `4:45` totals `12:15`, not `24:30`. If one child has no marker, retain `Not specified` for it rather than inferring the remainder.

## Output Format

Generate a structured outline with the following sections:
For VTI, retain source headings and nesting in the detailed outline; use duration-only labels when timestamps are unavailable. Omit an unsupported timeline and explain why. Report absent values as `Not specified`, not fabricated metadata.

### Executive Summary
- Total video duration for VTT; declared/calculated training duration for VTI, with discrepancies or incomplete coverage
- Number of major topics covered
- Overall content type (lecture, discussion, demo, etc.)
- Key takeaways (3-5 bullet points)

### Detailed Outline

For each section, provide:

```
## Section N: [Topic Title] (MM:SS - MM:SS, Duration: MM:SS)

**Key Points:**
- Main point 1
- Main point 2
- Main point 3

**Notable Quotes or Examples:**
- Relevant excerpts

**Transitions:**
- How this section connects to the next
```

### Timeline Reference

Provide a quick-reference timeline when source timestamps support it:

```
00:00 - 05:30 | Introduction and Setup
05:31 - 15:45 | Topic 1: [Name]
15:46 - 28:20 | Topic 2: [Name]
...
```

### VTI Duration Statistics

For VTI, include declared total, calculated total or known-duration subtotal, coverage and hierarchy level, and the average/longest/shortest durations for the reliable entries. Separate source declarations from calculations and list missing, invalid, ambiguous, or conflicting markers.

### Content Analysis

- **Difficulty Level**: Beginner/Intermediate/Advanced
- **Primary Topics**: List of main subjects covered
- **Prerequisites Mentioned**: Any assumed knowledge
- **Resources Referenced**: URLs, books, tools mentioned
- **Action Items**: Any homework or follow-up activities suggested

## Processing Instructions

1. Read the entire source first to understand overall structure
2. For VTT, identify natural breaks and topic shifts; for VTI, preserve explicit sections and subsections
3. For VTT, group timestamps into logical sections (typically 5-15 minutes each); do not regroup a VTI index merely to meet a duration target
4. Extract key vocabulary and technical terms
5. Note any visual demonstrations mentioned in the transcript
6. Flag any audio quality issues noted in the text
7. Identify questions from participants (if present)

## Optional Multi-File Response Aggregation

When the input is a set of questionnaire or feedback responses rather than a VTT or VTI:

1. Inventory each supplied response file and preserve its source identity for traceability.
2. Summarize each response separately before aggregating common themes, disagreements, and unanswered questions.
3. Attribute contributors only when the source explicitly identifies them and the user authorizes attribution; otherwise anonymize or use source IDs.
4. Ground clarifications in the supplied material and mark missing or ambiguous answers rather than filling them in.
5. Regenerate only the requested summary outputs, following the user's filename and directory conventions; do not overwrite existing summaries without approval.

## Quality Checks

- For VTT, verify section timestamps against source cues; compare the reported endpoint/span with the cue timeline, not an uninspected media file
- For VTI, verify hierarchy, marker scope, duration arithmetic, and complete versus partial coverage without counting parent and child time twice
- Account for all source content and report gaps or ambiguities rather than claiming they do not exist
- Confirm logical flow between sections
- Validate that key points accurately represent the content
- For response aggregation, check that every source was considered, duplicated themes are consolidated, minority views are retained, and each claim can be traced to its response source

## Output File

Save the analysis as a markdown file following this naming convention:
- Original file: `[name].vtt`
- Or training index: `[name].vti`
- Output file: `[name]-summary.md`
- Location: Same directory as source file unless the user supplies another destination
- Ask before overwriting. Do not edit the source.

Include complete provenance required by the [AI-assisted output policy](../../instructions/ai-assisted-output.instructions.md), plus source-analysis fields such as the following. Keep source duration separate from provenance `total_duration`, which measures AI task time. Use `Not specified` for unsupported duration values; do not claim a known subtotal is a complete source duration.
```yaml
source_file: "<VTT or VTI file path>"
source_format: "<VTT or VTI>"
analyzed_date: "<YYYY-MM-DD>"
source_duration: "<HH:MM:SS or Not specified>"
section_count: <number of top-level content sections>
```


