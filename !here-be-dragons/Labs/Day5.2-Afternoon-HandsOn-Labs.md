# Day 5 Afternoon - Hands-On Labs

## Advanced AI-Assisted Development with Vertical Slice Architecture

### Overview

These labs focus on implementing a production-ready application using vertical slice architecture, CQRS patterns, comprehensive testing strategies, and AI-assisted development workflows.

---

## Lab 1: Implementing Vertical Slice Architecture with AI (60 minutes)

### Objectives

- Understand vertical slice architecture principles
- Implement feature slices independently
- Use AI to generate slice-based implementations
- Validate slice completeness and integration

### Prerequisites

- Completed Day 1-4 labs
- Understanding of MVVM and CQRS patterns
- Familiarity with dependency injection

### Instructions

#### Part 1: Define Slice Requirements (15 minutes)

1. **Create a Slice Definition File**

   - Create `.github/copilot-instructions.md` with vertical slice guidance
   - Define slice structure:

     ```markdown
     # Vertical Slice Architecture Guidelines

     ## Slice Structure

     Each feature slice should be self-contained with:

     - Commands/Queries (CQRS pattern)
     - Handlers
     - Domain models
     - Validators
     - Tests

     ## Slice Independence

     - Each slice must be implementable on separate branches
     - Minimal shared dependencies (only common models)
     - No coupling between slices

     ## Implementation Pattern

     1. Define success criteria first
     2. Implement domain layer
     3. Add handlers
     4. Create UI components
     5. Write comprehensive tests (unit + integration)
     6. Document architecture decisions
     ```

2. **Define First Slice Requirements**
   - Create `requirements/slice-1-number-entry.md`
   - Include:
     - Feature description
     - Success criteria
     - Technical requirements
     - Test scenarios

#### Part 2: AI-Assisted Slice Implementation (30 minutes)

1. **Implement Slice 1**

   ```
   Prompt: "Implement slice 1 for basic number entry following vertical slice architecture.
   Include CQRS pattern with MediatR, MVVM pattern, and comprehensive tests."
   ```

2. **Review Generated Code**

   - Examine the folder structure
   - Check for proper separation of concerns
   - Verify test coverage
   - Review architectural patterns used

3. **Run and Validate**
   - Build the solution
   - Run unit tests
   - Run integration tests
   - Test the UI functionality

#### Part 3: Implement Second Slice (15 minutes)

1. **Create Slice 2 Requirements**

   - Define basic arithmetic operations
   - Specify interaction with Slice 1

2. **Implement Using AI**

   ```
   Prompt: "Implement slice 2 for basic arithmetic operations (add, subtract, multiply, divide).
   Maintain independence from slice 1. Follow established patterns."
   ```

3. **Validate Integration**
   - Ensure slices work together
   - Check for conflicts
   - Run all tests

### Validation Criteria

- [ ] Each slice has independent folder structure
- [ ] CQRS pattern is properly implemented
- [ ] All tests pass (unit and integration)
- [ ] UI is functional and responsive
- [ ] Code follows clean architecture principles
- [ ] Documentation is generated

### Troubleshooting Tips

- If build fails, ask AI to review and fix compilation errors
- Use `dotnet clean` and rebuild if encountering caching issues
- Check project references if dependencies are missing

---

## Lab 2: Adding UI Testing to Existing Applications (45 minutes)

### Objectives

- Add UI test infrastructure to an existing application
- Implement automated UI tests
- Use AI to generate test scenarios
- Integrate UI tests into CI/CD pipeline

### Prerequisites

- Working application from Lab 1
- Understanding of UI testing concepts

### Instructions

#### Part 1: Add UI Test Infrastructure (15 minutes)

1. **Request UI Test Setup**

   ```
   Prompt: "Add UI testing infrastructure for slice 1. Use .NET MAUI UI Test framework.
   Include test helpers and base classes."
   ```

2. **Review Generated Infrastructure**

   - Examine test project structure
   - Check test helper methods
   - Review element identification strategy (X:Name attributes)

