---
ai_generated: true
model: "openai/gpt-5.3-codex@2026-03-16"
operator: "johnmillerATcodemag-com"
chat_id: "calculator-project-exercise-deck-20260317"
prompt: |
  create an exercise slide deck, using the #file:exercise-template.md, for the provided calculator project exercise content.
started: "2026-03-17T03:28:00Z"
ended: "2026-03-17T03:36:00Z"
task_durations:
  - task: "content normalization"
    duration: "00:03:00"
  - task: "deck authoring"
    duration: "00:05:00"
total_duration: "00:08:00"
ai_log: "ai-logs/2026/03/17/calculator-project-exercise-deck-20260317/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---
# Exercise: Calculator Project Setup || Exercise: The Calculator That Launched a Thousand Prompts

## Exercise: Calculator Project - Setup and Basic Implementation

Objectives

- Use AI to generate starter code for arithmetic operations
- Understand how to validate AI-generated logic
- Integrate addition, subtraction, multiplication, and division functions

Activities

1. Project Initialization:

- Prompt AI to create a new project
- Review generated project structure
- Verify build configuration

2. Implement Basic Operations:

- Prompt AI to add methods for addition, subtraction, multiplication, and division

3. Review the Code:

- Check correctness and edge cases

4. Build and Run:

- Use Copilot to help with build commands
- Troubleshoot compilation errors with Copilot
- Run the application

Success Criteria

- Working calculator with 4 basic operations
- Application compiles and runs successfully
- Generated code is critically reviewed

::: notes
Duration ~01:00

## Setup and Basic Implementation Exercise Instructions

**Prerequisites:** Calculator project context available

### Objectives

- Scaffold core operations with AI assistance.
- Validate generated logic before accepting changes.
- Deliver a working baseline calculator.

### Activities

- Build project skeleton, implement 4 operations, and verify behavior.
- Emphasize manual review of AI output before merge.

### Success Criteria

- Four operations work end-to-end.
- Build is green.
- Team can explain logic and edge-case handling.
  :::

---

## Exercise: Calculator Project - Clear / Reset

Objectives

- Use AI to scaffold state-management logic
- Implement CE (clear entry) and C (clear all) behaviors
- Understand UI state transitions

Activities

1. Ask AI to outline the difference between CE and C
2. Generate code for clearing current input vs full state
3. Integrate logic into calculator state object
4. Test transitions with sample input sequences

Success Criteria

- CE clears only the active entry
- C resets the entire calculator state

::: notes
Duration ~00:15

## Clear / Reset Exercise Instructions

**Prerequisites:** Basic calculator state model

### Objectives

- Separate entry-level clear from full reset behavior.
- Verify expected transitions from each action.

### Activities

- Use focused prompts and test state transitions quickly.

### Success Criteria

- CE and C behaviors are consistent and explainable.
  :::

---

## Exercise: Calculator Project - Decimal Input

Objectives

- Use AI to generate input-validation logic
- Prevent multiple decimal points
- Ensure decimals flow through arithmetic operations

Activities

1. Ask AI for a decimal input strategy
2. Generate code to block duplicate decimals in one number
3. Integrate decimal support into input parser
4. Test decimal operations with AI-generated test cases

Success Criteria

- Decimal input works without duplication errors
- Arithmetic with decimals is correct
- Validation logic is explainable

::: notes
Duration ~00:12

## Decimal Input Exercise Instructions

**Prerequisites:** Input parser in place

### Objectives

- Implement robust decimal parsing and validation.

### Activities

- Target parser rules, then validate with focused tests.

### Success Criteria

- No duplicate decimal points accepted.
- Decimal math behaves correctly.
  :::

---

## Exercise: Calculator Project - Sign Toggle (+/-)

Objectives

- Use AI to generate sign-toggle logic
- Understand effect on active input and stored value

Activities

1. Ask AI to generate toggle-sign function for active value
2. Integrate into input workflow
3. Test before and after digit entry

Success Criteria

- Sign toggle works for integers and decimals
- Learner can explain stored vs active value impact

::: notes
Duration ~00:08

## Sign Toggle Exercise Instructions

**Prerequisites:** Numeric input flow functioning

### Objectives

