---
marp: true
theme: default
paginate: true
---

## Collaborating on a Solution

Project Setup
Adding Features
- Basic Arithmetic - Addition, subtraction, multiplication, division
- Clear / Reset Function - Quickly resets the current input or entire calculation
- Decimal Support - Allows entry and computation with decimal numbers
- Sign Toggle (+/–) - Switches values between positive and negative
- Percentage Function - Converts values to percentages for quick calculations
- Memory Functions (M+, M–, MR, MC) - Store, recall, add to, or clear memory values
- Error Handling - Displays errors such as division by zero
- Simple, Intuitive Interface - Numeric keypad, operation buttons, and display screen
Test Automation
- Code Coverage
Dependency Management
Comparing Implementations
Chat Management
Intro to Evergreen Software Development

::: notes
This slide outlines the collaborative development process we’ll follow for building our calculator application — and mob programming will be central to how we work together.

Except for Project Setup and Basic Arithmetic functions, the mob controls the direction of the implementation. The other labs are optional and can be used when the mob directs the development of that feature or as suggestions should the mob struggle for direction.

We begin with Project Setup, where the team configures the environment, aligns on goals, and prepares the repo. This is done as a mob — one keyboard, one screen, and everyone contributing ideas in real time. It ensures shared understanding from the start.

At the end of the day, we introduce Evergreen Software Development — a mindset of continuous improvement.

Random ideas:
Implementing Observability

Scaffold a new C# command line project using .NET. The project should include:
A Program.cs file with a simple "Hello, World!" example.
A .csproj file configured for a console application.
A README.md with build and run instructions.
The project should be ready to build and run from the command line.
:::

---

## Exercise: Calculator Project - Setup & Basic Implementation

Duration: 45-60 minutes
Objectives
- Use AI to generate starter code for arithmetic operations
- Understand how to validate AI‑generated logic
- Integrate addition, subtraction, multiplication, and division functions
Activities
1. Project Initialization:
- Prompt AI to create a new project
- Review generated project structure
- Verify build configuration
2. Implement Basic Operations:
- Prompt AI to add methods for addition, subtraction, multiplication, and division
3. Review the Code:
- For correctness and edge cases
4. Build and Run:
- Use Copilot to help with build commands
- Troubleshoot any compilation errors with Copilot's help
- Run the application
Success Criteria
- Working calculator with 4 basic operations
- Application compiles and runs successfully
- You've critically reviewed all generated code

---

## Exercise: Calculator Project – Clear / Reset

Duration: 15 minutes
Objectives
- Use AI to scaffold state‑management logic
- Implement CE (clear entry) and C (clear all) behaviors
- Understand how AI can help reason about UI state transitions
Activities
Prompt AI to outline the difference between CE and C
Generate code for clearing the current input vs. full state
Integrate the logic into your calculator’s state object
Test transitions by simulating user input sequences
Success Criteria
- - CE clears only the active entry
- - C resets the entire calculator state

---

## Exercise: Calculator Project – Decimal Input

Duration: 12 minutes
Objectives
Use AI to generate input‑validation logic
Prevent multiple decimal points
Ensure decimals flow correctly through arithmetic operation
Activities
Ask AI to propose a strategy for handling decimal input
Generate code to block multiple decimals in a single number
Integrate decimal support into the existing input parser
Test decimal operations using AI‑generated test cases
Success Criteria
Decimal input works without duplication errors
Arithmetic with decimals produces correct results
Learner can explain the validation logic

---

## Exercise: Calculator Project – Sign Toggle (+/–)

Duration: 8 minutes
Objectives
- Use AI to generate logic for toggling numeric sign
- Understand how sign toggling interacts with current input and stored values
Activities
Ask AI to generate a function that toggles sign on the active value
Integrate the function into the input workflow
Test sign toggling before and after entering digits
Success Criteria
- Sign toggle works consistently for integers and decimals
- Learner can explain how the toggle affects stored vs. active value

---

## Exercise: Calculator Project – Percentage

Duration: 15 minutes
Objectives
- Use AI to clarify how calculators interpret %
- Implement percentage logic for common patterns
- Validate behavior with AI‑generated examples
Activities
Ask AI to explain how % should behave in a standard calculator
Generate code for:
X × Y%
Y + X%
Y – X%
3. Test each pattern with AI‑generated sample values
Success Criteria
Percentage operations match standard calculator behavior
Learner can articulate the interpretation rules for %

---

## Exercise: Calculator Project – Memory Functions (M+, M–, MR, MC)

Duration: 18 minutes
Objectives
- Use AI to design a memory subsystem
- Implement memory add, subtract, recall, and clear
- Validate memory behavior across multiple operations
Activities
Ask AI to propose a memory‑state structure
Generate functions for M+, M–, MR, MC
Integrate memory operations into the calculator workflow
Test memory persistence across multiple calculations
Success Criteria
- Memory functions behave as expected
- Learner can explain how memory state is stored and updated

---

## Exercise: Calculator Project – Error Handling

