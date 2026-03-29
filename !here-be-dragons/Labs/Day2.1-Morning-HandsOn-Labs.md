# Day 2 Morning Session: Hands-On Labs

## Working with Legacy Code and AI

---

## Session Overview

These hands-on labs correspond to Day 2 Morning training session focused on working with legacy code using GitHub Copilot. The session emphasizes understanding legacy code definitions, preparing for modifications, managing context effectively, and implementing meta-instruction patterns for consistent AI-assisted development.

**Total Time**: ~6-8 hours
**Prerequisites**: Completion of Day 1 labs, GitHub Copilot access, understanding of basic Git workflows

---

## Lab 1: Understanding Legacy Code Definitions

**Time**: 20 minutes
**Objective**: Explore multiple definitions of legacy code and identify characteristics in real codebases

### Activities

1. **Use Copilot to Generate Legacy Code Definitions**

   - Open GitHub Copilot Chat
   - Use the prompt: "Give me 3 definitions of legacy code"
   - Review the results (likely: code without tests, outdated code, inherited code)
   - Expand the request: "Give me 10 definitions of legacy code"
   - Finally: "Give me 25 definitions of legacy code"

2. **Explore Non-Legacy Code Characteristics**

   - Prompt: "Give me 3 definitions of code that is NOT legacy"
   - Expected responses: modern code, tested code, well-documented code
   - Compare with legacy definitions

3. **Investigate Evergreen Code**

   - Prompt: "What are the definitions of Evergreen code?"
   - Identify common themes: continuously updated, future-proof, well-documented, well-tested
   - Note the emphasis on testing in all definitions

4. **Analyze Your Own Codebase**
   - Open a project from your organization
   - Use Copilot to analyze: "Based on common legacy code definitions, identify legacy characteristics in #codebase"
   - Document findings

### Success Criteria

- [ ] Generated at least 10 different legacy code definitions
- [ ] Identified key differences between legacy and Evergreen code
- [ ] Recognized that testing is central theme across definitions
- [ ] Analyzed at least one real codebase for legacy characteristics

### Key Concepts

- **Legacy Code**: No universally accepted definition; easier to define what it's NOT
- **All Code Starts as Greenfield**: Few codebases maintain Greenfield status over time
- **Code Degradation**: Codebases degrade over time without active maintenance
- **Testing as Foundation**: Lack of tests is primary legacy indicator across definitions

---

## Lab 2: Working with the "Working Effectively with Legacy Code" Book

**Time**: 30 minutes
**Objective**: Access and understand key strategies from Michael Feathers' seminal work on legacy code

### Activities

1. **Access the Book**

   - Visit: `archive.org`
   - Search for: "Working Effectively with Legacy Code" by Michael Feathers
   - Download EPUB version for reference
   - Note: This book is freely available through Internet Archive

2. **Identify Key Strategies**

   - Use Copilot to summarize: "What are the main strategies in 'Working Effectively with Legacy Code' by Michael Feathers?"
   - Focus on the first strategy emphasized in training: **You need more tests**
   - Explore how AI techniques can accelerate implementation of book's strategies

3. **Compare Techniques**
   - List traditional refactoring techniques from the book
   - Identify which techniques are enhanced by AI assistance
   - Document potential time savings with AI-assisted approach

### Success Criteria

- [ ] Located and accessed the book resource
- [ ] Identified "more tests" as primary strategy
- [ ] Listed at least 5 key strategies from the book
- [ ] Documented how AI can accelerate each strategy

### Key Concepts

- **Tests First**: Before modifying legacy code, establish comprehensive test coverage
- **AI Acceleration**: AI techniques help implement legacy code strategies more quickly
- **Risk Mitigation**: Tests provide confidence when making changes to production code

---

## Lab 3: Pre-Modification Strategies for Legacy Code

**Time**: 45 minutes
**Objective**: Implement essential strategies before modifying legacy code with AI assistance

### Activities

1. **Version Control Strategy**

   - Create a new branch for experiments: `git checkout -b legacy-exploration`
   - Establish backup strategy: branching, tagging, commits
   - Practice: `git tag backup-YYYYMMDD-HHMM`
   - Document rollback procedures

2. **Understand Non-Deterministic Code Generation**

   - Make the same request to Copilot 3 times in separate chat sessions
   - Compare the outputs - note differences
   - Document: Why version control matters when outputs vary
   - Key insight from training: Copilot once said "I've noticed you've not been accepting my changes. Perhaps I should try a different approach."

3. **Establish Testing Strategy**

   - Review existing test coverage in your project
   - Use Copilot: "Analyze test coverage for #file and suggest improvements"
   - Create plan for adding tests before modifications
   - Consider: Unit tests, integration tests, approval tests

4. **Feature Flagging Exploration**

   - Research feature flag implementations for your language
   - Prompt: "Show me how to implement feature flags in [language] to test new code in production without exposing to users"
   - Document benefits: Deploy to production, test safely, no user exposure

5. **Review Strategy Setup**

   - Establish code review checklist
   - Consider AI-assisted code review as first pass
   - Plan: AI review → Developer review → Approval
   - Create PR template requiring AI review completion

6. **Keep Changes Small**
   - Practice: Make one small change and commit
   - Target: Incremental changes over large rewrites
   - Review training insight: "You can easily build up large number of changes very quickly"

