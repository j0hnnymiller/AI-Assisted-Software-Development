# Day 4 Morning Session - Hands-On Labs

## Greenfield Development with AI Assistance

---

## Lab Overview

These hands-on labs are designed to reinforce the concepts covered in the Day 4 Morning Session, focusing on Greenfield development using AI assistance, vertical slice architecture, conceptual modeling with ORM, and systematic prompt-based development workflows.

---

## Lab 1: GitHub Actions Workflow with Prompt Execution (45 minutes)

### Objective

Create a GitHub Actions workflow that executes a prompt on pull requests to validate code style and business rules.

### Prerequisites

- GitHub repository with code
- Access to OpenAI API or GitHub Copilot CLI
- Understanding of GitHub Actions and workflows

### Tasks

#### Task 1.1: Set Up the Style Check Script

1. Create a Python script `style-checker.py` that:
   - Accepts an instruction/prompt file as input
   - Reads changed files from a pull request
   - Uses an AI API (OpenAI, Azure OpenAI, or GitHub Copilot) to analyze code
   - Returns style violations in a structured format

2. Configure your script to support multiple AI providers:
   - OpenAI API
   - Azure OpenAI
   - GitHub Copilot CLI (gh copilot suggest)

**Hint**: Remember the lesson learned - the GitHub Copilot CLI's `suggest` command is designed for interactive command suggestions, not structured data analysis. Use the API approach instead.

#### Task 1.2: Create the GitHub Actions Workflow

1. Create `.github/workflows/style-check.yml`
2. Configure the workflow to:
   - Trigger on pull request events
   - Install necessary dependencies (e.g., OpenAI SDK)
   - Run the style checker script
   - Post results as a PR comment

3. Add the required API key as a GitHub Secret:
   - Go to Settings → Secrets and variables → Actions
   - Add `OPENAI_API_KEY` (or equivalent for your chosen provider)

#### Task 1.3: Create an Instruction File

1. Create `.github/copilot/Promptfiles/style-guidelines.md` with:
   - Coding standards for your language
   - Naming conventions
   - Specific style rules to check

#### Task 1.4: Test the Workflow

1. Create a test file with intentional style violations:
   - Incorrect naming conventions
   - Missing documentation
   - Improper indentation
   - Hardcoded values that should be constants

2. Create a pull request with these violations
3. Verify the workflow:
   - Executes successfully
   - Identifies violations
   - Posts a detailed comment on the PR

### Deliverables

- Working GitHub Actions workflow
- Style checker script supporting at least one AI provider
- Instruction file with style guidelines
- Screenshot of PR comment showing detected violations

### Bonus Challenge

- Implement support for Azure DevOps pipelines instead of GitHub Actions
- Add severity levels to violations (error, warning, suggestion)
- Create a custom action that can be reused across repositories

---

## Lab 2: Vertical Slice Architecture Implementation (60 minutes)

### Objective

Implement a feature using vertical slice architecture with AI assistance, creating a complete end-to-end feature from UI to data layer.

### Prerequisites

- .NET, Node.js, or Python development environment
- Understanding of MVC/MVVM patterns
- GitHub Copilot or similar AI coding assistant

### Background

Vertical slice architecture organizes code by features rather than technical layers, allowing complete features to be implemented independently from UI through to database.

### Tasks

#### Task 2.1: Create Instruction Files for Vertical Slices

1. Create `.github/copilot-instructions.md` with:
   - Feature-centric organization structure
   - Naming conventions for features
   - CQRS pattern guidelines
   - Folder structure template:
     ```
     /Features
       /[FeatureName]
         - Command.cs
         - Handler.cs
         - Validator.cs
         - Repository.cs
         - DTOs.cs
     ```

2. Create a business rules instruction file:
   - Define validation rules
   - Specify business constraints
   - Document any exclusion or unique constraints

#### Task 2.2: Implement a User Registration Feature

Using AI assistance, create a complete user registration feature that includes:

1. **Command/Query Object**:
   - `RegisterUserCommand` with necessary properties
   - Input validation attributes

2. **Handler**:
   - Process the registration request
   - Apply business rules
   - Return appropriate results

3. **Validator**:
   - Validate email format
   - Check password strength
   - Verify unique username

4. **Repository**:
   - Data access layer
   - Database context integration

