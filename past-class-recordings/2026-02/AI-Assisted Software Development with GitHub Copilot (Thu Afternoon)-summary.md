# AI-Assisted Software Development with GitHub Copilot (Thu Afternoon)

## Overview

- **Total Duration**: 01:22:00
- **Sections**: 8
- **Format**: VTT (WebVTT)
- **Instructor**: John Miller
- **Session Focus**: Greenfield development workflow, instruction files, and vertical slicing architecture

---

## Section 1: Introduction and Repository Setup (Duration: 00:02:52) [ ]

### Key Topics

- Welcome back and screen sharing setup
- Updated repositories with core instruction files
- Greenfield branch introduction
- Product manager agent and prompt file for business requirements
- Calculator project setup

### Content Summary

- Instructor John Miller welcomes students back and shares his screen
- Both repositories (class repo and AIASD-2026) have been updated
- Students should pull from class repo and switch to Greenfield branch
- Core instruction files, agents, and prompt files are now available
- Goal: Generate business requirements document using the product manager agent

---

## Section 2: Business Requirements Generation Exercise (Duration: 00:17:04) [x]

### Key Topics

- Hands-on exercise: Creating business requirements document
- Using product manager agent
- Working with instruction files
- Version control and branching strategy
- Individual work on requirements documents

### Subsections

#### 2.1: Exercise Instructions (Duration: 00:03:00)

- Create personal branch from Greenfield branch
- Use product manager agent to generate requirements
- Utilize existing instruction files
- Build calculator requirements document

#### 2.2: Questions and Clarifications (Duration: 00:05:00)

- Repository clarification (AIASD-2026 class repo, not Zeus Academia 3)
- Branch strategy: personal branches off Greenfield
- Differences between Visual Studio and VS Code performance discussion
- Existing PRD handling

#### 2.3: Working Time and Support (Duration: 00:09:04)

- Students work independently on requirements generation
- Instructor available for questions
- Periodic check-ins for completion status
- Discussion of instruction file effectiveness

---

## Section 3: Greenfield Development Workflow (Duration: 00:08:00) [x]

### Key Topics

- Greenfield project development phases
- Core instruction files importance
- Tech stack instruction files
- Coding standards and quality gates
- Security and compliance requirements
- Repeatable development tasks
- Custom chat modes and domain expertise

### Content Summary

- Multi-phase approach to Greenfield development:
  1. **Foundation Phase**: Core instructions, tech stack files, coding standards, security requirements
  2. **Automation Phase**: Repeatable tasks, prompt files, execution templates
  3. **Specialization Phase**: Domain expertise, custom chat modes, conversational effectiveness
  4. **Integration Phase**: Complex workflows, team standards, training materials
- Emphasis on continuous iteration and improvement
- Using AI to validate instruction file effectiveness
- Avoiding technical debt through validation

---

## Section 4: AI-Assisted Workflow Pattern (Duration: 00:06:00) [x]

### Key Topics

- Requirements to solution transformation
- AI-assisted stakeholder requirements definition
- Implementation structure files
- Instruction file creation for tech stack
- Prompt creation for business requirements implementation
- Vertical slicing implementation strategy
- Feature-based development approach

### Content Summary

