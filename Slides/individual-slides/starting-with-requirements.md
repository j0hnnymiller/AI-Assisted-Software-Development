---
marp: true
theme: default
paginate: true
---

## Starting with Project Requirements

::: notes
Shift to greenfield best practices: requirements, prompts, and verification workflows.
:::

---




## Business Rules as Requirements

![Slide 2 image](images/_Starting_with_Project_Requirements_slide02_4.png)

---




## Conceptual Models

Technology Agnostic
  - Transformable into Logical Models
Clarity
Expressive
Formal
Conceptual Models are not a requirement

---




## Object Role Models

A type of conceptual model
Supported by a Visual Studio Extension (NORMA)
Object Role Models are textual and visual
  - Text can be visualized
  - Diagrams can be verbalized
Textual representation is in a formal natural language that can be validated by subject matter experts

---




## Zeus.Academia.3b

Based on a publicly available model of a commonly understood domain
  - https://orm.net/pdf/ORMwhitePaper.pdf
Allows us to quickly move from requirements to implementation
  - https://github.com/johnmillerATcodemag-com/zeus.academia.3b
Why 3b?
  - Third Iteration in progress
  - If something is hard, do it often

---




## Use Cases

Use cases are specific scenarios that guide data capture and processing in the application
  - Promote a Lecturer to Senior Lecturer
  - Promote a Senior Lecturer to Associate Professor
  - Promote an Associate Professor to Professor
  - Assign a Class to an Academic
  - Add a new Academic to the faculty capturing all required information and allowing the capture of optional information

---

## Exercise: Generate Business Requirements

Objectives:
Use the Product Manager chat mode to create a requirements document for a calculator
Activities:
Activate the Product Manager chat mode
Prompt the AI to create a requirements document
Review the requirements
Add an implementation plan using vertical slices
Review the changes
Add a diagram showing the relationship between Phases, Slices, and User Stories
Success Criteria
The requirements document exists and passes review

::: notes
Duration ~00:20

Author requirement docs, then use Copilot to generate scaffolding and validate alignment.

Prompt: create a requirements document for a simple calculator application
:::

---




## Exercise: Create Project Requirement

Objective: Create project requirement instructions, some project-specific, some generic, using both manual and Copilot-assisted methods.
Manually create a business requirements.md file and add:
  - Business rules
  - Workflows
  - Purpose
  - Tech stack
  - Architecture
Use Copilot to generate instruction files using the copilot-instructions.md and the codebase for context.
Bonus:
Review instruction files for errors and omissions.
Ask Copilot to suggest changes based on evolving tech and practices.

::: notes
Author requirement docs, then use Copilot to generate scaffolding and validate alignment.
:::

---

## Exercise: Generate Business Requirements

Objectives:
Use the Product Manager chat mode to update the requirements document to implement using vertical slices
Activities:
Activate the Product Manager chat mode
Prompt the AI to add a vertical slices implementation plan
Review the changes
Add a diagram showing the relationship between Phases, Slices, and User Stories
Success Criteria
The implementation plan passes review

::: notes
Duration ~00:20

Prompts:

using #file:business-rules-to-slices.instructions.md update the #file:calculator-app-requirements.md implementation plan to implement using vertical slices

what is the difference between the phases and vertical slices?

update the plan to make this distinction clear

add a diagram that shows the phases -> slices -> use cases

which of the slices can be implemented in parallel and which have a dependancy on another slice
:::
