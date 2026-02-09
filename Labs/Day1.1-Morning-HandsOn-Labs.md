# Hands-On Labs for GitHub Copilot Training Day 1 Morning Session

Based on the material covered in the training session, here are targeted hands-on labs that align with the demonstrated concepts and best practices.

---

## **Lab 1: Getting Started with GitHub Copilot**

**Duration:** 20-30 minutes
**Prerequisites:** VS Code installed

### Objectives

- Install and configure GitHub Copilot
- Verify authentication with GitHub account
- Explore the Copilot UI components

### Activities

1. Install GitHub Copilot extension from VS Code marketplace
2. Sign in with your GitHub account (verify Copilot subscription)
3. Locate and explore:
   - Chat window and chat history
   - New chat button
   - Quick chat feature (keyboard shortcut)
   - Settings menu
   - Model selection dropdown
4. Check your premium token usage bar
5. Create a new chat and experiment with the interface

### Success Criteria

- Copilot extension installed and authenticated
- Can open/close chat windows
- Understand difference between main chat and quick chat
- Know where to find chat history

---

## **Lab 2: Understanding Context Management**

**Duration:** 30-40 minutes
**Prerequisites:** Lab 1 completed, sample codebase available

### Objectives

- Learn to add context using @ symbols
- Understand context window limitations
- Practice writing effective prompts

### Activities

1. **Basic Context Addition:**
   - Use `@workspace` to search across your codebase
   - Use `@file` to reference specific files
   - Use `@terminal` to include terminal output in chat
   - Use `@vscode` to ask VS Code-specific questions

2. **Prompt Practice:**

   Practice the progression from vague to specific to context-aware prompts using these examples:

   **Example 1: Adding Error Handling**

   **Vague Prompt:**

   ```
   Add error handling to my code
   ```

   _Result: Generic response asking what type of errors, what language, what code?_

   **Specific Context:**

   ```
   Add error handling to my JavaScript function that calls an external API.
   I want to handle network timeouts, 404 errors, and JSON parsing failures.
   Return user-friendly error messages.
   ```

   _Result: Better, but still generic without seeing actual code structure_

   **With File References:**

   ```
   @file:api-client.js Add comprehensive error handling to the fetchUserData function.
   Handle network timeouts (>5s), HTTP errors (404, 500, etc.), and JSON parsing failures.
   Return user-friendly error messages that match our existing error format in @file:error-types.js
   ```

   _Result: Specific implementation that matches existing code patterns_

   **Example 2: Writing Tests**

   **Vague Prompt:**

   ```
   Write tests for my functions
   ```

   _Result: Generic test examples without knowing your testing framework or code structure_

   **Specific Context:**

   ```
   Write unit tests for my user authentication functions using Jest.
   Include tests for successful login, failed login, and session validation.
   Mock the database calls.
   ```

   _Result: Better structure but might not match existing test patterns_

   **With File References:**

   ```
   @file:auth.js Write Jest unit tests for the login() and validateSession() functions.
   Follow the testing patterns used in @file:__tests__/user.test.js
   Mock the database using the same approach as existing tests.
   ```

   _Result: Tests that match existing code style and testing patterns_

   **Example 3: Refactoring Code**

   **Vague Prompt:**

   ```
   Refactor this code to make it better
   ```

   _Result: Unclear what "better" means - performance, readability, maintainability?_

   **Specific Context:**

   ```
   Refactor this React component to improve performance by memoizing expensive calculations
   and splitting into smaller components. Follow modern React patterns.
   ```

   _Result: Focused improvements but might not follow project conventions_

   **With File References:**

   ```
   @file:UserProfile.jsx Refactor this component to improve performance using React.memo and useMemo.
   Follow the component structure pattern used in @file:ProductCard.jsx
   Split into smaller components following our naming convention in @file:components/index.js
   ```

   _Result: Refactoring that maintains consistency with existing codebase_

   **Your Turn - Practice Exercise:**
   1. Choose a simple task (e.g., "add validation", "fix a bug", "create a function")
   2. Start with a vague prompt - notice the generic/clarifying response
   3. Rewrite with specific requirements and constraints
   4. Add file references using @file or @workspace
   5. Compare the quality and usability of each response

   **Key Observations:**
   - Vague prompts require back-and-forth clarification
   - Specific prompts give actionable but potentially inconsistent results
   - Context-aware prompts with file references produce code that integrates well

