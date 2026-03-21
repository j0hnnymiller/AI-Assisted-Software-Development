---
marp: true
theme: default
paginate: true
---

## Greenfield Development

Creating Custom Chat Modes for Greenfield development
Chat Mode Command Prompts
Core Instruction Files

---

## What Copilot Looks For

Artifact Type | Required Location | Required Format | Notes
--- | --- | --- | ---
Org guardrails | Org settings | UI-managed | Always included
Repo guardrails | .github/instructions/ | .md | Always included
Path-scoped guardrails | Any folder | copilot-instructions.md | Applies to subtree
Agents (formerly chat modes) | .github/copilot/chat_modes/ | .json or .yaml | Folder name has NOT changed
Promptfiles | .github/copilot/promptfiles/ | .md | Only when invoked

::: notes
Even though “chat modes” are being renamed to “agents,” the folder name remains .github/copilot/chat_modes/ for now.
:::

---

## What’s Changing and What Isn’t

Changing:
Terminology in UI and documentation
Conceptual framing (agents = more powerful, structured roles)
Schema will expand over time
Not changing (yet):
Folder name: .github/copilot/chat_modes/
File discovery rules
Filename requirements
Promptfile behavior
Instruction stack mechanics

::: notes
Teams can safely start using the term “agent” in training and inside the file’s name: field, but must keep the existing folder structure.
:::

---

## Order of Precedence

Organization‑level instruction files
Chat mode file
Repository‑level instruction files
Workspace‑level instruction files
Prompt file (only when invoked)
User message

---

## What Are Custom Agents?

Custom agents are specialized AI assistants with:
Tailored expertise for specific development tasks
Configurable tools and capabilities
Custom instructions defining behavior
Reusable profiles across projects
Available in multiple environments (GitHub.com, VS Code, JetBrains, Eclipse, Xcode)

::: notes
Timing: 2-3 minutes

Key Points to Emphasize:

Custom agents are NOT separate AI models - they’re specialized configurations of GitHub Copilot

Think of them as “personas” or “roles” for your AI assistant

They’re defined in simple markdown files with YAML frontmatter

Examples to Share:

Testing specialist that focuses only on test code

Documentation writer that creates comprehensive docs

Implementation planner that designs before coding

Security reviewer that checks for vulnerabilities

Audience Interaction: “Has anyone worked with AI assistants that seemed too generic or gave responses outside their intended scope? Custom agents solve this problem.”

Transition: “Now let’s see where and how you can create these custom agents.”
:::

---

## Where to Create Custom Agents

GitHub.com
Navigate to github.com/copilot/agents
Available at repository, organization, or enterprise level
Template-based creation process
IDEs
VS Code: Configure Custom Agents menu
JetBrains: Configure Agents settings
Eclipse: Add custom agents dialog
Xcode: Create agent from dropdown

::: notes
Timing: 3 minutes

Delivery Instructions:

Show the GitHub.com interface if doing a live demo

Emphasize that agents created on GitHub can be used across all environments

IDE-based agents are more convenient for quick personal use

Key Decision Point: Help audience understand when to use each approach:

GitHub: For team-wide or shared agents

Organization/Enterprise: For standardized agents across multiple repos

IDE: For personal experimentation and workspace-specific agents

Technical Detail:

GitHub agents go in .github/agents/ directory

Organization/enterprise agents go in root agents/ directory of .github-private repo

IDE user profile agents are local to that machine

Common Question: “Can I use the same agent in both GitHub and my IDE?” Answer: Yes! Agents created on GitHub are automatically available in supported IDEs.

Transition: “Let’s walk through creating an agent on GitHub, which is the most common workflow.”
:::

---

## Creating on GitHub: Step-by-Step

Go to github.com/copilot/agents
Select repository (or .github-private for org/enterprise)
Click Copilot icon → Create an agent
Creates template: my-agent.agent.md in .github/agents/
Rename file with descriptive name (e.g., test-specialist.agent.md)
Configure agent profile (next slide)
Commit to default branch
Agent appears in dropdown immediately

::: notes
Timing: 4-5 minutes (include live demo if possible)

Step-by-Step Walkthrough:

Step 1-2: Emphasize the importance of selecting the right repository

Personal repo = just for you

Organization repo = for entire org

.github-private = special repository for org/enterprise-wide agents

Step 3-4: The template is your starting point

Don’t skip past it - it contains all required sections