3. **Verify Setup**
   - Build test project
   - Ensure dependencies are properly referenced

#### Part 2: Implement UI Tests (20 minutes)

1. **Generate Basic UI Tests**

   ```
   Prompt: "Create UI tests for number entry functionality. Test single digit,
   multiple digits, decimal entry, backspace, and clear operations."
   ```

2. **Review Test Implementation**

   - Check test structure and patterns
   - Verify element selectors
   - Review assertions

3. **Run UI Tests**
   - Execute tests
   - Address any failures
   - Use AI to fix issues:
     ```
     Prompt: "Fix the failing UI test for decimal entry. Error: [paste error]"
     ```

#### Part 3: Add Advanced Test Scenarios (10 minutes)

1. **Create Edge Case Tests**

   ```
   Prompt: "Add UI tests for edge cases: entering invalid characters,
   maximum number length, rapid button clicking, error recovery."
   ```

2. **Run Complete Test Suite**
   - Execute all UI tests
   - Check test execution time
   - Review test coverage

### Validation Criteria

- [ ] UI test project is properly configured
- [ ] All UI elements have proper identifiers
- [ ] Tests cover happy paths and edge cases
- [ ] All tests pass consistently
- [ ] Test execution time is reasonable (<5 minutes)

---

## Lab 3: Creating Custom Chat Modes for Team Roles (45 minutes)

### Objectives

- Create specialized chat modes for different team roles
- Configure appropriate tools and permissions
- Use personas to improve code quality
- Establish team development standards

### Prerequisites

- Understanding of GitHub Copilot chat modes
- Familiarity with team development workflows

### Instructions

#### Part 1: Create Senior Software Engineer Persona (15 minutes)

1. **Create Chat Mode Configuration**

   - Create `.github/copilot-chat-modes/senior-engineer.json`

   ```json
   {
     "name": "Senior Software Engineer",
     "description": "Expert developer focused on architecture, best practices, and code quality",
     "instructions": "You are a senior software engineer with 15+ years of experience...",
     "tools": [
       "edit_files",
       "read_files",
       "search_code",
       "run_tests",
       "review_code"
     ],
     "model": "claude-sonnet-4"
   }
   ```

2. **Test the Persona**

   ```
   Switch to Senior Software Engineer mode
   Prompt: "Review the codebase and provide architectural feedback"
   ```

3. **Refine Instructions**
   - Add specific review criteria
   - Include company coding standards
   - Specify focus areas (security, performance, maintainability)

#### Part 2: Create Test Engineer Persona (15 minutes)

1. **Create Test Engineer Chat Mode**

   ```json
   {
     "name": "Senior Test Engineer",
     "description": "Testing specialist focused on comprehensive test coverage",
     "instructions": "You are a test engineer specializing in TDD...",
     "tools": [
       "create_test_files",
       "run_tests",
       "analyze_coverage",
       "suggest_test_cases"
     ]
   }
   ```

2. **Use for Test Generation**
   ```
   Switch to Senior Test Engineer mode
   Prompt: "Analyze test coverage and suggest additional test scenarios
   for edge cases and error conditions"
   ```

#### Part 3: Create Review Workflow (15 minutes)

1. **Implement Multi-Persona Review**

   - Generate code with default agent
   - Review with Senior Engineer
   - Validate tests with Test Engineer
   - Document findings

2. **Create Review Checklist**

   ```
   Prompt (to Senior Engineer): "Create a code review checklist based on
   the issues you found in this codebase"
   ```

3. **Apply Improvements**
   ```
   Prompt: "Implement the priority improvements identified in the review"
   ```

### Validation Criteria

- [ ] Multiple chat modes are configured
- [ ] Each persona has appropriate tools
- [ ] Personas provide different perspectives
- [ ] Review process yields actionable feedback
- [ ] Code quality improves after review

---

## Lab 4: Handling Complex Development Workflows (60 minutes)

### Objectives

