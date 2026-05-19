# Hands-On Labs for GitHub Copilot Training Day 1 Afternoon Session

Based on the material covered in the afternoon training session, here are targeted hands-on labs focusing on CI/CD integration, test-driven development, and Evergreen software practices.

---

## **Lab 1: CI/CD Pipeline Creation**

**Duration:** 45-60 minutes
**Prerequisites:** Completed morning labs, calculator project from morning session

### Objectives

- Create a CI/CD pipeline using GitHub Actions
- Integrate automated testing and code coverage reporting
- Enforce code quality thresholds in the pipeline
- Understand YAML pipeline configuration

### Activities

1. **Generate GitHub Actions Workflow:**

   - Prompt: "Create a GitHub Actions workflow that builds, tests, and enforces 50% code coverage threshold"
   - Review the generated `.github/workflows/*.yml` file
   - Understand the workflow triggers (push, pull request)

2. **Pipeline Components:**
   Review and understand each step:

   - Checkout code
   - Set up .NET SDK
   - Restore dependencies
   - Build project
   - Run tests with coverage
   - Install report generator tool
   - Generate coverage report
   - Upload coverage as artifact
   - Enforce coverage threshold

3. **Create Feature Branch and PR:**

   - Use Copilot to create a feature branch
   - Commit and push changes
   - Create a pull request
   - Observe pipeline execution

4. **Troubleshooting:**
   - If pipeline fails, use Copilot to diagnose issues
   - Common issues: NuGet package sources, dependency paths, permissions
   - Practice iterative problem-solving with AI

### Success Criteria

- GitHub Actions workflow file created and committed
- Pipeline successfully builds and tests the project
- Code coverage report generated and uploaded as artifact
- Coverage threshold enforcement working (fails if below 50%)
- Understanding of CI/CD principles and YAML syntax

### Discussion Points

- Why set up CI/CD early in project lifecycle?
- Benefits of automated testing in pipelines
- How to balance strictness vs. practicality in coverage thresholds
- Alternative CI/CD platforms (Azure DevOps, Jenkins, GitLab CI)

---

## **Lab 2: Test Coverage Improvement**

**Duration:** 30-45 minutes
**Prerequisites:** Lab 1 completed, existing test suite

### Objectives

- Analyze code coverage reports
- Use Copilot to intelligently add tests
- Achieve target coverage percentage
- Balance quantity vs. quality of tests

### Activities

1. **Review Current Coverage:**

   - Run tests with coverage reporting
   - Identify uncovered code paths
   - Analyze coverage percentage by file/class

2. **Targeted Test Generation:**

   - Prompt: "Add tests to increase code coverage to [X]%"
   - Observe how Copilot identifies gaps
   - Review generated tests for quality

3. **Strategic Coverage Improvement:**
   Instead of just asking for more coverage, try:

   - "Add tests for edge cases in division operation"
   - "Add tests for corner cases like divide by zero"
   - "Add integration tests for evaluate arithmetic method"

4. **Verify Test Quality:**

   - Are tests actually calling implementation code?
   - Do tests verify expected behavior, not just execution?
   - Are edge cases properly handled?

5. **Re-run Coverage:**
   - Execute test suite with coverage
   - Compare before/after percentages
   - Identify remaining gaps

### Success Criteria

- Code coverage increased by at least 20 percentage points
- All new tests are meaningful and test actual implementation
- Tests include edge cases and error conditions
- Coverage report shows improved metrics
- Understanding of test quality vs. quantity trade-offs

### Key Learning Point

As discovered in the session, asking Copilot to "increase coverage to 50%" can work, and it will intelligently identify which code paths need testing. This is more efficient than manually identifying gaps.

---

## **Lab 3: Test-Driven Development (TDD) with Copilot**

**Duration:** 45-60 minutes
**Prerequisites:** Understanding of TDD principles

### Objectives