Template includes helpful comments

Step 5: Filename guidelines (critical!)

Use lowercase letters, numbers, dots, dashes, underscores only

Must end with .agent.md

Filename becomes the default agent name

Examples: test-specialist.agent.md, security-reviewer.agent.md, doc-writer.agent.md

Step 6: We’ll cover configuration in detail on next slides

Step 7-8: No build process or waiting

Immediate availability after merge

Refresh the page if you don’t see it

Common Pitfalls:

Forgetting to merge to default branch (agent won’t appear)

Using spaces or special characters in filename

Not providing a description in the YAML

Demo Tip: If showing live, create a simple agent like “hello-world.agent.md” to demonstrate the process.

Transition: “Now that we know how to create the file, let’s understand what goes inside it.”
:::

---

## Creating in VS Code

Open GitHub Copilot Chat
Agents dropdown → Configure Custom Agents…
Click Create new custom agent
Choose location:
  - Workspace: .github/agents/ (project-specific)
  - User profile: Personal agents (all workspaces)
Enter filename
Configure in .agent.md file
Use Configure Tools… button for tool selection
Set model: property for AI model preference

::: notes
Timing: 3-4 minutes

VS Code Advantages:

Integrated tool configuration UI

Immediate testing in the same environment

Better for rapid iteration and experimentation

User profile agents for personal productivity

Workspace vs User Profile Decision:

Workspace (.github/agents/):

Shared with team when committed

Project-specific context

Version controlled

Recommended for team agents

User Profile:

Available across all your projects

Not version controlled

Personal productivity tools

Examples: personal note-taking agent, time tracker

Configure Tools Button:

Opens visual dialog showing all available tools

Includes built-in tools (read, edit, search, etc.)

Shows MCP server tools if configured

Click OK to add selected tools to YAML

Model Property:

Override default model per agent

Useful for cost/performance tradeoffs

Example: Use faster model for simple tasks, advanced model for complex reasoning

Live Demo Suggestion: Show the Configure Tools dialog and model dropdown

Common Questions:

“Do I need to restart VS Code?” - No, agents are detected automatically

“Can I edit the YAML directly?” - Yes, the UI is just a helper

Transition: “The process is similar in JetBrains, Eclipse, and Xcode with slight UI variations. Now let’s focus on what matters most: the agent configuration itself.”
:::

---

## Agent Profile Structure

- --name: test-specialistdescription: Focuses on test coverage and qualitytools: ["read", "edit", "search"]model: gpt-4target: vscode # optional: vscode or github-copilot---You are a testing specialist...[Detailed instructions and behavior]
Key Components:
YAML frontmatter: Metadata and configuration
Markdown content: Instructions and behavior (max 30,000 chars)

::: notes
Timing: 4-5 minutes

Anatomy of an Agent Profile:

YAML Frontmatter (Required):

name (optional): Display name in dropdown

Defaults to filename without extension

Keep concise (2-4 words)

Examples: “Test Specialist”, “Security Reviewer”

description (REQUIRED): What the agent does

Must be clear and specific

Explains capabilities and domain

Appears in agent selection UI

1-2 sentence summary

tools (optional): Which tools agent can use

Omit to enable ALL tools

List specific tools to restrict access

Format: ["tool1", "tool2", "mcp-server/tool3"]

Common tools: read, edit, search, run, debug

model (IDE only): Which AI model to use

Only works in VS Code, JetBrains, Eclipse, Xcode

Examples: “gpt-4”, “gpt-3.5-turbo”, “claude-3-opus”

Ignored on GitHub.com

target (optional): Environment restriction

“vscode” = only in IDEs

“github-copilot” = only on GitHub.com

Omit = works everywhere

mcp-servers (org/enterprise only): Configure MCP servers for this agent

Markdown Content (The Agent’s “Brain”):

Define personality and expertise

Set boundaries and constraints

Provide examples of good behavior

Specify output formats

Maximum 30,000 characters (plenty of space!)

Best Practices:

Be specific about what the agent should AND shouldn’t do

Include examples of desired behavior

Mention file patterns or naming conventions

Specify testing/validation requirements

Transition: “Let’s see what these instructions look like in real agent examples.”
:::

---

## Example 1: Testing Specialist