5. **API Endpoint**:
   - RESTful endpoint for registration
   - Proper HTTP response codes
   - Error handling

6. **Basic UI Component**:
   - Registration form
   - Client-side validation
   - Success/error feedback

#### Task 2.3: Verify Independence

Test that your vertical slice is:

1. Independently deployable
2. Testable in isolation
3. Self-contained with minimal dependencies

### Deliverables

- Complete vertical slice implementation
- Unit tests for the feature
- Documentation showing the feature structure
- Demo of the working feature

### Bonus Challenge

- Implement feature flags to enable/disable the feature
- Add a second feature using the same architecture
- Create prompt templates for generating new vertical slices

---

## Lab 3: Conceptual Modeling with ORM Diagrams (45 minutes)

### Objective

Create an Object-Role Model (ORM) diagram to define business rules and use it to generate implementation artifacts with AI assistance.

### Prerequisites

- Understanding of business domain modeling
- Basic knowledge of entity relationships
- Access to a diagramming tool or text-based modeling

### Background

ORM (Object-Role Modeling) provides a formal, graphical way to capture business rules and constraints that is both human-readable and machine-processable.

### Tasks

#### Task 3.1: Create a Simple ORM Model

Choose a simple domain (e.g., library system, course enrollment, project management) and create an ORM model that includes:

1. **Entities** (at least 3):
   - Students, Courses, Enrollments
   - OR: Books, Authors, Borrowers
   - OR: Your own domain

2. **Facts/Predicates** showing relationships:
   - "Student is enrolled in Course"
   - "Student has StudentID"
   - "Course has maximum enrollment"

3. **Constraints**:
   - **Uniqueness constraints**: bars indicating which roles uniquely identify instances
   - **Mandatory constraints**: dots showing required relationships
   - **Exclusion constraints**: XOR relationships
   - **Value constraints**: allowed values for specific roles

4. **Subtyping** (if applicable):
   - Inheritance relationships
   - Subtype constraints

#### Task 3.2: Verbalize Your Model

1. Write out the natural language statements for each fact:
   - "Each Student is enrolled in zero or more Courses"
   - "Each Course has exactly one maximum enrollment count"

2. Document all constraints in plain English:
   - "A student cannot audit a course they are enrolled in"
   - "An instructor must work for the department they head"

#### Task 3.3: Generate Implementation Using AI

Using your ORM model as context:

1. Create a prompt file that includes:
   - The verbalized business rules
   - Entity definitions
   - Constraint descriptions

2. Ask AI to generate:
   - Database schema (SQL or NoSQL)
   - Entity classes/models
   - Validation logic for constraints
   - Repository interfaces

3. Review the generated code for:
   - Correct implementation of constraints
   - Proper relationship modeling
   - Business rule enforcement

#### Task 3.4: Create Instruction Files from ORM

1. Create `business-rules-to-vertical-slices.instructions.md`:
   - How to interpret ORM entities as features
   - How to enforce constraints in validation logic
   - How to implement relationships

2. Create specific prompts for:
   - Database schema generation
   - Entity class generation
   - Use case implementation

### Deliverables

- ORM diagram (can be hand-drawn/scanned, or digital)
- Natural language verbalization document
- Generated code artifacts (schema, entities, validators)
- Instruction files for future use

### Bonus Challenge

- Use NORMA extension in Visual Studio to create formal ORM models
- Generate multiple technology implementations (e.g., SQL, MongoDB, Neo4j)
- Create test cases directly from ORM constraints

---

## Lab 4: Systematic Greenfield Development Workflow (90 minutes)

### Objective

Build a small application from scratch using a systematic, AI-assisted workflow similar to the one demonstrated in the training.

### Prerequisites

- Development environment for your chosen stack
- GitHub Copilot or equivalent AI assistant
- Understanding of CQRS and vertical slices

### Project Scenarios (Choose One)

#### Option A: Course Management System

A simplified system for managing academic courses, enrollments, and faculty assignments.

**Required Features**:

- Student dashboard showing enrolled courses
- Faculty dashboard showing teaching assignments
- Course enrollment workflow
- Grade submission

#### Option B: Project Task Tracker

A lightweight project management tool for tracking tasks and assignments.

**Required Features**:

