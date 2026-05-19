# Day 4 Afternoon - Hands-On Labs

## Requirements-Driven Development & Vertical Slice Architecture

---

## Lab Overview

These labs focus on using AI to create comprehensive requirements documents, instruction files, and implementing features using vertical slice architecture. You'll learn to create meta-instructions that guide AI behavior and plan stakeholder demonstrations.

**Estimated Time:** 2-3 hours

---

## Prerequisites

- GitHub Copilot access with chat functionality
- Visual Studio Code or Visual Studio
- Basic understanding of software requirements
- Familiarity with your chosen technology stack (.NET, Java, Python, etc.)
- Git/GitHub repository for version control

---

## Lab 1: Creating Requirements Documents with AI (30 minutes)

### Objective

Learn to use AI assistance to create comprehensive requirements documents for new features or applications.

### Steps

#### 1.1 Create a New Requirements Document

1. Open a new markdown file in your project: `requirements.md`
2. Use GitHub Copilot Chat with this prompt:

   ```
   Create a requirements document for a [describe your application/feature]
   Don't use any existing implementation.
   ```

3. **Example Prompt:**
   ```
   Create a requirements document for a new calculator desktop application
   Don't use any existing implementation
   ```

#### 1.2 Review the Generated Requirements

Examine the output for these key sections:

- **Introduction** - Purpose and scope
- **Document Conventions** - How requirements are defined (shall, should, may)
- **Overall Description** - High-level functionality
- **User Classes and Characteristics** - Target users
- **Operating Environment** - Platforms and hardware requirements
- **System Features** - Detailed functional requirements
- **External Interface Requirements** - UI, hardware, software interfaces
- **Non-functional Requirements** - Performance, reliability, usability
- **Acceptance Criteria** - How success is measured

#### 1.3 Refine Requirements

Practice refining the requirements:

1. Ask AI to remove features you don't need:

   ```
   Remove all cross-platform requirements from this specification
   ```

2. Ask for clarification on specific sections:

   ```
   Expand the non-functional requirements section with specific metrics
   ```

3. Add missing requirements:
   ```
   Add requirements for accessibility features including keyboard shortcuts and screen reader support
   ```

### Expected Outcomes

- A comprehensive requirements document
- Understanding of how AI interprets domain knowledge
- Practice in iterative requirements refinement

### Discussion Questions

- How does the AI-generated requirements document compare to ones you've created manually?
- What domain knowledge did the AI demonstrate?
- Where did you need to add clarification or corrections?

---

## Lab 2: Creating Instruction Files for AI Guidance (45 minutes)

### Objective

Create instruction files that guide AI behavior when generating code for your project.

### Steps

#### 2.1 Create Technology-Specific Instructions

1. Create a new instruction file: `.github/copilot-instructions.md`
2. Use this prompt:

   ```
   Create an instruction file for a [language/framework] application
   based on the requirements in #file:requirements.md
   ```

3. **Example for C# Application:**
   ```
   Create an instruction file for a C# desktop application
   based on the requirements in #file:requirements.md
   ```

#### 2.2 Review Generated Instructions

Check for these key sections:

- **Technology Stack** - Frameworks, languages, versions
- **Project Structure** - Folder organization
- **Implementation Guidelines** - Architecture patterns, components
- **UI Specifications** - User interface guidelines
- **Testing Strategy** - Unit tests, integration tests, performance tests
- **Dependencies** - Required packages and libraries
- **Configuration** - App settings, environment variables
- **Build and Deployment** - How to build and deploy
- **Code Quality Standards** - Coding conventions, patterns to use

#### 2.3 Customize Instructions

Add project-specific guidance:

1. Specify exact technology versions:

   ```
   Update the instruction file to use .NET 9 and target Windows 11 or later
   ```

2. Add architectural preferences:

   ```
   Update to use MVVM pattern for WPF and specify dependency injection using Microsoft.Extensions.DependencyInjection
   ```

3. Define naming conventions:
   ```
   Add naming conventions: Pascal case for classes, camel case for private fields with underscore prefix
   ```

### Expected Outcomes

