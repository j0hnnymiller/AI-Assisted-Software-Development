---
name: finalize-pptx-local
agent: slide-master
description: Finalize a generated PPTX locally by running scripts/finalize_pptx_local.ps1 so PowerPoint applies shrink-to-fit behavior to overflowing text frames and table cells.
tags: [pptx, powerpoint, marp, slides, finalize, automation]
ai_generated: true
model: "openai/gpt-5.4@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "slide-master-agent-20260328"
prompt: |
  create a custom slide-master agent that is an expert in pptx files, powerpoint templates, marp, pandoc. the agent support two commands that run prompt files.

  #file:merge-marp-decks.prompt.md and #file:finalize_pptx_local.ps1
started: "2026-03-28T17:56:58.3714628-07:00"
ended: "2026-03-28T17:58:27.6040610-07:00"
task_durations:
  - task: "prompt authoring"
    duration: "00:01:00"
  - task: "workflow definition"
    duration: "00:00:45"
  - task: "provenance logging"
    duration: "00:00:30"
total_duration: "00:02:15"
ai_log: "ai-logs/2026/03/28/slide-master-agent-20260328/conversation.md"
source: "johnmillerATcodemag-com"
---

# Finalize PPTX Local

Run the local PowerPoint finalization script to force shrink-to-fit handling for overflow text in an existing PPTX.

## Runtime Inputs

Provide the PPTX path in the invocation text.

Preferred format:

```text
Path: slides/output/<deck>-draft.pptx
```

Optional output path:

```text
OutputPath: slides/output/<deck>-final.pptx
```

Also accepted:

```text
Finalize slides/output/<deck>-draft.pptx
Finalize slides/output/<deck>-draft.pptx to slides/output/<deck>-final.pptx
```

## Input Resolution

Resolve runtime values in this order:

1. A line starting with `Path:`
2. A plain-language instruction containing `Finalize <path>`
3. A line starting with `OutputPath:` for the optional destination

If no unambiguous PPTX input path is provided, abort immediately.

Abort message format:

```text
ERROR: Missing or invalid PPTX path. Provide an explicit path such as
slides/output/aiasd-311-monday-draft.pptx.
```

## Execution Rules

1. Resolve the PPTX input path first.
2. Confirm the input file exists before running anything.
3. Run the PowerShell script at [scripts/finalize_pptx_local.ps1](../../scripts/finalize_pptx_local.ps1).
4. If `OutputPath` is omitted, finalize the file in place.
5. If `OutputPath` is provided, allow the script to create or overwrite that destination.
6. Do not edit the PPTX manually outside the script.
7. Do not modify the script as part of this command unless the user explicitly asks for script changes.

## Command

Run:

```powershell
pwsh -File scripts/finalize_pptx_local.ps1 -Path "<input-path>"
```

If an output path is provided, run:

```powershell
pwsh -File scripts/finalize_pptx_local.ps1 -Path "<input-path>" -OutputPath "<output-path>"
```

## Environment Constraints

- This workflow is intended for Windows with Microsoft PowerPoint installed.
- If PowerPoint COM automation is unavailable, stop and report that prerequisite clearly.
- Treat missing input files, COM startup failures, and save failures as blockers.

## Expected Output

Report:

1. Finalized PPTX path
2. Updated text frame count
3. Fallback-adjusted text frame count
4. Skipped text frame count
5. Any prerequisite or COM automation blockers
