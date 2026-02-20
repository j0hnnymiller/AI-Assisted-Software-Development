# AI-Assisted Software Development with GitHub Copilot

## Course Outline - February 2026 Session

**Total Duration**: 5 Days (10 sessions, ~20 hours total)
**Instructor**: John Miller, Principal Software Engineer at Code
**Format**: Live virtual training with hands-on exercises
**Organization**: Code Training / Code Magazine

---

## Course Overview

A comprehensive 5-day training course covering AI-assisted software development from fundamentals through practical implementation. The course progresses from understanding LLMs and AI-first development philosophy through brownfield code management and culminates in greenfield development with vertical slice architecture.

**Key Themes**:

- AI-first vs. Prompt-first development methodologies
- Brownfield code analysis and technical debt management
- Greenfield development with vertical slicing
- Provenance tracking and compliance
- Test automation and quality assurance
- GitHub Copilot integration and advanced features

---

#### Course Introduction (15 minutes)

- Course structure and five-day overview
- Instructor background and credentials
- Code organization (consulting, staffing, magazine, training)
- Student introductions and backgrounds
- Agenda review

#### AI-Assisted Development Philosophy (9 minutes)

- Programming evolution from switches to natural language
- Why AI-assisted development matters
- "Superpowers" for developers - tackling "nice to haves"
- AI-first vs. Prompt-first distinction
  - **AI-first**: SDLC-wide integration, lifecycle philosophy
  - **Prompt-first**: Interaction mechanics, deterministic behavior

#### Large Language Models (5 minutes)

- Training on massive datasets
- Transformer architecture fundamentals
- Token-based processing
- Attention mechanisms
- Probabilistic next-token prediction
- Critical insight: Pattern matching, not true understanding

#### GitHub Copilot for Teams Key Considerations

- Benefits for Organizations
- Risks to Consider
- Governance and Compliance Risks
- IP and Data Protection
- Licensing and Legal Considerations
- Deployment Options
- Best Practices for Safe Use

#### Model Selection and Capabilities (5+ minutes)

- Available models in GitHub Copilot
- Context window limits (input/output)
- Subscription impact on usage
- Premium requests and allocation

#### Repository and Tool Setup (10 minutes)

- Cloning course repository
- GitHub authentication

#### Working with GitHub Copilot (15 minutes)

- Creating `.gitignore` file
- Keep/Undo functionality
- Three levels of change acceptance
- Copilot UI Tour

#### Building an Application with AI Assistance(50 minutes)

- Basic operations
- Input validation and error handling
- Blazor/Razor web interface
- Digit and operation buttons
- Display panel implementation

#### Evergreen Code Preview (10 minutes)

- Introduction to Evergreen philosophy
- Modern tooling and continuous quality
- AI-assisted technical debt management

#### Safety Measures & Best Practices (22 minutes)

- Feature flag removal strategies
- Testing: Coverage vs. signal quality
- Code review: Treat AI as "eager knowledgeable junior developer"
- Change review workflows
- Small change sets importance

#### Managing Copilot & Context Management (11 minutes)

- Context window limits and token management
- Advanced techniques:
  - **Summaries**: Condensing large contexts
  - **Chunking**: Breaking down large tasks
  - **Scoped Prompts**: Focusing on specific areas
  - **Instruction Files**: Persistent rules for AI behavior

#### Instruction Files & Provenance Tracking (38 minutes)

- Instruction files vs. prompt files vs. chat modes
- **Required Provenance Metadata** (11 fields):
  - ai_generated, model, operator, chat_id, prompt
  - timestamps, task durations, ai_log, source
- Validation checklists and quality gates
- FDA guidance discussion for regulated industries
- Conversation log structure and templates

#### Hands-On Exercise: Creating Prompt Files (22 minutes)

- **Phase 1**: Without instruction files (baseline)
- **Phase 2**: With instruction files (comparison)
- **Phase 3**: Comparing differences
- Key findings: Significant improvement in consistency, completeness, compliance

#### Creating Instruction Files from Prompts (7 minutes)

- Running generated prompt files
- Inference as enabler
- Prompt-first approach benefits
- Version control for prompts

#### Organizational vs. Repository Instruction Files (4 minutes)