- A comprehensive instruction file tailored to your technology stack
- Understanding of how to guide AI code generation
- Practice in defining technical standards

### Key Takeaway

Instruction files are placed in `.github/copilot-instructions.md` or can be named with `.instructions.md` extension and will be automatically recognized by GitHub Copilot.

---

## Lab 3: Creating Meta-Instructions for Consistency (30 minutes)

### Objective

Create instruction files that guide the creation of other instruction files for consistency across your project.

### Steps

#### 3.1 Create Instruction Generation Instructions

1. Create file: `.github/instruction-generation.instructions.md`
2. Use this prompt:
   ```
   Create an instruction file to guide the creation of new instruction files
   ```

#### 3.2 Review Meta-Instructions Content

The file should include:

- **Front Matter Format** - YAML header with description and applyTo
- **File Naming Conventions** - How instruction files should be named
- **File Location** - Where instruction files should be placed (`.github/` folder)
- **Content Structure** - Required sections in instruction files
- **Formatting Guidelines** - Markdown standards, heading levels
- **AI Optimization** - Versioning for AI model compatibility

#### 3.3 Apply Meta-Instructions

Test the meta-instructions:

1. Ask AI to create a new instruction file:

   ```
   Create an instruction file for vertical slice implementation
   following the instruction generation guidelines
   ```

2. Verify the output follows your meta-instructions format

#### 3.4 Create Conversation Logging Instructions

Create instructions for logging AI interactions:

```
Create an instruction file for logging conversations with AI
Include timestamp, prompt, response, and files created/modified
```

### Expected Outcomes

- Consistent instruction file format across project
- Automated logging of AI interactions
- Reusable templates for common instruction types

### Discussion Questions

- How do meta-instructions improve project consistency?
- What other types of meta-instructions would be useful?
- How can conversation logs support project documentation?

---

## Lab 4: Planning with Vertical Slice Architecture (45 minutes)

### Objective

Learn to decompose features into vertical slices and create implementation plans.

### Steps

#### 4.1 Create Vertical Slice Instructions

1. Create file: `.github/vertical-slice.instructions.md`
2. Use this prompt:
   ```
   Create instructions for implementing features using vertical slice architecture
   based on the requirements in #file:requirements.md
   ```

#### 4.2 Generate Implementation Plan

Create a detailed implementation plan:

```
Create a vertical slice implementation plan for the calculator application
Break down the implementation into logical slices with clear boundaries
```

#### 4.3 Review the Slice Structure

Each slice should include:

- **Feature Description** - What this slice implements
- **Slice Boundaries** - Clear scope definition
- **Dependencies** - What this slice depends on
- **Implementation Components**:
  - Domain models
  - Commands/Queries
  - Handlers
  - UI components
  - Tests
- **Success Criteria** - How to verify the slice works
- **Testing Requirements** - Unit, integration, and UI tests

#### 4.4 Analyze Slice Dependencies

Review the plan for:

1. **Foundation Slice** - The first slice that establishes the project structure
2. **Independent Slices** - Features that can be developed in parallel
3. **Dependent Slices** - Features that build on other slices

Example slice structure:

- **Slice 1: Foundation** - Project setup, basic input handling, display
- **Slice 2: Basic Operations** - Add, subtract, multiply, divide
- **Slice 3: Memory Functions** - Memory store, recall, clear
- **Slice 4: Advanced Operations** - Square root, power, percentage
- **Slice 5: Calculation History** - View past calculations
- **Slice 6: Error Handling** - Input validation, error messages

### Expected Outcomes

- Clear breakdown of features into implementable slices
- Understanding of dependencies between slices
- Testable success criteria for each slice

### Discussion Questions

- How does vertical slice architecture differ from layered architecture?
- What are the benefits of implementing features as vertical slices?
- How do you determine the right size for a slice?

---

## Lab 5: Adding Showcase Instructions to Slices (30 minutes)

### Objective

Learn to create demonstration plans for each vertical slice to facilitate stakeholder reviews.

### Steps

#### 5.1 Add Showcase Sections to Plan

Update your implementation plan:

```
Add to the plan instructions for showcasing each slice to stakeholders
```

#### 5.2 Review Showcase Instructions

Each slice's showcase section should include:

- **What to Demonstrate** - Key features to show
- **Demo Script** - Step-by-step demonstration flow
- **Functional Demo** - Specific actions to perform
- **Technical Highlights** - Architecture and testing to showcase
- **Success Metrics** - How to measure stakeholder acceptance

#### 5.3 Create Slice-Specific Showcase

For a specific slice, create detailed showcase instructions:

```
Create detailed showcase instructions for Slice 1 (Foundation)
Include specific steps, expected results, and talking points
```

Example showcase structure:

```markdown
## Slice 1: Foundation - Showcase

### What to Demonstrate

- Number input (single digits, decimals, negatives)
- Display updates
- Clear and backspace functionality

### Demo Script

1. Launch the application
2. Enter single digits and show display updates
3. Demonstrate decimal number entry
4. Show negative number handling
5. Demonstrate clear function
6. Test backspace functionality
7. Attempt invalid inputs to show validation

### Platform Demo

- Show running on Windows desktop
- Show on Android emulator (if cross-platform)
- Highlight consistent behavior

### Technical Highlights

- Vertical slice architecture
- Unit tests passing
- Command handler pattern walkthrough

### Success Criteria

- Stakeholders can successfully enter numbers
- Display updates are accurate
- Validation prevents invalid input
```

#### 5.4 Practice Showcase Preparation

For your project:

1. Choose one slice to showcase
2. Create specific test data
3. Write down expected results
4. Practice the demonstration flow
5. Identify potential questions stakeholders might ask

### Expected Outcomes

- Clear demonstration plan for each slice
- Testable acceptance criteria
- Documentation that can become user guides

### Discussion Questions

- How do showcase instructions drive better implementation?
- What makes an effective feature demonstration?
- How can showcase plans become user documentation?

---

## Lab 6: Implementing Your First Slice (30 minutes)

### Objective

Use the instruction files and plan to implement the foundation slice with AI assistance.

### Steps

#### 6.1 Reference Instruction Files

In GitHub Copilot Chat:

```
Using #file:.github/copilot-instructions.md
and #file:.github/vertical-slice.instructions.md
implement Slice 1 (Foundation) from the implementation plan
```

#### 6.2 Verify Against Instructions

As code is generated:

1. Check it follows the technology stack specified
2. Verify folder structure matches instructions
3. Confirm naming conventions are followed
4. Ensure tests are included

#### 6.3 Test the Slice

1. Run unit tests
2. Launch the application
3. Follow the showcase script
4. Verify success criteria are met

#### 6.4 Create Conversation Log

Document the implementation:

1. What prompts were used
2. What files were created
3. What adjustments were needed
4. What worked well vs. what needed refinement

### Expected Outcomes

- Working foundation slice
- Experience using instruction files
- Documentation of the AI-assisted development process

---

## Lab 7: Iterative Refinement Exercise (20 minutes)

### Objective

Practice refining instruction files and plans based on implementation experience.

### Steps

#### 7.1 Identify Gaps

After implementing Slice 1, identify:

- Requirements that were unclear
- Instructions that were missing
- Technology choices that need refinement
- Success criteria that need clarification

#### 7.2 Update Documentation

Make improvements to:

1. **Requirements Document**

   ```
   Update requirements.md to clarify [specific requirement]
   ```

2. **Instruction Files**

   ```
   Add guidance about [specific technical decision] to the instruction file
   ```

3. **Implementation Plan**
   ```
   Update the plan to reflect lessons learned from implementing Slice 1
   ```

#### 7.3 Verify Consistency

Ask AI to check consistency:

```
Review the requirements, instruction file, and implementation plan
Identify any inconsistencies or missing information
```

#### 7.4 Document Lessons Learned

Create a lessons-learned document:

- What worked well in the process
- What needs improvement
- How to improve AI prompts
- How to make instructions more effective

### Expected Outcomes

- Improved documentation based on real experience
- Better understanding of requirement clarity
- More effective instruction files