### Success Criteria

- [ ] Created backup strategy with branching and tagging
- [ ] Documented non-deterministic nature of AI code generation
- [ ] Established testing strategy for legacy code
- [ ] Researched feature flagging approach
- [ ] Created code review workflow including AI review
- [ ] Committed to incremental change philosophy

### Key Concepts

- **Backup Strategy**: Essential because AI generation is non-deterministic
- **Testing Confidence**: Must have confidence tests will catch issues before production
- **Feature Flags**: Deploy code to production for testing without user exposure
- **Incremental Changes**: Keep change sets small and manageable
- **AI Review First**: Use AI for initial code review to reduce developer review burden

---

## Lab 4: AI-Assisted Code Review Setup

**Time**: 60 minutes
**Objective**: Implement automated AI code review in your CI/CD pipeline

### Activities

1. **Explore GitHub Copilot CLI**

   - Install GitHub Copilot CLI if not already installed
   - Test basic commands: `gh copilot suggest`
   - Explore: `gh copilot explain`

2. **Design Review Workflow**

   - Question from training: "Is it copilot reviewing copilot generated code?"
   - Strategy: Use different models for generation vs. review
   - Example: "Write code in Claude 4.5, review with ChatGPT-4o"
   - Document model selection rationale

3. **Create Review Script**

   ```yaml
   # Example workflow structure
   name: AI Code Review
   on: pull_request
   jobs:
     ai-review:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v2
         - name: Run AI Review
           # Use Copilot CLI with specific model
           # Produce thumbs up/down for pipeline
   ```

4. **Define Review Criteria**

   - Create instruction file for AI reviewer
   - Specify what to check: security, performance, style, tests
   - Prompt template: "Review this PR for [criteria] and provide thumbs up/down with reasoning"

5. **Test the Workflow**

   - Create a test PR
   - Run AI review manually first
   - Observe output format
   - Refine criteria based on results

6. **Implementation Considerations**
   - From training: "Not implemented up to this point, but we can take a shot at it"
   - Question: "Is it PR decoration with comments or something more?"
   - Design decision: Comments on specific lines vs. summary review

### Success Criteria

- [ ] Installed and tested GitHub Copilot CLI
- [ ] Documented strategy for using different models
- [ ] Created AI review workflow structure
- [ ] Defined review criteria and instruction file
- [ ] Tested review on sample PR
- [ ] Documented PR decoration approach

### Key Concepts

- **Model Diversity**: Use different models for generation vs. review to avoid bias
- **Automated Quality Gates**: AI review as required step before human review
- **CLI Integration**: GitHub Copilot CLI enables pipeline automation
- **Thumbs Up/Down**: Simple pass/fail mechanism for pipeline decisions

### Instructor Notes

- This was discussed as something to potentially demonstrate "tomorrow or Thursday"
- Team was interested in seeing implementation
- Focus on practical implementation over theory

---

## Lab 5: Context Management Fundamentals

**Time**: 45 minutes
**Objective**: Master techniques for managing Copilot context to avoid overflow

### Activities

1. **Monitor Token Usage**

   - Access prompt request dashboard
   - Review your recent token usage
   - Identify highest token consumption activities
   - Document usage patterns

2. **Use Token Estimation Tools**

   - Visit OpenAI Tokenizer: `platform.openai.com/tokenizer`
   - Paste a code file and see token count
   - Test different file sizes
   - Document relationship between file size and tokens

3. **Detect Context Overflow**

   - Key symptom: "Off-topic replies"
   - Create example: Add many unrelated files to context
   - Ask specific question and observe degraded responses
   - Document: How to recognize overflow

4. **Practice Context Cleanup**

   - Open 10+ files in VS Code tabs
   - Use Copilot chat with #codebase
   - Now close all but 2 files
   - Ask same question - note improved responses
   - Key insight: "Keep number of tabs open in IDE to as few as possible"

5. **Clear and Rebuild Context**

   - Clear current chat session
   - Practice rebuilding context deliberately:
     - Use #file for specific files
     - Use #folder for directories
     - Use hashtag mentions for symbols
   - Compare context size before/after

6. **Token Window Analysis**
   - Review model capabilities from training:
     - Claude Sonnet 4.5: 200,000+ tokens
     - ChatGPT-4o: 128,000 input + 16,000 output
     - ChatGPT-4: 64,000 input + 8,000 output
   - Note: Output tokens = code generation capacity
   - Choose model based on context needs vs. reasoning style

### Success Criteria

- [ ] Located and reviewed prompt request dashboard
- [ ] Used tokenizer tool on sample files
- [ ] Identified off-topic replies as overflow symptom
- [ ] Practiced context cleanup by closing tabs
- [ ] Successfully cleared and rebuilt context
- [ ] Documented model token windows and use cases

### Key Concepts

- **Token Window**: Limited space for context + generation
- **Input vs. Output Tokens**: Input = context, Output = generated code
- **Context Inference**: Copilot infers context from open files
- **Model Selection Trade-offs**: Large context (Claude) vs. reasoning style (GPT-5)
- **Overflow Symptoms**: Off-topic or irrelevant responses indicate context issues

---

## Lab 6: Advanced Context Management with Hashtag Mentions

**Time**: 30 minutes
**Objective**: Use hashtag mentions to precisely control context scope