Duration: 10 minutes
Objectives
- Use AI to identify common error conditions
- Implement error messages and recovery logic
- Ensure the calculator resets gracefully after errors
Activities
Ask AI to list typical calculator errors (e.g., divide by zero)
Generate code for error detection and display
Implement a reset path after an error
Test error scenarios using AI‑generated test cases
Success Criteria
- Errors are detected and displayed correctly
- Calculator recovers cleanly after reset
- Learner can describe the error‑handling flow

---

## Exercise: Calculator Project – Add Trigonometric Functions

Duration: 15 minutes
Objectives
- Integrate trigonometric functions into the calculator’s operation set
- Use AI to generate math‑library wrappers and input‑parsing logic
- Ensure correct handling of degrees vs. radians
Activities
Ask AI to generate functions for sin, cos, and tan using your language’s math library
Prompt AI to propose a strategy for handling degree/radian mode
Implement UI bindings or command triggers for each trig function
Use AI to generate a table of sample inputs and expected outputs
Success Criteria
- Trig functions compute correct values in the selected angle mode
- Degree/radian mode switching works consistently
- UI or command triggers correctly call the trig functions
- Learner can explain how AI‑generated code was validated and refine

---

## Exercise: Calculator Project – UI

Duration: 15 minutes
Objectives
- Use AI to scaffold UI event handlers
- Connect buttons to logic functions
- Validate end‑to‑end user workflow
Activities
Ask AI to generate event‑binding code for numeric and operator buttons
Integrate logic functions from previous labs
Test a full workflow:
- Enter decimal
- Toggle sign
- Apply percentage
- Store result in memory
Success Criteria
- UI correctly triggers all calculator functions
- Full workflow completes without errors
- Learner can explain how UI events map to logic functions

---

## Exercise: Calculator Project - Testing

Duration: 45-60 minutes
Objectives
- Generate unit tests with AI assistance
- Identify quality issues in generated tests
- Understand the importance of reviewing AI-generated tests
Activities
1. Generate Initial Tests:
- Prompt: "Create unit tests for the calculator operations"
- Review generated test structure
- Critical Review: Are tests calling your calculator code?
2. Fix Test Issues (Replicating Session Demo):
- If tests are too simple (like `1 + 1 = 2` without calling calculator):
- Identify the problem
- Ask Copilot to fix it: "Update tests to call Calculator class methods"
- Verify tests now test actual implementation
3. Run Tests:
- Execute test suite
- Review test output
- Debug any failing tests with Copilot's help
4. Add Edge Cases:
- Prompt: "Add tests for edge cases like division by zero"
- Verify exception handling tests are correct
Success Criteria
- Test suite with minimum 8 test cases
- All tests call actual calculator methods (not just language arithmetic)
- Tests include edge cases and error conditions
- All tests pass

---

## Exercise: Code Coverage

Duration: 30-40 minutes
Objectives
- Set up code coverage reporting
- Interpret coverage results
- Improve test coverage based on gaps
Activities
1. Enable Coverage Collection:
- Prompt: "Add code coverage reporting to my test project"
- Review package dependencies added
- Handle any NuGet/dependency issues with Copilot's help
2. Generate Coverage Report:
- Run tests with coverage enabled
- Review coverage percentage
- Identify uncovered code paths
3. Improve Coverage:
- Add tests for uncovered methods
- Re-run coverage to verify improvement
- Discuss: Is 100% coverage always necessary?
Success Criteria
- Code coverage reporting successfully configured
- Can generate and read coverage reports
- Achieved reasonable coverage (>80% line coverage)
- Understand what coverage metrics mean
Discussion Points
- Feature coverage vs. code coverage (as raised by Tom in the session)
- When is test coverage sufficient?
- Quality of tests vs. quantity

---

## Exercise: Dependency Management & Troubleshooting

Duration: 30-40 minutes
Objectives
- Use Copilot to resolve dependency issues
- Handle package restoration problems
- Practice iterative problem-solving with AI
Activities
1. Simulate or Identify a Dependency Issue:
- Introduce a version conflict (or use existing issue)
- Prompt: "I'm getting [specific error]. How do I fix it?"
2. Follow Copilot's Guidance:
- Review suggested solutions
- Evaluate multiple approaches if offered
- Choose best solution collaboratively
3. Iterative Resolution:
- If first solution doesn't work, provide error details
- Continue conversation until resolved
4. Common Issues to Practice:
- NuGet package source configuration
- MSTest adapter version conflicts
- .NET SDK targeting issues
- Package restoration failures
Success Criteria
- Successfully resolved at least one dependency issue
- Understand how to provide error context to Copilot
- Practiced iterative problem-solving approach
Real-World Scenario
- This lab replicates the exact dependency challenges encountered in the training session:
- Updating test project to target .NET 8
- Resolving NuGet.org package source mapping
- MSTest adapter compatibility issues

---

## Exercise: Best Practices Review & Code Quality

Duration: 30-40 minutes
Objectives
- Apply best practices learned in session
- Review code quality systematically
- Identify and fix issues
Activities
1. Code Quality Check:
- Prompt: "Suggest improvements for code quality and maintainability"
- Evaluate suggestions critically
- Implement valuable improvements
Success Criteria
- Comprehensive documentation added
- Critically evaluated all AI suggestions