- Practice TDD workflow with AI assistance
- Write failing tests before implementation
- Use tests to drive design decisions
- Understand red-green-refactor cycle

### Activities

1. **Define New Feature:**
   Choose a feature to implement (e.g., memory operations for calculator):

   - Store current result (ANS/answer functionality)
   - Recall previous result
   - Handle "ANS + 5" style operations

2. **Write Failing Tests First:**

   - Prompt: "Using TDD, create tests for a memory/answer feature in the calculator. DO NOT implement the feature yet."
   - Review generated tests
   - Verify tests reference methods that don't exist yet

3. **Run Tests (Expect Failures):**

   - Execute test suite
   - Observe compilation errors or test failures
   - Document what's missing

4. **Implement Feature to Pass Tests:**

   - Prompt: "Implement the memory/answer feature to make the tests pass"
   - Review generated implementation
   - Run tests again
   - Verify all tests now pass

5. **Refactor:**
   - With tests passing, ask for improvements
   - "Refactor the answer implementation for better readability"
   - Verify tests still pass after refactoring

### Success Criteria

- Tests written before implementation
- Initial test run shows failures (red phase)
- Implementation makes all tests pass (green phase)
- Code refactored while maintaining passing tests
- Understanding of TDD benefits and workflow

### TDD Cycle

1. **Red:** Write a failing test
2. **Green:** Write minimal code to make it pass
3. **Refactor:** Improve code while keeping tests green

---

## **Lab 4: Integration Testing**

**Duration:** 30-45 minutes
**Prerequisites:** Existing unit test suite

### Objectives

- Understand difference between unit and integration tests
- Create integration tests that test multiple components together
- Learn when to use each type of test

### Activities

1. **Analyze Current Tests:**

   - Review existing test suite
   - Identify which are unit tests (isolated, mocked dependencies)
   - Identify opportunities for integration tests

2. **Create Integration Tests:**

   - Prompt: "Add integration tests that exercise the calculator's evaluator with real input parsing"
   - Compare to unit tests that might mock the parser

3. **Use Inline Copilot Explanation:**

   - Select an integration test
   - Press `Ctrl+I` to open inline chat
   - Prompt: "Explain this test and how it differs from a unit test"

4. **Test Real Workflows:**
   Integration tests should test:

   - User enters "2 + 3" → evaluator processes → returns 5
   - Multiple operations: "10 \* 2 + 5" → proper precedence → returns 25
   - Error handling through full stack

5. **Understand Trade-offs:**
   Discuss:
   - Unit tests: Fast, isolated, pinpoint failures
   - Integration tests: Slower, test interactions, catch integration bugs
   - When to use each type

### Success Criteria

- Created at least 3 integration tests
- Tests exercise multiple components together
- Can articulate difference between unit and integration tests
- Understand when dependencies should be mocked vs. real
- Test suite has appropriate balance of unit and integration tests

### Discussion: Unit vs Integration Tests

**Unit Tests:**

- Mock external dependencies
- Test single component in isolation
- Very fast execution
- Pinpoint exact failure location

**Integration Tests:**

- Use real dependencies
- Test component interactions
- Slower execution
- Catch integration issues

As discussed in the session, for this calculator project there aren't external dependencies to mock, so the distinction is subtle. Integration tests might test the full evaluate→parse→calculate→format workflow.

---

## **Lab 5: Advanced Features with Scientific Operations**

**Duration:** 45-60 minutes
**Prerequisites:** Working calculator with basic operations

### Objectives

- Extend calculator with advanced features
- Work with mathematical functions
- Practice TDD on new features
- Maintain high code coverage

### Activities

1. **Plan Scientific Features:**
   Features to add:

   - Trigonometric functions (sin, cos, tan)
   - Logarithmic functions (log, ln)
   - Power and square root operations
   - Support for these in string expressions

2. **Write Tests First:**

   - Prompt: "Add tests for scientific calculator functions: sin, cos, tan, log, ln, sqrt, power"
   - Review generated tests
   - Run tests (should fail)

