# AI-Assisted Software Development with GitHub Copilot (Wednesday Morning Session)

## Overview

- **Total Duration**: 01:57:51 (1 hour 57 minutes 51 seconds)
- **Sections**: 9 main sections
- **Format**: VTT (WebVTT)
- **Date**: Wednesday (Day 3 of course)
- **Primary Speaker**: John Miller
- **Session Focus**: Brownfield development, technical debt identification, backlog building, and test automation

---

## Section 1: Introduction & Morning Greetings (Duration: 00:02:48)

### Timestamp Range

00:00:30 - 00:03:18

### Key Topics

- Morning welcome and roll call
- Weather chat between participants
- Course housekeeping
- Introduction to Day 3 agenda

### Subsections

- **Opening** (00:00:30 - 00:01:40): Welcome and initial greetings
- **Agenda Preview** (00:03:18): Introduction to finishing brownfield work

---

## Section 2: Azure DevOps & GitHub Copilot Extensions (Duration: 00:03:01)

### Timestamp Range

00:03:25 - 00:06:26

### Key Topics

- Azure DevOps integration with GitHub Copilot
- Two relevant marketplace extensions discussed
- Git DevOps extension for using Copilot with Azure DevOps
- Copilot CLI extension for Azure DevOps pipelines
- Using Copilot for pipeline automation and commit evaluation

### Subsections

- **Extension Introduction** (00:03:41 - 00:04:37): Git DevOps extension overview
- **CLI Integration** (00:04:37 - 00:05:34): Copilot CLI in Azure DevOps pipelines
- **Resource Location** (00:05:34 - 00:06:26): Where to find extensions in marketplace

---

## Section 3: GitHub Copilot Pricing & Licensing (Duration: 00:00:22)

### Timestamp Range

00:06:35 - 00:06:57

### Key Topics

- Business vs Enterprise license comparison
- $19/month per user for business license
- GitHub organization requirements
- Single-person shop access to business features
- Organization-level instruction files

### Notable Points

- Only need one person to create an org
- Access to pro+ features for $19/month
- Cheaper alternative to individual pro license

---

## Section 4: Exercise Setup - Fork Repository & Personal Access Token (Duration: 00:10:13)

### Timestamp Range

00:06:52 - 00:17:05

### Key Topics

- Forking the AI-assisted software development brownfield repository
- Creating GitHub personal access token
- Setting up environment variables
- Cloning forked repository locally
- Exploring unfamiliar codebase scenario

### Subsections

#### Repository Setup (00:07:00 - 00:08:22)

- Fork the brownfield demo repository
- Clone to local machine
- Standalone copy for pushing changes

#### Personal Access Token (00:08:22 - 00:13:39)

- Creating classic vs fine-grained tokens
- Setting environment variable (user or system)
- Restarting VS Code after setup
- Token permissions and scope discussion

#### Exercise Completion (00:14:29 - 00:17:05)

- Participants complete setup
- Hand-raising system for tracking progress
- Repository context: fork of existing project
- Code base characteristics: modest size, multiple issues

---

## Section 5: Building a Backlog - Technical Debt Identification (Duration: 00:31:52)

### Timestamp Range

00:17:08 - 00:49:00

### Key Topics

- Identifying technical debt in unfamiliar codebase
- Automating GitHub issue creation
- Using AI prompts for code analysis
- Creating comprehensive backlog for modernization
- Categorizing and prioritizing technical debt

### Subsections

#### Technical Debt Categories (00:17:08 - 00:18:59)

- **What AI Can Identify**:
  - Outdated coding patterns and styles
  - High complexity areas
  - Duplicate logic
  - Missing tests
  - Security vulnerabilities
  - Architectural drift
- **Benefits**:
  - Rapid debt discovery
  - Consistent classification
  - Prioritized modernization roadmap
  - Supports change control process

#### Exercise: Building Backlog (00:18:59 - 00:32:20)

- Exploring new code base scenario
- Creating GitHub issues for identified problems
- Using workspace prompts for analysis:
  - Code base review prompts
  - Dead code detection
  - Bug identification
  - Security audits
  - Test gap analysis
- Comprehensive backlog creation in ~1 hour