- Business/Enterprise tier capabilities
- Path-scoped instruction files
- Folder-level technology-specific rules

#### Exercise: Technology Inventory & Instruction Generation (18 minutes)

- Creating inventory of project technologies
- Background sessions for concurrent work
- Generating multiple instruction files simultaneously
- Session management interface

#### Sessions vs. Conversations (6 minutes)

- Distinction clarification
- Session resets model's short-term memory
- Troubleshooting output variations

#### VS Code Configuration Tips (5.5 minutes)

- Custom keyboard shortcuts
- Multi-command extension for Marp slides

#### Metadata and README Updates (7 minutes)

- Automatic README updates for AI-generated files
- Context window management with instruction files
- Diagnostics view for monitoring token usage

#### Context Analysis and Validation (11 minutes)

- Running context analysis prompts
- Identifying issues in instruction files
- Implementing recommendations
- GitHub Action enforcement discussion

#### Documentation Generation (22 minutes)

- Automatic README updates
- Module-level documentation
- API documentation with usage samples
- Strategies for sync: Regular prompts, documentation instruction files

#### Architecture Diagrams with Mermaid (7 minutes)

- Generating C4 diagrams from code
- Component, container, and system context diagrams
- Diagram types: Dependency graphs, data flow, deployment topologies
- Mermaid rendering considerations

#### Code Explanation and Analysis (9 minutes)

- Explaining unfamiliar code
- Call chain mapping
- Test coverage analysis
- Gap identification and recommended tests

#### Code Translation and Compliance Review (12 minutes)

- Translating code between languages
- Instruction compliance review
- Scoped analysis for specific files/projects
- Creating GitHub issues from findings

---

#### Azure DevOps & GitHub Copilot Extensions (3 minutes)

- Git DevOps extension
- Copilot CLI extension for Azure DevOps pipelines
- Pipeline automation and commit evaluation

#### GitHub Copilot Pricing & Licensing (0.5 minutes)

- Business vs. Enterprise license comparison
- $19/month per user for business license
- Organization-level instruction files access

#### Exercise Setup: Repository Fork & PAT (10 minutes)

- Forking brownfield demo repository
- Creating GitHub personal access token
- Environment variable configuration
- Repository exploration

#### Building a Backlog - Technical Debt Identification (32 minutes)

- **What AI Can Identify**:
  - Outdated coding patterns
  - High complexity areas
  - Duplicate logic
  - Missing tests
  - Security vulnerabilities
  - Architectural drift
- **Exercise**: Comprehensive backlog creation in ~1 hour
- **Prioritization**: Impact vs. effort evaluation
- **Issue Creation**: GitHub issues vs. Azure DevOps work items
- **Key Insight**: Bottleneck is prioritization/review, not fixing

#### Managing Instruction Files & Context Windows (7 minutes)

- Sharing strategies: Copying, sub-repositories, organizational-level
- Instruction file scope and application
- Context window monitoring tools
- Token consumption tracking

#### Prioritization & Issue Management (4 minutes)

- AI-assisted prioritization matrix
- Technical debt visibility to organization
- Low-effort, high-impact items first

#### Protecting Brownfield Code Bases (2 minutes)

- Test suite importance
- Avoid risky refactors
- Fast deployment cycles
- Feature flags for incomplete features
- Incremental changes with well-isolated boundaries

#### Test Automation & Code Quality (5 minutes)

- AI-assisted test generation (unit, integration, e2e, performance)
- Intelligent linting beyond static analysis
- Coverage analysis and adequacy assessment
- Automated quality gates
- Continuous deployment strategies

---

#### Prompt Guidance Discussion (12 minutes)

- Structured prompting for AI-assisted development
- Effective prompt examples
- Avoiding literal copying of activity descriptions
- Phrase prompts for architectural analysis

#### Testing Frameworks (13 minutes)

- **Key Practices**: Prune obsolete tests, update with code changes, TDD with AI
- **Test Review**: Detect missing assertions, redundant tests, edge cases
- **Critical Principle**: Validate intent, not implementation
- **AI-Generated Tests**: Create instruction files with test expectations
- **Trust Building**: Use different models for analysis
- **Key Practices**: Prune obsolete tests, update with code changes, TDD with AI
- **Test Review**: Detect missing assertions, redundant tests, edge cases
- **Critical Principle**: Validate intent, not implementation
- **AI-Generated Tests**: Create instruction files with test expectations
- **Trust Building**: Use different models for analysis