- --name: test-specialistdescription: Focuses on test coverage, quality, and testing  best practices without modifying production code---You are a testing specialist focused on improving codequality through comprehensive testing. Your responsibilities:- Analyze existing tests and identify coverage gaps- Write unit tests, integration tests, and end-to-end tests- Review test quality and suggest improvements- Ensure tests are isolated, deterministic, and documented- Focus only on test files - avoid modifying production codeAlways include clear test descriptions and use appropriatetesting patterns for the language and framework.

::: notes
Timing: 3-4 minutes

Why This Example Works:

Clear Scope Definition:

“Focuses on test coverage” - tells user what it does

“Without modifying production code” - tells user what it WON’T do

Sets clear boundaries to prevent scope creep

Specific Responsibilities:

“Analyze existing tests” - audit capability

“Write unit/integration/e2e tests” - creation capability

“Review test quality” - critique capability

“Ensure tests are isolated” - quality standards

“Focus only on test files” - reinforces boundary

Behavioral Constraints:

“Focus only on test files” - prevents the agent from refactoring production code

“Avoid modifying production code unless specifically requested” - allows override when needed

Quality Standards:

“Isolated” - no shared state between tests

“Deterministic” - same input = same output

“Well-documented” - clear descriptions and comments

Pattern Recognition:

“Use appropriate testing patterns for the language and framework”

Agent will adapt to Jest, pytest, JUnit, etc.

Usage Scenarios:

Adding tests to legacy code

Improving test coverage metrics

Reviewing PR test quality

Learning testing best practices

Customization Ideas:

Add specific test frameworks to use

Include code coverage thresholds

Specify test naming conventions

Add mutation testing requirements

Common Question: “Why not enable all tools?” Answer: Not specified here, so all tools are available. But you might restrict to [“read”, “edit”] to prevent running or deploying.

Transition: “Here’s another example that shows a different use case - planning instead of coding.”
:::

---

## Example 2: Implementation Planner

- --name: implementation-plannerdescription: Creates detailed implementation plans and  technical specifications in markdown formattools: ["read", "search", "edit"]---You are a technical planning specialist. Your responsibilities:- Analyze requirements and break them into actionable tasks- Create detailed technical specs and architecture docs- Generate implementation plans with steps and dependencies- Document API designs, data models, and system interactions- Create markdown files that development teams can followAlways structure plans with clear headings, task breakdowns,and acceptance criteria. Include considerations for testing,deployment, and risks. Focus on thorough documentationrather than implementing code.

::: notes
Timing: 3-4 minutes

Strategic Difference from Test Specialist:

Tools Restriction:

Only ["read", "search", "edit"] enabled

NOT “run” or “debug” - this agent doesn’t execute code

NOT “shell” - doesn’t deploy or build

Enforces its role as a planner, not implementer

Planning-Specific Responsibilities:

“Analyze requirements” - requirements engineering

“Break them into actionable tasks” - work breakdown

“Technical specs and architecture docs” - documentation focus

“Implementation plans with dependencies” - sequencing and scheduling

“API designs, data models” - interface definition

Output Format:

“Markdown format” - specified in description

“Markdown files that development teams can follow” - artifact focus

“Clear headings, task breakdowns” - structure requirements

Non-Code Focus:

“Focus on thorough documentation rather than implementing code”

Critical boundary: this agent designs but doesn’t build

Prevents mixing planning and implementation concerns

When to Use This Agent:

Starting new features or projects

Architectural decision records (ADRs)

Epic and story breakdown

Technical RFCs

Onboarding documentation

Migration plans

Output Examples:

IMPLEMENTATION_PLAN.md with tasks and timeline

ARCHITECTURE.md with system design

API_SPEC.md with endpoint definitions

DATA_MODEL.md with schema definitions

Team Benefits:

Consistent planning documentation format

Separation of planning from coding

Better task estimation

Clear acceptance criteria

Risk identification upfront

Customization Ideas:

Add specific template sections

Include estimation guidance

Specify diagram types (C4, sequence, etc.)

Add stakeholder communication sections

Comparison to Test Specialist:

Test Specialist: All tools, focused on test files

Implementation Planner: Limited tools, focused on documentation

Transition: “These examples show two very different agent types. Now let’s learn how to actually use custom agents once they’re created.”
:::

---

## Using Custom Agents

On GitHub.com
Agents panel/tab dropdown → Select your custom agent
Assign custom agent to issues
Noted in PR descriptions when used
In IDEs
Chat window dropdown → Select agent
Switch agents mid-conversation
Access specialized configurations per task
GitHub Copilot CLI
/agent command to select agent
Reference agent in prompts
Command-line argument support

