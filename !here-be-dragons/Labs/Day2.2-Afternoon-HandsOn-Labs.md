# Day 2 Afternoon - Hands-On Labs

## AI-Assisted Software Development Course

---

## Lab Overview

These hands-on labs correspond to the Day 2 Afternoon session covering:

- Creating and using instruction files
- AI-assisted output logging and chat transcripts
- Code comparison and evaluation
- Multi-model implementation comparison
- Evergreen software development practices

---

## Lab 1: Creating Technology-Specific Instruction Files

**Objective**: Learn to create instruction files for your project's technology stack

**Duration**: 20 minutes

### Tasks:

1. **Analyze Your Project**
   - Open a project in VS Code
   - Identify the technologies used (e.g., C#, Python, React, etc.)

2. **Generate Instruction Files**

   ```
   Create instruction files for the technology in this project
   ```

   - Observe how GitHub Copilot identifies technologies
   - Review the generated instruction files

3. **Examine the Structure**
   - Note the `applyTo` clause in each file
   - Understand how path-based filtering works
   - Review the content and rules in each file

4. **Customize the Instructions**
   - Modify at least one instruction file to match your team's coding standards
   - Change indentation preferences (e.g., 2 spaces vs 4 spaces)
   - Add specific naming conventions for your organization

5. **Verify the Application**
   ```
   Show me the instruction files that are in scope for this workspace
   ```

**Deliverable**: A set of customized instruction files in `.github/instructions/` folder

---

## Lab 2: Implementing AI-Assisted Output Logging

**Objective**: Set up automated logging of AI interactions for audit and resume capabilities

**Duration**: 25 minutes

### Tasks:

1. **Create the Instruction Files**
   - Copy the `copilot-instructions.md` from the course repository
   - Copy the `ai-assisted-output.instructions.md` file
   - Place both in your `.github/instructions/` folder

2. **Test the Logging**
   - Start a new chat in GitHub Copilot
   - Ask it to perform a multi-step task (e.g., "Create a new class with tests")
   - Look for the generated log files in the `ai-logs/` folder

3. **Review the Generated Files**
   - Examine the conversation log structure
   - Review the summary file
   - Check the front matter metadata

4. **Test the Resume Feature**
   - Start a new chat
   - Attach the summary file
   - Try continuing from where you left off

5. **Experiment with Different Models**
   - Note: The model name in the log may not be accurate
   - Consider whether this limitation affects your usage

**Deliverable**: Working AI log structure with at least one complete conversation log

---

## Lab 3: Code Comparison Across Models

**Objective**: Compare implementations from different AI models to understand their strengths

**Duration**: 30 minutes

### Tasks:

1. **Setup**
   - Create a new branch called `main` or use existing
   - Identify a bug or feature to implement

2. **Implementation with First Model**

   ```
   Fix [describe bug] and create a branch for this fix.
   Run tests, commit, and push the changes.
   ```

   - Use Claude Sonnet (or your preferred model)
   - Note the branch name created

3. **Switch Models and Repeat**
   - Return to main branch
   - Clear your chat context (start new chat)
   - Switch to a different model (e.g., GPT-4, Gemini)
   - Run the same prompt
   - Note the new branch name

4. **Compare the Implementations**

   ```
   Compare the implementations of [bug fix] on branch [branch1]
   created by Claude Sonnet and branch [branch2] created by
   GPT-4. Report the pros and cons of each approach.
   ```

   - Use a third model (e.g., Gemini) to evaluate
   - Review the analysis

5. **Experiment with Bias**
   - Try using the model that created one solution to evaluate both
   - Compare results with the third-party evaluation
   - Discuss: Does the model favor its own solution?

**Deliverable**: Two branches with different implementations and a comparison report

---

## Lab 4: Validating Code Against Instruction Files

**Objective**: Use instruction files to ensure code quality and compliance

**Duration**: 25 minutes

### Tasks:

1. **Create Instruction Files** (if not done already)
   - Generate instruction files for your project
   - Ensure they include coding standards, naming conventions, etc.

2. **Compare Code to Instructions**

   ```
   Compare the code base with the instruction files in the
   .github/instructions folder and report where the code is
   not compliant.
   ```

3. **Review the Findings**
   - Examine the list of non-compliant code
   - Categorize issues (naming, formatting, structure, etc.)

4. **Create Issues for Findings**

   ```
   Is this code Evergreen? Create issues for what you find.
   ```

   - Review the generated issue files
   - Customize the issue template if needed

5. **Test in PR Workflow**
   - Discuss how this could be integrated into PR reviews
   - Consider automation possibilities
   - Brainstorm quality gates

**Deliverable**: A report of code compliance issues and a set of generated issue files

---

## Lab 5: Creating a Prompt File Library

**Objective**: Build reusable prompt files for common development tasks

**Duration**: 20 minutes

### Tasks:

1. **Identify Common Tasks**
   - List 3-5 tasks you perform regularly (e.g., code reviews, testing, documentation)

2. **Create Your First Prompt File**

   ```
   Create a prompt file that generates an instruction file
   for the technology in a project
   ```

   - Save in `.github/copilot/Promptfiles/` folder
   - Review the structure and front matter

3. **Create Additional Prompts**
   - Code review prompt
   - Test generation prompt
   - Documentation generation prompt

4. **Test the Prompts**
   - Run at least two of your prompt files
   - Evaluate the quality of output
   - Refine as needed

5. **Share and Reuse**
   - Consider which prompts could be shared across projects
   - Plan how to maintain a prompt library

**Deliverable**: At least 3 working prompt files in `.github/copilot/Promptfiles/` folder

---

## Lab 6: Implementing Evergreen Software Practices

**Objective**: Apply Evergreen principles using instruction files

**Duration**: 25 minutes

### Tasks:

1. **Create Evergreen Instruction File**

   ```
   Create an instruction file for Evergreen software development
   that applies to all files in this project
   ```

2. **Define Your Standards**
   - Review the generated file
   - Customize with your team's definition of "Evergreen"
   - Include principles like:
     - Maintainability
     - Documentation requirements
     - Test coverage expectations
     - Code clarity standards

3. **Evaluate Existing Code**

   ```
   Is this code Evergreen?
   ```

   - Run against your entire codebase
   - Review the verdict (Yes/No/Partial)

4. **Get Detailed Analysis**

   ```
   Tell me in detail why this code is or isn't Evergreen
   ```

   - Review specific recommendations
   - Prioritize improvements

5. **Create an Improvement Plan**
   - Generate issues for Evergreen violations
   - Categorize by priority
   - Create a roadmap for improvements

**Deliverable**: Evergreen instruction file and assessment report with action items

---

## Lab 7: Advanced - Bug Detection and Issue Creation

**Objective**: Use AI to proactively find and document bugs

**Duration**: 30 minutes

### Tasks:

1. **Define Bug Criteria**

   ```
   What do you consider a bug in code?
   ```

   - Review the AI's definition
   - Customize if needed for your context

2. **Scan for Bugs**

   ```
   Review the code base for bugs and create issues for your findings
   ```

3. **Review Generated Issues**
   - Check the issues folder
   - Evaluate each issue for validity
   - Note false positives
   - Identify genuinely useful findings

4. **Customize Issue Template**
   - Modify the issue format if needed
   - Add sections like:
     - Impact assessment
     - Suggested priority
     - Related files

5. **Integration with Work Management**
   - Research MCP tools for Azure DevOps or Jira
   - Plan how to automatically create work items
   - Consider a review workflow before auto-creation

**Deliverable**: Set of bug issues and a workflow plan for issue management

---

## Lab 8: Multi-Model Workflow Automation

**Objective**: Create an automated workflow that uses multiple models

**Duration**: 35 minutes

### Tasks:

1. **Design the Workflow**

   ```
   Plan a workflow that:
   - Uses Model A to implement a feature
   - Uses Model B to implement the same feature
   - Uses Model C to compare and recommend
   ```

2. **Create a Chat Mode or Prompt**
   - Document the workflow steps
   - Create a prompt that executes all steps
   - Include branch naming conventions

3. **Test the Workflow**
   - Pick a simple feature or bug fix
   - Run the complete workflow
   - Time the execution

4. **Evaluate the Results**
   - Did both models solve the problem?
   - Was the comparison helpful?
   - What would you change?

5. **Document Best Practices**
   - When to use this approach vs single model
   - Which models work best in which roles
   - Cost considerations

**Deliverable**: A documented multi-model workflow with test results

---

## Bonus Lab: Instruction File for Instruction Files

**Objective**: Create meta-instructions for generating instruction files

**Duration**: 15 minutes

### Tasks:

1. **Create the Meta-Instruction**

   ```
   Create an instruction file that provides guidelines for
   creating other instruction files. It should apply only to
   files named *.instructions.md
   ```

2. **Test the Meta-Instruction**
   - Create a new instruction file using the meta-instruction
   - Verify it follows the template

3. **Refine the Template**
   - Add sections for:
     - Required front matter
     - Recommended structure
     - Examples
     - Quality checklist

4. **Share Across Projects**
   - Consider placing in a shared repository
   - Document how to import across projects

**Deliverable**: A meta-instruction file for creating consistent instruction files

---

## Lab Submission Checklist

For each lab, ensure you have:

- [ ] Completed all tasks
- [ ] Created required deliverables
- [ ] Documented any issues or observations
- [ ] Tested the functionality
- [ ] Committed files to your repository

---

## Discussion Questions

After completing the labs, consider:

1. **Instruction Files**
   - How specific should instruction files be?
   - When is an instruction file too detailed?
   - How do you maintain instruction files as projects evolve?

2. **AI Logging**
   - What are the security implications of logging AI conversations?
   - How long should logs be retained?
   - Who should have access to logs?

3. **Model Comparison**
   - Is it worth the extra time/cost to compare implementations?
   - When would you use this approach?
   - How do you avoid bias in evaluations?

4. **Code Quality**
   - Can AI truly enforce "Evergreen" principles?
   - Should AI automatically reject PRs?
   - How much human oversight is needed?

5. **Regulated Industries**
   - How do these practices apply in FDA-regulated development?
   - What additional controls might be needed?
   - How do you document AI-assisted development for audits?

---

## Additional Resources

- Course repository with example instruction files
- GitHub Copilot documentation on instruction files
- Best practices for prompt engineering
- Model comparison frameworks
- Evergreen software principles

---

## Next Steps

After completing these labs:

1. Implement instruction files in your production projects
2. Establish team standards for AI-assisted development
3. Create a library of reusable prompts and instructions
4. Develop guidelines for when to use multi-model approaches
5. Plan integration with your CI/CD pipeline

---

**Remember**: The goal is not to replace developers but to amplify their capabilities and ensure consistent, high-quality code across your organization.