### Activities

1. **File-Level Context**

   ```
   Prompt: "Explain the main functionality in #file:calculator.cs"
   ```

   - Practice with 3 different files
   - Observe how response focuses on specific file
   - Note token usage for targeted context

2. **Folder-Level Context**

   ```
   Prompt: "Summarize test coverage in #folder:tests/"
   ```

   - Compare folder mention vs. opening all files
   - Document efficiency gains
   - Test nested folders

3. **Symbol-Level Context**

   ```
   Prompt: "Explain #symbol:Calculator.Add method"
   ```

   - Practice targeting specific classes, methods
   - Use for large files where you need specific portion
   - Compare token usage vs. entire file

4. **Combining Context Mentions**

   ```
   Prompt: "Compare #file:oldCalculator.cs with #file:newCalculator.cs"
   ```

   - Practice multi-file comparisons
   - Add folder context: "#folder:legacy/ versus #folder:modern/"
   - Document most effective combinations

5. **Chat Mode Context**
   - Used in chat modes and prompt files
   - Practice in both contexts
   - Note any behavioral differences

### Success Criteria

- [ ] Successfully used #file for targeted analysis
- [ ] Used #folder for directory-level operations
- [ ] Targeted specific symbols with #symbol
- [ ] Combined multiple context mentions effectively
- [ ] Documented token savings from targeted context

### Key Concepts

- **Precision Context**: Hashtag mentions restrict context scope
- **Token Efficiency**: Smaller context = more room for generation
- **Multi-File Operations**: Combine mentions for comparisons
- **Works in Multiple Modes**: Chat modes and prompt files both support mentions

---

## Lab 7: GitHub Copilot Spaces Exploration

**Time**: 30 minutes
**Objective**: Understand Copilot Spaces for sharing context across team

### Activities

1. **Access GitHub Copilot UI**

   - Navigate to `github.com`
   - Find Copilot interface (not VS Code)
   - Locate Spaces feature

2. **Create a Space**

   - Create new Space for your project
   - Add instruction files
   - Add documentation
   - Note: Can add repository in Space UI

3. **Reference Space in IDE**

   - In VS Code Copilot Chat
   - Use GitHub tool to recall Space
   - Add to current chat context
   - Limitation from training: "Repository is no longer in context when you reference in IDE"

4. **Combine Space with Codebase**

   - Reference Space for shared instructions
   - Add #codebase for current repository context
   - Test workflow: Space context + local code

5. **Compare with Project-Level Instructions**
   - Alternative: Define instructions in `.github/copilot/instructions/`
   - Commit to repository
   - Compare pros/cons of each approach
   - Training insight: "In my mind, just defining them within project and saving with project itself accomplishes same thing"

### Success Criteria

- [ ] Located GitHub Copilot UI and Spaces
- [ ] Created a test Space with instructions
- [ ] Referenced Space in VS Code
- [ ] Understood repository context limitation
- [ ] Compared Spaces vs. project instructions approaches

### Key Concepts

- **Shared Context**: Spaces allow team to share consistent context
- **Repository Limitation**: Repos in Space don't transfer to IDE context
- **Alternative Approach**: Project-level instructions saved in Git
- **Use Case**: Primarily for sharing instruction files across team

### Instructor Notes

- Instructor hasn't worked extensively with Spaces (primarily works alone)
- Emphasis on project-level instructions as simpler alternative
- Consider Spaces for team environments with standardized workflows

---

## Lab 8: Token Estimation and Monitoring

**Time**: 45 minutes
**Objective**: Develop Python tool to analyze context token usage

### Activities

1. **Review Training Example**

   - From training: "Did some work yesterday after class"
   - "Python library that can do context analysis"
   - "Rough estimate, not entirely accurate"

2. **Install Python Tokenizer Library**

   ```python
   pip install tiktoken  # OpenAI's tokenizer
   ```

3. **Create Token Counter Script**

   ```python
   import tiktoken
   import os

   def count_file_tokens(filepath, encoding_name="cl100k_base"):
       """Count tokens in a file"""
       encoding = tiktoken.get_encoding(encoding_name)
       with open(filepath, 'r', encoding='utf-8') as f:
           content = f.read()
       tokens = encoding.encode(content)
       return len(tokens)

   def count_directory_tokens(directory):
       """Count tokens across directory"""
       total_tokens = 0
       file_counts = {}

       for root, dirs, files in os.walk(directory):
           for file in files:
               if file.endswith(('.cs', '.py', '.js', '.ts', '.md')):
                   filepath = os.path.join(root, file)
                   try:
                       tokens = count_file_tokens(filepath)
                       file_counts[filepath] = tokens
                       total_tokens += tokens
                   except Exception as e:
                       print(f"Error processing {filepath}: {e}")

       return total_tokens, file_counts

   # Usage
   total, breakdown = count_directory_tokens("./src")
   print(f"Total tokens: {total:,}")
   print("\nTop 10 files by token count:")
   for file, count in sorted(breakdown.items(), key=lambda x: x[1], reverse=True)[:10]:
       print(f"{count:,} - {file}")
   ```

4. **Analyze Your Codebase**

   - Run script on your project
   - Identify highest token-consuming files
   - Calculate what fits in various model windows:
     - Claude Sonnet 4.5: ~200K tokens
     - ChatGPT-4o: ~128K tokens
     - ChatGPT-4: ~64K tokens

