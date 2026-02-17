# AI-Assisted Software Development with GitHub Copilot (Thu Morning)

## Overview

- **Total Duration**: ~1:01:00 (01:01:00)
- **Sections**: 7 major topics
- **Format**: VTT (WebVTT)
- **Instructor**: John Miller
- **Session**: Thursday Morning Session

---

## Section 1: Pre-Class Questions and Setup (Duration: 00:00:24 - 00:08:02)

### Key Topics

- Student questions about getting started with Copilot instruction files
- Discussion of starting from scratch vs. building incrementally
- Clarification on building instruction file skeletons
- Administrative questions about course invoices and documentation

### Main Discussion Points

- **Starting Point Guidance**: John explains that instruction files are built iteratively, starting with basic skeletons and expanding based on needs
- **Greenfield Approach**: Today's session will demonstrate starting from scratch, which addresses the student's question
- **Building Block Approach**: Begin with core instruction files that define how to build other instructions and files
- **Task-Oriented Prompt Files**: Capture recurring tasks into reusable prompt files
- **Progressive Sophistication**: Start simple with instruction files, then add chat modes and personas for higher-level context

---

## Section 2: Copilot Instruction Files and Context Management (Duration: 00:08:02 - 00:17:26)

### Key Topics

- Fine-grained control over instruction file inclusion
- The `appliesTo` clause for file pattern matching
- Hierarchy of instruction loading
- Context window management strategies

### Main Discussion Points

#### AppliesTo Clause

- **File Extension Targeting**: Use `appliesTo` to specify which file types should include specific instructions
  - Example: `appliesTo: "**/*.{ts,js,py}"` for TypeScript, JavaScript, and Python files
  - Instructions auto-include when working in matching file types
  - Instructions are excluded when working in non-matching file types

#### Scope Levels

- **Global**: Apply to all files (`appliesTo: "**/*"`)
- **Directory-Specific**: Apply to specific folder paths
- **Type-Specific**: Apply to specific file extensions
- **Repository-Specific**: Organization-wide instruction files can target specific repositories

#### Control Hierarchy

1. **File Context**: Files being edited determine initial context
2. **Instruction File Matching**: `appliesTo` patterns determine which instruction files are included
3. **Active Chat Mode**: Adds persona and behavioral context
4. **Prompt Files**: Add task-specific instructions when invoked
5. **Manual References**: Explicit `#file` references in prompts

### Important Distinctions

- **Prompt Files**: Execute tasks, don't control instruction inclusion
- **Instruction Files**: Provide guidance and can be auto-included via `appliesTo`
- **Chat Modes**: Define personas and specialized contexts, can include their own instructions but not reference other instruction files

---

## Section 3: Skills Support in GitHub Copilot (Duration: 00:15:30 - 00:16:40)

### Key Topics

- GitHub Copilot now supports skills (as of early month release)
- Skills folder for custom scripts and automation
- Compatibility with skills from other AI coding tools

### Main Discussion Points

- **Skills Folder**: Can create a skills folder to store reusable scripts
- **Cross-Platform Compatibility**: Skills should match standards used in tools like Cloud Code
- **Script Execution**: Skills can potentially run local scripts and pipelines
- **Instructor Note**: John hasn't had extensive time with skills yet, encourages students to explore

---

## Section 4: MCP (Model Context Protocol) Servers (Duration: 00:17:26 - 00:32:00)

### Key Topics

- Introduction to Model Context Protocol (MCP)
- Purpose and architecture of MCP servers
- Available pre-built servers
- Integration with GitHub Copilot

### Main Discussion Points

#### What is MCP?

- **Purpose**: Adds additional capabilities and data sources to GitHub Copilot
- **Standardized Protocol**: Allows tools and services to communicate with Copilot
- **Pre-built Servers**: Many community-built servers available for common integrations

#### Use Cases

- **External Data Access**: Connect Copilot to databases, APIs, and custom data sources
- **Tool Integration**: Integrate with tools like Terraform, Kubernetes, cloud providers
- **Custom Solutions**: Build custom MCP servers for proprietary systems or internal tools

