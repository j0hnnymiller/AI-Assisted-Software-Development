---
ai_generated: true
model: "openai/gpt-5.4@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "exercise-create-and-use-custom-skill-20260321"
prompt: |
  create a marp exercise deck that guides student in creating, and using a custom skill
started: "2026-03-21T23:40:00Z"
ended: "2026-03-21T23:55:00Z"
task_durations:
  - task: "exercise design"
    duration: "00:06:00"
  - task: "slide authoring"
    duration: "00:07:00"
  - task: "manifest and provenance updates"
    duration: "00:02:00"
total_duration: "00:15:00"
ai_log: "ai-logs/2026/03/21/exercise-create-and-use-custom-skill-20260321/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---
## Exercise: Create and Use a Custom Skill

**Objectives**

- Create a repository skill folder under `.github/skills/`
- Author a `SKILL.md` file with a clear description and step-based procedure
- Use Copilot with a matching prompt so the new skill can guide a real task

**Activities**

- **Phase 1 - Create**: Add `.github/skills/slide-quality-check/SKILL.md` with metadata (`name`, `description`) and a short procedure for reviewing Marp slides for provenance and speaker notes
- **Phase 2 - Refine**: Improve the skill by adding strong trigger words such as `Marp`, `slide`, `speaker notes`, and `provenance`, then tighten the procedure so the output is deterministic
- **Phase 3 - Use**: Prompt Copilot with a task such as `Review slides/marp/exercise-create-and-use-custom-agent.deck.md for slide metadata and ::: notes compliance` and compare the output to a normal untuned chat response

**Success Criteria**

- Skill folder and `SKILL.md` exist in `.github/skills/slide-quality-check/`
- Copilot responds with a workflow aligned to the skill procedure instead of a generic answer
- Student receives a structured review that checks metadata, notes coverage, and suggested fixes

::: notes
Duration ~00:25

Facilitate this as a procedural-workflow lab, not just a markdown-file exercise. Start by explaining that a skill is different from a custom agent: the agent shapes role behavior, while the skill packages a repeatable method Copilot can load when the prompt matches the description.

In Phase 1, have learners create `.github/skills/slide-quality-check/SKILL.md` with a simple but concrete purpose. Encourage them to write a description that contains likely trigger phrases and a procedure with explicit steps such as inspect front matter, verify every slide has `::: notes`, and report missing or weak sections.

In Phase 2, ask students to improve the skill after reading it once as if they were Copilot. Typical improvements are sharper trigger words, more deterministic steps, and output requirements such as `return findings as pass/fail bullets with suggested fixes`.

In Phase 3, students run a prompt against an existing slide file and see whether Copilot behaves like it has loaded the skill. If the response is too generic, coach them to adjust either the prompt wording or the skill description so the relevance match is stronger.

Timing guidance: 8 minutes create, 7 minutes refine, 8 minutes use and compare, 2 minutes recap. Close by emphasizing that strong skills are concise, keyword-aware, and procedural enough to produce repeatable results without bloating every chat.
:::