3. **Implement Features:**

   - Prompt: "Implement the scientific calculator functions to pass the tests"
   - Review implementation
   - Verify proper use of Math library
   - Check error handling (e.g., log of negative number)

4. **Test String Parsing:**

   - Ensure expressions like "sin(45)" work
   - Test "log(100)", "sqrt(16)", etc.
   - Verify proper precedence

5. **Update Coverage:**
   - Run tests with coverage
   - Verify new functions are well-tested
   - Aim to maintain or improve coverage percentage

### Success Criteria

- At least 6 new scientific functions implemented
- String parser handles function syntax
- Comprehensive tests for all new functions
- Edge cases handled (negative numbers, division by zero, etc.)
- Code coverage maintained above target threshold
- All tests passing

### Real-World Application

This lab demonstrates how to extend existing functionality systematically using TDD and AI assistance, maintaining quality throughout the process.

---

## **Lab 6: Building a User Interface**

**Duration:** 60-90 minutes
**Prerequisites:** Working console calculator

### Objectives

- Use Copilot to generate UI code
- Understand different UI frameworks
- Connect UI to existing business logic
- Practice iterative refinement of AI output

### Activities

1. **Choose UI Technology:**
   Options demonstrated in session:

   - WPF (Windows Presentation Foundation) for Windows desktop
   - Web-based (HTML/CSS/JavaScript)
   - Command-line with enhanced interface

2. **Generate Initial UI:**

   - Prompt: "Create a [WPF/web/etc.] UI for the calculator"
   - Review generated code
   - Understand project structure changes

3. **First Iteration - Text-Based UI:**
   As seen in the session, first attempt created a text input UI:

   - Text box for expression input
   - Enter key to evaluate
   - Display area for results
   - Simple but functional

4. **Iterate and Improve:**

   - Prompt: "Change the UI to look like a real calculator with buttons"
   - Review improvements
   - Test button click handlers
   - Verify proper integration with calculator logic

5. **Add Enhanced Features:**

   - History display
   - Memory buttons (M+, M-, MR, MC)
   - Scientific mode toggle
   - Theme options

6. **Test UI Functionality:**
   - Manual testing of all buttons
   - Verify correct calculations
   - Test error states
   - Check responsive behavior

### Success Criteria

- Functional UI created and running
- UI connects to existing calculator logic
- All operations accessible through UI
- Error messages display properly
- Understanding of UI framework basics
- Experienced iterative refinement with Copilot

### Discussion Points

- When is it better to start with text input vs. buttons?
- How to balance feature richness with development time?
- Testing strategies for UI code
- Separation of concerns (UI vs. business logic)

### Real-World Lesson

As demonstrated in the session, initial AI output may not match expectations (text-based vs. button-based calculator). This requires:

1. Clear, specific prompts
2. Willingness to iterate
3. Providing examples or references
4. Being prepared to guide the AI with more detail

---

## **Lab 7: Cross-Project Bug Tracking**

**Duration:** 30-40 minutes
**Prerequisites:** Multiple related projects or components

### Objectives

- Use Copilot to coordinate across codebases
- Practice root cause analysis
- Create effective prompts for other team members/projects
- Understand handoff communication

### Activities

1. **Scenario Setup:**
   Imagine a scenario where:

   - You have a UI project
   - And a back-end API project
   - A bug appears in the UI

2. **Root Cause Analysis:**
   In UI chat:

   - Prompt: "This button click isn't producing the expected result. What could be wrong?"
   - Review Copilot's analysis
   - Determine if it's a UI bug or back-end issue

3. **Generate Handoff Prompt:**
   If back-end is suspected:

   - Prompt: "Create a detailed prompt I can give to the back-end team to diagnose this issue"
   - Review generated documentation
   - Should include: symptoms, expected behavior, error messages, context