- Add predictable sign toggling.

### Activities

- Keep implementation minimal and test transitions.

### Success Criteria

- Toggle is stable across value states.
  :::

---

## Exercise: Calculator Project - Percentage

Objectives

- Use AI to clarify percentage interpretation rules
- Implement percentage logic for common patterns
- Validate behavior with AI-generated examples

Activities

1. Ask AI how percentage should behave in a standard calculator
2. Generate code for:

- X x Y%
- Y + X%
- Y - X%

3. Test each pattern with AI-generated values

Success Criteria

- Percentage operations match standard calculator behavior
- Learner can articulate percentage interpretation rules

::: notes
Duration ~00:15

## Percentage Exercise Instructions

**Prerequisites:** Core arithmetic implemented

### Objectives

- Align percentage behavior with user expectations.

### Activities

- Compare generated logic with known calculator semantics.

### Success Criteria

- Three key percentage patterns operate correctly.
  :::

---

## Exercise: Calculator Project - Memory Functions (M+, M-, MR, MC)

Objectives

- Use AI to design memory subsystem
- Implement memory add, subtract, recall, and clear
- Validate memory across multiple operations

Activities

1. Ask AI for memory-state structure
2. Generate functions for M+, M-, MR, MC
3. Integrate memory operations into calculator flow
4. Test memory persistence over sequences

Success Criteria

- Memory functions behave as expected
- Learner can explain memory state updates

::: notes
Duration ~00:18

## Memory Functions Exercise Instructions

**Prerequisites:** Calculator state architecture defined

### Objectives

- Add reliable memory operations.

### Activities

- Ensure memory state is explicit and testable.

### Success Criteria

- Memory operations are consistent and validated.
  :::

---

## Exercise: Calculator Project - Error Handling

Objectives

- Use AI to identify common error conditions
- Implement error messages and recovery logic
- Ensure graceful reset after errors

Activities

1. Ask AI to list calculator errors (for example divide by zero)
2. Generate error detection and display logic
3. Implement reset path after an error
4. Test error scenarios with AI-generated tests

Success Criteria

- Errors are detected and displayed correctly
- Calculator recovers cleanly
- Learner can explain error-handling flow

::: notes
Duration ~00:10

## Error Handling Exercise Instructions

**Prerequisites:** Core operations implemented

### Objectives

- Build robust error paths without breaking user flow.

### Activities

- Validate both error detection and post-error recovery.

### Success Criteria

- Error handling is visible, predictable, and recoverable.
  :::

---

## Exercise: Calculator Project - Add Trigonometric Functions

Objectives

- Integrate trigonometric operations
- Use AI for math wrappers and parsing logic
- Handle degrees vs radians correctly

Activities

1. Ask AI to generate sin, cos, tan functions using language math library
2. Ask AI for degree/radian mode strategy
3. Implement UI bindings or command triggers
4. Generate sample input/output table with AI and validate

Success Criteria

- Trig results are correct for selected angle mode
- Degree/radian switching works consistently
- UI or commands correctly call trig functions
- Learner can explain validation and refinement steps

::: notes
Duration ~00:15

## Trigonometric Functions Exercise Instructions

**Prerequisites:** Advanced operation framework available

### Objectives

- Add trig support with explicit angle-mode handling.

### Activities

- Implement and validate both behavior and mode switching.

### Success Criteria

- Trig pipeline works end-to-end with tested expectations.
  :::

---

## Exercise: Calculator Project - UI

Objectives

- Use AI to scaffold UI event handlers
- Connect UI controls to logic functions
- Validate end-to-end workflow

Activities

1. Ask AI to generate event-binding code for numeric/operator controls
2. Integrate logic functions from prior exercises
3. Test full workflow:

- Enter decimal
- Toggle sign
- Apply percentage
- Store result in memory

Success Criteria

- UI triggers all calculator functions correctly
- End-to-end workflow completes without errors
- Learner can explain UI-to-logic mapping

::: notes
Duration ~00:15

## UI Exercise Instructions

**Prerequisites:** Core logic stable and testable

### Objectives

- Wire UI interactions cleanly to existing logic.

### Activities

- Prioritize event mapping clarity over visual polish.

