---
marp: true
_class: lead
paginate: true
backgroundColor: "#fff" # Ensure the color value is quoted
---

# AI Assisted Software Development

## John Michael Miller

Senior Software Engineer at Code Staffing

Played roles of developer, architect, devops engineer, platform engineer, test architect, release manager

AI/ML Enthusiast and advocate for Effectively using AI to write code

- LinkedIn: `www.linkedin.com/in/johnmichaelmiller`
- Email: `john.miller@codestaffing.com`
- Blog: `https://codemag.com/blog/AIPractitioner`

---

# Day Four -- Greenfield Development

---

## But first...

Update on running prompts in GitHub Workflows

---

## High Level AI Assisted Workflow

CODE/Greenfield/AIASD-Workflow.png

- AI Assisted Workflow
- Project Requirements
  - What requirements?
  - Conceptual Models
  - Workflows
- Instructions
  - What are Copilot instructions
  - Creating Instructions
  - Generating Instructions
- Implementation Prompts
  - Implementation Verification
  - Executing Implementation Prompts
- Lessons Learned
- Iteration 3
- Tips and Tricks

---

## Exercise #1 -- Fork the repos

**Objective**: Fork the course repos

- Search GitHub for
  - AI-Assisted-Software-Development
  - zeus.academia.2
  - zeus.academia.3a
- Fork the repos
  - This will create a personal copy under your GitHub account
  - You can make changes without affecting the original repo

---

## Starting with Project Requirements

- Business rules
- Workflows
- Tech stack
- Architecture

::: notes
Shift to greenfield best practices: requirements, prompts, and verification workflows.
:::

---

## High Level AI Assisted Workflow

![AIASD Workflow](C:\git\AI-Assisted-Software-Development-Course\CODE\Greenfield\AIASD-Workflow.png)

- From Requirements to a Solution
  - Stakeholders define the requirements
  - AI transforms the requirements into implementation instructions
  - Stakeholders review and improve instructions
  - AI uses instructions to create implementation prompts
  - Stakeholders review and improve implementation prompts
  - AI uses implementation prompts and implementation instructions to implement the solution
  - Stakeholders review and improve implementation

---

## Project Requirements

Key Elements:

- Business Rules
- Workflows
- Tech Stack
- Architecture

---

# Business Rules as Instructions

---

## Conceptual Models

- Technology Agnostic
  - Transformable into Logical Models
- Clarity
- Expressive
- Formal
- Conceptual Models are not a requirement

---

## Object Role Models

- A type of conceptual model
- Supported by a Visual Studio Extension (NORMA)
- Object Role Models are textual and visual
  - Text can be visualized
  - Diagrams can be verbalized
- Textual representation is in a formal natural language that can be
  validated by subject matter experts

---

## Zeus.Academia.3b

- Based on a publicly available model of a commonly understood domain
  - [https://orm.net/pdf/ORMwhitePaper.pdf](https://orm.net/pdf/ORMwhitePaper.pdf)
- Allows us to quickly move from requirements to implementation
  - [https://github.com/johnmillerATcodemag-com/zeus.academia.2](https://github.com/johnmillerATcodemag-com/zeus.academia.2)
- Why 3b?
  - Third Iteration
  - If something is hard, do it often

---

## Use Cases

Use cases are specific scenarios that guide data capture and processing in the
application

- Promote a Lecturer to Senior Lecturer
- Promote a Senior Lecturer to Associate Professor
- Promote an Associate Professor to Professor
- Assign a Class to an Academic
- Add a new Academic to the faculty capturing all required information
  and allowing the capture of optional information

---

## Exercise: Create Project Requirement Instructions

- **Objective**: Create project requirement instructions, some
  project-specific, some generic, using both manual and Copilot-assisted
  methods.

- Manually create a business-requirements.md file and add:

  - Business rules
  - Workflows
  - Purpose
  - Tech stack
  - Architecture

- Use Copilot to generate instruction files using the
  business-requirements.md and the codebase for context.

**Bonus**:

- Review instruction files for errors and omissions.
- Ask Copilot to suggest changes based on evolving tech and practices.

::: notes
Author requirement docs, then use Copilot to generate scaffolding and validate alignment.
:::

---

# Day Five Agenda -- New Development

- Creating Custom Chat Modes
- Generating Implementation Prompts & Verification
- Exercises
- Wrap-Up and Open Q&A

::: notes
Final day: custom chat modes, verification prompts, and wrap-up exercises.
:::

---

## Exercise #10 -- Generate Instruction Files

**Objective**: Create instruction files, some project-specific, some
generic, using both manual and Copilot-assisted methods.

- Manually create a copilot-instructions.md file and add:
  - Business rules
  - Workflows
  - Purpose
  - Tech stack
  - Architecture
- Use Copilot to generate instruction files using the
  copilot-instructions.md and the codebase for context.

**Bonus**:

- Review instruction files for errors and omissions.
- Ask Copilot to suggest changes based on evolving tech and practices.

::: notes
Generate both project-specific and generic instructions; review and iterate.
:::

---

## Creating Custom Chat Modes

- Personas
- Workflows
- Examples
- Agents
- Allowing agents to take autonomous action
- agent.json
  - Safe commands
  - Unsafe commands

::: notes
Discuss persona design, safe command lists, and agent.json structure for safe automation.
:::

---

## Exercise #11 -- Creating Custom Chat Modes

**Objective**: Create custom chat modes for the project.

- Define personas and workflows for each chat mode.
- Implement chat modes using Copilot assistance.
- Create an agent.json file with safe commands.
- Test the agent's ability to execute safe commands.

::: notes
Practical steps: define personas, implement agent.json, and test allowed actions in a sandbox.
:::

---

## Generating Implementation Prompts & Verification

- Implementation prompts
- Implementation verification

::: notes
Teach how to craft reproducible prompts and verification checks to validate generated code.
:::

---

## Exercise #12 -- Executing Prompts

**Objective**: Execute implementation prompts using custom chat modes.

- Review the implementation prompts created earlier.
- Use prompts to guide agent actions.
- Test agent responses to prompts.
- Verify implementation passes verification checks.

::: notes
Execute prompts in custom modes, verify outputs, and refine prompts based on failures.
:::

---

## Wrap-Up and Open Q&A

- Review the day's learning outcomes.
- Address questions or concerns.
- Discuss next steps and future learning opportunities.

::: notes
Summarize key takeaways, next steps, and open the floor for questions and feedback.
:::
