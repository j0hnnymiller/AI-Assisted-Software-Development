# Day 5 Morning Session - Hands-On Labs

## Overview

These labs focus on custom chat modes, comparing AI control mechanisms, and implementing code using personas. By the end of these labs, you will understand how to create and use custom chat modes effectively in your AI-assisted development workflow.

---

## Lab 1: Understanding AI Control Mechanisms (30 minutes)

### Objective

Compare and contrast instruction files, prompt files, and custom chat modes to understand when to use each approach.

### Tasks

#### Task 1.1: Review the Comparison Matrix

1. Open a new chat session in GitHub Copilot
2. Ask: "What are the key differences between instruction files, prompt files, and custom chat modes?"
3. Create a markdown document that lists:
   - When to use instruction files
   - When to use prompt files
   - When to use custom chat modes
   - Examples of each from your own project context

#### Task 1.2: Analyze Your Current Setup

1. Review your project's `.github` folder
2. Identify what instruction files you currently have
3. List what prompt files exist
4. Document which custom chat modes are configured
5. Create a table showing:
   - File/Mode name
   - Type (instruction/prompt/chat mode)
   - Purpose
   - Scope (repository-wide, file-specific, etc.)

#### Task 1.3: Decision Framework Exercise

For each of the following scenarios, decide whether to use an instruction file, prompt file, or custom chat mode:

1. Enforcing code formatting standards across all files
2. Generating API documentation for a specific endpoint
3. Getting security review advice on authentication implementation
4. Creating a new React component following team conventions
5. Establishing naming conventions for database tables

**Deliverable**: A document with your decisions and justifications for each scenario.

---

## Lab 2: Creating Custom Chat Modes (60 minutes)

### Objective

Create functional custom chat modes for different development personas that can be used in your project.

### Prerequisites

- Access to `.github/copilot/chat-modes/` folder in your repository
- Understanding of YAML front matter

### Tasks

#### Task 2.1: Create a Security Analyst Chat Mode

1. Create a new file: `.github/copilot/chat-modes/security-analyst.md`
2. Add the required front matter:
   ```yaml
   ---
   id: security-analyst
   name: Security Analyst
   version: 1.0.0
   description: Security expert for code review and secure coding practices
   category: Security
   tags: [security, code-review, vulnerabilities]
   tools: [create, edit]
   ---
   ```
3. Define the persona with:

   - Role identity and expertise
   - Communication style
   - Key behaviors (focus on security best practices)
   - Quality standards
   - Specific knowledge areas (OWASP Top 10, secure authentication, data protection)

4. Test the chat mode by:
   - Opening GitHub Copilot Chat
   - Selecting your new security analyst mode
   - Asking it to review a code file for security vulnerabilities

#### Task 2.2: Create a Software Architect Chat Mode

1. Create a new file: `.github/copilot/chat-modes/software-architect.md`
2. Define the persona focusing on:

   - System design and architecture patterns
   - Scalability and performance considerations
   - Technology stack decisions
   - Code structure and organization
   - Best practices for maintainability

3. Include specific expertise areas:

   - Design patterns (SOLID, DRY, KISS)
   - Microservices vs monolithic architecture
   - Database design
   - API design principles
   - Cloud architecture considerations

4. Test by asking for architectural advice on your current project

#### Task 2.3: Create a Test Automation Engineer Chat Mode

1. Create a new file: `.github/copilot/chat-modes/test-engineer.md`
2. Define the persona focusing on:

   - Test strategy and planning
   - Test automation frameworks
   - Code coverage and quality metrics
   - Test maintainability
   - CI/CD integration

3. Include expertise in:

   - Unit testing best practices
   - Integration testing strategies
   - Test-driven development (TDD)
   - Mocking and stubbing
   - Performance testing

4. Test by asking for test implementation for a specific component

#### Task 2.4: Create a Senior Developer Chat Mode

1. Create a comprehensive senior developer persona that includes:

   - Code quality and maintainability focus
   - Performance optimization knowledge
   - Debugging expertise
   - Mentoring approach
   - Best practices across multiple languages/frameworks

2. Enable tools in the front matter:

   ```yaml
   tools: [create, edit, issues]
   ```

3. Test with multiple scenarios:
   - Code review request
   - Refactoring suggestions
   - Performance optimization advice
   - Debugging assistance

**Deliverable**: Four working chat mode files with documented test results

---