::: notes
Timing: 4-5 minutes

GitHub.com Usage:

Agents Panel Workflow:

Open Copilot agents panel or tab

Click dropdown (currently shows “Coding Agent”)

Select your custom agent from list

Enter your prompt or task

Agent works within its configured scope

Issue Assignment:

Assign Copilot to an issue

Choose custom agent from dropdown

Agent follows its specialized instructions

Great for repetitive tasks (bug triage, documentation updates)

PR Tracking:

When Copilot creates a PR, it notes which agent was used

Helps with attribution and understanding the approach

Example: “This PR was created by @copilot using the test-specialist agent”

IDE Usage Benefits:

Mid-Conversation Switching:

Start with planning agent

Switch to implementation agent

Switch to review agent

Maintain conversation context

Task-Specific Workflows:

Use planning agent for architecture decisions

Use coding agent for implementation

Use test agent for test coverage

Use security agent for vulnerability review

Use doc agent for documentation

Example IDE Workflow:

User: "I need to add user authentication"
[Select implementation-planner agent]
Agent: Creates detailed plan with tasks

User: "Now implement the first task"
[Switch to coding agent]
Agent: Implements based on plan

User: "Add tests for this"
[Switch to test-specialist agent]
Agent: Creates comprehensive test suite

CLI Usage (Advanced):

Basic Agent Selection:

gh copilot /agent test-specialist "add tests for authentication"

In Prompts:

gh copilot "using security-reviewer, check this PR for vulnerabilities"

Via Arguments:

gh copilot --agent=doc-writer "document the API endpoints"

Best Practices:

Choose the Right Agent:

Match agent expertise to task

Don’t use generic agent when specialized one exists

Provide Context:

Custom agents still need context

Reference files, requirements, constraints

Iterate:

Refine agent instructions based on results

Agents improve as you tune them

Document Usage:

Tell team which agents to use for which tasks

Include in CONTRIBUTING.md or team wiki

Common Scenarios:

Code Review: Use review agent on PRs

Legacy Refactoring: Use planning agent first, then coding agent

Documentation Sprint: Use doc agent across multiple files

Security Audit: Use security agent on entire codebase

Test Coverage Drive: Use test agent to fill coverage gaps

Transition: “Let’s wrap up with some best practices and resources to help you get started.”
:::

---

## Best Practices

Start Simple: Create one agent for a specific pain point
Be Specific: Define clear boundaries and responsibilities
Restrict Tools: Only enable tools the agent needs
Iterate: Refine instructions based on real usage
Share: Create org/enterprise agents for common tasks
Document: Include usage examples in agent description
Test: Validate agent behavior before team rollout

::: notes
Timing: 4 minutes

Detailed Best Practices:

1. Start Simple:

Don’t try to create every agent at once

Identify ONE repetitive task that’s painful

Create an agent for that specific task

Validate it works before creating more

Example: If code reviews always miss test coverage, start with test-specialist

2. Be Specific:

Vague: “Help with coding”

Specific: “Write unit tests following Jest conventions for React components”

Include examples of good behavior

Specify what NOT to do

Bad example: “Be helpful”

Good example: “Focus only on test files in tests directories. Never modify source files in src/ directory.”

3. Restrict Tools:

More tools ≠ better agent

Restrict to enforce boundaries

Planning agent doesn’t need “run” tool

Doc agent doesn’t need “debug” tool

Security agent might only need “read” and “search”

Benefits:

Faster execution (fewer options to consider)

Clear scope (can’t do things outside role)

Safer (can’t accidentally deploy or delete)

4. Iterate:

Agents aren’t “write once and forget”

Monitor what they produce

Collect feedback from team

Refine instructions based on real usage

Example iteration:

V1: “Write tests”

V2: “Write tests with descriptive names”

V3: “Write tests with descriptive names following pattern: describe-context-behavior”

V4: Add specific Jest matchers to prefer

5. Share:

Don’t create duplicate agents across repos

Use organization-level agents for standards

Examples:

Code style checker (enforces org conventions)

Security reviewer (org security policies)

Doc generator (org documentation standards)

Benefits:

Consistency across projects

Single place to maintain

Easier onboarding

6. Document:

Good description is crucial

Include examples in the agent markdown

Add usage instructions

Example:

## Usage Examples

❌ Bad: "Fix the tests"
✅ Good: "Add unit tests for the UserService class covering success and error cases"

❌ Bad: "Make it better"
✅ Good: "Increase test coverage for auth module to 80%"

7. Test:

Try agent on sample tasks before team rollout

Test edge cases

Verify it respects boundaries

Check tool usage is appropriate

Get feedback from 2-3 team members first

Make it easy to rollback (version control!)

Anti-Patterns to Avoid:

Too Generic: “Help with everything” - defeats the purpose

Too Narrow: “Only fix typos in README” - waste of an agent

No Constraints: All tools enabled, no guidelines - unpredictable

Copy-Paste: Duplicating built-in agents - adds confusion

Set and Forget: Never updating based on experience

No Testing: Rolling out to team without validation

Success Metrics:

Time saved on repetitive tasks

Consistency in output quality

Reduction in review comments for that area

Team adoption rate

Positive feedback from users

Transition: “You now have everything you need to create your first custom agent. Here are resources to dive deeper.”
:::

---

## Greenfield Chat Modes

Product Manager
Solution Architect
Senior Developer
Technical Writer
Security Reviewer
DevOps Engineer
DevTest Engineer
SRE (Site Reliability Engineer)

::: notes
This presentation covers 8 critical roles in modern software development. Each persona has unique needs when working with GitHub Copilot Chat. We’ll explore both the skills needed and responsibilities required. Focus on practical, actionable guidance for each role. Tables format allows easy comparison between skills and responsibilities.
:::

---

## Product Manager

Skills | Responsibilities
--- | ---
Requirements Translation - Convert business needs into precise technical prompts | Requirement Validation - Ensure AI-generated requirements align with business objectives
Context Management - Maintain conversation threads for complex feature discussions | Quality Assurance - Review AI outputs for accuracy, completeness, and feasibility
Documentation Review - Evaluate AI-generated specs, user stories, and technical docs | Cross-functional Alignment - Coordinate AI-assisted planning across development teams
Stakeholder Communication - Present AI-assisted analysis to technical and business teams | Risk Assessment - Identify potential issues in AI-suggested technical approaches
Iterative Refinement - Guide AI through multiple rounds of requirement clarification | Delivery Tracking - Use AI insights to monitor progress and adjust roadmaps accordingly

::: notes
Product Managers are the bridge between business and technical teams. Their success with AI depends on clear requirement translation. Key challenge: ensuring AI outputs align with business objectives. Focus on iterative refinement - rarely get perfect results on first try. Context management is crucial for complex feature discussions. Always validate AI-generated requirements against business goals.
:::

---

## Solution Architect

Skills | Responsibilities
--- | ---
Architecture Prompting - Frame complex system design questions for optimal AI responses | Design Validation - Verify AI-generated architectural decisions against enterprise standards
Pattern Recognition - Identify and validate AI-suggested architectural patterns and anti-patterns | Technical Governance - Ensure AI-assisted designs follow organizational guidelines
Technology Evaluation - Assess AI recommendations for technology stack decisions | Risk Mitigation - Evaluate AI suggestions for security, performance, and maintainability risks
Scalability Analysis - Guide AI through performance and scalability considerations | Knowledge Sharing - Document and communicate AI-derived architectural insights
Integration Planning - Use AI to model system interactions and API designs | Standards Compliance - Maintain adherence to coding standards and architectural principles

::: notes
Solution Architects work at the highest technical abstraction level. Pattern recognition is critical - AI often suggests common patterns. Must validate AI architectural decisions against enterprise standards. Integration planning is complex - AI can help model system interactions. Risk mitigation is a key responsibility - evaluate long-term implications. Knowledge sharing ensures AI insights benefit the broader organization.
:::

---

## Senior Developer

Skills | Responsibilities
--- | ---
Code Generation Prompting - Craft precise requests for complex code implementations | Code Quality Assurance - Validate AI-generated code for correctness, efficiency, and maintainability
Debug Assistance - Effectively use AI for troubleshooting and error resolution | Security Review - Ensure AI-suggested code follows security best practices
Code Review with AI - Combine human experience with AI analysis for thorough reviews | Performance Optimization - Analyze AI recommendations for potential performance impacts
Refactoring Guidance - Leverage AI for code improvement and optimization suggestions | Mentorship Integration - Guide junior developers in effective AI-assisted development
Testing Strategy - Use AI to generate comprehensive test cases and scenarios | Technical Debt Management - Use AI insights to identify and prioritize technical debt reduction

