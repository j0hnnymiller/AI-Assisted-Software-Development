# AI-Assisted Software Development with GitHub Copilot (Wed Morning)

## Overview

- **Total Duration**: 01:57:53
- **Sections**: 9
- **Format**: VTT (WebVTT)
- **Session**: Day 3 - Wednesday Morning
- **Instructor**: John Miller
- **Topic**: Brownfield Development - Code Analysis and Technical Debt Management

---

## Section 1: Opening and Introductions (Duration: 00:03:19)

### Key Topics

- Morning greetings and weather chat
- Day 3 introduction
- Setting session context for brownfield work

### Content Summary

Session begins at 00:00:30 with informal greetings. Instructor welcomes participants to day three, preparing to finish brownfield work but first addressing questions from previous sessions.

---

## Section 2: Azure DevOps and GitHub Copilot Integration (Duration: 00:03:02)

**Timestamps**: 00:03:19 - 00:06:21

### Key Topics

- Azure DevOps extensions for GitHub Copilot
- GitHub Copilot CLI extension for Azure DevOps pipelines
- Using Copilot in CI/CD workflows
- GitHub marketplace extensions

### Content Summary

Instructor shares two relevant marketplace extensions:

1. **Git DevOps Extension** - Enables GitHub Copilot usage with Azure DevOps (built by Microsoft team, not GitHub Copilot team)
2. **Copilot CLI Extension** - Allows Copilot CLI usage in Azure DevOps pipelines for automated code evaluation

Both extensions found by searching "GitHub Copilot" + "Azure DevOps" in the marketplace. Resources committed to course repository for participant access.

---

## Section 3: GitHub Copilot Licensing Discussion (Duration: 00:01:19)

**Timestamps**: 00:06:21 - 00:07:40

### Key Topics

- Business vs Enterprise licensing comparison
- Organization-level access
- Cost-effective licensing for individuals
- GitHub organization requirements

### Content Summary

Instructor presents comparison table showing:

- **Business license**: $19/month per user
- **Requirement**: GitHub organization (can be single person)
- **Benefits**: Pro Plus features, business-level configuration, org-level instruction files
- **Strategy**: Individual developers can create GitHub org for cost-effective access

---

## Section 4: Exercise 1 - Repository Setup (Duration: 00:36:02)

**Timestamps**: 00:07:40 - 00:43:42

### Key Topics

- Forking brownfield repository
- Cloning forked repository locally
- Creating GitHub personal access token
- Setting environment variables
- Visual Studio Code configuration

### Exercise Steps

1. Fork AI-assisted brownfield repository
2. Clone forked repo to local machine
3. Create GitHub personal access token (classic vs fine-grained)
4. Store token in environment variable
5. Restart VS Code to recognize token

### Technical Issues Addressed

- Enterprise GitHub accounts preventing forks (solution: use personal account)
- Personal access token scope (classic recommended for training, fine-grained for production)
- Environment variable configuration (user vs system level)
- VS Code workspace context management

### Participant Questions

- **Chris Bishop**: Folder organization and Copilot context (separate workspaces recommended)
- **Tom Bui**: Fine-grain vs classic tokens
- **Tom Bui**: Enterprise fork restrictions
- **Matt Hoffman**: Environment variable location
- **Dan Blanchard**: Token repository access scope

---

## Section 5: Exercise 2 - Building Technical Debt Backlog (Duration: 00:24:00)

**Timestamps**: 00:43:42 - 01:07:42

### Key Topics

- Technical debt identification
- Automated GitHub issue creation
- Code base assessment strategies
- Backlog prioritization
- AI-assisted code review

### Technical Debt Categories Identified

- Outdated coding patterns and styles
- High complexity code
- Duplicate logic
- Missing tests and test gaps
- Security vulnerabilities
- Architectural drift
- Dead code

### Benefits Discussed

- Rapid rediscovery of technical debt
- Consistent classification of issues
- Prioritized modernization roadmap
- Change control process facilitation
- Visibility of technical debt to organization

### Available Prompts (from course repository)

- Code base vs instruction audit
- Create issues for dead code
- Create issues for found bugs
- Security audit
- Test gap analysis

### Issue Creation Workflow

1. Use GitHub CLI for authentication (`gh auth login`)
2. Run analysis prompts against codebase
3. Automatically create GitHub issues with findings
4. Prioritize by impact vs effort
5. Consider issue dependencies

### GitHub CLI Integration

- **Check auth status**: `gh auth status`
- **Login**: `gh auth login`
- Copilot can use GitHub CLI commands directly
- Requires proper authentication to create issues

### Technical Challenges

- Copilot not creating issues automatically (solution: explicitly request with follow-up prompt)
- GitHub authentication required
- Alternative: Create issues in files if GitHub interaction fails

---

## Section 6: Prioritization and Impact Analysis (Duration: 00:04:00)

**Timestamps**: 01:07:42 - 01:11:42

### Key Topics

- Impact vs effort evaluation
- Dependency mapping
- Backlog organization strategies
- Prompt file sharing across projects

### Content Summary

Discusses methods for evaluating technical debt issues:

- **Impact Assessment**: Business impact of not fixing
- **Effort Estimation**: Development time required
- **Dependency Analysis**: Issues blocking other work
- **Prioritization Matrix**: Impact vs Effort quadrants