## Lab 3: Configuring Chat Mode Capabilities (30 minutes)

### Objective

Understand and configure the tools and capabilities available to custom chat modes.

### Tasks

#### Task 3.1: Understanding Tool Permissions

1. Review the available tool options:

   - `create`: Create new files
   - `edit`: Edit existing files
   - `issues`: Create GitHub issues
   - `terminal`: Execute terminal commands

2. For each of your chat modes from Lab 2, determine which tools should be enabled:

   - Security Analyst: Should it create issues for vulnerabilities?
   - Software Architect: Should it create/edit files?
   - Test Engineer: What permissions make sense?
   - Senior Developer: Should it have full access?

3. Update your chat mode files with appropriate tool configurations

#### Task 3.2: Temperature Settings

1. Learn about temperature settings (0.0 to 1.0)

   - Lower temperature: More deterministic and focused
   - Higher temperature: More creative and varied

2. Add temperature settings to your chat modes:

   ```yaml
   temperature: 0.7
   ```

3. Experiment with different values:

   - Test with 0.3 (precise, code generation)
   - Test with 0.7 (balanced)
   - Test with 0.9 (creative, exploration)

4. Document which temperature works best for each persona

#### Task 3.3: Context Management

Add context management rules to your chat modes:

- Specify what files/patterns should be included in context
- Define repository awareness requirements
- Establish project-specific knowledge requirements

Example:

