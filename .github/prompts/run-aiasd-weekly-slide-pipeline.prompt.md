---
mode: agent
model: "openai/gpt-5.4@unknown"
toolsets: ["weekly-slide-pipeline"]
description: Delegates the AIASD Monday-Friday slide pipeline to parallel subagents so each manifest is merged and exported to PPTX in one coordinated run.
prompt_metadata:
  id: run-aiasd-weekly-slide-pipeline
  title: Run AIASD Weekly Slide Pipeline
  owner: johnmillerATcodemag-com
   version: 1.2.0
  created: 2026-03-21
  updated: 2026-03-21
  output_path: slides/output/aiasd-311-<day>-draft.pptx
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

The weekly pipeline is **output-only**. Subagents may create or overwrite the derived merged
deck and PPTX outputs, but they must treat manifest YAML files and source Marp slides as
**read-only inputs**. If they find malformed manifest entries, missing slide files, or source
validation problems, they must report them instead of editing those inputs.

## Fixed Manifest Set

Run the pipeline for exactly these manifests:

1. `slides/manifests/aiasd-311-monday.manifest.md`
2. `slides/manifests/aiasd-311-tuesday.manifest.md`
3. `slides/manifests/aiasd-311-wednesday.manifest.md`
4. `slides/manifests/aiasd-311-thursday.manifest.md`
5. `slides/manifests/aiasd-311-friday.manifest.md`

## Required Workflow

1. Launch one writable subagent per manifest.
2. Start all five subagents before waiting for any individual result.
3. In each subagent prompt, explicitly direct the subagent to execute
   `.github/prompts/merge-marp-decks.prompt.md` with the exact invocation text:

   ```text
   Manifest: slides/manifests/aiasd-311-<day>.manifest.md
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
9. Do not modify any `slides/manifests/*.manifest.md` manifest or any file under `slides/marp/`.
10. Report manifest issues and source-slide issues exactly as found; do not auto-correct them.

## Subagent Prompt Template

Use this structure for each subagent, replacing only the manifest path:

```text
Execute `.github/prompts/merge-marp-decks.prompt.md` for this exact invocation:

Manifest: slides/manifests/aiasd-311-<day>.manifest.md

Follow that prompt end-to-end. Create or overwrite the derived merged deck and PPTX outputs.
Treat the manifest YAML file and all source slide files as read-only. Do not repair or rewrite
manifest entries, rename slide paths, replace `.pptx` references with guessed `.md` files, or
edit the source Marp slides. If you find input issues, report them.

Return a concise status report with:
- manifest path
- merged deck path
- PPTX output path
- manifest issues, if any
- validation warnings, if any
- final status: success or failure
```

## Expected Outputs

| Manifest                                           | Merged Deck                                  | PPTX Output                                    |
| -------------------------------------------------- | -------------------------------------------- | ---------------------------------------------- |
| `slides/manifests/aiasd-311-monday.manifest.md`    | `slides/merged/aiasd-311-monday-draft.md`    | `slides/output/aiasd-311-monday-draft.pptx`    |
| `slides/manifests/aiasd-311-tuesday.manifest.md`   | `slides/merged/aiasd-311-tuesday-draft.md`   | `slides/output/aiasd-311-tuesday-draft.pptx`   |
| `slides/manifests/aiasd-311-wednesday.manifest.md` | `slides/merged/aiasd-311-wednesday-draft.md` | `slides/output/aiasd-311-wednesday-draft.pptx` |
| `slides/manifests/aiasd-311-thursday.manifest.md`  | `slides/merged/aiasd-311-thursday-draft.md`  | `slides/output/aiasd-311-thursday-draft.pptx`  |
| `slides/manifests/aiasd-311-friday.manifest.md`    | `slides/merged/aiasd-311-friday-draft.md`    | `slides/output/aiasd-311-friday-draft.pptx`    |

## Final Response Format

After all subagents finish, provide:

1. A compact per-manifest status table with `Success` or `Failed`
2. Any manifest issues and source-slide validation warnings reported by the subagents
3. A short failure section listing the manifest and blocking error for any unsuccessful run
4. A final summary stating how many manifests completed successfully out of five

## Success Criteria

- All five manifest runs are dispatched through subagents
- The dispatch is concurrent, not sequential
- PPTX generation overlaps across manifest runs
- Output files use the standard derived names from `merge-marp-decks.prompt.md`
- No manifest YAML or source Marp slide file is modified by the pipeline run
- The final report clearly identifies successes, manifest issues, source warnings, and failures