- Project dashboard showing active projects
- Task creation and assignment
- Status tracking workflow
- Team member management

#### Option C: Library Management System

A system for managing books, borrowers, and checkouts.

**Required Features**:

- Catalog search and browse
- Checkout/return workflow
- Borrower management
- Overdue tracking

### Tasks

#### Phase 1: Requirements and Modeling (20 minutes)

1. **Create Use Cases**:
   - List 3-5 primary use cases
   - Write brief descriptions
   - Identify actors and preconditions

2. **Create ORM/Conceptual Model**:
   - Identify entities and relationships
   - Define business rules and constraints
   - Document in text or diagram form

3. **Define Vertical Slices**:
   - List features to implement
   - Prioritize by value and dependency
   - Plan implementation order

#### Phase 2: Set Up Instruction Files (15 minutes)

Create the following instruction files in `.github/copilot-instructions/`:

1. `vertical-slices-implementation.instructions.md`:
   - Feature-centric folder structure
   - CQRS pattern usage
   - Naming conventions

2. `business-rules.instructions.md`:
   - Your ORM-derived business rules
   - Constraint enforcement guidelines
   - Validation patterns

3. `api-patterns.instructions.md`:
   - RESTful endpoint conventions
   - Error handling patterns
   - Response formats

4. `ui-patterns.instructions.md`:
   - Component structure
   - State management approach
   - Error display patterns

#### Phase 3: Implement First Vertical Slice (30 minutes)

Using AI assistance throughout:

1. **Backend Implementation**:
   - Create command/query objects
   - Implement handler with business logic
   - Create validator
   - Implement repository/data access
   - Create API endpoint

2. **Frontend Implementation**:
   - Create UI component
   - Wire up API calls
   - Add validation feedback
   - Implement error handling

3. **Testing**:
   - Write unit tests for business logic
   - Test API endpoints
   - Verify UI functionality

#### Phase 4: Debugging and Refinement (15 minutes)

1. Run your application
2. Use browser developer tools to capture console errors
3. Use the "copy console" technique to feed errors to AI
4. Iterate on fixes until the feature works

#### Phase 5: Add Second Feature (10 minutes)

1. Implement a second, related vertical slice
2. Reuse instruction files
3. Verify feature independence
4. Test integration between features

### Workflow Tips

**Prompting Strategy**:

1. Start with: "Using the instruction files in this repository, create a [feature name] feature"
2. Reference specific business rules: "This feature must enforce the constraint that..."
3. Request specific artifacts: "Generate the Command, Handler, Validator, and Repository for..."
4. For UI: "Create a [framework] component that calls the [endpoint] API"

**Debugging Strategy**:

1. Run application frequently
2. Check both frontend console and backend logs
3. Copy entire error messages to AI
4. Ask: "I'm seeing this error: [paste]. What changes are needed?"
5. If the error is frontend-related but caused by backend, ask AI to "create a prompt for investigating this on the backend"

**Simple Browser Technique**:

1. Open app in VS Code Simple Browser
2. Use "Add element to chat" to select UI elements
3. Request specific UI changes: "Add more spacing between these elements"
4. Use continuous selection for complex UI regions

### Deliverables

- Working application with at least 2 vertical slices
- Complete set of instruction files
- ORM/conceptual model documentation
- README documenting your development process

### Bonus Challenge

- Implement CI/CD pipeline for deployment
- Add feature flags for toggling features
- Create architectural decision records (ADRs)
- Implement logging and observability

---

## Lab 5: Multi-Repository Coordination (Optional, 30 minutes)

### Objective

Practice coordinating AI assistance across separate frontend and backend repositories.

### Prerequisites

- Completion of Lab 4
- Understanding of client-server architecture

### Tasks

#### Task 5.1: Split Your Application

1. Separate your application into two repositories:
   - Frontend repository
   - Backend API repository

2. Update instruction files for each:
   - Backend focuses on API patterns, data models, business rules
   - Frontend focuses on UI patterns, state management, API integration

#### Task 5.2: Cross-Repository Debugging

1. Introduce an intentional mismatch:
   - Change an API endpoint path in backend
   - Keep old path in frontend

2. Run the application and capture frontend error

3. Use AI to generate a cross-repository prompt:
   - In frontend chat: "Create a detailed prompt for the backend team to investigate this API error"
   - Copy that prompt to backend chat
   - Let AI in backend repo identify and fix the issue