3. **Context Window Experiment:**
   - Start a long conversation in one chat
   - Notice when Copilot starts "forgetting" earlier context
   - Practice starting new chats for new topics

### Success Criteria

- Can use all @ context types
- Understand when to start fresh chat sessions
- Notice quality difference between vague and specific prompts

---

## **Lab 3: Exploring Copilot Modes**

**Duration:** 30-40 minutes
**Prerequisites:** Labs 1-2 completed

### Objectives

- Understand differences between Ask, Edit, and Agent modes
- Know when to use each mode
- Understand premium token implications

### Activities

1. **Ask Mode:**
   - Ask Copilot to explain a code snippet (no changes made)
   - Request multiple implementation approaches
   - Try different models and observe response quality
   - **Note:** This doesn't consume premium tokens for advanced models

2. **Edit Mode:**
   - Select code in a file
   - Ask Copilot to refactor it
   - Observe inline suggestions and changes
   - Accept or reject proposed changes

3. **Agent Mode:**
   - Ask Copilot to create a new file and add content
   - Request changes across multiple files
   - Have Copilot run terminal commands
   - Check premium token usage after agent actions

### Success Criteria

- Can distinguish when to use each mode
- Understand token consumption differences
- Successfully use agent mode for multi-file operations

---

## **Lab 4: Calculator Project - Part 1 (Setup & Basic Implementation)**

**Duration:** 45-60 minutes
**Prerequisites:** Labs 1-3 completed, C# or Go environment

### Objectives

- Create a simple calculator project from scratch
- Practice collaborative prompting with AI
- Review AI-generated code critically

### Activities

1. **Project Initialization:**
   - Ask Copilot: "Create a new calculator console application in [C#/.NET or Go]"
   - Review generated project structure
   - Verify build configuration

2. **Implement Basic Operations:**
   - Prompt: "Add methods for addition, subtraction, multiplication, and division"
   - Review generated code for:
     - Error handling (division by zero)
     - Input validation
     - Code organization
   - Make improvements as needed

3. **Build and Run:**
   - Use Copilot to help with build commands
   - Troubleshoot any compilation errors with Copilot's help
   - Run the application

### Success Criteria

- Working calculator with 4 basic operations
- Code includes proper error handling
- Application compiles and runs successfully
- You've critically reviewed all generated code

---

## **Lab 5: Calculator Project - Part 2 (Testing)**

**Duration:** 45-60 minutes
**Prerequisites:** Lab 4 completed

### Objectives

- Generate unit tests with AI assistance
- Identify quality issues in generated tests
- Understand the importance of reviewing AI-generated tests

### Activities

1. **Generate Initial Tests:**
   - Prompt: "Create unit tests for the calculator operations"
   - Review generated test structure
   - **Critical Review:** Are tests actually calling your calculator code?

2. **Fix Test Issues (Replicating Session Demo):**
   - If tests are too simple (like `1 + 1 = 2` without calling calculator):
     - Identify the problem
     - Ask Copilot to fix it: "Update tests to call Calculator class methods"
   - Verify tests now test actual implementation

3. **Run Tests:**
   - Execute test suite
   - Review test output
   - Debug any failing tests with Copilot's help

4. **Add Edge Cases:**
   - Prompt: "Add tests for edge cases like division by zero"
   - Verify exception handling tests are correct

### Success Criteria

- Test suite with minimum 8 test cases
- All tests call actual calculator methods (not just language arithmetic)
- Tests include edge cases and error conditions
- All tests pass

### Key Learning Point

This lab replicates the exact issue discovered in the training session where initial tests showed 0% code coverage because they tested basic arithmetic operations (`1 + 1 = 2`) rather than calling the actual Calculator class methods. This demonstrates why critical review of AI-generated tests is essential.

---

## **Lab 6: Code Coverage Analysis**

**Duration:** 30-40 minutes
**Prerequisites:** Lab 5 completed

### Objectives

- Set up code coverage reporting
- Interpret coverage results
- Improve test coverage based on gaps

### Activities

1. **Enable Coverage Collection:**
   - Prompt: "Add code coverage reporting to my test project"
   - Review package dependencies added
   - Handle any NuGet/dependency issues with Copilot's help