---

## Exercise: Model Comparisons

Duration: 20-30 minutes
Objectives
- Compare outputs from different AI models
- Understand when to use premium vs standard models
- Monitor token usage
Activities
1. Same Prompt, Different Models:
- Choose a coding task (e.g., "implement bubble sort")
- Try with GPT-4 (standard - unlimited)
- Try with Claude Sonnet (premium - 1x token)
- Compare results for quality, style, completeness
2. Token Usage Analysis:
- Check premium token bar before and after
- Calculate tokens consumed
- Discuss: Was premium model worth the cost?
3. Best Use Cases:
- Identify tasks where standard models suffice
- Identify tasks requiring premium models
- Create personal guidelines for model selection
4. Ask Mode Advantage:
- Use Ask mode with premium models (no token cost)
- Compare to Agent mode token consumption
Success Criteria
- Compared at least 2 different models
- Understand token consumption impact
- Can make informed model selection decisions
Token Economics
- Standard models (unlimited): ChatGPT-4
- Premium tokens (counted):
- Claude Haiku 4.5: 1/3 token per request
- Claude Sonnet: 1x token per request
- O2 mini: 1/3 token per request
- New models: May be 10x when first released

---

## Exercise: Calculator Project – Encapsulate Core Logic

Duration: 15 minutes
Objectives
Separate UI concerns from computational logic
Use AI to scaffold a standalone “core logic” module/class
Ensure the UI communicates with the logic layer through a clean, well‑defined API
Validate that encapsulation improves testability and maintainability
Activities
1. - Ask AI to generate a dedicated component (e.g., CalculatorEngine, CalculatorCore) containing:
- Arithmetic operations
- State management
- Trig/percentage/memory logic (if implemented)
2. Review the AI‑generated API surface and refine naming, inputs, and return types
3. Replace UI‑embedded logic with calls into the new component
Success Criteria
- All calculator features run through the external logic component
- UI contains no computational logic — only event handling and display updates
- Learner can explain how encapsulation improves modularity, reuse, and AI‑assisted development workflow

---

## Exercise: Security Review

Duration: 30-40 minutes
Objectives
- Apply best practices learned in session
- Review code quality systematically
- Identify and fix issues
Activities
1. Security Review:
- Prompt: "Review this code for security vulnerabilities"
- Address any identified issues
- Add input validation where missing
Success Criteria
- Code has no obvious security issues
- Critically evaluated all AI suggestions

---

## Exercise: Documentation

Duration: 30-40 minutes
Objectives
- Add documentation to a project
- Update existing documentation
Activities
1. Documentation:
- Ask Copilot to generate XML/doc comments
- Review for accuracy and completeness
- Add README with usage instruction
- Ask AI to update existing documentation
Success Criteria
- Comprehensive documentation added
- Critically evaluated all AI suggestions

---

## Exercise: Refactoring

Duration: 30-40 minutes
Objectives
- Apply best practices learned in session
- Review code quality systematically
- Identify and fix issues
Activities
1. Refactoring Exercise:
- Ask Copilot for alternative implementation approaches
- Compare different solutions
- Discuss trade-offs (as mentioned in session)
Success Criteria
- Code has no obvious security issues
- Comprehensive documentation added
- At least one refactoring improvement implemented
- Critically evaluated all AI suggestions

---

## Evergreen Software Development - Core Principles

Intent‑First Design
- Define the system’s purpose, invariants, and boundaries before writing code to ensure long‑term clarity.
Stable Interfaces, Evolving Internals
- Keep contracts predictable while allowing implementations to improve continuously.
Continuous Regeneration with Guardrails
- Use AI to rewrite or extend components safely, backed by tests, specs, and architectural constraints.
Modular, Replaceable Components
- Structure the system so any part can be regenerated, swapped, or upgraded without cascading breakage.
Lifecycle Governance
- Maintain quality through automated tests, versioning discipline, and human‑in‑the‑loop validation.

---

## Software Engineering vs “Vibe Coding”

Engineering approach: systematic, tested, documented, maintainable
Vibe coding: “it works” mentality, technical debt accumulation
AI should enhance engineering practices, not replace them
Proper testing, code review, and architecture still essential

::: notes
Contrast disciplined engineering practices with quick “vibe” coding; stress that AI should augment engineering rigor, not replace it.
:::

---

## Why Software Fails to Be Evergreen

Intent Rot
- The original purpose, constraints, and invariants are undocumented or lost, making safe regeneration impossible.
Unstable or Leaky Interfaces
- APIs, data contracts, and boundaries change unpredictably, causing cascading breakage when internals evolve.
Tightly Coupled Architecture
- Components depend on each other’s internal details, preventing isolated regeneration or replacement.
Insufficient Guardrails
- Missing tests, specs, or validation layers mean AI‑assisted regeneration can’t be trusted to preserve behavior.
One‑Off Patches and Drift
- Ad‑hoc fixes accumulate, diverging the system from its intended design and making regeneration unsafe.