5. **Create Context Budget**

   - Document token budget for different tasks
   - Example: "Analysis tasks need more context (use Claude)"
   - Example: "Step-by-step operations need less (use GPT-5)"

6. **Add to IDE Workflow**
   - Create script to check open tabs token count
   - Display warning if approaching limit
   - Suggest which files to close

### Success Criteria

- [ ] Installed tiktoken or equivalent library
- [ ] Created working token counter script
- [ ] Analyzed token distribution in your codebase
- [ ] Identified highest token-consuming files
- [ ] Created context budget for different scenarios

### Key Concepts

- **Rough Estimation**: Token counters provide approximation
- **File Analysis**: Identify which files consume most context
- **Context Budgeting**: Plan context usage based on task type
- **Proactive Monitoring**: Check token count before hitting limits

---

## Lab 9: Meta-Instruction Files - AI-Assisted Output

**Time**: 60 minutes
**Objective**: Implement AI-assisted output instruction file for audit trail and provenance

### Activities

1. **Understand the Pattern**

   - Reference file: `.github/copilot/instructions/ai-assisted-output.instructions.md`
   - Review metadata header format
   - Key requirement: ALL AI-generated output must include provenance header

2. **Create Base Instruction File**

   ```markdown
   ---
   applyTo: "**/*"
   description: "Guidelines for all AI-generated output"
   ---

   # AI-Assisted Output Requirements

   ## Metadata Header

   All AI-generated files must include a header with:

   - **Prompt**: The prompt that created this output
   - **Execution Time**: How long generation took
   - **AI Log**: Path to conversation log
   - **Source**: The prompt file that was executed
   - **Applies To**: What files/contexts this affects
   - **Generated Date**: ISO 8601 format timestamp
   - **Model**: Which AI model was used

   ## Example Header Format

   <!--
   AI-Generated: true
   Prompt: "Create calculator class with add/subtract methods"
   Generated: 2025-01-13T10:30:00Z
   Model: claude-sonnet-4.5
   Source: .github/copilot/prompts/create-calculator.prompt.md
   AI-Log: .ai-logs/2025/01/13/calculator-creation.md
   -->
   ```

3. **Test Output Generation**

   - Create a simple prompt file
   - Execute with Copilot
   - Verify output includes required header
   - Check if AI log was created

4. **Understand AI Log Structure**
   From training, AI logs should contain:

   - Conversation history
   - Summary suitable for resuming
   - Current step in multi-step operations
   - Context snapshot

5. **Create Example AI Log**

   ```markdown
   # AI Session Log: Calculator Creation

   **Session ID**: calc-2025-01-13-001
   **Started**: 2025-01-13T10:30:00Z
   **Model**: claude-sonnet-4.5

   ## Conversation

   ### User

   Create a calculator class with add and subtract methods

   ### Assistant

   [Generated code with explanation]

   ### User

   Add multiply and divide methods

   ### Assistant

   [Generated code]

   ## Summary

   Created Calculator class with four basic operations.
   All methods include input validation and test coverage.
   Ready for integration testing.

   ## Context Snapshot

   - Files modified: Calculator.cs
   - Tests created: CalculatorTests.cs
   - Dependencies: None added

   ## Next Steps

   - Run unit tests
   - Add to CI/CD pipeline
   ```

6. **Implement for Binary Files**

   - For non-text files (images, binaries)
   - Create sidecar file: `filename.ext.ai-metadata`
   - Include same metadata structure

7. **Set Up AI Log Directory Structure**
   ```
   .ai-logs/
     2025/
       01/
         13/
           calculator-creation.md
           ui-design.md
       02/
         01/
           refactoring-session.md
   ```

### Success Criteria

- [ ] Created ai-assisted-output.instructions.md file
- [ ] Generated output with proper metadata header
- [ ] Created AI log with conversation history
- [ ] Implemented sidecar files for binary assets
- [ ] Established AI log directory structure
- [ ] Tested header appears in generated code

### Key Concepts

- **Clear Provenance**: Every AI output must be traceable to its source
- **Audit Trail**: AI logs record how artifacts were created
- **Resumable Sessions**: Summary files allow continuing work later
- **Metadata Headers**: In-line for text files, sidecar for binaries
- **Benefits**: Traceability, reproducibility, team collaboration, audit compliance

### Instructor Notes

- Training emphasized this as "very powerful way of defining"
- Two main benefits: Metadata provenance + Session resumption
- Summary files allow "resuming that process at point it left off"

---

## Lab 10: Session Resumption with Summary Files

**Time**: 45 minutes
**Objective**: Practice resuming long-running AI sessions using summary files

### Activities

1. **Start a Multi-Step Project**

   - Choose complex task: "Modernize legacy authentication system"
   - Begin conversation with Copilot
   - Make several rounds of changes (at least 5 exchanges)
   - Generate initial code