- Manage AI context for complex implementations
- Handle long-running AI tasks
- Deal with context limits and token budgets
- Implement parallel slice development

### Prerequisites

- Completed previous labs
- Understanding of Git branching
- Familiarity with merge workflows

### Instructions

#### Part 1: Managing AI Context (20 minutes)

1. **Create Context Management Strategy**

   - Create `.github/copilot-session-context.md`
   - Document:
     - Essential files to include
     - Files to exclude
     - Context refresh triggers

2. **Test Context Optimization**

   ```
   Prompt: "Review the current context and suggest which files should be
   excluded to optimize token usage"
   ```

3. **Implement Session Files**
   - Save working context to session file
   - Clear chat context
   - Resume with session file:
     ```
     Prompt: "Using @session-context.md, implement slice 3"
     ```

#### Part 2: Parallel Slice Development (20 minutes)

1. **Set Up Branch Strategy**

   ```bash
   git checkout -b feature/slice-3
   git checkout -b feature/slice-4
   ```

2. **Implement Multiple Slices**

   - On branch `feature/slice-3`:

     ```
     Prompt: "Implement slice 3 for scientific operations
     (sin, cos, tan, log, sqrt) following established patterns"
     ```

   - On branch `feature/slice-4`:
     ```
     Prompt: "Implement slice 4 for memory operations
     (M+, M-, MR, MC) following established patterns"
     ```

3. **Merge and Resolve Conflicts**
   - Merge slice-3 to main
   - Merge slice-4 to main
   - Use AI to resolve conflicts:
     ```
     Prompt: "Help resolve merge conflicts between slice-3 and slice-4"
     ```

#### Part 3: Handling Token Limits (20 minutes)

1. **Test Limit Scenarios**

   - Request a very large implementation
   - Observe when limits are reached
   - Learn recovery strategies

2. **Implement Chunking Strategy**

   ```
   Instead of: "Implement slices 3, 4, and 5"

   Use: "Implement slice 3 only"
   Then: "Implement slice 4 only"
   Then: "Implement slice 5 only"
   ```

3. **Configure Timeout Settings**
   - Locate and adjust max execution time settings
   - Test with complex requests

### Validation Criteria

- [ ] Context is managed effectively
- [ ] Session files enable continuation
- [ ] Parallel development succeeds
- [ ] Merge conflicts are resolved
- [ ] Token limits are understood and managed

---

## Lab 5: Building Enterprise-Grade Applications with AI (90 minutes)

### Objectives

- Apply all learned concepts to a production scenario
- Implement full software development lifecycle
- Create comprehensive documentation
- Establish quality gates

### Prerequisites

- Completed all previous labs
- Understanding of enterprise requirements

### Instructions

#### Part 1: Requirements and Architecture (20 minutes)

1. **Define Enterprise Requirements**

   ```
   Prompt: "Create a requirements document for an enterprise calculator
   application including: user authentication, audit logging, error handling,
   accessibility, internationalization, and deployment options"
   ```

2. **Create Architecture Document**

   ```
   Prompt (using Senior Engineer mode): "Design the architecture for this
   enterprise application using vertical slices, clean architecture principles,
   and cloud-native patterns"
   ```

3. **Define Quality Gates**
   - Code coverage minimum (e.g., 80%)
   - Performance benchmarks
   - Security requirements
   - Accessibility standards

#### Part 2: Iterative Implementation (40 minutes)

1. **Implement Core Features** (20 minutes)

   - User authentication
   - Audit logging
   - Error handling

   ```
   Prompt: "Implement user authentication using Azure AD.
   Include proper error handling and audit logging"
   ```

2. **Add Cross-Cutting Concerns** (20 minutes)
   - Logging infrastructure
   - Exception handling
   - Performance monitoring
   ```
   Prompt: "Add comprehensive logging using Serilog, structured logging
   patterns, and Application Insights integration"
   ```

#### Part 3: Quality Assurance (30 minutes)