4. **Cross-Project Communication:**

   - Take the generated prompt to back-end project
   - Open that project in VS Code
   - Paste prompt into Copilot chat
   - Observe how it responds with different project context

5. **Close the Loop:**
   Practice the scenario where back-end AI points back to front-end:
   - "This is not a back-end issue. The problem is in the UI's request formatting."
   - Return to UI project with this information

### Success Criteria

- Successfully diagnosed issue location (UI vs. back-end)
- Created clear, detailed handoff documentation
- Practiced context switching between projects
- Understood how Copilot adapts to different codebases
- Experienced cross-team communication pattern

### Key Insight from Session

As John demonstrated, Copilot can act as an intermediary, helping teams communicate issues across project boundaries. It can analyze whether an issue belongs in component A or B, and generate appropriate documentation for the responsible team.

---

## **Lab 8: Controlling Copilot Output Verbosity**

**Duration:** 15-20 minutes
**Prerequisites:** Any previous lab with Copilot chat

### Objectives

- Learn to control how much explanation Copilot provides
- Balance detail with efficiency
- Customize output for different scenarios

### Activities

1. **Verbose Output (Default):**

   - Ask a coding question without constraints
   - Observe detailed explanations, multiple options, context

2. **Concise Output:**

   - Add to prompt: "Be concise in your response"
   - Compare to previous output
   - Note reduced explanations

3. **Minimal Output:**

   - Prompt: "Provide minimal output - just show the code without explanations"
   - Useful when you know what you want

4. **Contextual Adjustment:**
   Practice different levels for different needs:

   - Learning: Verbose (need explanations)
   - Rapid development: Concise (understand concepts, need quick answers)
   - Expert usage: Minimal (just need code snippets)

5. **Save Important Context:**
   When you get valuable explanations:
   - Copy to documentation
   - Save to project notes
   - Add as code comments

### Success Criteria

- Can request different levels of detail
- Understand when each level is appropriate
- Know how to save valuable AI-generated explanations
- Improved efficiency in AI interactions

### Prompt Examples

- "Explain in detail..." (verbose)
- "Give me a concise solution..." (balanced)
- "Show only the code..." (minimal)

---

## **Lab 9: Evergreen Software Analysis**

**Duration:** 45-60 minutes
**Prerequisites:** Completed calculator project from earlier labs

### Objectives

- Understand Evergreen software development principles
- Use Copilot to analyze technical debt
- Identify anti-patterns and code smells
- Create remediation plans

### Activities

1. **Evergreen Principles:**
   Understand what makes code "Evergreen":

   - ✅ Platform-independent
   - ✅ Uses relative paths, not absolute
   - ✅ No hard-coded environment-specific values
   - ✅ Up-to-date dependencies
   - ✅ Automated, reproducible builds
   - ✅ Comprehensive documentation
   - ✅ Minimal technical debt

2. **Analyze Your Code:**

   - Prompt: "Analyze this project for Evergreen software development principles. Identify issues that make it less maintainable or portable."
   - Review comprehensive analysis (as shown in session)

3. **Review Identified Issues:**
   Common issues found in session:

   - Hard-coded paths in log file references
   - Platform-specific SDK usage
   - Coverage HTML committed to repo
   - Pinned package versions requiring manual updates
   - Global tool dependencies not documented

4. **Prioritize Remediation:**

   - Categorize issues by severity
   - Identify quick wins vs. major refactors
   - Create action items

5. **Implement Fixes:**
   Choose 2-3 issues to fix:

   - Use Copilot to suggest solutions
   - Implement fixes
   - Verify improvements
   - Re-run analysis to confirm fixes

6. **Create Prevention Strategy:**
   - Prompt: "How can we prevent these issues in future development?"
   - Review suggestions for coding standards, CI checks, etc.

### Success Criteria

- Comprehensive analysis of technical debt completed
- Understand Evergreen software principles
- At least 2-3 issues remediated
- Prevention strategy documented
- Can identify similar issues in real projects