2. **Create Summary File Manually**

   ```markdown
   # Session Summary: Authentication Modernization

   **Session ID**: auth-modern-2025-01-13
   **Current Step**: 3 of 7
   **Status**: In Progress

   ## Objectives

   1. ✅ Analyze current authentication system
   2. ✅ Design new OAuth2 implementation
   3. 🔄 Implement user service refactoring (CURRENT)
   4. ⏳ Add JWT token generation
   5. ⏳ Implement refresh token logic
   6. ⏳ Update authorization middleware
   7. ⏳ Migration strategy for existing users

   ## Completed Work

   - Analyzed legacy BasicAuth implementation
   - Identified security vulnerabilities
   - Designed OAuth2 architecture
   - Created database migration scripts

   ## Current Context

   Working on UserService class:

   - Refactoring password storage from MD5 to bcrypt
   - Adding email verification workflow
   - Implementing account lockout policy

   ## Code References

   - #file:src/Services/UserService.cs (primary)
   - #file:src/Models/User.cs
   - #file:database/migrations/001_auth_tables.sql

   ## Decisions Made

   - Use OAuth2 with PKCE flow
   - JWT tokens with 15-minute expiry
   - Refresh tokens stored in Redis
   - Migrate users on first login

   ## Next Actions

   1. Complete UserService refactoring
   2. Add unit tests for new UserService methods
   3. Begin JWT token generation implementation
   ```

3. **Clear Context and Resume**

   - Close all tabs
   - Start new Copilot chat session
   - Add summary file to context: #file:.ai-logs/2025/01/13/auth-modern-summary.md
   - Continue from step 3: "Continue with UserService refactoring from the summary"

4. **Test Context Transfer**

   - Verify Copilot remembers:
     - Architectural decisions (OAuth2, PKCE)
     - Current step (3 of 7)
     - Files being modified
     - Next actions
   - Make next change and observe continuity

5. **Update Summary File**

   - After completing step 3
   - Update summary with progress
   - Mark step 3 as ✅ complete
   - Update current step to 4
   - Add new context from step 3 work

6. **Practice Resume Cycle Multiple Times**
   - Complete step 4
   - Update summary
   - Clear context
   - Resume from updated summary
   - Repeat for remaining steps

### Success Criteria

- [ ] Created detailed multi-step summary file
- [ ] Successfully cleared and resumed session
- [ ] Copilot continued work coherently from summary
- [ ] Updated summary after completing steps
- [ ] Completed full cycle at least twice
- [ ] Verified context reduction after clearing

### Key Concepts

- **Multi-Step Tracking**: Summary tracks progress through complex operations
- **Context Efficiency**: Clear and resume reduces token usage
- **Continuity**: Well-written summaries enable seamless continuation
- **Step Markers**: Track which steps completed, current, and pending
- **Decision Log**: Record architectural choices for consistency

### Real-World Application

From training: "If you're in a chat session that is going to be lengthy and involve a lot of back and forth... essentially update that summary file and then clear your chat window to clear up context window and then just add that one summary file back into context"

---

## Lab 11: Copilot Instructions File

**Time**: 30 minutes
**Objective**: Create project and personal instruction files for consistent Copilot behavior

### Activities

1. **Create Personal Instructions**

   - Access Copilot settings in VS Code
   - Find personal instructions section
   - Add instructions for output verbosity (from training question about controlling output)

   ```markdown
   # Personal Copilot Instructions

   ## Response Style

   - Provide concise, terse responses
   - Minimize explanatory text
   - Focus on code over commentary
   - Only explain complex concepts when asked

   ## Code Generation

   - Follow my organization's style guide
   - Always include error handling
   - Generate unit tests by default
   ```

2. **Create Project-Level Instructions**

   - Create: `.github/copilot/instructions/copilot-instructions.instructions.md`

   ```markdown
   ---
   applyTo: "**/*"
   description: "General Copilot usage instructions for this project"
   ---

   # Project Copilot Instructions

   ## Code Standards

   - Use C# 12 features
   - Follow Microsoft naming conventions
   - Async methods must be suffixed with Async
   - All public APIs must have XML documentation

   ## Testing Requirements

   - Generate xUnit tests for all new methods
   - Minimum 80% code coverage
   - Use Moq for mocking dependencies

   ## Security

   - Never hardcode credentials
   - Use configuration files for settings
   - Validate all user inputs
   - Use parameterized SQL queries

   ## Dependencies

   - Prefer built-in .NET libraries
   - Check package popularity before suggesting new dependencies
   - Document reason for adding new packages
   ```

3. **Test Personal vs. Project Instructions**

   - Ask Copilot to generate a method
   - Verify it follows both sets of instructions:
     - Personal: Terse output
     - Project: C# 12, XML docs, tests
   - Document which instructions take precedence

4. **Scope Different Instructions**

   - Create language-specific instructions:
     - `.github/copilot/instructions/csharp.instructions.md` (applyTo: '\*_/_.cs')
     - `.github/copilot/instructions/typescript.instructions.md` (applyTo: '\*_/_.ts')
   - Test that Copilot applies appropriate instructions per file type

5. **Organize Generated vs. Manual Instructions**
   - Create folders:
     - `.github/copilot/instructions/` (manual instructions)
     - `.github/copilot/instructions/generated/` (AI-generated)
   - Name with suffix: `*.instructions.md`
   - From training: "I've also used folder under instruction folder called generated, which I put instruction files that are generated by Copilot in comparison to instruction files that I've created personally"

### Success Criteria

- [ ] Created personal instructions for output style
- [ ] Created project-level instructions file
- [ ] Tested instruction precedence
- [ ] Created language-specific scoped instructions
- [ ] Organized manual vs. generated instructions
- [ ] Verified instructions are being followed