#### Task 5.3: Coordinated Feature Development

1. Plan a new feature that requires changes in both repositories
2. Create prompts for both sides:
   - Backend: API endpoint requirements
   - Frontend: UI and integration requirements
3. Implement in parallel using AI assistance
4. Integrate and test

### Deliverables

- Two separate repositories
- Documentation of cross-repository workflow
- Example prompts for coordination

---

## Lab 6: Instruction File Iteration and Improvement (Optional, 30 minutes)

### Objective

Learn to iteratively improve instruction files based on AI output quality.

### Tasks

#### Task 6.1: Baseline Implementation

1. Create a simple feature using minimal instruction files
2. Document issues with the generated code:
   - Incorrect patterns
   - Missing business rules
   - Inconsistent naming
   - Missing error handling

#### Task 6.2: Enhance Instructions

1. Update your instruction files to address each issue
2. Add specific examples of desired patterns
3. Include negative examples (what NOT to do)
4. Add validation checklists

#### Task 6.3: Re-generate and Compare

1. Delete the original implementation
2. Use the same prompts with enhanced instructions
3. Compare results
4. Document improvements

#### Task 6.4: Create Instruction File Templates

1. Create reusable templates for:
   - Architecture patterns
   - Business rule enforcement
   - Testing requirements
   - Documentation standards

### Deliverables

- Before/after comparison of generated code
- Improved instruction files
- Template library for future projects

---

## Additional Resources

### Key Concepts from Training

- **Vertical Slice Architecture**: Feature-centric organization enabling independent deployment
- **CQRS**: Command Query Responsibility Segregation pattern
- **ORM Modeling**: Conceptual modeling technique with rich constraint language
- **Systematic Prompting**: Using instruction files to guide AI consistently
- **Iterative Refinement**: Improving prompts and instructions based on output quality

### Recommended Reading

- Vertical Slice Architecture articles
- CQRS pattern documentation
- ORM (Object-Role Modeling) fundamentals
- GitHub Actions workflow syntax
- AI-assisted development best practices

### Tools Mentioned

- **NORMA**: Visual Studio extension for ORM modeling
- **GitHub Copilot**: AI pair programmer
- **Simple Browser**: VS Code's integrated browser with AI integration
- **GitHub Actions**: CI/CD automation platform

---

## Lab Completion Checklist

- [ ] Lab 1: Created and tested GitHub Actions workflow with prompt execution
- [ ] Lab 2: Implemented a complete vertical slice feature
- [ ] Lab 3: Created an ORM model and generated implementation artifacts
- [ ] Lab 4: Built a small application using systematic Greenfield workflow
- [ ] Lab 5 (Optional): Coordinated development across multiple repositories
- [ ] Lab 6 (Optional): Iterated on instruction files for improved quality

---

## Questions for Reflection

1. How did vertical slice architecture change your approach to feature implementation compared to traditional layered architecture?

2. What was the most effective instruction file you created, and why?

3. How did the ORM model help (or hinder) the implementation process?

4. What debugging techniques were most valuable when working with AI-generated code?

5. How would you adapt this workflow for your team's existing projects?

6. What additional instruction files would be valuable for your specific domain?

7. How can you balance AI assistance with manual coding for optimal results?

---

## Success Criteria

**Minimum Requirements**:

- Completed Labs 1, 2, and 3
- Working code for at least one vertical slice
- Documented instruction files
- Basic ORM model with business rules

**Proficiency Level**:

- Completed Labs 1-4
- Multiple vertical slices implemented
- Comprehensive instruction files
- Iterative refinement demonstrated
- Working end-to-end application

**Mastery Level**:

- Completed all labs including optional ones
- Cross-repository coordination demonstrated
- Template library created
- Architectural decision records
- Production-ready code quality
- CI/CD pipeline implemented

---

## Notes for Instructors

- Recommend 4-5 hours total for core labs (1-4)
- Optional labs add 1-2 hours
- Students should work in pairs for Lab 4
- Provide sample domains if students struggle with choices
- Emphasize the iterative nature of instruction file development
- Share examples of good instruction files
- Demonstrate the Simple Browser technique live
- Have backup API keys available for students