### Evergreen Issues Found in Session

**Issue Categories:**

1. **Fragile Paths:** Hard-coded, environment-specific paths
2. **Platform Coupling:** Windows-specific SDKs where cross-platform options exist
3. **Repository Pollution:** Generated files (HTML coverage reports) in source control
4. **Dependency Management:** Manual tool installation requirements, pinned versions
5. **Configuration:** Global tool assumptions, environment-specific settings

**For Each Issue, Analysis Provided:**

- What the issue is
- Why it's problematic
- Remediation steps
- Files affected

---

## **Lab 10: Preventing Technical Debt in CI/CD**

**Duration:** 30-45 minutes
**Prerequisites:** Lab 9 completed, CI/CD pipeline from Lab 1

### Objectives

- Integrate Evergreen analysis into CI/CD
- Automate technical debt detection
- Prevent new technical debt from being introduced
- Create failing builds for policy violations

### Activities

1. **Baseline Technical Debt:**

   - Run Evergreen analysis
   - Save results to a baseline file
   - Commit baseline to repository

2. **Create CI Check:**

   - Prompt: "Add a CI/CD step that runs the Evergreen analysis and compares against the baseline. Fail the build if new technical debt is introduced."
   - Review generated pipeline modification

3. **Understand the Process:**
   The CI step should:

   - Run the same Evergreen analysis prompt
   - Compare output to baseline file
   - Identify new issues (diff)
   - Fail build if new issues found
   - Report specific new problems

4. **Test the Gate:**

   - Intentionally introduce technical debt (hard-coded path)
   - Commit and push
   - Observe pipeline failure
   - Review failure details

5. **Fix and Verify:**

   - Remove technical debt
   - Push again
   - Pipeline should pass

6. **Establish Policy:**
   Document team agreement:
   - No new technical debt allowed
   - Existing debt must decrease over time
   - Each PR should improve or maintain quality

### Success Criteria

- Technical debt baseline established
- CI/CD pipeline enforces debt policy
- Build fails when new debt introduced
- Team understands and agrees to policy
- Path forward for reducing existing debt

### Key Concept: Technical Debt as a Ratchet

As discussed in session:

- **Traditional approach:** Allocate 10-20% of sprint to technical debt

  - Problem: You add more debt than you fix → debt grows

- **Evergreen approach:** Never add new debt
  - Each change must be Evergreen-compliant
  - Existing debt decreases over time
  - Eventually reach zero technical debt

---

## **Lab 11: Git Branch Management with Copilot**

**Duration:** 20-30 minutes
**Prerequisites:** Git repository initialized

### Objectives

- Use Copilot to help with Git operations
- Create and manage feature branches
- Handle common Git issues
- Understand Git workflows

### Activities

1. **Create Feature Branch:**

   - Prompt: "Create a feature branch for CI/CD implementation"
   - Review branch naming suggestions
   - Execute Git commands

2. **Handle Git Issues:**
   As encountered in session, Copilot may:

   - Execute commands in wrong directory
   - Need multiple attempts to succeed
   - Require explicit guidance on current directory

3. **Commit with Meaningful Messages:**

   - Prompt: "Generate a commit message for these changes"
   - Review and refine suggested message
   - Follow conventional commit format if desired

4. **Push and Create PR:**

   - Push branch to remote
   - Create pull request (manually or via Copilot)
   - Add PR description
   - Link to related issues

5. **Troubleshoot Common Problems:**
   Practice resolving:
   - Authentication issues
   - Remote configuration problems
   - Merge conflicts
   - Divergent branches

### Success Criteria

- Created and pushed feature branch successfully
- Generated meaningful commit messages
- Created pull request
- Resolved at least one Git issue with Copilot's help
- Understanding of Git workflow

### Real-World Lesson from Session

Git operations with Copilot can be inconsistent. It may:

- Execute in wrong directory
- Need multiple attempts
- Require explicit current directory information

**Best Practice:** Verify Copilot's Git commands before executing, especially for destructive operations.

---

## **Lab 12: GitHub Issues Generation**

**Duration:** 20-30 minutes
**Prerequisites:** GitHub repository

### Objectives

- Automate issue creation from code analysis
- Generate well-structured GitHub issues
- Link issues to code locations
- Create actionable work items

### Activities

1. **Analyze Code for Improvements:**

   - Prompt: "Analyze this code and create GitHub issues for improvements needed"
   - Review suggested issues

2. **Generate Issue Files:**
   As seen in session:

   - Copilot can create markdown files for each issue
   - Files include title, description, acceptance criteria
   - Structured format ready for GitHub

3. **Review Issue Quality:**
   Good issues should have:

   - Clear, descriptive title
   - Detailed description
   - Specific acceptance criteria
   - File and line references
   - Priority/severity indication

4. **Create Issues in GitHub:**

   - Either manually create from generated files
   - Or use GitHub CLI with Copilot assistance
   - Organize with labels and milestones

5. **Link to Project Board:**
   - Add issues to project tracking
   - Prioritize work items
   - Assign to team members

### Success Criteria

- Generated at least 3 well-structured issues
- Issues are specific and actionable
- Issues linked to code locations
- Understanding of automated issue management
- Issues created in GitHub (or ready to create)

### Example Issues from Session

1. **Add unit tests for evaluate arithmetic and edge cases**

   - Description: Improve test coverage
   - Acceptance criteria: Tests for specific scenarios
   - File references: test file locations

2. **Add integration tests**
   - Description: Test component interactions
   - Acceptance criteria: Full workflow testing

---

## **Lab Sequence Recommendations**

### **Afternoon Session Follow-up (Core Skills)**

**Labs:** 1, 2, 3, 4
**Time Required:** 2.5-3.5 hours
**Focus:** CI/CD, testing strategies, TDD

### **Extended Afternoon Practice (Advanced)**

**Labs:** 1-7
**Time Required:** 4.5-6 hours
**Focus:** Full development workflow with Evergreen principles

### **Full Day Workshop Integration**

**Morning:** Day 1 Morning Labs (Fundamentals)
**Afternoon:** Labs 1-4 from this session
**Time Required:** 6-8 hours total
**Focus:** Complete greenfield development cycle

### **Quality & Sustainability Focus**

**Labs:** 2, 3, 9, 10
**Time Required:** 2.5-3.5 hours
**Focus:** Test quality, technical debt, Evergreen practices

---

## **Assessment Criteria**

Participants should demonstrate:

### **Technical Skills**

- ✅ Create and configure CI/CD pipelines
- ✅ Generate and improve test coverage
- ✅ Practice test-driven development
- ✅ Distinguish unit from integration tests
- ✅ Extend applications with new features
- ✅ Build user interfaces
- ✅ Analyze code for technical debt
- ✅ Manage Git workflows

### **AI Collaboration Skills**

- ✅ Write specific, contextual prompts
- ✅ Iterate on AI output to improve results
- ✅ Control verbosity and output format
- ✅ Use AI for cross-project coordination
- ✅ Validate AI suggestions before accepting

### **Quality Practices**

- ✅ Maintain or improve code coverage
- ✅ Write meaningful tests (not just coverage)
- ✅ Identify and remediate technical debt
- ✅ Apply Evergreen software principles
- ✅ Prevent new technical debt introduction

---

## **Key Concepts from Afternoon Session**

### **1. CI/CD Pipeline Early**

"When I have my DevOps hat on, the pipeline is one of the very first things I want to see working." - John Miller

**Why:**

- Immediate feedback on build/test status
- Deploy to independent environments early
- Demonstrate progress to stakeholders
- Catch integration issues sooner

### **2. Test Coverage Intelligence**

