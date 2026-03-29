About John M. Miller

- Principal Software Developer/Architect CODE Staffing

- Played roles of developer, architect, devops engineer, platform
engineer, test architect, release manager

- Contributor to the AI Practitioner's View blog

Agenda

- Review of Part 1

- AI Assisted Workflow, Requirements, Instructions, Implementation
Prompts

- Implementation Prompt Execution

- Implementation Verification

- Executing Implementation Prompts

- Lessons Learned

- Iteration 3

- Tips and Tricks

- The "Nice to have" dilemma

"AI will not replace humans, but those who use AI will replace those who
don't."\
--- Ginni Rometty

AI Assisted Workflow

- From Requirements to a Solution

- Stakeholders define the requirements

- AI transforms the requirements into implementation instructions

- Stakeholders review and improve instructions

- AI uses instructions to create implementation prompts

- Stakeholders review and improve implementation prompts

- AI uses implementation prompts and implementation instructions to
implement the solution

- Stakeholders review and improve implementation

Business Rules as Instructions

Workflows

Workflows are use cases that guide data capture and processing in the
application. Implement the following workflows and ensure that all
business rules are enforced during their execution:

- Promote a Lecturer to Senior Lecturer

- Promote a Senior Lecturer to Associate Professor

- Promote an Associate Professor to Professor

- Assign a Class to an Academic

- Add a new Academic to the faculty capturing all required information
and allowing the capture of optional information.

- ...

Implementation Prompts

Topics:

- Prompt Creation

- Verification Logic

- Ensuring Safe Execution

Demo

Executing Prompts

Objective:

- Use prompts to guide agent actions and verify outcomes.

Tasks:

- Review existing prompts

- Execute via chat modes

- Test agent responses

- Verify results

---

## Executing Implementation Prompts

- Prompt: Implement Prompt x Task y
  - Starting with Prompt 6: implement prompt x task y. First write the
tests and the implement the code. Verify that all acceptance criteria
are met.
  - Keep changes
  - dotnet build
    - Prompt: Fix the compiler errors and warnings
  - dotnet test
    - Prompt: Fix the failing tests
- In the real world
  - Review the tests
  - Review the code
- Prompt: commit the changes and create a tag for Prompt x Task y
  - When all prompt tasks are completed
    - Prompt: Confirm that the Prompt x Success Criteria are met
    - Before proceeding to the next prompt
      - Zero compilation errors or warnings
      - Zero failing tests
- Prompt: Create a tag for the completion of Prompt x

Demo

- Build

- Test

- Run

.\\start-zeus-academia.ps1

API

Student Portal

Faculty Dashboard

Admin Interface

Lessons Learned

- Review the code, especially the test automation

- Keep, Commit often to keep change sets small

- Be a bit more prescriptive about the tech stack

- Be clear about the definition of done

- Tests, documentation, diagrams, etc.

- Don't proceed if there are errors

- Define the expected developer workflow

- Work on a development branch

- Test Automation

- Quality Gates

- Merge to main when the app is in a deployable state

- Treat AI as a highly productive junior developer

- Be clear about infrastructure constraints and standards

Next Iteration

- Issues to Address

- Prodding to create test automation

- Test automation instructs didn't take

- Reduce the number of test automation errors

- Too much time spent on fixing tests and code

- Reduce Gold-plating

- Improvements

- Implement Vertical Slicing

- Ask for Showcases

- Find ways to support multiple streams of development

- Take advantage of agent delegation

- Instructions for generating a UI from conceptual models and workflows

- UX Instructions

- UI Implementation Instructions

Zeus.Academia Second Iteration

- https://github.com/johnmillerATcodemag-com/zeus.academia.2

Tips and Tricks

- Prompting: When encountering errors that are possibly due to problems
in another tier, ask Copilot to write a prompt that can then be used to
trouble shoot the issue on the other tier

- Prompting: Quick Chat

- Stop and Continue

- Responses: Watch out for rabbit holes

The "Nice to Have" Dilemma

- Enterprise teams often maintain 300--500 items in their product
backlog, with some reporting over 1,000+ items depending on project
scope and organizational size.

- A case study from StackExchange noted a team with 400 backlog items,
completing only 5 per sprint (biweekly), leading to severe
prioritization challenges and duplication.

- According to Ruhani Rabin's backlog metrics guide, a growing backlog
signals that new items are being added faster than they're completed ---
often due to over-scoping or unrealistic projections.

- The last two-thirds of most backlogs are likely to change or become
obsolete before implementation, reinforcing the need for pruning and
consolidation.

**Free Subscription**

The leading software development magazine,\
written by expert developers for developers.

All registered attendees will receive a\
**free digital subscription** to CODE Magazine!

Share this link to our free subscription:\
**[bit.ly/JohnDEVINT2025]{.underline}**

Q&A\
\
Contact us with questions!

CODE Contact

codemag.com\
info@codemag.com\
facebook.com/codemag\
x.com/codemagazine

Presenter Contact

john.miller@codestaffing.com

www.linkedin.com/in/johnmichaelmiller