### Success Criteria

- Workflow passes from input to output with no breaks.
  :::

---

## Exercise: Calculator Project - Testing

Objectives

- Generate unit tests with AI assistance
- Identify quality issues in generated tests
- Understand why generated tests require review

Activities

1. Generate Initial Tests:

- Prompt: "Create unit tests for the calculator operations"
- Review generated test structure
- Verify tests call calculator code

2. Fix Test Issues:

- If tests are trivial (for example 1 + 1 only), identify issue
- Prompt: "Update tests to call Calculator class methods"
- Verify improved test quality

3. Run Tests:

- Execute test suite
- Review output
- Debug failing tests with Copilot

4. Add Edge Cases:

- Prompt: "Add tests for edge cases like division by zero"
- Verify exception handling tests

Success Criteria

- Minimum 8 test cases
- Tests call actual calculator methods
- Edge cases and error conditions included
- All tests pass

::: notes
Duration ~01:00

## Testing Exercise Instructions

**Prerequisites:** Calculator logic implemented

### Objectives

- Improve test quality, not just test count.

### Activities

- Review generated tests critically before accepting.

### Success Criteria

- Test suite is meaningful, comprehensive, and green.
  :::

---

## Exercise: Code Coverage

Objectives

- Set up code coverage reporting
- Interpret coverage data
- Improve coverage based on identified gaps

Activities

1. Enable Coverage Collection:

- Prompt: "Add code coverage reporting to my test project"
- Review dependencies added
- Resolve NuGet/dependency issues with Copilot

2. Generate Coverage Report:

- Run tests with coverage
- Review percentage
- Identify uncovered paths

3. Improve Coverage:

- Add tests for uncovered methods
- Re-run coverage and verify improvement
- Discuss if 100% coverage is necessary

Success Criteria

- Coverage reporting configured successfully
- Coverage reports can be generated and interpreted
- Reasonable coverage achieved (>80% line coverage)
- Learner understands what coverage metrics mean

::: notes
Duration ~00:40

## Code Coverage Exercise Instructions

**Prerequisites:** Stable test suite

### Objectives

- Use coverage as a guide for targeted testing.

### Activities

- Treat uncovered code as investigation points, not automatic defects.

### Success Criteria

- Coverage setup works and leads to actionable improvements.
  :::

---

## Exercise: Dependency Management and Troubleshooting

Objectives

- Use Copilot to resolve dependency issues
- Handle package restoration problems
- Practice iterative AI-assisted troubleshooting

Activities

1. Simulate or Identify a Dependency Issue:

- Introduce version conflict or use an existing issue
- Prompt: "I'm getting [specific error]. How do I fix it?"

2. Follow Copilot Guidance:

- Review suggested solutions
- Evaluate alternatives
- Select best option collaboratively

3. Iterative Resolution:

- Provide new error details when needed
- Continue until resolved

4. Practice common issues:

- NuGet package source configuration
- MSTest adapter version conflicts
- .NET SDK targeting issues
- Package restoration failures

Success Criteria

- At least one dependency issue resolved
- Learner can provide useful error context to Copilot
- Iterative problem-solving pattern demonstrated

::: notes
Duration ~00:40

## Dependency Troubleshooting Exercise Instructions

**Prerequisites:** Build/test environment configured

### Objectives

- Build confidence in diagnosing and fixing dependency failures.

### Activities

- Emphasize iterative debugging and evidence-based prompts.

### Success Criteria

- Issue resolution is repeatable and well-documented.
  :::

---

## Exercise: Best Practices Review and Code Quality

Objectives

- Apply best practices from session
- Review code quality systematically
- Identify and implement meaningful improvements

Activities

1. Code Quality Check:

- Prompt: "Suggest improvements for code quality and maintainability"
- Evaluate suggestions critically
- Implement high-value improvements

Success Criteria

- Documentation and maintainability improved
- AI suggestions are critically evaluated before adoption

::: notes
Duration ~00:40

## Best Practices Review Exercise Instructions

**Prerequisites:** Working project baseline

### Objectives

- Turn AI suggestions into intentional quality improvements.

### Activities

- Keep only changes with clear maintainability value.

### Success Criteria

- Improvements are justified and validated.
  :::