::: notes
Senior Developers are power users of AI coding assistance. Code generation prompting requires precise, specific requests. Debug assistance can dramatically speed troubleshooting. Code review with AI combines human insight with AI analysis. Security review is critical - AI may suggest vulnerable patterns. Mentorship integration helps junior developers use AI effectively. Performance optimization requires evaluating AI suggestions carefully.
:::

---

## Technical Writer

Skills | Responsibilities
--- | ---
Content Structuring - Guide AI to create well-organized, logical documentation flow | Content Accuracy - Ensure all AI-generated documentation is technically correct and current
Audience Adaptation - Adjust AI outputs for different technical skill levels and roles | Editorial Standards - Maintain quality, clarity, and consistency in AI-assisted content
Style Consistency - Maintain organizational voice and formatting standards in AI content | User Experience - Optimize AI-generated docs for end-user comprehension and usability
Technical Verification - Validate AI-generated technical content for accuracy | Version Control - Manage documentation updates and revisions with AI assistance
Multi-format Publishing - Convert AI outputs across various documentation formats | Cross-team Collaboration - Coordinate with SMEs to validate and enhance AI-generated content

::: notes
Technical Writers can leverage AI for content creation and organization. Content structuring helps AI create logical, well-organized documentation. Audience adaptation is key - same content needs different presentations. Style consistency maintains organizational voice across AI-generated content. Technical verification ensures accuracy - AI can hallucinate technical details. Multi-format publishing expands content reach and usability. Editorial standards maintain quality and consistency.
:::

---

## Security Reviewer

Skills | Responsibilities
--- | ---
Threat Modeling - Use AI to identify potential security vulnerabilities and attack vectors | Vulnerability Assessment - Validate AI-identified security issues and remediation strategies
Compliance Analysis - Leverage AI for regulatory and standards compliance checking | Code Security Review - Ensure AI-suggested code changes don’t introduce security risks
Risk Assessment - Guide AI through security impact analysis and risk prioritization | Policy Enforcement - Verify AI recommendations align with organizational security policies
Security Testing - Generate security test cases and penetration testing scenarios | Audit Trail Maintenance - Document security decisions and rationale for AI-assisted reviews
Incident Response - Use AI for security event analysis and response planning | Threat Intelligence - Stay current on security trends that may affect AI recommendation quality

::: notes
Security Reviewers must validate all AI security recommendations. Threat modeling with AI can identify vulnerabilities humans might miss. Compliance analysis leverages AI’s knowledge of regulatory requirements. Risk assessment requires balancing AI suggestions with security expertise. Security testing scenarios can be comprehensive with AI assistance. Policy enforcement ensures AI recommendations align with org standards. Audit trail maintenance is critical for security accountability.
:::

---

## DevOps Engineer

Skills | Responsibilities
--- | ---
Infrastructure as Code - Generate and optimize IaC templates, scripts, and configurations | Pipeline Reliability - Ensure AI-generated CI/CD configurations are stable and efficient
CI/CD Pipeline Design - Use AI for build, test, and deployment pipeline optimization | Security Integration - Validate AI-suggested DevSecOps practices and security controls
Monitoring & Alerting - Create comprehensive observability strategies with AI assistance | Performance Monitoring - Implement AI-recommended monitoring and alerting strategies
Automation Scripting - Generate operational scripts and automation workflows | Cost Management - Review AI suggestions for infrastructure cost optimization
Cloud Resource Optimization - Leverage AI for cost optimization and resource management | Disaster Recovery - Develop and test AI-assisted backup and recovery procedures

::: notes
DevOps Engineers can accelerate infrastructure automation with AI. Infrastructure as Code generation can speed deployment and configuration. CI/CD pipeline design benefits from AI optimization suggestions. Monitoring and alerting strategies become more comprehensive with AI. Automation scripting reduces manual operational overhead. Pipeline reliability must be validated - AI-generated configs need testing. Cost management is crucial - review AI suggestions for optimization opportunities.
:::

---

## DevTest Engineer