- Workflow stages:
  1. Stakeholders define requirements with AI assistance
  2. Use AI to transform requirements into implementation structure files
  3. Add instruction files for chosen tech stack (e.g., C#/ASP.NET/EF)
  4. Review, improve, and approve instruction files
  5. Ask AI to create prompts for implementing business requirements
  6. Use vertical slicing approach with feature-based profiles
  7. Execute implementation prompts and verify
- Each feature encapsulates implementation guidance, validation steps, and demonstration instructions
- Implementation profiles are version-controlled and reusable

---

## Section 5: Technology Stack Instruction Files (Duration: 00:17:00) [x]

### Key Topics

- Creating instruction files for specific technologies
- HTML5, CSS3, and vanilla JavaScript standards
- Command-line prompt for instruction file generation
- Model differences (Claude Sonnet vs. GPT-4)
- Validation checklists
- Multi-model evaluation strategy

### Subsections

#### 5.1: Creating Technology Instructions (Duration: 00:08:00)

- Review requirements document for technology stack
- Simple prompt: "Create instruction files for the following technologies"
- HTML5, CSS, vanilla JavaScript (or TypeScript alternative)
- Comprehensive coverage: semantic markup, accessibility, modern CSS, security, performance

#### 5.2: Instruction File Review (Duration: 00:05:00)

- Generated file structure and content review
- Validation checklist inclusion
- Target audience: AI assistants (primary), developers (secondary)
- Comprehensive guidelines for semantic HTML5, CSS3, vanilla JavaScript
- Security and performance considerations
- Related documentation references

#### 5.3: Multi-Model Evaluation (Duration: 00:04:00)

- Using different models to review instruction files (e.g., Gemini reviewing Claude output)
- Comparing outputs to identify improvements
- Building instruction files from multiple sources
- Model-specific characteristics (Claude Sonnet: comprehensive, GPT-4: variable)
- Importance during foundation phase

---

## Section 6: Vertical Slicing Architecture Introduction (Duration: 00:19:00) [x]

### Key Topics

- Vertical slicing architectural pattern
- Feature-based organization vs. layered approach
- Self-contained, independent features
- Maintainability benefits
- CQRS (Command Query Responsibility Segregation) relationship
- Developer experience improvements

### Subsections

#### 6.1: Vertical Slicing Concepts (Duration: 00:08:00)

- **Definition**: Architectural pattern organizing code by features rather than layers
- **Characteristics**:
  - Spans all technical layers vertically
  - Everything needed for a feature in one place
  - Self-contained and independent
  - Features don't directly reference each other
  - Localized changes improve maintainability

#### 6.2: File Structure Comparison (Duration: 00:03:00)

- **Layered Approach**: Controllers, Services, Repositories, Models (separate folders)
- **Vertical Slices**: Features folder with sub-folders per feature
  - Example: Features/UserRegistration/ contains all user registration code
  - All code for a feature in single location
  - Easy to enhance or modify specific features

#### 6.3: Benefits (Duration: 00:05:00)

- **Developer Experience**:
  - Faster feature development
  - All related code in single location
  - No folder jumping
  - New features don't affect existing ones
- **Maintainability**:
  - Localized changes
  - Clear boundaries reduce bugs
  - Feature-contained refactoring
- **Team Collaboration**:
  - Parallel feature development
  - Fewer merge conflicts
  - Clear ownership and responsibility
- **Testing**:
  - Test complete features, not layers
  - Mock at feature boundaries
  - Independent work with mocked dependencies
  - Straightforward integration

#### 6.4: CQRS Relationship (Duration: 00:03:00)

- Command Query Responsibility Segregation overview
- Separate display (read) from data collection (write)
- Two different stacks joined by messaging
- Optimize read side for performance (denormalization, caching)
- Optimize write side for data updates
- Natural fit with vertical slices: implement read/write portions simultaneously per feature

---

## Section 7: Creating Vertical Slice Implementation Plans (Duration: 00:16:00) [x]

### Key Topics

- Vertical slice planning instruction file
- Slice identification strategies
- Decomposition principles
- Using AI to create implementation plans
- Slice definitions and specifications
- Implementation roadmap creation

### Subsections

#### 7.1: Slice Planning Instruction File Review (Duration: 00:05:00)

- Located in `.github/instructions/vertical-slice-planning.instructions.md`
- **Slice Identification Strategies**:
  - User action decomposition (request-to-response flows)
  - Entity CRUD operations
  - Workflow stage decomposition
  - Business event decomposition
  - CQRS-optimized (separate reads from writes)
- **Decomposition Principles**:
  - Single responsibility
  - Complete vertical stack
  - No horizontal sharing
  - Minimize external dependencies
- **Slicing Guidelines**: Not too big, not too small
- **Decision Tree**: Strategy selection guidance
- **Analysis**: Data dependencies, service dependencies

#### 7.2: Generating Implementation Plans (Duration: 00:07:00)

- Prompt: "Using vertical slice planning instructions and web calculator requirements, create implementation plan using vertical slices"
- AI generates comprehensive plan with:
  - Summary of requirements
  - Slice identification and decomposition
  - Dependency diagram
  - Proposed implementation sequence
  - Sprint organization
- Model differences in output detail and approach

#### 7.3: Multi-Model Evaluation Exercise (Duration: 00:04:00)

- Using Gemini 2.5 Pro to evaluate Claude Sonnet's vertical slice planning file
- Identified six improvement areas:
  - Missing task duration metadata
  - Incomplete decomposition examples
  - Need more complete dependency strategy examples
  - Finish implementation sequencing examples
  - Complete roadmap template
  - Finalize slice specification template
- Demonstrates value of multi-model review strategy

---

## Section 8: Implementation Prompts and Verification (Duration: 00:22:00) [x]

### Key Topics

- Creating implementation prompts for individual slices
- Slice-specific prompt files
- Verification steps inclusion
- Showcase/demonstration instructions
- Detailed specifications for HTML, CSS, JavaScript
- File structure and component organization

### Subsections

#### 8.1: Implementation Prompt Creation (Duration: 00:08:00)

- Select a slice from implementation plan (e.g., Slice 1: Display Current Value)
- Prompt: "Using slice X instructions and implementation plan, create prompts file that implements slice 1. Include verification steps and showcase instructions that demonstrate the functionality to stakeholders."
- Generated prompt file includes:
  - Files to create (index.html, styles.css, main.js)
  - Detailed specifications for each component
  - HTML structure requirements
  - CSS styling (colors, fonts, layout)
  - JavaScript functionality (current value property, display object, update function)

#### 8.2: Verification Steps (Duration: 00:05:00)

- **Initial State**: Calculator displays "0" on page load
- **State Update**: Manual value changes in console update display
- **Accessibility**: Color contrast ratio ≥ 4.5:1, font size ≥ 2rem
- Automated testing guidance
- Manual verification procedures

#### 8.3: Showcase Instructions (Duration: 00:04:00)

- Current version: Code snippet for demonstration
- Improvement suggestion: Target human demonstrators
- Should list what users see and can do
- Behavior descriptions
- Interactive demonstration guidance

#### 8.4: Creating Multiple Slice Prompts (Duration: 00:05:00)

- Repeating process for additional slices (Slice 2, etc.)
- Building complete implementation roadmap
- Each slice prompt is version-controlled
- Reusable for future modifications
- Sequential execution and review approach
- Systematic implementation verification

---

## Summary Statistics

- **Total sections**: 8
- **Average section length**: 10:15
- **Longest section**: Section 2 (Business Requirements Generation Exercise) - 17:04
- **Shortest section**: Section 1 (Introduction and Repository Setup) - 00:02:52

## Key Takeaways

### Workflow Pattern

1. **Foundation**: Requirements → Instruction Files → Tech Stack Standards
2. **Planning**: Vertical Slice Decomposition → Implementation Plan
3. **Implementation**: Slice-Specific Prompts → Verification → Showcase
4. **Iteration**: Multi-Model Evaluation → Continuous Improvement

### Architecture Insights

- Vertical slicing enables feature-based development
- Each slice is complete, independent, and demonstrable
- Natural fit with AI-assisted development
- Facilitates incremental implementation and validation
- CQRS pattern complements vertical slicing

### AI Development Strategy

- Use multiple models for evaluation and validation
- Create comprehensive instruction files early
- Version control all prompts and instruction files
- Iterate and improve based on output quality
- Balance between specification and flexibility

### Team Collaboration

- Personal branches off Greenfield branch
- Shared instruction files and patterns
- Independent parallel feature development
- Reduced merge conflicts through vertical slicing
- Clear ownership and responsibility boundaries

---

**Generated**: 2026-02-17
**Source**: AI-Assisted Software Development with GitHub Copilot (Thu Afternoon).vtt
**Tool**: VTT Content Summarizer
**Duration**: 1:22:00