---

## Exercise: Model Comparisons

Objectives

- Compare outputs from different AI models
- Understand premium vs standard model trade-offs
- Monitor token usage impact

Activities

1. Same Prompt, Different Models:

- Use one coding task (for example implement bubble sort)
- Compare standard and premium model outputs

2. Token Usage Analysis:

- Check premium token bar before/after
- Estimate consumed tokens
- Discuss value vs cost

3. Best Use Cases:

- Identify tasks for standard vs premium models
- Create model selection guidelines

4. Ask Mode Advantage:

- Use Ask mode with premium model
- Compare with Agent mode token behavior

Success Criteria

- At least two models compared
- Token consumption trade-offs understood
- Learner can choose model by task type

::: notes
Duration ~00:30

## Model Comparisons Exercise Instructions

**Prerequisites:** Access to multiple model options

### Objectives

- Build practical model-selection judgment.

### Activities

- Compare quality, speed, and token cost for same prompt.

### Success Criteria

- Team can explain when premium models are worth it.
  :::

---

## Exercise: Calculator Project - Encapsulate Core Logic

Objectives

- Separate UI concerns from computational logic
- Use AI to scaffold standalone core logic module/class
- Ensure UI communicates through a clean API
- Validate improved testability and maintainability

Activities

1. Ask AI to generate dedicated component (for example CalculatorEngine or CalculatorCore) containing:

- Arithmetic operations
- State management
- Trig/percentage/memory logic where implemented

2. Review and refine API surface (naming, inputs, outputs)
3. Replace UI-embedded logic with component calls

Success Criteria

- All features route through external logic component
- UI contains only event handling/display updates
- Learner can explain modularity and reuse benefits

::: notes
Duration ~00:15

## Encapsulate Core Logic Exercise Instructions

**Prerequisites:** UI and logic currently coupled

### Objectives

- Improve architecture through separation of concerns.

### Activities

- Create clear, testable boundaries between UI and engine.

### Success Criteria

- Core logic is isolated and reusable.
  :::

---

## Exercise: Security Review

Objectives

- Systematically review code for security issues
- Address discovered vulnerabilities
- Strengthen input validation and safe patterns

Activities

1. Security Review:

- Prompt: "Review this code for security vulnerabilities"
- Address identified issues
- Add input validation where missing

Success Criteria

- No obvious security issues remain
- AI recommendations are critically evaluated and validated

::: notes
Duration ~00:40

## Security Review Exercise Instructions

**Prerequisites:** Functional calculator project

### Objectives

- Apply practical security checks to working code.

### Activities

- Validate fixes with tests and review, not assumptions.

### Success Criteria

- Security posture improves with documented rationale.
  :::

---

## Exercise: Documentation

Objectives

- Add and improve project documentation
- Review AI-generated docs for accuracy and completeness

Activities

1. Documentation:

- Ask Copilot to generate XML/doc comments
- Review and refine for correctness
- Add README usage instructions
- Ask AI to update existing documentation sections

Success Criteria

- Documentation is comprehensive and accurate
- AI-generated content is critically reviewed before acceptance

::: notes
Duration ~00:40

## Documentation Exercise Instructions

**Prerequisites:** Stable code to document

### Objectives

- Produce maintainable, user-focused documentation.

### Activities

- Treat generated docs as drafts requiring technical review.

### Success Criteria

- Docs are complete, correct, and actionable.
  :::

---

## Exercise: Refactoring

Objectives

- Apply refactoring best practices
- Compare alternative implementations
- Evaluate trade-offs before choosing changes

Activities

1. Refactoring Exercise:

- Ask Copilot for alternative implementations
- Compare readability, complexity, and maintainability
- Discuss trade-offs and select best approach

Success Criteria

- At least one refactoring improvement implemented
- Code quality and maintainability improved
- AI suggestions critically evaluated

::: notes
Duration ~00:40

## Refactoring Exercise Instructions

**Prerequisites:** Existing implementation with improvement opportunities

### Objectives

- Use AI for option generation, then apply engineering judgment.

### Activities

- Compare alternatives using explicit criteria.

### Success Criteria

- Selected refactor improves clarity without regressions.
  :::