---

## Challenge Exercises

### Challenge 1: Technology Migration

Scenario: Your stakeholders want to switch from WPF to .NET MAUI for cross-platform support.

Tasks:

1. Update the requirements document
2. Modify the instruction file for MAUI
3. Update the implementation plan
4. Identify what changes in each slice
5. Create migration-specific showcase instructions

### Challenge 2: New Feature Slice

Design a completely new slice:

1. Choose a feature not in the original requirements
2. Write requirements for it
3. Define it as a vertical slice
4. Create showcase instructions
5. Identify dependencies on existing slices

### Challenge 3: Multi-Team Coordination

Scenario: Three teams will implement different slices in parallel.

Tasks:

1. Identify which slices can be developed independently
2. Define interfaces between slices
3. Create coordination instructions
4. Plan integration testing strategy
5. Design a combined showcase

---

## Best Practices Summary

### Requirements Documents

- ✅ Use clear language (shall, should, may)
- ✅ Focus on WHAT, not HOW
- ✅ Include acceptance criteria
- ✅ Specify non-functional requirements
- ✅ Review and refine iteratively

### Instruction Files

- ✅ Place in `.github/` folder or use `.instructions.md` suffix
- ✅ Include front matter with applyTo scope
- ✅ Be specific about technology versions
- ✅ Define architecture patterns clearly
- ✅ Include testing requirements

### Vertical Slices

- ✅ Each slice delivers end-to-end value
- ✅ Start with foundation slice
- ✅ Minimize dependencies between slices
- ✅ Include tests in every slice
- ✅ Define clear success criteria

### Showcase Planning

- ✅ Create specific demonstration scripts
- ✅ Include expected results
- ✅ Show technical highlights
- ✅ Define stakeholder acceptance criteria
- ✅ Practice before presenting

---

## Troubleshooting

### Issue: AI-generated requirements are too generic

**Solution:** Provide more context about your domain, users, and constraints. Reference similar applications or specific use cases.

### Issue: Instruction file isn't being recognized

**Solution:**

- Verify file is in `.github/` folder or has `.instructions.md` suffix
- Check front matter syntax
- Ensure applyTo glob pattern is correct
- Try explicitly referencing with `#file:` in chat

### Issue: Slices have too many dependencies

**Solution:**

- Review slice boundaries
- Consider splitting into smaller slices
- Create foundation slice with shared infrastructure
- Use interfaces to decouple slices

### Issue: Showcase instructions are too detailed

**Solution:**

- Focus on key features and value
- Create separate detailed test scripts
- Tailor to stakeholder audience
- Practice to find right level of detail

---

## Additional Resources

### Templates

- Requirements Document Template
- Instruction File Template
- Vertical Slice Plan Template
- Showcase Script Template

### Recommended Reading

- Vertical Slice Architecture patterns
- Requirements engineering best practices
- AI-assisted documentation techniques
- Stakeholder communication strategies

### Tools

- GitHub Copilot Chat for requirements generation
- Markdown preview for reviewing documents
- Git branches for slice implementation
- Conversation logging tools

---

## Reflection Questions

1. How did creating requirements upfront change your development approach?
2. What impact did instruction files have on code generation quality?
3. How does vertical slice architecture support parallel development?
4. What role do showcase instructions play in driving implementation quality?
5. How can you apply these techniques to your current projects?

---

## Next Steps

After completing these labs:

1. Apply requirements-driven development to a real feature
2. Create a library of instruction files for your team
3. Implement a complete feature using vertical slices
4. Present a slice showcase to stakeholders
5. Build a knowledge base of lessons learned

---

## Lab Submission (Optional)

If completing these labs as part of a course, submit:

1. Your requirements document
2. At least 2 instruction files (including meta-instructions)
3. A vertical slice implementation plan
4. Showcase instructions for at least one slice
5. Code for your foundation slice
6. A reflection document on lessons learned

---

**Remember:** The goal is not perfect documentation on the first try, but iterative improvement. Use AI as a collaborative partner to create comprehensive requirements and guidance that improve with each iteration.
