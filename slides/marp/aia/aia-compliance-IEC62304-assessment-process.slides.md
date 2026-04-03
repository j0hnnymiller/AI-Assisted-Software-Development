---
ai_generated: true
model: "openai/gpt-5.4@unknown"
operator: "github-copilot"
chat_id: "assessment-process-slide-deck-20260402"
prompt: |
  create a marp slide deck describing the assessment process. include slides to demo significant artifacts. include speaker notes in the pandoc format.

  also include slides to demo the ai guardrails
started: "2026-04-02T18:50:00Z"
ended: "2026-04-02T19:20:10Z"
task_durations:
  - task: "assessment process research"
    duration: "00:11:30"
  - task: "slide deck drafting"
    duration: "00:13:40"
  - task: "provenance logging and README update"
    duration: "00:05:00"
total_duration: "00:30:10"
ai_log: "ai-logs/2026/04/02/assessment-process-slide-deck-20260402/conversation.md"
source: "user-request"
marp: true
theme: default
paginate: true
headingDivider: 2
style: |
  section {
    font-family: Aptos, "Segoe UI", sans-serif;
    background:
      radial-gradient(circle at top right, #e8f2ff 0%, transparent 30%),
      linear-gradient(135deg, #f7fbff 0%, #eef4ea 100%);
    color: #17324d;
  }
  h1, h2, h3 {
    color: #0e4a6d;
  }
  strong {
    color: #0b6b57;
  }
  code {
    background: rgba(255,255,255,0.7);
    border-radius: 0.2rem;
    padding: 0.05rem 0.2rem;
  }
  table {
    font-size: 0.82em;
  }
  .notes {
    display: none;
  }
---

# IEC 62304 Assessment Process

Assessment workflow, artifact demo, and AI guardrails

**Repository:** CODE-Presents-AIASD-Compliance
**Baseline Example:** Assessment 1 for D0003329 Rev 03 Final

::: notes
- Open by framing this as an operational walkthrough, not a theory deck.
- The goal is to show how the repository turns an IEC 62304 assessment into a repeatable, auditable process.
- Tell the audience that the demo section will use Assessment 1 artifacts because it is the current baseline and has the most complete outputs.
:::

---

## Why This Process Exists

- Create a repeatable baseline assessment against IEC 62304
- Produce decision-ready outputs for engineering and leadership
- Preserve audit evidence for how findings were generated
- Keep AI assistance inside explicit quality and provenance guardrails

**Assessment 1 outcome:** 66% overall compliance, 34 total gaps, 8 critical

::: notes
- Emphasize that the process is designed to answer three questions: what is compliant, what is missing, and what should be fixed first.
- Call out that the process is not only about analysis quality; it is also about reproducibility and inspection readiness.
- Mention that the baseline example found substantial compliance but still surfaced critical issues in risk management, legacy software, and problem resolution.
:::

---

## Inputs And Preconditions

| Input | Purpose |
| --- | --- |
| `sop/D0003329_Rev_03_Final.md` | Primary procedure under assessment |
| `standards/BSEN-62304.md` | Normative reference text |
| Related SOPs such as `sop/D0003098_Rev_05_Final.md` | Context for cross-references and controls |
| Standardized prompts in `.github/prompts/` | Consistent assessment method |
| AI provenance policy in `.github/instructions/` | Logging and metadata guardrails |

**Precondition:** start with a new assessment folder and decide the scope before running prompts.

::: notes
- Explain that the process intentionally front-loads context quality.
- The assessment quality drops quickly if the source SOP, the standard text, or the supporting SOPs are missing from context.
- Mention that the prompts are modular by clause, which makes the workflow parallelizable.
:::

---

## Process Overview

1. Create a new `assessments/assessment.{n}/` workspace
2. Run clause-specific assessments for 4.4, 5, 6, 7, 8, and 9
3. Synthesize findings into the comprehensive assessment
4. Generate executive, remediation, and projection outputs
5. Verify provenance, completion criteria, and README updates

**Execution model:** parallel clause analysis, then sequential synthesis

::: notes
- Walk the audience through the shape of the process: broad analysis first, consolidation second, governance checks last.
- Stress that the clause assessments are intentionally separate so that each clause can be reviewed independently before synthesis.
- This is the main reason the team can move quickly without losing traceability.
:::

---

## Phase 1 To 2: Clause Analysis Pipeline

| Phase | What Happens | Main Output |
| --- | --- | --- |
| Prep | Create folder, load source files, select prompts | Assessment workspace |
| Clause execution | Run prompts for 4.4, 5, 6, 7, 8, 9 | Six clause analysis files |
| Clause review | Check consistency, severity, citations | Normalized findings |

**Assessment 1 timing:** the parallel clause phase reduced total runtime by about 65% versus a sequential run.

::: notes
- Use this slide to explain why the process scales.
- In Assessment 1, clause analysis was the biggest leverage point for time savings.
- If asked why not do one large prompt, the answer is that smaller clause-scoped analyses are easier to verify and compare.
:::

---

## Phase 3 To 5: Synthesis And Decision Outputs

| Phase | Outcome | Audience |
| --- | --- | --- |
| Comprehensive synthesis | Unified compliance score, gap catalog, cross-cutting themes | Compliance leads, engineering |
| Executive summary | Leadership view, top gaps, roadmap, ROI | Senior stakeholders |
| Remediation planning | Gap-by-gap recommendations and implementation dependencies | Process owners |
| Projection analysis | Scenario-based improvement targets | Decision makers |
| Completion check | Deliverable checklist and quality verification | Auditors, maintainers |

::: notes
- Explain that the process deliberately produces different artifacts for different consumers.
- Engineering needs specificity, while leadership needs prioritization and resource framing.
- The completion document closes the loop by proving the required outputs and provenance are actually present.
:::

---

## Assessment 1 Artifact Set

- 6 clause-specific assessment files
- 1 comprehensive compliance assessment
- 1 executive summary
- 1 gap analysis and remediation recommendations document
- 1 projected compliance improvement analysis
- 1 completion summary

**Total content:** about 65,000 words across 11 deliverables

::: notes
- Position the artifact set as a documentation system, not a single report.
- Each artifact has a distinct job and should be treated as part of the compliance evidence package.
- Mention that the completion summary also documents the execution timeline and acceptance checks.
:::

---

## Demo Slide: Clause-Level Artifact

**Open:** `assessments/assessment.1/D0003329_REV_03_Final.Analysis.Clause7.md`

Demo points:

- Show clause-specific scoring and findings structure
- Point out the direct IEC 62304 references and severity language
- Highlight why Clause 7 was rated 55% and marked critical
- Show how a single clause artifact can stand alone for reviewer inspection

::: notes
- This is the first live artifact to open in the demo.
- Clause 7 is a strong example because it clearly shows both strengths and critical gaps.
- Call out that the artifact is independently useful during review because it contains citations, findings, and remediation direction in one place.
:::

---

## Demo Slide: Comprehensive Synthesis Artifact

**Open:** `assessments/assessment.1/D0003329_Rev_03_IEC62304_Compliance_Assessment_2026-04-01.md`

Demo points:

- Show the weighted compliance roll-up across clauses
- Review the gap severity distribution and critical gap list
- Explain the move from clause findings to a portfolio-level view
- Use it to answer: "What is the current compliance baseline?"

::: notes
- This is the artifact that converts clause analysis into a single operational picture.
- When presenting, focus on the overall score, the distribution of gap severity, and the cross-cutting implications.
- This is usually the anchor document for planning remediation work.
:::

---

## Demo Slide: Decision Artifacts

**Open in sequence:**

- `assessments/assessment.1/D0003329_REV_03_Final.IEC62304_Executive_Summary.md`
- `assessments/assessment.1/Gap_Analysis_and_Remediation_Recommendations.md`
- `assessments/assessment.1/Projected_Compliance_Improvement_Analysis.md`

What to show:

- Executive summary for leadership framing and top-10 gap view
- Remediation document for implementation detail and dependency mapping
- Projection analysis for scenario planning: 73%, 82%, 92%

::: notes
- This sequence shows how the same assessment supports different decision horizons.
- The executive summary is for prioritization, the remediation plan is for execution, and the projection analysis is for resource tradeoffs.
- If time is short, at least show the recommended Scenario B audit-ready path.
:::

---

## AI Guardrails: Before And During Assessment

- Use standardized prompts rather than ad hoc prompting
- Load the governing SOP and the standard text explicitly
- Keep clause scope bounded to reduce drift and improve reviewability
- Require structured filenames and assessment folders
- Capture exact prompt text, model, timestamps, and source references

**Guardrail intent:** make the process reproducible before content quality is judged.

::: notes
- Frame these as process controls rather than preferences.
- The key idea is that the repository constrains how AI is used so outputs are inspectable later.
- Explain that prompt standardization and explicit source loading are the two highest-value controls at the front of the workflow.
:::

---

## AI Guardrails: Artifact-Level Controls

| Guardrail | Evidence In Repo |
| --- | --- |
| YAML provenance front matter | `chat_id`, `ai_log`, model, operator, prompt |
| Conversation preservation | `ai-logs/YYYY/MM/DD/<chat-id>/conversation.md` |
| Session summary | `ai-logs/.../summary.md` |
| Completion verification | `assessments/.../ASSESSMENT_COMPLETION.md` |
| README registration | Root-level discoverability and traceability |

**Result:** no notable AI-generated artifact should be orphaned from its provenance trail.

::: notes
- This slide is about auditability.
- Show that the artifact, the conversation that produced it, and the repository index all point to each other.
- If someone asks how this helps IEC 62304, connect it to configuration management, review evidence, and procedural discipline.
:::

---

## Demo Slide: Guardrails In Action

**Open in sequence:**

- `.github/instructions/ai-assisted-output.instructions.md`
- `assessments/assessment.1/ASSESSMENT_COMPLETION.md`
- `ai-logs/2026/04/01/assessment-1-comprehensive-20260401/conversation.md`

What to show:

- Policy requirements for provenance and logging
- Completion checklist proving deliverables and metadata exist
- Conversation log as the underlying audit trail for an assessment artifact

::: notes
- This is the most important guardrail demo slide.
- The message is that the AI output is never just a markdown file; it is part of a controlled record.
- If the audience is skeptical about AI-assisted compliance work, this is the slide that addresses that concern directly.
:::

---

## What Success Looks Like

- The assessment is reproducible by another operator
- Every major finding traces back to a clause artifact or source document
- Leadership gets a concise decision package
- Remediation owners get a prioritized execution plan
- Auditors can inspect provenance without reconstructing the workflow manually

::: notes
- Close by tying the process back to operational outcomes.
- A good assessment process produces not just findings, but a maintained evidence chain and a practical remediation path.
- Invite the audience to treat the repository as both a delivery mechanism and a control system.
:::
