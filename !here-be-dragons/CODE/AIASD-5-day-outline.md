# AI-Assisted Software Development — 5-Day Workshop Outline

## Course Overview

- **Audience:** Software developers, architects, QA, and tech leads familiar with Git and at least one programming language.
- **Format:** 5 days, instructor-led, lectures + demos + hands-on labs, pair programming encouraged.
- **Learning Goals:** Safely and effectively use GitHub Copilot and LLMs to accelerate development, improve tests and documentation, and make low-risk changes to legacy code.
- **Materials:** [CODE/AIASD-slides.md](CODE/AIASD-slides.md), starter repos (calculator), VS Code with Copilot, sample legacy repo forks.
- **Assessment:** Daily lab deliverables, final legacy refactor mini-project, checklist-based review.

---

## Daily Structure (typical day)

- Morning lecture (60–90m): concepts + demos
- Midday hands-on lab (90m): guided exercises
- Afternoon project/practice (120m): deeper tasks, pair-review
- End-of-day checkpoint (30m): share progress, blockers, deliverables

---

## Day 1 — Foundations & Hands-On Intro

### Objectives

- Understand LLM basics, limitations, and safe usage.
- Configure Copilot and use Ask/Edit modes.
- Complete a small coding exercise to experience assisted development.

### Morning — Foundations

- Topics: LLM conceptual architecture, tokens & attention, capabilities vs limitations, software engineering vs "vibe coding".
- Deliverable: short discussion/quiz listing 3 risks and 3 mitigations when using LLMs.

### Midday — Copilot Overview

- Topics: Ask/Edit/Agent/Custom Chat Modes; instruction files vs prompt files vs chat modes; workspace guidance files.
- Demo: Configure Copilot in VS Code and show inline suggestions and Edit mode.

### Afternoon — Hands-On: Simple Calculator

- Exercise: Implement a CLI calculator (Golang recommended) using Ask Mode.
- Prompts to try: "Implement a simple command line calculator in Golang", "Add square root support", "Create unit tests for add/subtract".
- Deliverable: runnable calculator and initial unit tests (or failing TDD tests if chosen).

### Homework

- Fork a small repo for Day 3 legacy work; find a small Golang project with open issues.

---

## Day 2 — Prompting, Testing, and TDD with AI

### Objectives

- Master prompt engineering patterns and workspace-level instruction files.
- Use TDD with AI: write tests first, then implement.

### Morning — Effective Prompting & Instruction Files

- Topics: crafting multi-step prompts, constraining outputs, examples of `.copilot.json` & prompt files, prompt templates.
- Exercise: convert a vague prompt into a structured multi-step prompt with expected outputs.

### Midday — TDD with AI

- Exercise: Write tests for calculator memory/logging features first (tests intentionally fail).
- Deliverable: test-suite with failing tests that fully describe desired behavior.

### Afternoon — Edit Mode & Safe Edits

- Topics: read-only exploration (explain, review), safe automated edits, edit-review checklist, small refactors that preserve behavior.
- Exercise: Use Edit Mode to implement helper functions and run tests.

### Checkpoint

- Pair-review a teammate's test-first changes and provide feedback.

---

## Day 3 — Working with Legacy Code & Risk Management

### Objectives

- Learn legacy-code analysis techniques and how to minimize change risk.
- Produce an initial test plan and component summary for a real repo.

### Morning — Legacy Code Theory

- Topics: what is legacy code, evergreen code characteristics, safety nets for changes.
- Reading: selected excerpt from _Working Effectively with Legacy Code_.

### Midday — Exploration Techniques (Read-only)

- Exercise: Load your forked repo, use Copilot/Chat to summarize modules, surface likely risks, and propose tests to add.
- Deliverable: component summary document and prioritized test plan.

### Afternoon — Small Safe Change (Vertical Slice)

- Objective: implement a minimal end-to-end improvement (bug fix or small feature) with tests and a rollback plan.
- Exercise: make the change on a feature branch, write unit/regression tests, and create a PR description with risk analysis.

---

## Day 4 — Advanced Copilot Modes, Governance & IP

### Objectives

- Use custom chat modes and agents for team workflows.
- Understand IP, privacy, and governance for Copilot in organizations.

### Morning — Chat Modes & Agents

- Topics: authoring a Chat Mode persona (code reviewer persona), agent-based workflows for multi-step automation.
- Exercise: create a Chat Mode that enforces tests-first feedback and suggested edits.

### Midday — Governance, Security, Legal

- Topics: Copilot for Business/Enterprise protections, public-code filter, secrets policy, licensing risks.
- Deliverable: Team policy checklist covering prompt hygiene, secrets handling, and public-code filter settings.

### Afternoon — Automation & CI Integration

- Objective: add AI-assisted automation into CI (test generation, linting suggestions, basic PR checks).
- Exercise: create an example `.github/workflows` snippet that runs tests and a simple generated-test validation step.

---

## Day 5 — Capstone: Legacy Refactor Mini-Project & Review

### Objectives

- Deliver an end-to-end vertical slice on a real forked repo using AI assistance.
- Produce evergreen artifacts: tests, docs, CI rules, and instruction files.

### Morning — Planning & Triage

- Activity: Teams pick a mini-project from their forks and break it into vertical slices with acceptance criteria.

### Midday & Afternoon — Implement Slices

- Activity: Implement at least one full vertical slice: code + tests + docs + PR.
- Deliverable: review-ready PR, test coverage notes, demonstration of behavior and risk mitigation.

### Late Afternoon — Retrospective & Evergreen Checklist

- Deliverable: Team retrospective notes and a shared "Keep-It-Evergreen" checklist (tests, docs, CI, instruction files, prompt hygiene).

---

## Prompts Bank (selected)

- Implement CLI calculator in Golang
- "Write tests for a memory feature that stores previous calculations (TDD)"
- "Explain this module and list likely edge cases and tests to add"
- "Suggest minimal safe refactor to add dependency injection for testability"

## Instructor Resources & Templates

- Lecture slides: [CODE/AIASD-slides.md](CODE/AIASD-slides.md)
- Lab starter: `calculator` sample repo (include README with run/test commands)
- PR template: summary, risk, test plan, rollback steps
- Team policy checklist: prompt hygiene, secrets policy, public-code filter settings

## Evaluation Rubric (brief)

- Lab completeness (30%): functionality & tests
- Test quality (25%): coverage, edge cases, TDD discipline
- Safety & risk mitigation (20%): small changes, rollback plan
- Documentation & CI integration (15%)
- Team collaboration & retrospective insights (10%)

---

## Next Steps

1. Instructor: review the outline and request any customizations (language choices, timing adjustments, extra labs).
2. I can split this into per-day markdown lesson files or produce a printable PDF/slide-ready version — tell me which you want.