2. **Generate Coverage Report:**
   - Run tests with coverage enabled
   - Review coverage percentage
   - Identify uncovered code paths

3. **Improve Coverage:**
   - Add tests for uncovered methods
   - Re-run coverage to verify improvement
   - Discuss: Is 100% coverage always necessary?

### Success Criteria

- Code coverage reporting successfully configured
- Can generate and read coverage reports
- Achieved reasonable coverage (>80% line coverage)
- Understand what coverage metrics mean

### Discussion Points

- Feature coverage vs. code coverage (as raised by Tom in the session)
- When is test coverage sufficient?
- Quality of tests vs. quantity

---

## **Lab 7: Dependency Management & Troubleshooting**

**Duration:** 30-40 minutes
**Prerequisites:** Any previous lab with build issues

### Objectives

- Use Copilot to resolve dependency issues
- Handle package restoration problems
- Practice iterative problem-solving with AI

### Activities

1. **Simulate or Identify a Dependency Issue:**
   - Introduce a version conflict (or use existing issue)
   - Prompt: "I'm getting [specific error]. How do I fix it?"

2. **Follow Copilot's Guidance:**
   - Review suggested solutions
   - Evaluate multiple approaches if offered
   - Choose best solution collaboratively

3. **Iterative Resolution (as seen in demo):**
   - If first solution doesn't work, provide error details
   - Continue conversation until resolved
   - Note: This mirrors the NuGet config issue from the demo

4. **Common Issues to Practice:**
   - NuGet package source configuration
   - MSTest adapter version conflicts
   - .NET SDK targeting issues
   - Package restoration failures

### Success Criteria

- Successfully resolved at least one dependency issue
- Understand how to provide error context to Copilot
- Practiced iterative problem-solving approach

### Real-World Scenario

This lab replicates the exact dependency challenges encountered in the training session:

- Updating test project to target .NET 8
- Resolving NuGet.org package source mapping
- MSTest adapter compatibility issues

---

## **Lab 8: Best Practices Review & Code Quality**

**Duration:** 30-40 minutes
**Prerequisites:** Completed calculator project

### Objectives

- Apply best practices learned in session
- Review code quality systematically
- Identify and fix issues

### Activities

1. **Security Review:**
   - Prompt: "Review this code for security vulnerabilities"
   - Address any identified issues
   - Add input validation where missing

2. **Code Quality Check:**
   - Prompt: "Suggest improvements for code quality and maintainability"
   - Evaluate suggestions critically
   - Implement valuable improvements

3. **Documentation:**
   - Ask Copilot to generate XML/doc comments
   - Review for accuracy and completeness
   - Add README with usage instructions

4. **Refactoring Exercise:**
   - Ask Copilot for alternative implementation approaches
   - Compare different solutions
   - Discuss trade-offs (as mentioned in session)

### Success Criteria

- Code has no obvious security issues
- Comprehensive documentation added
- At least one refactoring improvement implemented
- Critically evaluated all AI suggestions

### Key Principles from Session

- **DO:** Always review and test AI-generated code
- **DON'T:** Blindly accept AI suggestions
- **DO:** Provide clear, specific prompts with context
- **DON'T:** Skip testing because "AI wrote it"
- **DO:** Use AI to explore different implementation approaches
- **DON'T:** Rely on AI for architectural decisions without human oversight

---

## **Lab 9: Model Comparison Exercise**

**Duration:** 20-30 minutes
**Prerequisites:** Understanding of model selection

### Objectives

- Compare outputs from different AI models
- Understand when to use premium vs standard models
- Monitor token usage

### Activities

1. **Same Prompt, Different Models:**
   - Choose a coding task (e.g., "implement bubble sort")
   - Try with GPT-4 (standard - unlimited)
   - Try with Claude Sonnet (premium - 1x token)
   - Compare results for quality, style, completeness

2. **Token Usage Analysis:**
   - Check premium token bar before and after
   - Calculate tokens consumed
   - Discuss: Was premium model worth the cost?

3. **Best Use Cases:**
   - Identify tasks where standard models suffice
   - Identify tasks requiring premium models
   - Create personal guidelines for model selection

4. **Ask Mode Advantage:**
   - Use Ask mode with premium models (no token cost)
   - Compare to Agent mode token consumption

