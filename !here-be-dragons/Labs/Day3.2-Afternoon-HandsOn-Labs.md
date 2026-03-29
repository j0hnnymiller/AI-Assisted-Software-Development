# Day 3 Afternoon - Hands-On Labs

## AI-Assisted Software Development Course

---

## Lab 1: Constraint Enforcement and Multi-Layer Defense Strategy

**Objective:** Learn to enforce project constraints and prevent AI from violating established rules.

**Scenario:** You have a project that must use .NET 8 but AI keeps suggesting .NET 9 features.

### Tasks:

1. **Create a Project Constraint File**

   - Create an instruction file that explicitly states: "CRITICAL: Must use .NET 8 only, no .NET 9 features"
   - Add this constraint to multiple instruction files for redundancy
   - Use clear markers like "CRITICAL" to emphasize importance

2. **Implement Enforcement Mechanisms**

   - Modify the `.csproj` file to specify the language version
   - Create a `global.json` file to lock the SDK version
   - Ask AI to create a `verify-constraints.ps1` script that checks for version compliance

3. **Create a Pre-Code Checklist**

   - Ask AI to generate a checklist file that must be verified before any code generation
   - Include items like:
     - Verify project uses .NET 8 only
     - Check for C# 12 compatibility (not C# 13)
     - Ensure no preview or experimental features
     - List common .NET 9 features to avoid

4. **Set Up Pre-Commit Hooks**

   - Create a Git pre-commit hook that runs the constraint verification script
   - Configure the hook to block commits if constraints are violated
   - Test by attempting to commit code with .NET 9 features

5. **CI/CD Integration**
   - Add constraint verification to your CI/CD pipeline
   - Ensure the build fails if constraints are violated

**Discussion Questions:**

- What are the advantages of multi-layer defense for constraint enforcement?
- How can you make instruction files more effective in guiding AI behavior?
- When would you use automated enforcement vs. human review?

---

## Lab 2: Instruction File Validation with Context Checking

**Objective:** Learn to validate instruction files for consistency and identify conflicts before they cause issues.

**Scenario:** You have multiple instruction files that may contain conflicting guidance.

### Tasks:

1. **Create Instruction Files**

   - Generate at least 3 instruction files for your project:
     - Project requirements (technology stack, constraints)
     - Coding standards (naming conventions, style guidelines)
     - Testing practices (coverage targets, test patterns)

2. **Create a Context Check Instruction**

   - Create or copy the `check-context.instructions.md` file
   - This should check for:
     - Conflicting instructions
     - Factual inconsistencies
     - Logical contradictions
     - Technical incompatibilities
     - Communication gaps
     - Duplication and redundancy

3. **Run Context Validation**

   - Use the check-context prompt with all instruction files in scope
   - Review the report for:
     - Critical issues (e.g., .NET version conflicts)
     - Medium severity issues (e.g., duplication)
     - Low severity issues (e.g., naming inconsistencies)

4. **Resolve Conflicts**

   - Address each conflict identified
   - Update instruction files to align with project requirements
   - Re-run validation to ensure issues are resolved

5. **Create an Instruction Standards File**
   - Generate an instruction file that defines standards for creating other instruction files
   - Include:
     - Required front matter format
     - Naming conventions (e.g., `*instructions.md`)
     - Structure guidelines
     - Apply-to patterns

**Discussion Questions:**

- How often should you validate instruction files during a project?
- What's the best way to handle conflicting requirements from different stakeholders?
- How can you prevent instruction drift over time?

---

## Lab 3: Code Base Review Against Instructions

**Objective:** Audit existing code to identify deviations from established instructions and create a technical debt backlog.

**Scenario:** You've defined project standards but need to assess compliance in existing code.

### Tasks:

1. **Create a Code Base Review Prompt**

   - Generate or use the `codebase-review.prompt.md` file
   - Configure it to:
     - Analyze the repository
     - Report deviations from instruction files
     - Prioritize issues by severity and effort

2. **Run the Review**

   - Execute the code base review with all instruction files in context
   - Let AI scan the entire project structure
   - Wait for the comprehensive audit report