You can ask Copilot to "increase coverage to X%" and it will:

- Analyze current coverage
- Identify uncovered code paths
- Generate appropriate tests
- Target specific gaps

### **3. Test Quality > Quantity**

Coverage percentage is important but:

- Tests must verify actual behavior
- Edge cases and error conditions matter
- Integration tests complement unit tests
- Real bugs require real fixes, not just more tests

### **4. Test-Driven Development with AI**

TDD cycle with Copilot:

1. Write failing tests first (Red)
2. Implement minimal code to pass (Green)
3. Refactor with tests as safety net
4. AI helps with all three phases

### **5. Evergreen Software Development**

**Definition:** Code that remains maintainable, portable, and up-to-date without constant refactoring.

**Principles:**

- No hard-coded paths or environment-specific values
- Platform-independent where possible
- Automated builds and tests
- Up-to-date dependencies
- Minimal technical debt

**Anti-pattern:** Allocating 10-20% of sprint to technical debt

- You add more debt than you fix
- Debt grows over time
- Eventually becomes unmaintainable

**Evergreen pattern:** Never add new debt

- Each change must be Evergreen-compliant
- Existing debt only decreases
- Eventually reach zero technical debt

### **6. Technical Debt as Quality Gate**

Can be enforced in CI/CD:

1. Establish baseline of current technical debt
2. Run analysis on each PR
3. Compare to baseline
4. Fail build if new debt introduced
5. Require fixes before merge

### **7. Cross-Project Communication**

Use AI to coordinate between components:

- Analyze issue in one project
- Determine root cause location
- Generate detailed prompt for other team
- Transfer context effectively
- Close feedback loop

### **8. Iterative UI Development**

First attempt may not match expectations:

- Start with simple/functional
- Iterate to improve
- Provide specific guidance
- Use examples or mockups
- Be prepared for multiple rounds

### **9. Context-Specific Prompts**

Control output to your needs:

- Verbose: Learning new concepts
- Concise: Balanced efficiency
- Minimal: Expert-level, code only
- Save valuable explanations

---

## **Common Challenges & Solutions**

### **Challenge 1: Pipeline Configuration Issues**

**Problem:** NuGet sources, authentication, paths
**Solution:**

- Use Copilot to diagnose specific error messages
- Iterate on configuration
- Test locally before committing
- Document environment requirements

### **Challenge 2: Tests Don't Improve Coverage**

**Problem:** New tests don't increase coverage percentage
**Solution:**

- Verify tests actually call implementation code
- Check that tests aren't just testing language features
- Review coverage report to see what's missing
- Ask Copilot specifically about uncovered lines

### **Challenge 3: Too Much or Too Little AI Output**

**Problem:** Can't see the code for the explanations (or vice versa)
**Solution:**

- Adjust prompts: "be concise" or "explain in detail"
- Save important explanations separately
- Use appropriate verbosity for context

### **Challenge 4: Git Issues with Copilot**

**Problem:** Commands executed in wrong directory, authentication failures
**Solution:**

- Verify current directory before Git operations
- Provide explicit path information
- Use terminal directly for complex Git operations
- Double-check commands before executing

### **Challenge 5: Generated UI Doesn't Match Vision**

**Problem:** Text input instead of button-based calculator
**Solution:**

- Be very specific in prompts
- Provide examples or mockups
- Reference existing UIs
- Iterate multiple times
- Break into smaller steps

---

## **Best Practices Reinforced**

### **From Morning (Refresher):**

- ✅ Always review AI-generated code
- ✅ Test everything thoroughly
- ✅ Provide specific context in prompts
- ✅ Critical thinking required

### **Added from Afternoon:**

- ✅ Set up CI/CD early in project lifecycle
- ✅ Use code coverage as guide, not absolute metric
- ✅ Practice TDD with AI as pair programmer
- ✅ Analyze and prevent technical debt systematically
- ✅ Document Evergreen principles for team
- ✅ Iterate on AI output until it meets needs
- ✅ Save valuable AI-generated explanations
- ✅ Use AI for cross-component communication