#### Feature Flags and Test Suites (7 minutes)

- **As-Is Test Suites**: Capture current behavior, protect regressions
- **To-Be Test Suites**: Define future behavior, validate WIP features
- **Workflow**: Feature flags around modifications, separate test strategies
- **Feature Flag Retirement**: AI-assisted flag removal

#### Testing in Production (7 minutes)

- Shadow traffic and canary releases
- Observability dashboards
- Automated rollback with error budgets
- Beta testing strategy
- Database schema change challenges

#### Addressing Technical Debt: JWT Security Fix (8 minutes)

- **Scenario**: JWT secrets hardcoded in source control
- **5-Phase Fix**:
  1. Immediate remediation (remove from source)
  2. Secure configuration (user secrets, environment variables)
  3. Enterprise-grade security (Key Vault integration)
  4. Git history cleanup
  5. Testing strategy
- **Critical Step**: Rotate secrets after exposure

#### Implementation Review (4 minutes)

- Selecting appropriate issues for demonstration
- Evaluating implementation complexity
- Issue selection criteria

#### AI Implementation Workflow (10 minutes)

- **Best Practice**: Request proposal first, don't execute immediately
- Review proposed fix for completeness
- Identify gaps before proceeding
- Multi-tasking: Concurrent work with AI sessions

#### Effective Prompts for Technical Debt (8 minutes)

- **Required Elements**: Clear description, constraints, expected outcomes, test updates, documentation
- **GitHub Integration**: Issue creation via Copilot, assigning to @copilot
- **Paid Feature**: Copilot autonomous implementation (Enterprise/Pro Plus)

#### Hands-On Exercise (17 minutes)

- Student implementation practice
- Pull request workflow
- GitHub Actions and workflow approvals
- Troubleshooting: Workflow approvals, Copilot PR reviews

---

#### Pre-Class Questions: Getting Started with Instructions (8 minutes)

- Building instruction files iteratively
- Starting from scratch vs. incremental building
- Building block approach
- Progressive sophistication

#### Copilot Instruction Files and Context Management (9 minutes)

- **AppliesTo Clause**: Fine-grained control over file pattern matching
- **Scope Levels**: Global, directory-specific, type-specific, repository-specific
- **Control Hierarchy**: File context → Instruction matching → Chat mode → Prompt files → Manual references

#### Skills Support in GitHub Copilot (1 minute)

- Skills folder for custom scripts
- Cross-platform compatibility
- Early release feature

#### MCP (Model Context Protocol) Servers (15 minutes)

- **Purpose**: Add capabilities and data sources to Copilot
- **Architecture**: Client, Server, Protocol, Resources, Tools
- **Available Servers**: GitHub repos, databases, Terraform, Kubernetes, cloud providers
- **Finding Servers**: VS Code gallery, modelcontextprotocol.io
- **Installation**: Extension-based, token usage considerations (~128 tokens per server)

#### Custom Agents (19 minutes)

- **Definition**: Specialized AI assistants with custom instructions
- **Recent Changes**: Stored in `.github/agents/` with `.agent.md` extension
- **Storage Locations**: Repository-level vs. user data folder (personal)
- **Creating Agents**: Via VS Code chat interface
- **Tool Restrictions**: Limit capabilities for focused, safe behavior
- **Examples**: Security analyzer (read/search only), test specialist, planner agent

#### Best Practices for Agent Design (5 minutes)

- Start simple, one agent per pain point
- Define clear responsibilities
- Restrict tools appropriately
- Refine based on usage
- Create org/enterprise agents for common tasks

#### Session Transition: Greenfield Exercise Preview (5 minutes)

- Requirements-to-implementation process
- Workflow components: MCP servers, agents, requirements, rules, instructions
- Topics to cover: Requirements analysis, business rules, vertical slices

---

#### Repository Setup (3 minutes)

- Updated repositories with core instruction files
- Greenfield branch introduction
- Product manager agent and prompt files