Methods for sharing prompts:

- Sync approach (copy files between repos)
- Copilot settings files
- Sub-repositories
- Organization-level instruction files (recommended)

---

## Section 7: GitHub Copilot Workspace Integration (Duration: 00:08:00)

**Timestamps**: 01:11:42 - 01:19:42

### Key Topics

- Assigning issues to Copilot
- Monitoring Copilot progress
- Copilot code reviews
- Pull request automation
- Session viewing

### Copilot Workspace Features

- **Issue Assignment**: Assign issues directly to Copilot from GitHub
- **Progress Monitoring**: View Copilot session while working on issues
- **Initial Plan Commit**: Copilot creates plan before implementation
- **Pull Request Creation**: Automatic PR creation with changes
- **Code Review**: Enable automatic Copilot code reviews in settings

### Code Review Configuration

1. Navigate to repository settings
2. Select Copilot section
3. Enable "Code Review"
4. Create rule set
5. Copilot auto-assigns as reviewer on all PRs

### Multi-Model Review Strategy

- Use different models to review same code
- Eliminates model bias (models prefer their own code)
- **Voting System**: 2-of-3 model agreement provides confidence
- **Best Practice**: Review by different model than code generator
- Can create separate branches for each model evaluation

---

## Section 8: Custom Agents and Chat Modes (Duration: 00:08:00)

**Timestamps**: 01:19:42 - 01:27:42

### Key Topics

- Creating domain-specific agents
- Prompt files vs instruction files
- Agent command definition
- Solutions architect example
- Agent expertise areas

### Agent Use Cases

- **C# Development**: Language-specific standards
- **C++ Development**: Language-specific patterns
- **Unit Testing**: Testing best practices
- **Refactoring**: Code improvement strategies
- **Architecture**: Design patterns and decisions

### Agent Configuration

- Define expert domain areas
- Create custom commands for agent
- Link commands to specific prompts
- Target functionality to agent specialization

### Example: Solutions Architect Agent

- Expert in specific software development areas
- Custom commands for common architectural tasks
- Integrates with prompt files for standardized workflows
- Maintains consistent architectural guidance

---

## Section 9: Advanced Topics and Q&A (Duration: 00:30:11)

**Timestamps**: 01:27:42 - 01:57:53

### Key Topics

- Azure DevOps vs GitHub future
- Complex code base scenario discussions
- Agent-based workflow optimization
- Brownfield modernization strategies

### Azure DevOps Discussion

- Microsoft favoring GitHub long-term
- GitHub has better AI integration currently
- Azure DevOps extensions available but less mature
- Issue types: Azure (features, PBIs, tasks, bugs) vs GitHub (issues with labels)

### Brownfield Modernization Insights

- Real-world scenario: inheriting unfamiliar codebase
- Hour-long analysis can establish comprehensive backlog
- Bottleneck shifts from fixing to reviewing and prioritizing
- Human oversight critical for:
  - Prioritization decisions
  - Code review validation
  - Business impact assessment
  - Architecture decisions

### Visual Studio Code Version Issue

- Compatibility issue between VS Code and Copilot extensions
- Solution: Update to VS Code 1.109.2 or later
- API change required updated VS Code version
- Critical for Copilot functionality

---

## Summary Statistics

- **Total sections**: 9
- **Average section length**: ~13 minutes
- **Longest section**: Exercise 2 - Building Technical Debt Backlog (24:00)
- **Shortest section**: Copilot Licensing Discussion (01:19)
- **Total exercises**: 2
- **Technical issues resolved**: 6+
- **Participant questions**: 15+

---

## Key Takeaways

1. **Azure DevOps Integration**: Multiple paths for GitHub Copilot integration with Azure DevOps through marketplace extensions

2. **Cost-Effective Licensing**: Individual developers can access business features by creating GitHub organization for $19/month

3. **Technical Debt Discovery**: AI can rapidly identify and categorize technical debt across multiple dimensions (security, testing, complexity, etc.)

4. **Automated Backlog Creation**: GitHub CLI integration enables automatic issue creation from code analysis

5. **Multi-Model Review Strategy**: Using different AI models for code review eliminates bias and increases confidence

6. **Copilot Workspace**: Issues can be assigned directly to Copilot for autonomous implementation with human oversight

7. **Custom Agents**: Domain-specific agents (architecture, testing, security) provide specialized guidance and workflows

8. **Modernization Workflow**:
   - Analyze codebase (~1 hour for comprehensive audit)
   - Create prioritized backlog
   - AI implements fixes
   - Human reviews and approves
   - Bottleneck is review/prioritization, not implementation

9. **Enterprise Constraints**: Enterprise GitHub accounts may restrict forking; personal accounts provide workaround

10. **Tool Integration**: GitHub CLI, VS Code extensions, and environment configuration critical for smooth workflow

---

**Document Created**: 2026-02-17
**Source File**: AI-Assisted Software Development with GitHub Copilot (Wed Morning).vtt
**Generated By**: AI Summary Tool
**Session Date**: 2026-02 (Week of course delivery)
**Course**: AI-Assisted Software Development with GitHub Copilot
