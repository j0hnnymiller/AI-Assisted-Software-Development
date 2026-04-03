---
ai_generated: true
model: "openai/gpt-5.3-codex@2026-03-21"
operator: "johnmillerATcodemag-com"
chat_id: "exercise-create-and-use-custom-agent-20260321"
prompt: |
  create a marp exercise deck that guides student in creating, and using a custom agent
started: "2026-03-21T23:35:00Z"
ended: "2026-03-21T23:50:00Z"
task_durations:
  - task: "exercise design"
    duration: "00:06:00"
  - task: "slide authoring"
    duration: "00:07:00"
  - task: "manifest and provenance updates"
    duration: "00:02:00"
total_duration: "00:15:00"
ai_log: "ai-logs/2026/03/21/exercise-create-and-use-custom-agent-20260321/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---

# Exercise: Create and Use a Custom Agent || Exercise: Build the AI That Does Your Job (Just This One Task)

---

## Exercise: Create and Use a Custom Agent

**Objectives**
  - Create a repository-scoped custom agent file in `.github/agents/`
  - Configure a clear agent role, description, and tool scope
  - Use the agent in Copilot Chat to complete a targeted task

**Activities**
  1. Create: Add `.github/agents/test-specialist.agent.md` with frontmatter (`name`, `description`, `tools`) and focused behavior instructions
  2. Refine: Tighten scope by clarifying what the agent should do and refuse, then save and re-open chat
  3. Use: Select the new custom agent in Copilot Chat and run a prompt such as “Review this feature and propose a test plan with unit and integration tests”

::: column

**Success Criteria**
  - Agent appears in Copilot Chat agent picker after file creation
  - Agent responses stay within the declared role and tool boundaries
  - Student receives a usable, structured output aligned to the prompt goal

::: notes
Duration ~00:25

Facilitate this as a role-scoping lab, not just a file-authoring task. Start by showing students that a custom agent is essentially a reusable behavioral contract: it combines role intent, tool limits, and execution style.

In Phase 1, have learners create `.github/agents/test-specialist.agent.md` with a concise description and explicit tools list. Encourage strong verbs and constraints, for example "analyze tests, propose coverage improvements, avoid production-code refactors unless asked".

In Phase 2, ask each student to improve one weak instruction in their agent definition. Typical improvements are adding refusal boundaries, output format requirements, or quality checks such as "include risks and assumptions".

In Phase 3, students activate the agent and run one practical prompt against current repo files. Debrief by comparing outputs from default mode versus custom agent mode, then discuss where the custom agent improved consistency and where additional refinement is needed.

Timing guidance: 8 minutes create, 7 minutes refine, 8 minutes run and compare, 2 minutes recap. Close by emphasizing iterative agent tuning and least-privilege tool access as core best practices.
:::
