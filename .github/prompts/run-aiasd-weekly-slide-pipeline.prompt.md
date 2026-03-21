---
mode: agent
model: "openai/gpt-5.4@unknown"
tools: ["read", "search", "run_command"]
description: Delegates the AIASD Monday-Friday slide pipeline to parallel subagents so each manifest is merged and exported to PPTX in one coordinated run.
prompt_metadata:
  id: run-aiasd-weekly-slide-pipeline
  title: Run AIASD Weekly Slide Pipeline
  owner: johnmillerATcodemag-com
  version: 1.0.0
  created: 2026-03-21
  updated: 2026-03-21
  output_path: Slides/output/aiasd-311-<day>-draft.pptx
  output_format: markdown
  category: slides
  tags: [marp, slides, pptx, subagent, parallel, pipeline]
---

# Run AIASD Weekly Slide Pipeline

Execute the existing slide merge pipeline for the full AIASD week by delegating each
manifest to its own writable subagent.

## Context

Use `.github/prompts/merge-marp-decks.prompt.md` as the execution contract for each
manifest-specific run. Do not reimplement the merge logic in this prompt. The subagent must
follow that prompt's validation, merge, overwrite, slide-count, and PPTX-generation rules.

## Fixed Manifest Set

Run the pipeline for exactly these manifests:

1. `Slides/aiasd-311-monday.yaml`
2. `Slides/aiasd-311-tuesday.yaml`
3. `Slides/aiasd-311-wednesday.yaml`
4. `Slides/aiasd-311-thursday.yaml`
5. `Slides/aiasd-311-friday.yaml`

## Required Workflow

1. Launch one writable subagent per manifest.
2. Start all five subagents before waiting for any individual result.
3. In each subagent prompt, explicitly direct the subagent to execute
   `.github/prompts/merge-marp-decks.prompt.md` with the exact invocation text:

   ```text
   Manifest: Slides/aiasd-311-<day>.yaml
   ```

4. Each subagent must run the full workflow for its assigned manifest:
   - manifest validation
   - Phase 0 source-file validation
   - Phase 1 merged deck generation
   - Phase 2 PPTX generation via `scripts/generate_pptx.py`
5. Do not serialize PPTX generation. Because each manifest runs in its own subagent, PPTX
   creation must proceed in parallel with the other manifest runs.
6. Do not edit `.github/prompts/merge-marp-decks.prompt.md`.
7. Do not substitute a read-only explorer agent for the execution subagents.
8. If one manifest fails, continue collecting results from the remaining subagents and report
   the failure alongside the successful runs.

## Subagent Prompt Template

Use this structure for each subagent, replacing only the manifest path:

```text
Execute `.github/prompts/merge-marp-decks.prompt.md` for this exact invocation:

Manifest: Slides/aiasd-311-<day>.yaml

Follow that prompt end-to-end. Create or overwrite the derived merged deck and PPTX outputs.
Return a concise status report with:
- manifest path
- merged deck path
- PPTX output path
- validation warnings, if any
- final status: success or failure
```

## Expected Outputs

| Manifest                          | Merged Deck                           | PPTX Output                                    |
| --------------------------------- | ------------------------------------- | ---------------------------------------------- |
| `Slides/aiasd-311-monday.yaml`    | `Slides/aiasd-311-monday-draft.md`    | `Slides/output/aiasd-311-monday-draft.pptx`    |
| `Slides/aiasd-311-tuesday.yaml`   | `Slides/aiasd-311-tuesday-draft.md`   | `Slides/output/aiasd-311-tuesday-draft.pptx`   |
| `Slides/aiasd-311-wednesday.yaml` | `Slides/aiasd-311-wednesday-draft.md` | `Slides/output/aiasd-311-wednesday-draft.pptx` |
| `Slides/aiasd-311-thursday.yaml`  | `Slides/aiasd-311-thursday-draft.md`  | `Slides/output/aiasd-311-thursday-draft.pptx`  |
| `Slides/aiasd-311-friday.yaml`    | `Slides/aiasd-311-friday-draft.md`    | `Slides/output/aiasd-311-friday-draft.pptx`    |

## Final Response Format

After all subagents finish, provide:

1. A compact per-manifest status table with `Success` or `Failed`
2. Any validation warnings reported by the subagents
3. A short failure section listing the manifest and blocking error for any unsuccessful run
4. A final summary stating how many manifests completed successfully out of five

## Success Criteria

- All five manifest runs are dispatched through subagents
- The dispatch is concurrent, not sequential
- PPTX generation overlaps across manifest runs
- Output files use the standard derived names from `merge-marp-decks.prompt.md`
- The final report clearly identifies successes, warnings, and failures
