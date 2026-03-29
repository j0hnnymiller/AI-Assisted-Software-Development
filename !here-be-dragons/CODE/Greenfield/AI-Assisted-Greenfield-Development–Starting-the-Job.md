- AI Assisted Workflow

- Project Requirements

- What requirements?

- Conceptual Model

- Workflows

- Instructions

- What are Copilot instructions

- Creating Instructions

- Generating Instructions

- Implementation Prompts

- Tips and Tricks

- Part 2

- Next Steps

"AI will not replace humans, but those who use AI will replace those who
don't."\
--- Ginni Rometty

High Level AI Assisted Workflow

- From Requirements to a Solution
  - Stakeholders define the requirements
  - AI transforms the requirements into implementation instructions
  - Stakeholders review and improve instructions
  - AI uses instructions to create implementation prompts
  - Stakeholders review and improve implementation prompts
  - AI uses implementation prompts and implementation instructions to implement the solution
  - Stakeholders review and improve implementation

## Project Requirements

Key Elements:

- Business Rules
- Workflows
- Tech Stack
- Architecture

## Business Rules as Instructions

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

## Zeus.Academia.2

- Based on a publicly available model of a commonly understood domain
  - [https://orm.net/pdf/ORMwhitePaper.pdf](https://orm.net/pdf/ORMwhitePaper.pdf)
- Allows us to quickly move from requirements to implementation
  - [https://github.com/johnmillerATcodemag-com/zeus.academia.2](https://github.com/johnmillerATcodemag-com/zeus.academia.2)
- Why 2?
  - Second Iteration
  - Third in planning
  - If something is hard, do it often

---

## Use

Use cases are specific scenarios that guide data capture and processing in the
application

- Promote a Lecturer to Senior Lecturer
- Promote a Senior Lecturer to Associate Professor
- Promote an Associate Professor to Professor
- Assign a Class to an Academic
- Add a new Academic to the faculty capturing all required information
and allowing the capture of optional information

---

- ...

Demo

Create Project Requirements

Objective:

- Create project requirement instructions manually

Tasks:

- business-rules.md

- Purpose, Include business rules, workflows

Copilot Instructions Files

Instruction files acts as a guide for Copilot

- Located in

- .github/instructions -- project scoped

- User data folder -- user scoped

- Helps Copilot to:

- Understand the project\'s context and requirements.

- Generate consistent, high-quality code.

- Follow best practices and coding standards.

- Adapt to specialized tools and workflows.

Demo

Generate Instruction Files

Objective:

- Generate instruction files with Copilot.

Tasks:

- Run generate-instructions-prompt.md

- Use Copilot to generate contextual instructions

- Review and refine with AI suggestions

Implementation Prompts

Topics:

- Prompt Creation

- Verification Logic

- Ensuring Safe Execution

Demo

Objective:

- Generate Implementation Prompts with Copilot

Tasks:

- Review generate-implementation-prompts-prompt.md

- Use Copilot to generate prompts to implement solution

- These prompts can be used to guide a traditional implementation or an
AI assisted implementation

## Tips and Tricks

- VS Code Setting: \@id:terminal.integrated.focusAfterRun = terminal

- Instructions: Before making code changes, file modifications, or
system operations describe:
  - What I want to change
  - Where the changes will be made
  - Why the changes are necessary
  - How the changes will impact the system
  - Ask for permission to proceed with the changes
- Instructions: When running automated tests, report the code coverage
metrics
- Instructions: Separate the instruction into to groups, project
specific and generic.

---

## Part 2 -- Finishing the Job

- Implementation Prompt Execution
- Implementation Verification
- Lessons Learned
- Iteration 3
- Tips and Tricks
- The "Nice to have" dilemma
---

## Zeus.Academia Second Iteration

- https://github.com/johnmillerATcodemag-com/zeus.academia.2

Q&A and Next Steps

CODE Contact

codemag.com\
info@codemag.com\
facebook.com/codemag\
x.com/codemagazine

Presenter Contact

john.miller@codestaffing.com

www.linkedin.com/in/johnmichaelmiller

**Free Subscription**

The leading software development magazine,\
written by expert developers for developers.

All registered attendees will receive a\
**free digital subscription** to CODE Magazine!

Share this link to our free subscription:\
**[bit.ly/JohnDEVINT2025]{.underline}**