Skills | Responsibilities
--- | ---
Test Case Generation - Create comprehensive test scenarios across functional and non-functional areas | Test Coverage Validation - Ensure AI-generated tests provide adequate coverage
Test Data Management - Generate realistic test data sets and scenarios | Test Environment Management - Maintain consistent, reliable test environments
Automation Framework - Build robust test automation with AI assistance | Quality Metrics - Track and report on quality metrics derived from AI-assisted testing
Performance Testing - Design load, stress, and performance test strategies | Test Maintenance - Keep AI-generated test suites current with application changes
Defect Analysis - Use AI for root cause analysis and bug reproduction | Bug Triage - Prioritize and categorize defects with AI analysis support

::: notes
DevTest Engineers can dramatically improve test coverage with AI. Test case generation creates comprehensive scenarios across functional areas. Test data management becomes easier with AI-generated realistic datasets. Automation framework development accelerates with AI assistance. Performance testing strategies benefit from AI-designed load scenarios. Test coverage validation ensures AI-generated tests are comprehensive. Quality metrics tracking provides insights into AI-assisted testing effectiveness.
:::

---

## SRE (Site Reliability Engineer)

Skills | Responsibilities
--- | ---
Incident Response - Use AI for rapid incident analysis, diagnosis, and resolution | System Reliability - Maintain service availability using AI-driven monitoring and response
SLA/SLO Monitoring - Generate comprehensive reliability metrics and alerting | Performance Optimization - Continuously improve system performance with AI insights
Capacity Planning - Leverage AI for resource forecasting and scaling decisions | Incident Documentation - Create detailed incident reports and prevention strategies
Post-mortem Analysis - Create thorough incident reviews with AI assistance | Change Management - Assess deployment risks using AI-powered analysis
Reliability Engineering - Design fault-tolerant systems with AI recommendations | On-call Excellence - Optimize on-call procedures and reduce MTTR with AI support

::: notes
SREs can leverage AI for faster incident response and resolution. Incident response benefits from AI’s rapid analysis and diagnosis capabilities. SLA/SLO monitoring becomes more comprehensive with AI-generated metrics. Capacity planning leverages AI for accurate resource forecasting. Post-mortem analysis creates thorough incident reviews with AI assistance. System reliability requires validating AI-driven monitoring recommendations. Performance optimization is continuous with AI insights into system behavior.
:::

---

## Solution Architect Prompts

Prompt File | Description
--- | ---
architecture-design.prompt.md | Comprehensive system architecture designs
pattern-analysis.prompt.md | Architectural pattern analysis and recommendations
technology-evaluation.prompt.md | Technology evaluation and selection
scalability-planning.prompt.md | Scalability and capacity planning
integration-design.prompt.md | System integration and API design
security-architecture.prompt.md | Security controls and threat mitigation
performance-analysis.prompt.md | Performance analysis and bottleneck identification
migration-strategy.prompt.md | System migration and modernization planning
compliance-check.prompt.md | Compliance validation and standards alignment
risk-assessment.prompt.md | Architectural risk assessment and mitigation

::: notes
Prompt: create prompt files for the interactive commands in the #file:solution-architect.chatmode.md. call the prompt files when the interactive commands are triggered

created:

* architecture-design.prompt.md - Comprehensive system architecture designs
* pattern-analysis.prompt.md - Architectural pattern analysis and recommendations
* technology-evaluation.prompt.md - Technology evaluation and selection
* scalability-planning.prompt.md - Scalability and capacity planning
* integration-design.prompt.md - System integration and API design
* security-architecture.prompt.md - Security controls and threat mitigation
* performance-analysis.prompt.md - Performance analysis and bottleneck identification
* migration-strategy.prompt.md - System migration and modernization planning
* compliance-check.prompt.md - Compliance validation and standards alignment
* risk-assessment.prompt.md - Architectural risk assessment and mitigation
:::

---

## If you said: "Design an architecture for a Windows desktop application that manages real-time inventory for a warehouse"

The chatmode would deliver:
Component breakdown (UI for warehouse staff, inventory service, database layer, real-time sync)
Tech stack (WinUI 3 or WPF, .NET 8, SQL Server, SignalR for real-time updates)
Patterns (MVVM for UI, Repository pattern for data, async/await for responsiveness)
Performance angles (connection pooling, efficient queries, UI thread optimization)
Security (role-based access, encrypted communications, audit logging)
Rollout plan (Phase 1: core inventory, Phase 2: real-time sync, Phase 3: analytics)

::: notes
Prompt: when using the solution architect chat mode, explain what happens when I ask it to design a new architecture for windows application
:::

---
