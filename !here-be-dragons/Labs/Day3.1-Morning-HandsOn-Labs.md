# Day 3 Morning Session - Hands-On Labs

## Understanding and Documenting Legacy Code

---

## Lab 1: Documenting Existing Code (20 minutes)

### Objective

Learn how to use GitHub Copilot to automatically generate documentation for existing code, including inline comments and XML documentation.

### Prerequisites

- VS Code with GitHub Copilot installed
- Calculator project or any existing C# project

### Steps

1. **Generate Inline Documentation**

   - Open an existing code file (e.g., `Evaluator.cs`)
   - Select the entire file or a specific method
   - Press `Ctrl+I` to open Copilot Chat inline
   - Enter the prompt: `document this code`
   - Review the suggested XML documentation comments
   - Accept or modify the changes as needed

2. **Document Specific Code Sections**

   - Select a complex piece of code (e.g., a complex method or algorithm)
   - Press `Ctrl+I`
   - Enter: `explain this code`
   - Review the detailed explanation provided
   - Optional: Follow up with `add this explanation as comments to the code`

3. **Verify Documentation Quality**
   - Review the generated comments for accuracy
   - Ensure XML documentation includes:
     - `<summary>` tags for classes and methods
     - `<param>` tags for method parameters
     - `<returns>` tags for return values
     - `<exception>` tags for thrown exceptions

### Expected Outcomes

- Code files have consistent XML documentation
- Complex code sections include explanatory comments
- Documentation is clear and follows language conventions

---

## Lab 2: Updating Project README Files (25 minutes)

### Objective

Use Copilot to generate and maintain comprehensive project documentation including architecture diagrams.

### Steps

1. **Update README with Project Overview**

   - Open the chat window (no file selected for project-wide context)
   - Enter: `update the documentation for the current state of this project`
   - Review the generated content for the README
   - Accept changes and verify the following sections are included:
     - Project overview
     - Project structure
     - Getting started
     - Prerequisites
     - Build and run instructions

2. **Generate Mermaid Architecture Diagrams**

   - In the chat window, enter:
     ```
     update the documentation with a mermaid architecture diagram,
     include sequence diagrams and a class diagram
     ```
   - Review the generated Mermaid diagrams
   - Preview the README to see rendered diagrams
   - Verify diagrams include:
     - System architecture diagram
     - Component interaction flow
     - Class diagram
     - Data flow diagram

3. **Add Deployment Documentation**
   - Enter: `add a deployment guide to the README`
   - Review and accept the deployment section
   - Verify it includes environment setup and deployment steps

### Expected Outcomes

- README.md is comprehensive and up-to-date
- Multiple Mermaid diagrams visualize system architecture
- Documentation can be easily previewed in VS Code

---

## Lab 3: Generating Migration Plans (30 minutes)

### Objective

Create a detailed migration plan for upgrading framework versions or dependencies.

### Steps

1. **Create Migration Plan**

   - Open the chat window
   - Enter:
     ```
     create a comprehensive migration plan to upgrade this project
     from .NET 8 to .NET 9. Include:
     - Pre-migration analysis
     - Breaking changes review
     - Step-by-step migration tasks
     - Testing strategy
     - Rollback plan
     ```

2. **Review Generated Plan**

   - Examine the migration phases and tasks
   - Review estimated effort (note: estimates should be validated)
   - Check for:
     - Dependency analysis
     - API obsolescence warnings
     - Breaking changes documentation
     - Risk assessment

3. **Deep Dive into Breaking Changes**

   - Follow up with:
     ```
     Review the System.Data table changes.
     Identify APIs marked as obsolete.
     Document the potential impact on the calculator code base.
     ```
   - Review the detailed analysis of breaking changes

4. **Generate Implementation Tasks**
   - Ask: `create implementation tasks from this migration plan`
   - Review generated tasks that could be assigned to team members or agents

### Expected Outcomes

- Comprehensive migration plan document
- Understanding of breaking changes and risks
- Actionable tasks for implementation
- Risk mitigation strategies

---

## Lab 4: Working with Instruction Files (35 minutes)

### Objective

Generate and use instruction files to maintain coding standards and project practices.

### Steps

1. **Generate Project Instruction Files**

   - Create or use an existing prompt file: `generate-instructions.prompt.md`
   - Add the following content:
     ```markdown
     Generate comprehensive instruction files for this project including:

     - C# coding standards
     - Project structure guidelines
     - Error handling practices
     - Code quality standards
     - Style conventions
     - Testing methodology
     - WPF-specific guidelines (if applicable)
     ```

2. **Run the Instruction Generation Prompt**

   - Right-click the prompt file
   - Select "Run Prompt"
   - Wait for Copilot to generate all instruction files
   - Review generated files in `.github/instructions/` folder:
     - `csharp.instructions.md`
     - `project.instructions.md`
     - `error-handling.instructions.md`
     - `code-quality.instructions.md`
     - `style.instructions.md`
     - `testing.instructions.md`

3. **Review Generated Instructions**

   - Open each instruction file
   - Verify they contain:
     - Clear rules and guidelines
     - Code examples
     - Do's and don'ts
     - Appropriate `applyTo:` patterns
   - Customize instructions to match your team's standards

4. **Evaluate Code Against Instructions**

   - Open a code file (e.g., `Evaluator.cs`)
   - In chat, enter:
     ```
     Evaluate this file against the project instruction files.
     Report any deviations and suggest fixes.
     ```
   - Review the compliance report
   - Note issues found:
     - Style violations
     - Missing documentation
     - Code quality issues
     - Incomplete implementations (TODOs)

5. **Apply Suggested Fixes**
   - Review each suggested fix
   - Accept or modify corrections
   - Re-evaluate to confirm compliance