#### Architecture Components

- **Client**: VS Code/GitHub Copilot
- **Server**: MCP server providing capabilities
- **Protocol**: Standardized communication layer
- **Resources**: Data and capabilities exposed by the server
- **Tools**: Functions the server provides to Copilot

#### Available Servers

- **GitHub Repos**: Repository integration
- **Database Systems**: Database connectivity
- **Terraform**: Infrastructure as code
- **Kubernetes**: Container orchestration
- **Cloud Provider APIs**: AWS, Azure, GCP integrations

#### Finding MCP Servers

- **VS Code Extension Gallery**: Search for "MCP" to find available servers
- **Model Context Protocol Website**: modelcontextprotocol.io
- **GitHub Repository**: Community-maintained server collection

#### Installation and Configuration

- Install MCP servers as VS Code extensions
- Enable/configure in Copilot tools settings
- Each enabled server adds to context window token usage
- Current limit: ~128 tokens per enabled server
- Be intentional about which servers to enable

---

## Section 5: Custom Agents (Duration: 00:32:00 - 00:51:00)

### Key Topics

- Specialized AI assistants with custom instructions
- Creating and configuring custom agents
- Agent storage locations
- Tool restrictions and capabilities
- Best practices for agent design

### Main Discussion Points

#### What are Custom Agents?

- **Specialized Assistants**: AI agents configured for specific tasks or domains
- **Custom Instructions**: Provide tailored guidance and behavioral rules
- **Reusable Profiles**: Can be shared across projects and teams
- **Multi-Environment Support**: Work in VS Code, GitHub.com, JetBrains, and other IDEs

#### Recent Changes (January 2025 Release)

- **New Location**: Custom agents now stored in `.github/agents/` folder (repository level)
- **Agent Extension**: Files use `.agent.md` extension
- **Legacy Support**: Old chat mode files may still work but agents are the new standard

#### Storage Locations

- **Repository Level**: `.github/agents/` folder (shared with team)
- **User Data Folder**: Personal agents stored outside repository, available across all projects
  - Useful for personal preferences and workflows
  - Not committed to version control
  - Available globally across all your projects

#### Creating Custom Agents

**Via VS Code**:

1. Open Copilot Chat
2. Click agents dropdown
3. Select "Create an agent" or "Configure Custom Agents"
4. VS Code creates agent template in `.github/agents/`
5. Configure name, description, and instructions
6. Define capabilities and tool restrictions

**Agent Structure**:

```markdown
---
name: my-agent
description: Brief description of agent's purpose and capabilities
tools: ["read", "edit", "search", "create_issue"]
---

# Agent Instructions

[Detailed instructions, behavioral guidelines, examples]
```

#### Tool Restrictions

- **Purpose**: Limit what the agent can do for focused, safe behavior
- **Available Tools**: read, edit, search, create, delete, terminal, github, etc.
- **Security**: Restrict dangerous operations (e.g., no terminal access for review agents)
- **Examples**:
  - Security agent: `["read", "search", "create_issue"]` (no code modification)
  - Test agent: `["read", "create", "test"]` (no production code edits)
  - Planner agent: `["read", "search"]` (no file modifications)

#### Agent Capabilities

- **Arguments**: Pass parameters to agents for dynamic behavior
- **Context Awareness**: Access to workspace, open files, repository structure
- **Behavioral Guidelines**: Define how agent should approach tasks
- **Domain Expertise**: Focus on specific areas (security, testing, documentation, etc.)

### Best Practices

#### Design Principles

1. **Start Simple**: Create one agent for a specific pain point
2. **Clear Responsibilities**: Define exact scope and boundaries
3. **Appropriate Tool Access**: Restrict to only necessary tools
4. **Iterative Refinement**: Improve based on real usage patterns
5. **Organization/Enterprise Sharing**: Share common agents across teams

#### Quality Guidelines

- **Include Examples**: Show how to use the agent effectively
- **Document Capabilities**: Clear description of what agent does
- **Validate Behavior**: Test agent before deploying to team
- **Version Control**: Track agent changes like code
- **Team Communication**: Ensure team understands agent purpose and usage