### Key Concepts

- **Personal Instructions**: User-specific preferences (not committed)
- **Project Instructions**: Team-shared guidelines (committed to Git)
- **Scope Control**: Use applyTo field to target specific files
- **Organization**: Separate manual and generated instructions
- **Naming Convention**: Use `*.instructions.md` suffix

### From Training

- Question: "How to control output in terms of how much verbage it gives you?"
- Answer: "Personal instruction file... say I just give me very very terse responses"
- "That might be good use of copilot instruction file, because other people may not want that same instruction"

---

## Lab 12: Meta-Instructions for Prompts and Instructions

**Time**: 60 minutes
**Objective**: Implement meta-instruction files that guide creation of other instruction and prompt files

### Activities

1. **Understand Meta-Instruction Concept**
   From training: "Meta instructions... applicable across any project you might be working with"

   Four types discussed:

   1. AI-assisted output instructions (completed in Lab 9)
   2. Copilot instructions (completed in Lab 11)
   3. Instruction prompt instruction file - for creating effective prompts
   4. Prompt file instruction - for prompt structure

2. **Create Instruction Prompt Instruction File**

   - File: `.github/copilot/instructions/instruction-prompt.instructions.md`

   ````markdown
   ---
   applyTo: "**/*.prompt.md"
   description: "Guidelines for creating effective prompt files"
   ---

   # Instruction Prompt Instructions

   Instructions for creating effective prompts

   ## Prompt File Structure

   Every prompt file must include:

   ### 1. Header Metadata

   ```yaml
   ---
   title: Clear descriptive title
   description: What this prompt accomplishes
   model: Recommended AI model (claude-sonnet-4.5, gpt-4o, etc.)
   context: Required files/folders for context
   ---
   ```
   ````

   ### 2. Objective Statement

   Clear, concise statement of what the prompt should achieve.

   ### 3. Context Section

   Specify required context:

   - #file references for specific files
   - #folder references for directories
   - #symbol references for specific code elements

   ### 4. Constraints

   Any limitations or requirements:

   - Must maintain backward compatibility
   - Maximum X lines of code
   - Must include tests
   - Specific libraries to use/avoid

   ### 5. Success Criteria

   Checklist of what successful output includes:

   - [ ] Meets functional requirements
   - [ ] Includes tests
   - [ ] Follows style guide
   - [ ] Has documentation

   ### 6. Examples (Optional)

   Show example input/output if helpful

   ## Writing Guidelines

   **Be Specific**
   ❌ Bad: "Make it better"
   ✅ Good: "Refactor UserService to use dependency injection"

   **Provide Context**
   ❌ Bad: "Add authentication"
   ✅ Good: "Add JWT authentication to #file:api/controller.cs using OAuth2 flow defined in #file:docs/security.md"

   **Define Success**
   ❌ Bad: "Improve tests"
   ✅ Good: "Increase test coverage to 80% by adding unit tests for all public methods in UserService"

   ```

   ```

3. **Create Prompt File Instruction**

   - File: `.github/copilot/instructions/prompt-file.instructions.md`

   ```markdown
   ---
   applyTo: "prompts/**/*.md"
   description: "Standards for prompt file creation"
   ---

   # Prompt File Instructions

   Instructions for prompts - more targeted than instruction prompt file

   ## File Naming

   - Use kebab-case: `create-user-service.prompt.md`
   - Suffix must be `.prompt.md`
   - Store in: `.github/copilot/prompts/`

   ## Content Requirements

   ### Must Include

   - Clear objective statement
   - Required context files (#file/#folder/#symbol)
   - Expected output format
   - Success criteria checklist

   ### Should Include

   - Constraints and requirements
   - Model recommendation
   - Estimated execution time
   - Dependencies on other prompts

   ### May Include

   - Example input/output
   - Alternative approaches
   - Troubleshooting tips

   ## Context Management

   - Be explicit with context mentions
   - Don't assume #codebase - too broad
   - Specify exact files when possible
   - Document why each context item is needed

   ## Testing Prompts

   Before committing:

   - Execute prompt in clean chat session
   - Verify output meets success criteria
   - Check token usage is reasonable
   - Test with recommended model
   - Document execution time
   ```

4. **Test the Meta-Instructions**

   - Create a new prompt file
   - Prompt: "Create a prompt file for adding a new API endpoint"
   - Verify Copilot follows instruction prompt instructions
   - Generated prompt should include: metadata, objective, context, constraints, success criteria