### Expected Outcomes

- Complete set of instruction files for the project
- Understanding of how instruction files guide AI behavior
- Code evaluated and improved based on standards
- Ability to maintain consistent coding standards

---

## Lab 5: Using Background Coding Agents (25 minutes)

### Objective

Delegate tasks to background coding agents for autonomous implementation.

### Prerequisites

- Access to the background agent feature (sparkle icon in chat)
- Git repository initialized

### Steps

1. **Identify a Task for Background Processing**

   - Choose a task that can be implemented independently
   - Example: `create a chat mode for updating documentation`

2. **Delegate to Background Agent**

   - Enter your task in the chat window
   - Click the sparkle/delegate icon
   - Confirm delegation when prompted
   - Note the message: "Copilot will continue your work in a pull request"

3. **Monitor Background Agent Progress**

   - The agent will:
     - Create a new branch
     - Implement the requested changes
     - Create a pull request
   - You'll receive a notification when complete

4. **Spin Up Multiple Background Tasks**

   - Start another chat window
   - Delegate a different task
   - Observe multiple agents working simultaneously
   - Note: This overcomes the single-threaded limitation of interactive Copilot

5. **Review Agent Results**
   - When notified, review the pull request
   - Check the implemented code
   - Review the commit history
   - Merge or request changes as needed

### Expected Outcomes

- Understanding of background agent capabilities
- Ability to work on multiple tasks concurrently
- Increased productivity through task delegation
- Pull requests ready for review

---

## Lab 6: Exploring Code with MCP Extensions (15 minutes)

### Objective

Use Model Context Protocol (MCP) extensions to interact with external systems.

### Steps

1. **Install Azure DevOps MCP Extension**

   - Open Extensions view in VS Code
   - Search for `@mcp azure devops`
   - Install the Azure DevOps MCP extension
   - Review the extension capabilities:
     - Get work items
     - Create work items
     - List projects
     - Query work items

2. **Explore MCP Tools**

   - In chat, explore what the extension can do
   - Example prompts:
     - `list available Azure DevOps projects`
     - `create a work item for the namespace style issue we found`
     - `get work items assigned to me`

3. **Integrate MCP with Instruction Files**
   - Create a chat mode that uses the MCP extension
   - Example: A chat mode that creates work items from code analysis results

### Expected Outcomes

- Understanding of MCP extensions
- Ability to integrate external tools with Copilot
- Automated workflow between code and project management

---

## Bonus Lab: Code Explanation Pipeline (20 minutes)

### Objective

Create a workflow for understanding and documenting unfamiliar code.

### Steps

1. **Select Complex Code**

   - Find a complex algorithm or method in your codebase
   - Example: A calculation method with multiple conditions

2. **Request Step-by-Step Explanation**

   - Select the code
   - Press `Ctrl+I`
   - Enter: `explain this code step by step`
   - Review the detailed explanation

3. **Generate Sequence Diagram**

   - Follow up with: `create a sequence diagram for this code`
   - Review the Mermaid sequence diagram
   - Preview to see the visualization

4. **Add Documentation Comments**

   - Follow up with: `add concise comments to the code based on the explanation`
   - Review and accept the documentation
   - Balance between helpful comments and over-commenting

5. **Create Knowledge Base Entry**
   - Follow up with:
     ```
     Create a knowledge base entry in the documentation
     folder explaining this algorithm
     ```
   - Review the generated documentation file

### Expected Outcomes

- Deep understanding of complex code
- Visual representations of code flow
- Well-documented code
- Reusable knowledge base entries

---

## Challenge Exercises

### Challenge 1: Evergreen Documentation Workflow

Create a prompt file that can be run as part of a CI/CD pipeline to automatically update project documentation on every commit.

**Requirements:**

- Updates README.md with current project state
- Regenerates architecture diagrams
- Updates API documentation
- Creates a summary of recent changes

### Challenge 2: Custom Instruction File Set

Create a custom set of instruction files for your team's specific needs, including:

- Language-specific guidelines
- Framework-specific patterns
- Team coding standards
- Security requirements
- Performance guidelines

### Challenge 3: Automated Code Quality Enforcement

Create a workflow that:

1. Generates instruction files from existing code
2. Evaluates all code files against instructions
3. Creates work items for violations
4. Delegates fixes to background agents
5. Creates pull requests for review

---

## Key Takeaways

1. **Documentation Automation**: Copilot can generate comprehensive documentation, including XML comments, README files, and Mermaid diagrams

2. **Migration Planning**: AI can analyze breaking changes and create detailed migration plans with effort estimates

3. **Instruction Files**: Use instruction files to maintain coding standards and guide AI behavior consistently across projects

4. **Background Agents**: Delegate tasks to background agents for parallel processing and autonomous implementation

5. **Code Evaluation**: Automatically evaluate code against standards and generate actionable improvement tasks

6. **MCP Extensions**: Extend Copilot capabilities with external integrations like Azure DevOps

7. **Evergreen Maintenance**: Use AI to keep documentation and code quality current with minimal manual effort

---

## Additional Resources

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [Mermaid Diagram Syntax](https://mermaid.js.org/)
- [MCP Extensions](https://code.visualstudio.com/docs/copilot/copilot-extensibility)
- [.NET Migration Guide](https://learn.microsoft.com/en-us/dotnet/core/porting/)

---

## Notes for Instructors

- Ensure participants have appropriate Copilot licenses
- Background agent feature may not be available to all users
- Emphasize the importance of reviewing AI-generated content
- Encourage participants to customize instruction files for their teams
- Discuss the balance between automation and human oversight
- Address concerns about technical debt and code quality