3. **Analyze the Results**

   - Review positive findings (what's working well)
   - Examine technical debt items identified
   - Note compliance gaps by category:
     - Naming conventions
     - Code documentation
     - Test coverage
     - Error handling
     - Architectural patterns

4. **Create a Remediation Plan**

   - Group issues by:
     - Priority (critical, high, medium, low)
     - Effort required (quick wins vs. major refactoring)
     - Impact on system
   - Generate work items or issues for tracking
   - Assign to appropriate sprint/backlog

5. **Address One Compliance Gap**
   - Select one medium-severity issue
   - Ask AI to fix it according to the instruction files
   - Verify the fix resolves the issue
   - Re-run the review to confirm

**Discussion Questions:**

- How does this approach compare to traditional code reviews?
- What types of issues are best caught by AI vs. human reviewers?
- How would you integrate this into a regular development workflow?

---

## Lab 4: Comprehensive Test Gap Analysis

**Objective:** Identify missing tests using behavior-focused analysis rather than line coverage metrics.

**Scenario:** Your project has 77% code coverage but you want to ensure all critical functionality is properly tested.

### Tasks:

1. **Create Test Gap Analysis Prompt**

   - Use or create the `test-gap-analysis.prompt.md` file
   - Configure it to:
     - Discover existing test infrastructure
     - Inventory current tests by type (unit, integration, e2e)
     - Map critical functionality
     - Identify gaps and risks
     - Recommend specific tests with rationale

2. **Run Gap Analysis**

   - Execute the prompt against your test project
   - Review the comprehensive report including:
     - Current test framework and tooling
     - Test inventory by component
     - Coverage statistics
     - Gap analysis by priority

3. **Analyze Critical Gaps**

   - Identify Phase 1 (critical) gaps:
     - Core mathematical or business logic functions
     - Error handling and edge cases
     - UI interaction paths
     - Integration points
   - Note the predicted coverage improvement

4. **Implement Phase 1 Tests**

   - Ask AI to implement all Phase 1 critical gap tests
   - Review generated tests for:
     - Appropriate test patterns
     - Edge case coverage
     - Proper assertions
     - Clear test names
   - Run tests to verify they pass

5. **Address Test Failures**

   - If tests fail, determine if issue is in:
     - The test code (fix the test)
     - The implementation (fix the bug)
   - Work with AI to resolve issues
   - Re-run until all tests pass

6. **Verify Coverage Improvement**
   - Run code coverage analysis
   - Compare before/after metrics
   - Confirm predicted improvements were achieved

**Discussion Questions:**

- How does behavior-focused testing differ from line coverage?
- What are the limitations of automated test generation?
- How do you balance test coverage with development velocity?

---

## Lab 5: Creating Evergreen Development Instructions

**Objective:** Set up instructions for keeping dependencies and frameworks up-to-date.

**Scenario:** You want to establish a process for regular updates while maintaining stability.

### Tasks:

1. **Generate Evergreen Development Instructions**

   - Ask AI to create an `evergreen-development.instructions.md` file
   - Include guidance on:
     - Current framework versions
     - Update cadence (e.g., quarterly reviews)
     - Testing requirements before updates
     - Rollback procedures
     - Documentation requirements

2. **Apply Instruction Standards**

   - Use your instruction standards file to ensure consistency
   - Verify the file includes:
     - Proper front matter
     - Clear scope definitions
     - Prerequisites
     - Output requirements

3. **Resolve Version Conflicts**

   - If you have version-specific constraints (like .NET 8),
     adjust the Evergreen instructions accordingly
   - Document the migration plan for when you're ready to upgrade
   - Run context check to ensure no conflicts

4. **Define Update Process**

   - Create a workflow for:
     - Assessing available updates
     - Testing in development environment
     - Reviewing breaking changes
     - Planning migration
     - Executing updates
     - Validating results

5. **Test the Process**
   - Identify one minor dependency update
   - Follow your new Evergreen process
   - Document any issues or improvements

**Discussion Questions:**

- How do you balance staying current with maintaining stability?
- What role should AI play in managing technical debt?
- How often should dependency updates be reviewed?

---

## Lab 6: Creating Automated Style Checks in PRs

**Objective:** Set up automated code style validation that runs on pull requests.

**Scenario:** You want to ensure all code follows your style guidelines before it's merged.

### Tasks:

1. **Create a Style Evaluation Prompt**

   - Generate a `evaluate-csharp-style.prompt.md` file
   - Define what it should check:
     - Naming conventions (PascalCase, camelCase, etc.)
     - Code organization
     - Documentation standards
     - Best practices
   - Specify pass/fail criteria

2. **Design the Workflow**

   - Ask AI to create a GitHub Actions workflow file
   - Configure it to:
     - Trigger on pull request creation/update
     - Read the style evaluation prompt
     - Read relevant instruction files
     - Analyze only changed .cs files
     - Use GitHub Copilot API for evaluation
     - Post results as PR comment
     - Pass or fail the check

3. **Simplify the Workflow**

   - Ensure the workflow reads from prompt files rather than embedding logic
   - Remove regex or other inline validation code
   - Make it easy to update rules by editing instruction files only

4. **Test Locally First**

   - Create a test with intentional style violations
   - Run the style evaluation prompt manually
   - Verify it catches the issues
   - Review the report format

5. **Deploy and Test the Workflow**

   - Commit the workflow file
   - Merge to main branch
   - Create a new branch with style violations
   - Create a PR and verify:
     - Workflow triggers
     - Style check runs
     - Results posted to PR
     - Check passes/fails appropriately

6. **Iterate and Improve**
   - If checks don't work as expected, refine the prompt
   - Test different types of violations
   - Adjust severity levels
   - Document the process in a README

**Discussion Questions:**

- What types of style issues are best caught by automation?
- How do you handle false positives in automated checks?
- Should style checks block merging or just provide guidance?

---

## Lab 7: Multi-Step Task Automation with Progress Tracking

**Objective:** Use AI to complete complex tasks with multiple steps while tracking progress.

**Scenario:** You need to implement several related test files and want visibility into progress.

### Tasks:

1. **Define a Multi-Step Task**

   - Choose a complex task like:
     - Implementing all Phase 1 critical tests
     - Refactoring a component to match standards
     - Adding comprehensive error handling
   - Break it into clear, testable steps

2. **Request AI Create a To-Do List**

   - Ask AI to create a to-do list for the task
   - Ensure each item is:
     - Specific and actionable
     - Testable/verifiable
     - Properly scoped (not too large)

3. **Monitor Progress**

   - Watch as AI:
     - Marks items as in-progress
     - Completes implementation
     - Marks items as completed immediately
     - Moves to next item
   - Note the transparency this provides

4. **Handle Issues**

   - If AI encounters problems:
     - Review the error
     - Provide guidance
     - Let AI adjust approach
     - Continue tracking progress

5. **Verify Completion**

   - When all items are marked complete:
     - Run tests to verify
     - Check code quality
     - Review documentation
   - Confirm the task meets requirements

6. **Create a Template**
   - Document the pattern for multi-step tasks
   - Create a prompt template for similar work
   - Share with team for consistency

**Discussion Questions:**

- When should you use to-do lists vs. single-shot requests?
- How do you balance AI autonomy with human oversight?
- What types of tasks are best for multi-step automation?

---

## Lab 8: Iterative Workflow Improvement

**Objective:** Learn the iterative process of refining AI-generated automation.

**Scenario:** Your first attempt at a workflow doesn't work perfectly - refine it through iterations.

### Tasks:

1. **Start with Initial Requirements**

   - Define what you want to automate (e.g., style checking on PR)
   - Write a clear but brief prompt
   - Let AI generate the initial solution

2. **Test the First Version**

   - Deploy or run the generated solution
   - Identify what works and what doesn't
   - Document specific issues

3. **Provide Specific Feedback**

   - Don't just say "it doesn't work"
   - Be specific: "Don't use regex, use the instruction file instead"
   - Or: "The prompt should be in a separate file, not embedded"
   - Give clear direction for improvements

4. **Iterate on the Solution**

   - Let AI make adjustments
   - Test again
   - Provide more feedback
   - Continue until it works correctly

5. **Document the Process**

   - Keep a log of:
     - Initial requirements
     - Issues encountered
     - Refinements made
     - Final working solution
   - This becomes valuable institutional knowledge

6. **Extract Patterns**
   - Identify what worked well
   - Note common pitfalls
   - Create guidelines for similar tasks
   - Update instruction files if needed

**Discussion Questions:**

- How many iterations are typical for complex automation?
- When should you start over vs. continuing to refine?
- How do you know when a solution is "good enough"?

---

## Lab 9: Creating Reusable Prompts

**Objective:** Build a library of prompts that can be reused across projects.

**Scenario:** You've created several useful prompts and want to standardize them for team use.

### Tasks:

1. **Identify Common Patterns**

   - Review prompts you've created:
     - Test gap analysis
     - Code base review
     - Style evaluation
     - Constraint checking
   - Identify which are project-specific vs. reusable

2. **Parameterize Prompts**

   - Convert hard-coded values to placeholders
   - Example: `<FRAMEWORK_VERSION>` instead of ".NET 8"
   - Document required parameters
   - Provide example values

3. **Create a Prompts Library Structure**

   ```
   prompts/
     general/
       codebase-review.prompt.md
       test-gap-analysis.prompt.md
     technology-specific/
       dotnet/
         evaluate-csharp-style.prompt.md
       python/
         evaluate-python-style.prompt.md
   ```

4. **Document Each Prompt**

   - Add front matter or README with:
     - Purpose and use cases
     - Required context/files
     - Parameters to customize
     - Expected output format
     - Example usage

5. **Test Across Projects**

   - Try using a prompt in a different project
   - Identify customization needs
   - Refine for broader applicability
   - Update documentation

6. **Share with Team**
   - Create a team wiki or documentation
   - Conduct a brief training session
   - Gather feedback and iterate
   - Establish a process for adding new prompts

**Discussion Questions:**

- What makes a prompt reusable vs. project-specific?
- How do you balance flexibility with simplicity?
- Who should maintain the prompts library?

---

## Lab 10: Debugging AI-Generated Code Issues

**Objective:** Learn to identify and fix issues when AI makes mistakes.

**Scenario:** AI generated tests that are failing or changed the wrong thing.

### Tasks:

1. **Reproduce the Issue**

   - Run the code/tests
   - Capture the exact error message
   - Identify what's wrong:
     - Bug in implementation?
     - Bug in test?
     - Misunderstanding of requirements?

2. **Analyze AI's Reasoning**

   - Review the code AI generated
   - Try to understand why it made that choice
   - Check if your prompt was ambiguous
   - Verify instruction files were clear

3. **Provide Corrective Guidance**

   - Don't just say "fix it"
   - Explain the correct approach:
     - "The test is correct, fix the implementation"
     - "The E character is valid in scientific notation"
   - Reference instruction files if relevant

4. **Verify the Fix**

   - Let AI correct the issue
   - Run tests again
   - Confirm the problem is resolved
   - Check for side effects

5. **Prevent Future Occurrences**

   - Update instruction files to clarify
   - Add the scenario to test cases
   - Document the lesson learned
   - Share with team if applicable

6. **Common AI Mistakes to Watch For**
   - Changing tests to match buggy code
   - Ignoring instruction files
   - Making assumptions about requirements
   - Over-engineering simple solutions
   - Using deprecated patterns

**Discussion Questions:**

- How do you know when to trust AI's judgment?
- What are red flags that AI might be heading down the wrong path?
- How do you build confidence in AI-generated code?

---

## Bonus Lab: Full Workflow Integration

**Objective:** Integrate multiple automated checks into a complete development workflow.

**Scenario:** Set up a complete automated quality pipeline.

### Tasks:

1. **Map Your Quality Gates**

   - Build success
   - Unit tests pass
   - Code coverage threshold
   - Style compliance
   - Constraint compliance
   - Security scan (if applicable)

2. **Create Workflows for Each Gate**

   - CI/CD pipeline (build and test)
   - PR style checker
   - Constraint verifier
   - Coverage reporter

3. **Integrate with Development Process**

   - Pre-commit hooks for local checks
   - PR automation for review
   - Merge requirements
   - Post-merge validation

4. **Add Reporting**

   - Dashboard for metrics
   - Notifications for failures
   - Trend analysis over time

5. **Document for Team**

   - Setup instructions
   - How to run locally
   - How to bypass (when appropriate)
   - Troubleshooting guide

6. **Gather Feedback and Iterate**
   - Are checks too strict/loose?
   - Are they catching real issues?
   - Are they slowing development?
   - What improvements are needed?

---

## Additional Resources

### Recommended Reading

- GitHub Actions documentation for workflow syntax
- Best practices for instruction file creation
- Code coverage vs. test quality metrics
- Constraint-based development principles

### Tools to Explore

- GitHub Copilot API
- Code coverage tools (coverlet, etc.)
- Pre-commit hook frameworks
- Static analysis tools

### Next Steps

- Apply these patterns to your real projects
- Build a team library of prompts and instructions
- Establish team standards for AI-assisted development
- Share lessons learned with the broader community

---

## Conclusion

These labs cover the key topics from Day 3 Afternoon:

- Constraint enforcement and multi-layer defense
- Instruction file validation and management
- Code base auditing and technical debt identification
- Test gap analysis and test generation
- Automated quality checks in CI/CD
- Iterative refinement of AI-generated solutions
- Building reusable patterns and prompts

The goal is to move from ad-hoc AI assistance to systematic, repeatable processes that improve code quality and maintain consistency across your projects.