5. **Create Sample Prompt Using Guidelines**

   ````markdown
   ---
   title: Add User Authentication Endpoint
   description: Create POST /api/auth/login endpoint with JWT response
   model: claude-sonnet-4.5
   context:
     -  #file:src/Controllers/BaseController.cs
     -  #file:src/Services/AuthService.cs
     -  #file:docs/api-standards.md
   ---

   # Add User Authentication Endpoint

   ## Objective

   Create a new POST endpoint at /api/auth/login that accepts email/password
   and returns a JWT token on successful authentication.

   ## Context

   - Extend BaseController pattern from #file:src/Controllers/BaseController.cs
   - Use AuthService from #file:src/Services/AuthService.cs
   - Follow API standards in #file:docs/api-standards.md

   ## Requirements

   - Accept JSON body: { "email": string, "password": string }
   - Return 200 with JWT token on success
   - Return 401 on invalid credentials
   - Return 400 on validation errors
   - Include rate limiting (5 attempts per minute)
   - Log authentication attempts

   ## Success Criteria

   - [ ] Endpoint created in appropriate controller
   - [ ] Input validation implemented
   - [ ] AuthService integrated correctly
   - [ ] Appropriate status codes returned
   - [ ] Unit tests with 80%+ coverage
   - [ ] Integration test for happy path
   - [ ] API documentation updated
   - [ ] Rate limiting configured

   ## Example Request

   ```json
   POST /api/auth/login
   {
     "email": "user@example.com",
     "password": "SecurePass123!"
   }
   ```
   ````

   ## Example Response

   ```json
   {
     "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
     "expiresAt": "2025-01-13T12:00:00Z",
     "refreshToken": "..."
   }
   ```

   ```

   ```

6. **Document the System**
   - Create README for instructions folder
   - Explain the four meta-instruction types
   - Provide examples of each
   - Document when to use which type

### Success Criteria

- [ ] Created instruction-prompt.instructions.md file
- [ ] Created prompt-file.instructions.md file
- [ ] Tested by generating new prompt file
- [ ] Generated prompt follows guidelines
- [ ] Created comprehensive sample prompt
- [ ] Documented meta-instruction system

### Key Concepts

- **Meta-Instructions**: Instructions for creating other instructions
- **Standardization**: Ensures consistent prompt/instruction quality
- **Applicable Across Projects**: These patterns work for any codebase
- **Hierarchy**: Instructions that guide creation of instructions that guide code generation

### From Training

- "Instruction prompt instruction file - instructions for creating effective prompts"
- "Prompt file instruction - instructions for prompts, bit more targeted"
- "Allows you to standardize the way in which instructions are built or prompt files are built"
- "Define what every prompt file should have in terms of its structure"

---

## Lab 13: MCP Servers and Agentic Tools

**Time**: 45 minutes
**Objective**: Explore Model Context Protocol servers for enhanced AI functionality

### Activities

1. **Understand MCP Concept**
   From training:

   - "Only come out earlier in the year"
   - "Proposed and implemented by Anthropic"
   - "Lot of adoption"
   - "Part of move towards Agentic models"
   - "Being able to actually do things"

2. **Research MCP Servers**

   - Visit Anthropic's MCP documentation
   - Understand: "Provide ability to do lot more functional things"
   - Original limitation: "Only thing you could do was ask"
   - Now: Tools enable actions, not just responses

3. **Explore Available MCP Servers**

   - Search GitHub for MCP servers
   - Categories to explore:
     - File system operations
     - Database interactions
     - API integrations
     - Development tools

4. **Install an MCP Server**

   - Choose simple MCP server (file operations or Git)
   - Follow installation instructions
   - Configure in Copilot settings if applicable

5. **Test MCP Functionality**

   - Example: "Use the file system MCP to create a new directory structure"
   - Compare to just asking: "Tell me how to create a directory structure"
   - Difference: MCP can actually DO it vs. just describing it

6. **Design Custom MCP Use Case**
   - Identify repetitive task in your workflow
   - Consider: "What would I want AI to actually DO for me?"
   - Examples:
     - Create pull request
     - Run tests and analyze results
     - Deploy to environment
     - Update documentation from code

### Success Criteria

- [ ] Understand MCP purpose (actions vs. just responses)
- [ ] Researched available MCP servers
- [ ] Installed at least one MCP server
- [ ] Tested MCP functionality
- [ ] Identified potential custom MCP use cases

### Key Concepts

- **MCP = Actions**: Model Context Protocol enables AI to perform actions
- **Beyond Chat**: Not just asking, but doing
- **Anthropic-Proposed**: Standard for AI tool integration
- **Wide Adoption**: Many tools implementing MCP
- **Agentic Future**: Part of evolution toward autonomous AI agents

### Instructor Notes

- Training covered this at high level, didn't demo
- Emphasis on "being able to actually do things"
- Part of broader agentic AI trend

---

## Lab 14: Applying Techniques to Legacy Code Project

**Time**: 90-120 minutes
**Objective**: Apply all learned techniques to a real legacy codebase

### Activities

1. **Select Target Codebase**
   Options mentioned in training:

   - Calculator project from Day 1
   - Instructor's internal CODE application (early stage with "target rich environment for improvement")
   - Fork a GitHub project with open issues (from earlier suggestion)
   - Your own organization's legacy code

2. **Initial Assessment**

   ```
   Prompt (in new chat):
   "Analyze #codebase for legacy code characteristics including:
   - Code without tests
   - Outdated dependencies
   - Hard to understand code
   - Technical debt
   - Non-standard patterns
   Provide summary with specific examples."
   ```

3. **Implement Pre-Modification Strategies**

   - Create backup: `git checkout -b legacy-assessment-2025-01-13`
   - Tag starting point: `git tag before-legacy-work`
   - Document rollback procedure

4. **Add Testing Foundation**

   ```
   Prompt:
   "Review #file:[your-main-class] and create comprehensive unit tests.
   Use approval testing pattern where appropriate.
   Target 80% code coverage."
   ```

   - Generate tests
   - Run tests to establish baseline
   - Commit: "Add baseline test coverage"