#### Prioritization Discussion (00:32:20 - 00:45:40)

- Impact vs effort evaluation
- Risk scoring for changes
- Dependency analysis between issues
- AI-assisted prioritization
- Visibility of technical debt to organization

#### Issue Creation Methods (00:40:00 - 00:45:31)

- Using GitHub issues vs Azure DevOps work items
- Issue types in GitHub (all are "issues" with labels)
- Azure DevOps comparison (features, PBIs, tasks, bugs)
- Extension for Azure DevOps integration
- Creating issues from VS Code

#### Process Bottlenecks (00:45:40 - 00:49:00)

- Real bottleneck: prioritization and review, not fixing
- AI can fix issues quickly
- Human review remains essential for:
  - Verifying accuracy
  - Approving fixes
  - Testing changes
  - Ensuring alignment with standards
- Making technical debt visible accelerates approval

---

## Section 6: Managing Instruction Files & Context Windows (Duration: 00:06:39)

### Timestamp Range

00:49:00 - 00:55:39

### Key Topics

- Sharing instruction files across projects
- Context window management
- Limitation of instruction file usage
- Monitoring token consumption

### Subsections

#### Sharing Strategies (00:49:00 - 00:51:43)

- **Current Approach**: Copying files between repositories (async)
- **Alternative Methods**:
  - Copody setting files
  - Sub-repositories
  - Central location sharing
  - Organizational-level instruction files (ideal for many scenarios)

#### Instruction File Scope (00:51:43 - 00:53:25)

- Explicit reference in prompts
- Reference in prompt files
- Using agents for encapsulated instructions (discussed tomorrow)
- File extension-based application
- Pattern-based file matching
- Folder-specific instruction files

#### Context Window Limits (00:53:25 - 00:55:39)

- **Monitoring Tools**:
  - Diagnostics panel showing token usage
  - System instructions view
  - Context window percentage indicators
- **Observed Growth**: Started at 5%, reached 33%, demonstrated at 68%
- **UI Warnings**: Visual changes when approaching limits
- **Management Need**: Will discuss focusing strategies on Day 4
- **Finite Limit**: All instruction files consume context window space

---

## Section 7: Prioritization & Issue Management (Duration: 00:04:29)

### Timestamp Range

01:06:54 - 01:11:23

### Key Topics

- Security issue identification (exposed secrets)
- Missing HTTPS implementation
- No test coverage
- Missing CI/CD pipeline
- AI-assisted prioritization matrix

### Subsections

#### Security Findings (01:06:54 - 01:07:24)

- Exposed secret detected
- Not using HTTPS
- Missing AI logs (expected compliance)
- No test coverage
- No CI/CD pipeline

#### Prioritization Approach (01:07:35 - 01:09:12)

- Prioritizing by impact vs effort
- Asking AI to analyze issues
- Creating prioritization matrix
- Visual representation options (Mermaid diagrams)
- Updating GitHub issues with priorities

#### Technical Debt Visibility (01:09:12 - 01:11:17)

- Making debt visible to organization
- Low-effort, high-impact items first
- AI can propose implementation solutions
- Rapid pay-down of technical debt
- Achieving "Evergreen" state efficiently
- Phase Zero security with infinite ROI

---

## Section 8: Protecting Brownfield Code Bases (Duration: 00:02:19)

### Timestamp Range

01:11:31 - 01:13:50

### Key Topics

- Safety nets for brownfield systems
- Preserving existing behavior
- Incremental modernization strategies
- Risk management approaches

### Subsections

#### Protection Strategies (01:11:31 - 01:12:43)

- **Test Suite Importance**: Constant reassurance of no breakage
- **Automated Verification**: Minimize human intervention
- **Avoid Risky Refactors**: Break into small, verifiable pieces
- **Fast Deployment**: Quick production releases
- **Feature Flags**: Hide incomplete features while in production

#### Modernization Approach (01:12:43 - 01:13:50)

- **Incremental Changes**: Slow, steady stream of improvements
- **Size Management**: Nothing too big or risky
- **Architectural Boundaries**: Well-isolated, decoupled areas
- **Independent Testing**: Areas can be tested separately
- **AI Change Documentation**: AI logs and metadata tracking
- **Critical System Protection**: Avoid AI-introduced production issues