### Success Criteria

- Compared at least 2 different models
- Understand token consumption impact
- Can make informed model selection decisions

### Token Economics (from session)

- **Standard models (unlimited):** ChatGPT-4
- **Premium tokens (counted):**
  - Claude Haiku 4.5: 1/3 token per request
  - Claude Sonnet: 1x token per request
  - O2 mini: 1/3 token per request
  - New models: May be 10x when first released

---

## **Lab 10: Chat Management & Workflow**

**Duration:** 20-30 minutes
**Prerequisites:** All previous labs

### Objectives

- Organize chat sessions effectively
- Use chat history for reference
- Develop efficient workflow patterns

### Activities

1. **Chat Organization:**
   - Review your chat history
   - Identify chats that should have been separate sessions
   - Practice starting new chats at appropriate times

2. **Context Preservation:**
   - Start a focused chat for one feature
   - Add relevant context systematically
   - Complete task without context overflow

3. **Quick Chat Practice:**
   - Use main chat for primary task
   - Use quick chat for side questions
   - Return to main chat without losing context

4. **Chat History Review:**
   - Find and reference previous solutions
   - Learn from past prompts that worked well
   - Identify patterns in effective conversations

### Success Criteria

- Chat history is organized and meaningful
- Can find and reference previous solutions
- Efficient workflow developed for using multiple chat windows

### Context Window Management

Remember from the session:

- Context is a **limited resource**
- Start new chat when changing focus areas
- Keep conversations targeted and specific
- When Copilot "forgets" earlier context, it's time for a new session

---

## **Bonus Lab: Mob Programming Setup**

**Duration:** 15-20 minutes
**Optional - based on session mention**

### Objectives

- Explore collaborative coding with Copilot
- Set up for team development

### Activities

1. Research mob programming tools (mob.sh or alternatives)
2. Configure for your environment
3. Practice driver/navigator roles with Copilot as assistant
4. Discuss how AI changes mob programming dynamics

### Discussion Questions

- How does AI change the driver/navigator dynamic?
- Should AI suggestions be discussed by the mob before accepting?
- How to handle disagreements between mob and AI suggestions?

---

## **Lab Sequence Recommendations**

### **For Morning Session Follow-up (Core Skills)**

**Labs:** 1, 2, 3, 4, 5, 6
**Time Required:** 3-4 hours
**Focus:** Essential skills demonstrated in the session

### **For Extended Practice (Mastery)**

**Labs:** All labs 1-10
**Time Required:** 5-6 hours
**Focus:** Mastery and workflow optimization

### **For Team Training (Collaborative)**

**Labs:** 1-3 individually, then 4-6 as group exercises
**Time Required:** 2-3 hours
**Focus:** Team collaboration, shared decision-making

### **Suggested Daily Schedule**

#### **Half-Day Session (4 hours)**

- Labs 1-2: Foundation (50-70 min)
- Break (10 min)
- Lab 3: Modes (30-40 min)
- Break (10 min)
- Lab 4: Calculator Part 1 (45-60 min)
- Break (10 min)
- Lab 5-6: Testing & Coverage (75-100 min)

#### **Full-Day Session (6-7 hours)**

- Morning: Labs 1-6 (as above)
- Lunch Break
- Afternoon: Labs 7-10 (2-3 hours)

---

## **Assessment Criteria**

Participants should be able to demonstrate:

### **Technical Skills**

- ✅ Install and configure GitHub Copilot
- ✅ Use @-references to add context
- ✅ Switch between Ask, Edit, and Agent modes
- ✅ Generate and review code critically
- ✅ Create and validate unit tests
- ✅ Set up code coverage reporting
- ✅ Troubleshoot dependency issues

### **Best Practices**

- ✅ Always review AI-generated code before accepting
- ✅ Provide specific, contextual prompts
- ✅ Test all generated code thoroughly
- ✅ Recognize when tests don't actually test implementation
- ✅ Manage context windows effectively
- ✅ Choose appropriate models for tasks

### **Critical Thinking**

- ✅ Identify flaws in AI-generated solutions
- ✅ Evaluate trade-offs between implementation approaches
- ✅ Make architectural decisions independently
- ✅ Understand limitations of AI assistance

---

## **Common Pitfalls & Solutions**

Based on the training session, watch for these issues:

### **Pitfall 1: Tests Don't Test Actual Code**

**Problem:** Tests like `Assert.AreEqual(2, 1 + 1)` instead of calling Calculator methods
**Solution:** Always verify tests call your actual implementation
**Lab:** Lab 5 specifically addresses this

### **Pitfall 2: Dependency Configuration Issues**

**Problem:** NuGet packages won't restore, version conflicts
**Solution:** Provide error details to Copilot, iterate on solutions
**Lab:** Lab 7 practices this scenario

### **Pitfall 3: Context Overload**

**Problem:** Copilot starts repeating itself or forgetting earlier context
**Solution:** Start new chat sessions when changing focus
**Lab:** Lab 2 and Lab 10 address this

### **Pitfall 4: Blindly Accepting Suggestions**

**Problem:** Generated code has logical errors or security issues
**Solution:** Always review, test, and validate AI output
**Lab:** All labs emphasize this principle

### **Pitfall 5: Premium Token Exhaustion**

**Problem:** Running out of premium tokens mid-project
**Solution:** Use Ask mode for research, standard models when sufficient
**Lab:** Lab 9 teaches token management

---

## **Key Takeaways from Session**

Throughout all labs, reinforce these core principles:

### **Philosophy: AI Assistance, Not Replacement**

- AI is a tool to help you write better code faster
- You remain the engineer making decisions
- Critical review is non-negotiable

### **Software Engineering vs. "Vibe Coding"**

- **Vibe Coding:** Quick iterations without systematic approach
- **Engineering:** Systematic, tested, documented, maintainable
- AI works best when enhancing engineering practices, not replacing them

### **Context is Everything**

- More specific context → Better outputs
- Context window is a limited resource
- Organize chats to preserve relevant context

### **The Iteration Cycle**

1. Write specific prompt with context
2. Review AI output critically
3. Test generated code
4. Refine and iterate as needed
5. Document decisions and rationale

### **Quality Assurance**

- Testing is MORE important with AI, not less
- Code coverage reports what's tested, not what's correct
- Security reviews remain essential
- Team code reviews catch issues AI might miss

---

## **Additional Resources**

### **From Training Session**

- GitHub Copilot Documentation
- Copilot for Business Overview
- Security & Privacy FAQ
- Enterprise Admin Controls

### **Recommended Reading**

- Clean Code principles
- Test-Driven Development practices
- Security best practices for your language
- Code review guidelines

### **Team Discussion Topics**

- When to use AI vs. manual coding
- Team standards for reviewing AI-generated code
- Architectural decision-making process with AI input
- Balancing speed gains with quality maintenance

---

## **Instructor Notes**

### **For Session Facilitators**

**Lab 4-6 (Calculator Project):**

- This mirrors the exact demo from the training session
- Expect to encounter similar issues (test quality, dependencies)
- Use these as teaching moments, not failures
- Emphasize the importance of critical review

**Real-World Complexity:**

- Don't shy away from showing when things don't work perfectly
- Dependency issues and configuration problems are normal
- Demonstrate iterative problem-solving with Copilot

**Collaborative Decision-Making:**

- Encourage group discussion of AI suggestions
- Ask "Should we accept this?" before applying changes
- Model the driver/navigator approach mentioned in session

**Token Awareness:**

- Help participants understand token economics
- Teach model selection strategy
- Demonstrate Ask mode for premium models without token cost

---

## **Success Metrics**

Participants successfully complete the labs when they can:

1. **Independently** set up and use GitHub Copilot
2. **Critically** review and improve AI-generated code
3. **Effectively** provide context for better results
4. **Identify** when tests don't actually test implementation
5. **Troubleshoot** common issues with AI assistance
6. **Manage** chat sessions and context windows
7. **Make informed decisions** about when and how to use AI

Most importantly, participants should understand that **AI is a powerful tool that enhances their engineering capabilities but does not replace their judgment, expertise, or responsibility for code quality.**

---

## **Next Steps**

After completing these labs:

- Continue with Day 1 Afternoon session labs (Brownfield/Legacy code)
- Practice on real work projects with Copilot
- Share learnings with team members
- Develop team-specific best practices and guidelines
- Set up instruction files for project-specific standards

Remember: The goal is not to write code faster, but to write better code faster while maintaining quality, security, and maintainability standards.