5. **Manage Context for Large Codebase**

   - Create token analysis of project
   - Identify high-token files
   - Choose model: Claude for large context, GPT-5 for reasoning
   - Practice targeted context: #file:#folder:#symbol

6. **Implement AI-Assisted Output Pattern**

   - Add `.github/copilot/instructions/ai-assisted-output.instructions.md`
   - Generate some code with proper provenance headers
   - Create AI log entry
   - Verify metadata is included

7. **Create Project Instructions**

   - Add `.github/copilot/instructions/copilot-instructions.instructions.md`
   - Include:
     - Code standards
     - Testing requirements
     - Security guidelines
     - Dependency preferences
   - Test that new generations follow instructions

8. **Create Prompt Library**

   - `.github/copilot/prompts/add-tests.prompt.md`
   - `.github/copilot/prompts/refactor-method.prompt.md`
   - `.github/copilot/prompts/modernize-dependency.prompt.md`
   - Follow instruction-prompt guidelines from Lab 12

9. **Perform Incremental Refactoring**

   - Select one small area for improvement
   - Create prompt for the change
   - Generate code
   - Review carefully
   - Run tests
   - Commit small change
   - Repeat
   - Goal: Keep change sets small (from training: "easily build up large number of changes very quickly")

10. **Create Session Summary**
    - Document all changes made
    - Record decisions
    - Note current progress
    - Create resumable summary file
    - Test resuming work from summary

### Success Criteria

- [ ] Selected appropriate legacy codebase
- [ ] Created backup strategy with branch and tags
- [ ] Added baseline test coverage
- [ ] Managed context effectively for codebase size
- [ ] Implemented AI-assisted output pattern
- [ ] Created project instruction files
- [ ] Built prompt library
- [ ] Made incremental improvements with proper commits
- [ ] Created resumable session summary

### Key Concepts

- **Comprehensive Application**: Uses all techniques learned in single project
- **Real-World Practice**: Mirrors actual legacy code modernization workflow
- **Incremental Progress**: Small changes, frequent commits
- **Audit Trail**: Every AI change documented and traceable
- **Team Collaboration**: Shared instructions and prompts

### Real-World Application

This lab replicates the Day 2 focus: "Working in legacy code environment... rules are quite a bit different than what we were doing yesterday."

---

## Session Review and Assessment

### Key Takeaways

1. **Legacy Code Definition**: No universal definition; focus on what it's NOT
2. **Testing Foundation**: Tests are prerequisite for safe legacy code modification
3. **Pre-Modification Strategies**: Backup, testing, feature flags, review processes
4. **Context Management**: Critical skill for effective AI assistance
5. **Token Awareness**: Monitor and manage token usage actively
6. **Meta-Instructions**: Standardize AI interactions across team
7. **AI-Assisted Output**: Provenance and audit trail for all AI-generated code
8. **Session Resumption**: Long operations can be paused and resumed efficiently
9. **Incremental Changes**: Small, frequent commits over large rewrites
10. **MCP and Agentic AI**: Evolution from asking to doing

### Common Challenges

1. **Context Overflow**: Off-topic responses indicate context issues
2. **Non-Deterministic Output**: Same prompt can produce different results
3. **Token Management**: Easy to exceed limits without monitoring
4. **Audit Trail Overhead**: Initial setup time for meta-instructions
5. **Team Adoption**: Getting team to follow instruction file patterns

### Solutions Demonstrated

1. Clear chat and rebuild context deliberately
2. Version control strategy for backing out changes
3. Token estimation tools and monitoring scripts
4. Template files and examples for quick setup
5. Documentation and training materials in repository

### Next Steps

- Day 2 Afternoon: Read-only techniques for legacy code analysis
- Day 2 Afternoon: Modifying legacy code with AI assistance
- Days 3-5: Advanced topics and real-world application

### Additional Resources

- "Working Effectively with Legacy Code" by Michael Feathers (archive.org)
- GitHub Copilot CLI documentation
- Anthropic MCP documentation
- OpenAI Tokenizer tool
- GitHub Copilot Spaces documentation

---

## Instructor Notes

### Training Observations

- Instructor emphasizes testing as foundation ("you need more tests")
- Real example shared: Copilot said "I've noticed you've not been accepting my changes. Perhaps I should try a different approach"
- Team question about AI reviewing AI code - answer: use different models
- Interest in automated AI code review in PR pipeline
- Instructor hasn't extensively used Spaces (works alone)
- Token management tools created "yesterday after class" - shows active development

### Key Quotes from Training

- "Code bases can degrade over time"
- "Very easy for code to go from Greenfield to legacy. Doesn't take long."
- "You can easily build up large number of changes very quickly"
- "Keep your change sets as small as possible"
- "In my mind, just defining [instructions] within project and saving with project itself accomplishes same thing"
- "If you're in chat session that is going to be lengthy... clear your chat window to clear up context window"

### Timing Notes

- Session ended early due to team meeting
- More content planned: copilot instructions, generating prompts, guidance for AI
- Good stopping point after AI-assisted output discussion

### Demonstrations Planned But Not Completed

- Copilot instructions file in detail
- Prompt generation guidance
- Specific examples of instruction files
- More on generating instruction files

These topics will likely be covered in Day 2 Afternoon session.