1. **Comprehensive Testing**

   ```
   Prompt (using Test Engineer mode): "Create comprehensive test suite including:
   - Unit tests (>80% coverage)
   - Integration tests
   - UI tests
   - Performance tests
   - Security tests"
   ```

2. **Security Review**

   ```
   Prompt: "Perform security review focusing on authentication,
   authorization, data protection, and OWASP top 10 vulnerabilities"
   ```

3. **Performance Testing**
   ```
   Prompt: "Create performance test scenarios and benchmarks for critical paths"
   ```

#### Part 4: Documentation and Deployment (20 minutes)

1. **Generate Documentation**

   ```
   Prompt: "Generate comprehensive documentation including:
   - Architecture overview
   - API documentation
   - Deployment guide
   - User manual
   - Developer onboarding guide"
   ```

2. **Create Deployment Pipeline**
   ```
   Prompt: "Create GitHub Actions workflow for CI/CD including:
   - Build
   - Test execution
   - Code quality gates
   - Security scanning
   - Automated deployment to staging
   - Manual approval for production"
   ```

### Validation Criteria

- [ ] All quality gates pass
- [ ] Code coverage exceeds 80%
- [ ] Security vulnerabilities addressed
- [ ] Performance meets benchmarks
- [ ] Documentation is complete
- [ ] CI/CD pipeline is functional
- [ ] Application is deployable

---

## Bonus Lab: Creating Custom Knowledge Bases (Optional, 30 minutes)

### Objectives

- Create a custom knowledge base for company-specific information
- Train AI on internal documentation
- Integrate custom models with GitHub Copilot

### Instructions

1. **Prepare Knowledge Base Content**

   - Collect internal documentation
   - Gather code examples
   - Document standards and practices

2. **Use Azure AI Studio**

   - Create custom knowledge base
   - Upload documents
   - Configure search and retrieval

3. **Integrate with Copilot**
   - Configure custom model endpoint
   - Test retrieval
   - Use in development:
     ```
     Prompt: "@custom-kb How should we implement error handling
     according to company standards?"
     ```

---

## Additional Resources

### Recommended Reading

- "Vertical Slice Architecture" by Jimmy Bogard
- "Clean Architecture" by Robert C. Martin
- "Test-Driven Development" by Kent Beck
- Books on AI ethics and limitations

### Tools and Extensions

- AI Toolkit for Visual Studio Code
- GitHub Copilot Agent Mode
- .NET MAUI Testing Framework
- Azure AI Studio

### Best Practices

1. Always review AI-generated code
2. Maintain human oversight in critical decisions
3. Use multiple personas for different perspectives
4. Keep context focused and relevant
5. Document architectural decisions
6. Establish quality gates early
7. Test comprehensively
8. Monitor AI token usage

### Common Pitfalls to Avoid

1. Over-reliance on AI without review
2. Not managing context size
3. Skipping validation steps
4. Implementing too much at once
5. Not using version control effectively
6. Ignoring performance implications
7. Insufficient testing
8. Poor documentation

---

## Lab Completion Checklist

After completing these labs, you should be able to:

- [ ] Implement applications using vertical slice architecture
- [ ] Generate comprehensive test suites (unit, integration, UI)
- [ ] Create and use custom chat modes/personas
- [ ] Manage complex AI development workflows
- [ ] Handle merge conflicts with AI assistance
- [ ] Build enterprise-grade applications with AI
- [ ] Establish quality gates and standards
- [ ] Create effective documentation
- [ ] Set up CI/CD pipelines
- [ ] Understand AI limitations and best practices

## Next Steps

1. Apply these concepts to your own projects
2. Create team-specific chat modes and instructions
3. Build a knowledge base for your organization
4. Establish AI-assisted development standards
5. Continue learning about AI capabilities and limitations

## Support and Questions

- Review session recordings for detailed examples
- Consult the course materials repository
- Reach out to the instructor for ongoing mentorship
- Share experiences and learnings with your team

---

**Remember**: AI is a powerful assistant, but human judgment, creativity, and oversight remain essential for producing high-quality, maintainable software that meets regulatory and business requirements.