#### Business Requirements Generation Exercise (17 minutes)

- Creating personal branches
- Using product manager agent
- Generating requirements document
- Version control and branching strategy

#### Greenfield Development Workflow (8 minutes)

- **Phase 1 - Foundation**: Core instructions, tech stack, coding standards, security
- **Phase 2 - Automation**: Repeatable tasks, prompt files, templates
- **Phase 3 - Specialization**: Domain expertise, custom chat modes
- **Phase 4 - Integration**: Complex workflows, team standards, training
- Continuous iteration and validation

#### AI-Assisted Workflow Pattern (6 minutes)

- **Stages**:
  1. Stakeholders define requirements with AI
  2. Transform into implementation structure files
  3. Add tech stack instruction files
  4. Review and approve instructions
  5. Create prompts for implementation
  6. Use vertical slicing with feature-based profiles
  7. Execute and verify

#### Technology Stack Instruction Files (17 minutes)

- Creating instructions for HTML5, CSS3, vanilla JavaScript
- Command-line prompt generation
- Model differences (Claude Sonnet vs. GPT-4)
- Validation checklists
- **Multi-Model Evaluation**: Different models reviewing each other's output

#### Vertical Slicing Architecture Introduction (19 minutes)

- **Definition**: Organize code by features, not layers
- **Characteristics**: Self-contained, independent, spans all technical layers
- **File Structure**: Features folder with sub-folders per feature
- **Benefits**:
  - Faster feature development
  - Localized changes
  - Clear boundaries
  - Parallel development
  - Independent testing
- **CQRS Relationship**: Separate read/write stacks per feature

#### Creating Vertical Slice Implementation Plans (16 minutes)

- Vertical slice planning instruction file review
- **Slice Identification Strategies**: User actions, entity CRUD, workflow stages, business events, CQRS-optimized
- **Decomposition Principles**: Single responsibility, complete vertical stack, no horizontal sharing
- Generating implementation plans with AI
- Multi-model evaluation exercise (Gemini reviewing Claude output)

#### Implementation Prompts and Verification (22 minutes)

- Creating slice-specific prompt files
- Detailed specifications (HTML, CSS, JavaScript)
- Verification steps inclusion
- Showcase/demonstration instructions
- Building complete implementation roadmap
- Version-controlled, reusable prompts

---

#### Opening and Introductions (3 minutes)

- Morning greetings and session setup

#### AI Practitioner Resources Overview (10 minutes)

- Custom tool for managing AI resources
- GitHub Actions integration for gist storage
- Risk scoring mechanism
- Repository structure and artifact tracking

#### AI-First Development Methodology (4 minutes)

- Prompt-first methodology
- Tracking provenance of AI artifacts
- Transparency in AI-assisted development

#### GitHub Project Workflow Exploration (27 minutes)

- Repository structure and organization
- Contributor guidelines
- Issue creation and management
- **Implementation Plan Review**: 30 vertical slices identified
- Removing sprint/duration estimates for continuous flow
- Diagram generation and visualization
- Mermaid diagram troubleshooting

#### Dependency Analysis and Planning (3.5 minutes)

- Reading dependency diagrams
- Implementation sequencing
- Critical path identification
- Foundational vs. dependent features

#### Vertical Slice Implementation (41.5 minutes)

- **Setup**: Selecting first slice, reviewing acceptance criteria
- **Issue Review**: Comparing prompt to generated issue, scope verification
- **Live Coding**: Using Copilot for generation, file organization
- **Manual Verification**: Discussion of automation vs. manual steps
- **Key Focus**: Automated testing over manual verification

#### Pull Request and Code Review (11.5 minutes)

- Creating PR with "slice-1" branch
- Associating PRs with issues
- Assigning human reviewers
- **Initiating GitHub Copilot code review**
- **AI Review Findings**:
  - Missing AI provenance metadata
  - DOM element access patterns
  - Code quality improvements
- Addressing review comments

#### GitHub Code Review with Copilot (18 minutes)

- **PR #4 Review**: 8 comments identified
- **Findings**: Unicode characters, state management, missing metadata, dead code, test gaps
- **Process Observations**:
  - Copilot "thinking process" visible
  - Manual comment resolution
  - Using review output to improve instruction files