---

## **Connections to Tomorrow's Content**

The afternoon session ended with a preview of Day 2:

**Focus:** Working with Legacy Code

- Taking the "legacy" code we created today
- Applying Evergreen analysis
- Systematic remediation of technical debt
- Maintaining Evergreen standards going forward

**Key Transition:** We've created code that has technical debt (as the Evergreen analysis showed). Tomorrow we'll learn how to:

1. Assess legacy codebases
2. Identify improvement opportunities
3. Systematically remediate issues
4. Establish ongoing quality practices
5. Keep code in Evergreen state

---

## **Additional Practice Ideas**

### **For Teams**

- Rotate roles: One person prompts, others review
- Compare different AI approaches to same problem
- Establish team coding standards via instruction files
- Practice code review of AI-generated code

### **For Individuals**

- Try same lab with different programming language
- Experiment with different AI models
- Document patterns that work well for your domain
- Build a library of effective prompts

### **Real Project Application**

- Apply Evergreen analysis to actual project
- Set up CI/CD pipeline for team project
- Improve test coverage on existing code
- Create GitHub issues from analysis

---

## **Success Metrics**

Participants successfully complete these labs when they can:

1. **Independently** create and configure CI/CD pipelines
2. **Strategically** improve code coverage with quality tests
3. **Effectively** practice test-driven development
4. **Critically** distinguish between unit and integration tests
5. **Systematically** analyze code for technical debt
6. **Proactively** prevent new technical debt
7. **Iteratively** refine AI output to meet requirements
8. **Collaboratively** use AI for cross-team communication

Most importantly, participants should understand:

- **CI/CD enables fast, reliable feedback loops**
- **Test quality matters more than coverage percentage**
- **Evergreen development prevents technical debt accumulation**
- **AI is a collaborative partner requiring guidance and validation**

---

## **Resources for Further Learning**

### **CI/CD**

- GitHub Actions documentation
- Azure DevOps pipelines
- Jenkins tutorials
- GitLab CI/CD guides

### **Testing**

- Test-driven development books/courses
- Unit testing best practices
- Integration testing strategies
- Code coverage tools comparison

### **Evergreen Software**

- Technical debt management
- Software maintainability patterns
- Continuous refactoring practices
- Code quality metrics

### **AI-Assisted Development**

- Prompt engineering techniques
- GitHub Copilot best practices
- AI pair programming patterns
- Code review with AI

---

## **Instructor Notes**

### **Lab 1 (CI/CD):**

- Expect troubleshooting - this is valuable learning
- Common issues: authentication, paths, package sources
- Don't rush through errors - use them as teaching moments
- Peter's comment: "I'm more interested in the concepts" - balance working vs. understanding

### **Lab 3 (TDD):**

- Emphasize red-green-refactor cycle
- Show how AI helps with all three phases
- Discuss benefits: design feedback, safety net, documentation

### **Lab 6 (UI):**

- First attempt may not match expectations (text input vs. buttons)
- Use this as teaching moment about iteration
- Show how to refine prompts for better results

### **Lab 9 (Evergreen):**

- This is the "aha moment" lab
- Shows power of AI for code analysis
- Sets up tomorrow's legacy code work
- "Where the real power comes into play" - John Miller

### **Lab 10 (Debt Prevention):**

- Connect to earlier discussion about sprint allocation
- Emphasize prevention over remediation
- Show how to operationalize quality standards

---

## **Next Steps**

After completing these labs:

- Review Evergreen analysis results
- Prepare for Day 2: Legacy Code Remediation
- Consider which issues to address in your real projects
- Discuss team adoption strategies
- Document lessons learned

**Day 2 Preview:** We'll take legacy code (including what we created today) and systematically improve it using Copilot, applying Evergreen principles throughout.