```markdown
## Context Management

- Include: `**/*.cs`, `*.md`, `.github/**`
- Focus on: Security-related files when analyzing
- Project awareness: Understand current tech stack
```

**Deliverable**: Updated chat mode files with appropriate tool permissions, temperature settings, and context management rules.

---

## Lab 4: Using Chat Modes for Implementation (45 minutes)

### Objective

Use your custom chat modes to implement features following a vertical slice approach.

### Prerequisites

- Completed Lab 2 (custom chat modes created)
- A project with requirements or user stories

### Tasks

#### Task 4.1: Set Up Your Project Context

1. Review your project requirements
2. Identify a simple feature to implement (e.g., calculator operations, user login, data validation)
3. Create a vertical slice plan for the feature:
   - Slice 1: Core functionality
   - Slice 2: Error handling
   - Slice 3: Testing
   - Slice 4: Documentation

#### Task 4.2: Implement Using Senior Developer Mode

1. Activate your Senior Developer chat mode
2. Provide context about the feature to implement
3. Ask it to implement Slice 1 of your feature
4. Review the generated code:
   - Does it follow your project conventions?
   - Is it maintainable?
   - Does it include proper error handling?

#### Task 4.3: Security Review

1. Switch to your Security Analyst chat mode
2. Ask it to review the code generated in Task 4.2
3. Address any security concerns identified
4. Have the security mode create GitHub issues for any major findings

#### Task 4.4: Architecture Review

1. Switch to your Software Architect chat mode
2. Ask for architectural feedback on your implementation
3. Request suggestions for improvement
4. Implement any recommended changes

#### Task 4.5: Add Tests

1. Switch to your Test Engineer chat mode
2. Ask it to create comprehensive tests for your implementation
3. Ensure tests include:
   - Unit tests
   - Edge cases
   - Error scenarios
4. Run the tests and verify coverage

**Deliverable**: A complete feature implementation with:

- Working code
- Security review documentation
- Architecture review notes
- Comprehensive test suite

---

## Lab 5: Optimizing Chat Mode Effectiveness (30 minutes)

### Objective

Improve your chat modes based on real-world usage and token optimization.

### Tasks

#### Task 5.1: Token Usage Analysis

1. Use GitHub Copilot to analyze the token count of your chat mode files
2. Identify verbose sections that could be more concise
3. Create an "AI-optimized" version of one chat mode:
   - Remove unnecessary words
   - Use bullet points instead of paragraphs
   - Keep essential context but reduce token count by 30-40%

#### Task 5.2: Test and Compare

1. Test both the original and optimized versions
2. Compare results:
   - Quality of responses
   - Speed of responses
   - Accuracy and relevance
3. Document which version performs better and why

#### Task 5.3: Best Practices Implementation

Add best practices sections to your chat modes:

```markdown
## Quality Standards

- [ ] Code follows project conventions
- [ ] Includes error handling
- [ ] Has appropriate comments
- [ ] Passes linting rules
- [ ] Includes unit tests

## Common Patterns

- Use async/await for asynchronous operations
- Follow SOLID principles
- Implement defensive programming
- Use dependency injection
```

#### Task 5.4: Activation Triggers

Configure activation triggers for your chat modes:

```yaml
activation:
  phrases: ["security review", "check security", "vulnerability scan"]
  auto_activate: false
```

Test that the triggers work as expected.

**Deliverable**: Optimized chat modes with best practices, quality checklists, and activation triggers configured.

---

## Lab 6: Multi-Persona Workflow (45 minutes)

### Objective

Create a complete workflow that uses multiple chat modes to deliver a feature from conception to deployment.

### Tasks

#### Task 6.1: Feature Planning

1. Use the Software Architect mode to:
   - Design the feature architecture
   - Identify dependencies
   - Create implementation plan
   - Define interfaces/contracts

#### Task 6.2: Implementation

1. Use the Senior Developer mode to:
   - Implement the core functionality
   - Follow the architect's design
   - Write clean, maintainable code
   - Add inline documentation

#### Task 6.3: Testing

1. Use the Test Engineer mode to:
   - Create unit tests
   - Create integration tests
   - Set up test fixtures
   - Implement mocks where needed

#### Task 6.4: Security Review

1. Use the Security Analyst mode to:
   - Review code for vulnerabilities
   - Check authentication/authorization
   - Verify input validation
   - Review error handling
   - Create issues for any findings

#### Task 6.5: Documentation

Create a document that shows:

- Which persona was used at each step
- The prompts provided
- The output received
- Any modifications made
- Final code quality assessment

**Deliverable**: A complete feature with documentation showing the multi-persona workflow used to create it.

---

## Lab 7: Personal vs Repository Instruction Files (30 minutes)

### Objective

Understand the difference between personal and repository instruction files and when to use each.

### Tasks

#### Task 7.1: Create a Personal Instruction File

1. Locate your VS Code user settings folder:

   - Windows: `%APPDATA%\Code\User\`
   - Mac/Linux: `~/.config/Code/User/`

2. Create a personal instruction file: `copilot-instructions.md`

3. Add personal preferences:

   ```markdown
   # My Personal Coding Preferences

   - I prefer TypeScript over JavaScript
   - Always use async/await instead of callbacks
   - Include JSDoc comments for all functions
   - Use 2 spaces for indentation
   - Prefer functional programming patterns
   ```

4. Test that these preferences are applied across all projects

#### Task 7.2: Compare Scopes

1. Create a test project with its own instruction file
2. Add different coding standards in the repository instruction file
3. Test which rules take precedence
4. Document the hierarchy of instruction files

#### Task 7.3: Multi-Project Strategy

Design a strategy for using instruction files across multiple projects:

1. What goes in personal files?
2. What goes in repository files?
3. How to handle conflicts?
4. How to share common standards across projects?

Consider approaches like:

- Symbolic links
- Git submodules
- Shared configuration repositories

**Deliverable**: Documentation of your multi-project instruction file strategy with examples.

---

## Lab 8: Monitoring and Cost Management (20 minutes)

### Objective

Understand how to monitor usage and manage costs associated with GitHub Copilot.

### Tasks

#### Task 8.1: Check Usage Metrics

1. In VS Code, check your current usage:
   - Look for the premium requests indicator
   - Note your current percentage used
2. Document your typical daily usage patterns

#### Task 8.2: Optimize Token Usage

Review your chat modes and instruction files for token optimization:

1. Identify the largest files
2. Calculate approximate token count (roughly 4 characters per token)
3. Prioritize optimization efforts on high-token files
4. Create "compact" versions where appropriate

#### Task 8.3: Usage Best Practices

Create guidelines for your team:

- When to use premium models vs standard models
- How to structure prompts efficiently
- How to reuse context effectively
- How to avoid redundant requests

**Deliverable**: Usage monitoring report and optimization guidelines.

---

## Lab 9: Integration with Existing Workflows (30 minutes)

### Objective

Integrate custom chat modes into your existing development workflows and CI/CD pipelines.

### Tasks

#### Task 9.1: Code Review Integration

1. Configure your Security Analyst mode to be used in pull requests
2. Create a prompt file for automated code reviews:

   ```markdown
   ---
   mode: security-analyst
   ---

   # Security Review Prompt

   Review the following changes for security vulnerabilities:

   - Check for SQL injection risks
   - Verify input validation
   - Check authentication/authorization
   - Review error handling
   - Check for sensitive data exposure
   ```

#### Task 9.2: Pre-commit Hooks

Design a pre-commit hook strategy that:

1. Runs specific chat modes before commit
2. Checks code quality
3. Verifies documentation
4. Ensures tests exist

#### Task 9.3: CI/CD Integration

Plan how to integrate chat modes into your CI/CD pipeline:

- Which checks should be automated?
- Which require human review?
- How to fail builds based on chat mode feedback?

**Deliverable**: Integration plan document with example configurations.

---

## Lab 10: Advanced Chat Mode Patterns (45 minutes)

### Objective

Implement advanced patterns and techniques for custom chat modes.

### Tasks

#### Task 10.1: Specialized Domain Expert

Create a chat mode for a specific technology in your stack:

- Database optimization expert
- React/Angular/Vue specialist
- API design expert
- Performance tuning specialist

Include:

- Deep technical knowledge in the domain
- Best practices specific to that technology
- Common pitfalls and how to avoid them
- Tools and resources specific to that domain

#### Task 10.2: Mentoring Mode

Create a chat mode that acts as a mentor for junior developers:

- Patient, educational tone
- Explains the "why" behind recommendations
- Provides learning resources
- Breaks down complex concepts
- Suggests incremental learning paths

#### Task 10.3: Code Migration Specialist

Create a mode for migrating code between:

- Language versions (e.g., Python 2 to 3)
- Frameworks (e.g., AngularJS to Angular)
- Architectures (e.g., Monolith to Microservices)

Include:

- Migration strategy advice
- Step-by-step conversion approach
- Risk identification
- Testing strategy for migrations

**Deliverable**: Three advanced chat modes with documentation and test cases.

---

## Bonus Lab: Validation for Regulated Industries (30 minutes)

### Objective

Understand how to use GitHub Copilot in regulated industries requiring tool validation.

### Tasks

#### Task B.1: Validation Strategy Document

Create a document that outlines:

1. What needs to be validated:

   - Chat mode configurations
   - Instruction files
   - Model versions used
   - Output verification process

2. How to validate:

   - Testing procedures
   - Documentation requirements
   - Change control process
   - Version locking strategies

3. Compliance considerations:
   - Code review requirements
   - Audit trails
   - Traceability
   - Quality gates

#### Task B.2: Implement Controls

1. Lock down model versions in your configuration
2. Create verification checklists for AI-generated code
3. Design a review process that includes:
   - Human verification of all AI-generated code
   - Static analysis tools
   - Security scanning
   - Test coverage requirements

#### Task B.3: Documentation

Create templates for:

- AI-generated code documentation
- Review checklist for AI outputs
- Validation report template
- Change control forms

**Deliverable**: Complete validation strategy document with templates.

---

## Summary and Next Steps

After completing these labs, you should be able to:

1. ✅ Understand the differences between instruction files, prompt files, and custom chat modes
2. ✅ Create and configure custom chat modes for different personas
3. ✅ Use multiple chat modes in a coordinated workflow
4. ✅ Optimize chat modes for token efficiency
5. ✅ Integrate chat modes into existing development workflows
6. ✅ Monitor usage and manage costs
7. ✅ Implement validation strategies for regulated environments

### Recommended Follow-up Activities

1. Create a library of chat modes for your organization
2. Share best practices with your team
3. Continuously refine chat modes based on usage patterns
4. Explore combining chat modes with GitHub Actions for automation
5. Experiment with different model temperatures for different tasks

### Additional Resources

- GitHub Copilot Documentation: https://docs.github.com/copilot
- Custom Chat Modes Examples: Check the `.github/copilot/chat-modes/` folder
- Best Practices Guide: Review the AI instruction files in your repository

---

## Evaluation Criteria

For each lab, evaluate your work based on:

- **Functionality** (40%): Does it work as intended?
- **Quality** (30%): Is it well-structured and maintainable?
- **Documentation** (20%): Is it properly documented?
- **Innovation** (10%): Does it show creative problem-solving?

### Self-Assessment Questions

1. Can you explain when to use each AI control mechanism?
2. Have you created chat modes that improve your productivity?
3. Can you demonstrate a multi-persona workflow?
4. Have you optimized for token usage?
5. Can you integrate chat modes into your existing workflows?

---

**End of Day 5 Morning Labs**

_Remember: The goal is not to replace human judgment but to augment your capabilities as a developer. Always review and validate AI-generated code before committing to your repository._