---

#### Vertical Slice Review (5 minutes)

- Review of dependency diagram
- Parallel implementation capabilities
- Critical path identification (VSO 2 → VSO 3)
- Task assignments

#### Issue Identification & Diagram Corrections (8 minutes)

- Slice numbering inconsistencies found
- AI-assisted validation and correction
- Iterative debugging of Mermaid diagrams

#### Slice 4 Showcase - Order of Operations (7 minutes)

- Chris Bishop demonstrates implementation
- Test scenarios: Basic operations, order of operations, edge cases
- **Key Insight**: Using Cursor AI tool, minimal manual coding
- Discussion: Value shifting from coding to specification skills

#### Slice 3 Showcase - Clear Button (14 minutes)

- Christopher Rockwell demonstrates implementation
- Merged VSO 4 work first
- Clear button resets calculator
- **Merge Conflicts**: Copilot resolved on first try
- Suggestion: Modularize code to reduce conflicts

#### GitHub CLI & PR Management (11 minutes)

- Default merge strategy discussion (squash vs. merge commit)
- GitHub settings navigation
- Requesting Copilot code reviews via web interface
- GitHub CLI commands for comment resolution
- Personal access token permissions

#### Development Process Q&A (6 minutes)

- **Merge Conflict Strategies**: VS Code vs. GitHub web
- **Requirements Document Creation**: When AI can help vs. domain expertise needs
- AI useful for structure/refinement, not domain knowledge

#### Adoption Strategy & Wrap-up (12 minutes)

- **Step 1 - Build Instruction Files**: Core instructions, tech-specific, metadata requirements
- **Step 2 - Brownfield Analysis**: Interrogate codebase, identify deviations, build backlog
- **Step 3 - Greenfield Setup**: Core instructions, tech stack files, requirements, agents
- **Step 4 - Iterative Refinement**: Review output, update instructions, validate improvements
- **Key Philosophy**: Iterating on guardrails and prompts, not just code

---

## Technologies & Tools Covered

**Core Technologies**:

- GitHub Copilot (AI coding assistant)
- VS Code (primary IDE)
- C# / .NET 9
- ASP.NET / Blazor / Razor Pages
- HTML5, CSS3, JavaScript/TypeScript
- Git / GitHub

**AI & Automation Tools**:

- GitHub Copilot agents
- MCP (Model Context Protocol) servers
- GitHub Actions
- GitHub CLI (gh)
- Azure DevOps MCP tool

**Development Tools**:

- mob.sh (mob programming)
- Mermaid (diagrams)
- xUnit (testing)
- NuGet (package management)
- Cursor AI (alternative AI coding tool)

**Documentation & Diagramming**:

- Markdown
- Marp (markdown slides)
- YAML (front matter, configuration)
- C4 architecture diagrams

---

## Key Concepts & Methodologies

### Development Approaches

- **AI-First Development**: SDLC-wide integration, lifecycle philosophy
- **Prompt-First Development**: Deterministic behavior through versioned prompts
- **Vertical Slice Architecture**: Feature-based organization vs. layered
- **CQRS**: Command Query Responsibility Segregation
- **Evergreen Code**: Continuously maintained modern code
- **Brownfield vs. Greenfield**: Existing systems vs. new development

### Safety & Quality

- Test-driven development with AI assistance
- Code review treating AI as junior developer
- Feature flags for safe deployments
- As-Is vs. To-Be test suites
- Testing in production (shadow traffic, canary releases)
- Automated quality gates

### Provenance & Compliance

- Required metadata: 11 fields for AI-generated artifacts
- Conversation logging structure: `ai-logs/yyyy/mm/dd/<chat-id>/`
- FDA preliminary guidance discussions
- Chain of custody for AI artifacts

### Advanced Techniques

- Instruction files for persistent AI guidance
- Prompt files for reusable tasks
- Chat modes for persona-based interactions
- Custom agents for specialized tasks
- MCP servers for extended capabilities
- Multi-model evaluation strategies

---

## Learning Outcomes

By the end of this course, participants can:

1. **Understand AI Fundamentals**
   - LLM architecture and limitations
   - Token-based processing and context windows
   - AI-first vs. prompt-first methodologies