---

## Section 9: Test Automation & Code Quality (Duration: 00:05:16)

### Timestamp Range

01:52:35 - 01:57:51

### Key Topics

- AI-assisted test generation
- Intelligent linting beyond static analysis
- Coverage analysis and adequacy assessment
- Automated quality gates
- Continuous deployment strategies

### Subsections

#### Test Generation Capabilities (01:52:47 - 01:54:16)

- **Test Types Supported**:
  - Unit tests
  - Integration tests
  - End-to-end tests
  - Performance tests
- **Benefits**:
  - Rapidly expand test coverage
  - Quality equals comprehensive testing
  - Consistent structure and naming conventions
  - Reduced onboarding time for developers

#### Intelligent Linting (01:54:16 - 01:55:21)

- **Beyond Syntax Checking**:
  - Architectural violations
  - Anti-pattern detection
  - Unsafe refactors
  - Missing documentation
  - Inconsistent naming
  - Domain terminology consistency
- **Semantic Analysis**: Understanding code meaning, not just syntax
- **Architectural Guardrails**: Enforce boundaries and patterns
- **Long-term Benefits**: Reduce technical debt accumulation

#### Coverage Analysis (01:55:21 - 01:56:22)

- **Gap Identification**:
  - Coverage gaps
  - Missing edge cases
  - Over-testing implementation details
  - Under-testing business logic
  - Redundant or brittle tests
- **Meaningful Metrics**: Signal of production readiness
- **Goal**: Confidence to auto-deploy passing PRs
- **Continuous Deployment**: Push small changes rapidly
- **Maintenance Reduction**: Consistent, reliable test suite

#### Automated Quality Gates (01:56:22 - 01:57:51)

- **PR-Level Requirements**:
  - Minimum test coverage for PR creation
  - Higher coverage requirements for merge to main
  - Linting and architectural checks
  - Provenance requirements for auditing
- **Pipeline Integration**:
  - PR-level test generation
  - Risk scoring for changes
  - Automated regression prevention
- **Development Philosophy**: Support Evergreen development mindset

---

## Summary Statistics

- **Total sections**: 9
- **Average section length**: ~13 minutes
- **Longest section**: Building a Backlog - Technical Debt Identification (31:52)
- **Shortest section**: GitHub Copilot Pricing & Licensing (00:22)
- **Primary Focus Areas**:
  1. Technical debt identification and management (26% of session)
  2. Hands-on exercises and setup (18% of session)
  3. Test automation and quality (4% of session)
  4. Context management and tooling (6% of session)

---

## Key Takeaways

### For Brownfield Development

1. AI can rapidly identify technical debt across multiple dimensions
2. Automating backlog creation makes debt visible organization-wide
3. Prioritization based on impact vs effort enables strategic improvements
4. Incremental modernization reduces risk while maintaining production systems
5. Test automation is critical for confidence in AI-assisted changes

### For Tool Usage

1. Azure DevOps has extensions for Copilot integration
2. Personal access tokens enable programmatic GitHub access
3. Instruction files consume context window space - monitor usage
4. Organization-level instruction files ideal for team standardization
5. Multiple prompts available for different analysis needs

### For Quality & Testing

1. AI can generate comprehensive test suites across all test types
2. Intelligent linting goes beyond syntax to semantic analysis
3. Coverage analysis identifies gaps in edge cases and business logic
4. Automated quality gates enable continuous deployment
5. Consistent naming and structure accelerate team effectiveness

### Session Logistics

- Break taken at 01:57:51 (1 hour break mentioned)
- Hands-on exercises with participant interaction
- Hand-raising system for tracking progress
- Active Q&A throughout session
- Recorded for later reference

---

**Generated**: February 17, 2026
**Source File**: AI-Assisted Software Development with GitHub Copilot (Wed Morning).vtt
**Session Type**: Training - Day 3 Morning
**Participants**: 8-10 active participants (Chris Bishop, Dan Blanchard, Peter Goostree, Matt Hoffman, Tom Bui, Rich LaVorgna, Rockwell Christopher, Rebecca/Regalberto, and instructor John Miller)