### Example Agents Discussed

**Security Analyzer**:

- **Purpose**: Analyze code for vulnerabilities without modifying production code
- **Tools**: read, search, create_issue
- **Behaviors**: OWASP Top 10 analysis, security best practices, issue creation

**Test Specialist**:

- **Purpose**: Generate and improve tests
- **Tools**: read, create, test (no production code modification)
- **Behaviors**: Unit tests, integration tests, coverage analysis

**Planner Agent** (Built-in):

- **Purpose**: Plan implementation without executing
- **Tools**: read, search (no file modifications)
- **Behaviors**: Break down tasks, create implementation plans

---

## Section 6: Best Practices and Q&A (Duration: 00:51:00 - 00:56:00)

### Key Topics

- Agent design best practices
- Tool restriction strategies
- Team collaboration considerations
- Questions about agent capabilities

### Main Discussion Points

#### Agent Design Best Practices (Recap)

1. **Start Simple**: One agent per specific pain point
2. **Define Clear Responsibilities**: Explicit scope and boundaries
3. **Restrict Tools Appropriately**: Grant minimum necessary access
4. **Refine Based on Usage**: Iterate and improve
5. **Create Org/Enterprise Agents**: Share common tasks
6. **Include Examples**: Show effective usage patterns
7. **Validate Before Rollout**: Test behavior in production scenarios

#### Student Questions

- **Tool Restrictions**: How the built-in planner agent uses tool restrictions to prevent editing
- **Custom Planner Agents**: Can create custom planner-style agents with similar tool limitations
- **Skills and Scripts**: Discussion of running local scripts via skills
- **MCP Server Integration**: Questions about integrating external tools

---

## Section 7: Session Transition and Preview (Duration: 00:56:00 - 01:01:00)

### Key Topics

- Transition to Greenfield exercise
- Overview of AI-assisted workflow
- Requirements-to-implementation process

### Main Discussion Points

#### Greenfield Exercise Preview

- **Starting Point**: Begin with project idea and requirements
- **End Goal**: Complete implementation with working code
- **Approach**: Step-by-step methodology using AI assistance

#### AI-Assisted Workflow Components

1. **MCP Servers**: Additional capabilities and integrations
2. **Custom Agents**: Specialized assistants for specific tasks
3. **Project Requirements**: Capturing and structuring requirements
4. **Conceptual Model**: Business rules and process modeling
5. **Structural Rules**: Defining data structures and relationships
6. **Process Rules**: Defining workflows and business logic
7. **Project Instructions**: Guiding implementation approach
8. **Implementation Prompts**: Generating actual code

#### Topics to Cover

- **Requirements Analysis**: How to capture and structure requirements
- **Business Rules**: Extracting structural and process rules
- **Vertical Slices**: Breaking features into implementable slices
- **Instruction Files**: Creating project-specific guidance
- **Implementation Prompts**: Guiding code generation
- **Lessons Learned**: Practical insights from real projects

---

## Summary Statistics

- **Total sections**: 7
- **Average section length**: ~08:45
- **Longest section**: Custom Agents - ~19:00
- **Shortest section**: Skills Support - ~01:10
- **Primary Topics**: Instruction file management, MCP servers, Custom agents, Greenfield workflow preparation

## Key Takeaways

1. **Context Control**: Use `appliesTo` clause for fine-grained control over which instruction files are loaded
2. **Hierarchical Loading**: Understand how files, instructions, chat modes, and prompt files work together
3. **MCP Servers**: Extend Copilot capabilities with external data sources and tools
4. **Custom Agents**: Create specialized assistants with focused responsibilities and tool restrictions
5. **Storage Locations**: Repository-level (`.github/agents/`) vs. user-level (personal) agents
6. **Tool Restrictions**: Essential for security and focused agent behavior
7. **Iterative Approach**: Start simple and refine based on actual usage
8. **Skills Support**: New capability for running scripts and automation
9. **Greenfield Preparation**: Setting up for requirements-to-implementation workflow
10. **Best Practices**: Clear responsibilities, appropriate tools, validation, and team collaboration