2. **Manage AI-Assisted Development**
   - Create and maintain instruction files
   - Build effective prompts for code generation
   - Track provenance and maintain compliance
   - Use GitHub Copilot effectively

3. **Handle Brownfield Code**
   - Identify and prioritize technical debt
   - Build backlog systematically
   - Use AI for code analysis and modernization
   - Protect existing systems with safety measures

4. **Build Greenfield Projects**
   - Generate business requirements with AI
   - Decompose features into vertical slices
   - Create implementation plans and prompts
   - Build complete applications iteratively

5. **Implement Quality Practices**
   - Generate comprehensive test suites
   - Use feature flags for safe deployment
   - Implement intelligent linting
   - Create automated quality gates

6. **Collaborate Effectively**
   - Use GitHub Copilot for code review
   - Manage merge conflicts
   - Share instruction files across teams
   - Build organization-wide standards

---

## Course Materials & Repository Structure

```
AI-Assisted-Software-Development-Course/
├── .github/
│   ├── instructions/           # Instruction files for AI guidance
│   │   ├── ai-assisted-output.instructions.md
│   │   ├── vertical-slice-architecture.instructions.md
│   │   ├── cqrs-architecture.instructions.md
│   │   └── [technology-specific].instructions.md
│   ├── prompts/                # Reusable prompt files
│   │   ├── create-requirements.prompt.md
│   │   └── [feature-specific].prompt.md
│   └── agents/                 # Custom AI agents
│       ├── product-manager.agent.md
│       ├── security-analyzer.agent.md
│       └── test-specialist.agent.md
├── ai-logs/                    # Conversation logs with provenance
│   └── yyyy/mm/dd/<chat-id>/
│       ├── conversation.md
│       └── summary.md
├── Labs/                       # Hands-on lab exercises
├── CODE/                       # Course slides and content
└── past-class-recordings/      # Session recordings and summaries
    └── 2026-02/
```

---

## Best Practices Emphasized

1. **Start Simple**: Begin with basic instruction files, iterate and improve
2. **Version Control Everything**: Prompts, instructions, agents
3. **Review AI Output**: Never accept without human validation
4. **Keep Changes Small**: Easier to review and safer to deploy
5. **Use Multiple Models**: Cross-validate with different AI models
6. **Track Provenance**: All 11 required metadata fields
7. **Automate Testing**: Prefer automated over manual verification
8. **Modularize Code**: Reduce merge conflicts
9. **Focus on Intent**: Specification skills over coding skills
10. **Iterate on Instructions**: Continuous improvement of guardrails

---

## Summary Statistics

- **Total Course Duration**: ~20 hours over 5 days
- **Sessions**: 10 (2 per day)
- **Hands-On Exercises**: 12+
- **Calculator Implementations**: Console, Web (Blazor), Web (vanilla JS)
- **Vertical Slices Developed**: 30 identified, 4-10 implemented during course
- **Pull Requests Created**: Multiple across student implementations
- **Instruction Files Created**: 10+ (core, technology-specific, project-specific)
- **Custom Agents Demonstrated**: Product manager, security analyzer, test specialist

---

**Course Completed**: February 14, 2026
**Documentation Generated**: February 17, 2026
**Next Offering**: Check Code Training website for schedule


---

Archive

#### Brownfield Overview (8 minutes)

- Definition: Existing systems with constraints, real users, production requirements
- Course agenda: Understanding Evergreen code, safety measures, context techniques, documentation
- Calculator demo with Windows-style UI
- Workspace compliance review



#### Large Language Models - Part 2 (3 minutes)

- **Capabilities**: Code completion, generation, refactoring, optimization, bug detection, documentation, test generation, multi-language support
- **Current Limitations**: No real-time knowledge, statistically correct but logically flawed code, hallucinations, limited context windows, no business logic understanding

#### LLM Architecture for Code Generation (3 minutes)

- Processing pipeline walkthrough
- From developer input to code generation
- Context window importance
- Post-processing and validation

#### Mob Programming Introduction (4 minutes)

- Role definitions: Driver, Navigator, Supporters
- Mob.sh tool benefits
- Remote collaboration approach
