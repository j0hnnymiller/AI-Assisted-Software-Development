---
ai_generated: true
model: "anthropic/claude-3.5-sonnet@2024-10-22"
operator: "johnmillerATcodemag-com"
chat_id: "code-translation-hotspot-20260317"
prompt: |
  create a marp deck titled "Code Translation and Technical Hotspot Analysis" explaining the following content:

  Translating code between languages; Instruction compliance review; Scoped analysis for specific files/projects; Creating GitHub issues from findings
started: "2026-03-17T22:30:00Z"
ended: "2026-03-17T22:45:00Z"
task_durations:
  - task: "content planning and structure"
    duration: "00:05:00"
  - task: "slide authoring"
    duration: "00:10:00"
total_duration: "00:15:00"
ai_log: "ai-logs/2026/03/17/code-translation-hotspot-20260317/conversation.md"
source: "johnmillerATcodemag-com"
---

## Code Translation and Technical Hotspot Analysis

- **Code Translation** between programming languages
- **Instruction Compliance** review and validation
- **Scoped Analysis** for targeted code review
- **GitHub Issues** automated creation from findings

::: notes
Introduce this module as covering advanced AI-assisted code analysis techniques. Emphasize that AI can help translate code between languages, verify instruction compliance, analyze specific code sections for technical debt, and automatically create GitHub issues from findings.

Key points:

- Code translation is useful for migrations and modernization
- Compliance review ensures standards are followed
- Scoped analysis targets specific problem areas
- Automated issue creation streamlines workflow

Timing: 1-2 minutes on this overview slide.
Transition: "Let's start with code translation..."
:::

---

## Code Translation Between Languages

**The Challenge**: Migrating codebases across languages

**Why Translate?**

- Modernizing legacy systems
- Platform migration (e.g., .NET Framework → .NET Core)
- Performance optimization
- Team expertise realignment

**AI-Assisted Approach**:

- Semantic understanding beyond syntax
- Preserves business logic and intent
- Identifies idiom mismatches

::: notes
Explain the common scenarios where code translation is necessary. Emphasize that AI goes beyond simple syntax conversion—it understands semantic intent and can identify when direct translation would lose meaning.

Real-world examples:

- Legacy VB6 to C#migrations
- Java to Kotlin conversions
- JavaScript to TypeScript upgrades

Key point: AI can preserve business logic that would be lost in simple syntax translation. For example, converting Python's dynamic typing to TypeScript's static typing requires understanding the intended types.

Timing: 3-4 minutes.
Transition: "Let's look at the translation process..."
:::

---

## Translation Process

**Step 1: Analyze Source Code**

```prompt
Analyze this [source language] codebase and identify:
- Core business logic
- Framework dependencies
- External integrations
- Architecture patterns
```

**Step 2: Request Translation Strategy**

```prompt
Propose a translation strategy for migrating this
[source] code to [target language], including:
- Framework equivalents
- Dependency mapping
- Test coverage approach
```

---

## Translation Best Practices

**Request Incremental Translation**:

- Translate module by module, not entire codebase
- Start with pure utility functions (no dependencies)
- Progress to components with external dependencies

**Validation Strategy**:

- **Parallel testing**: Run both versions with same inputs
- **Behavioral comparison**: Assert identical outputs
- **Performance benchmarking**: Compare metrics

**Critical Prompt Additions**:

```prompt
Include unit tests that verify behavioral equivalence
Flag any semantic differences requiring manual review
```

---

## Example: Python to TypeScript

**Source (Python)**:

```python
def calculate_discount(price: float, tier: str) -> float:
    """Calculate discount based on customer tier"""
    rates = {"gold": 0.20, "silver": 0.10, "bronze": 0.05}
    return price * (1 - rates.get(tier, 0))
```

**AI Translation Prompt**:

```prompt
Translate this Python function to TypeScript with:
- Proper type definitions
- Equivalent error handling
- Jest unit tests
```

---

## Example: Python to TypeScript (Result)

**Target (TypeScript)**:

```typescript
type CustomerTier = "gold" | "silver" | "bronze";

export function calculateDiscount(price: number, tier: CustomerTier): number {
  const rates: Record<CustomerTier, number> = {
    gold: 0.2,
    silver: 0.1,
    bronze: 0.05,
  };

  return price * (1 - (rates[tier] || 0));
}
```

**AI Advantages**: Type safety, idiomatic patterns, testability

---

## Instruction Compliance Review

**Purpose**: Ensure codebase adheres to project standards

**Common Instruction Categories**:

- **Architectural patterns** (vertical slice, CQRS, etc.)
- **Naming conventions** (file names, classes, methods)
- **Security policies** (secret management, authentication)
- **Documentation requirements** (comments, README updates)
- **Testing standards** (coverage, test structure)

**AI Role**: Automated compliance auditing

---

## Setting Up Compliance Review

**Step 1: Identify Instruction Files**

Your repository's `.github/instructions/` directory contains:

- `vertical-slice-architecture.instructions.md`
- `dependency-management-policy.instructions.md`
- `ai-assisted-output.instructions.md`
- Custom project-specific instructions

**Step 2: Scope the Review**

```prompt
Review the codebase for compliance with the instructions in:
- .github/instructions/vertical-slice-architecture.instructions.md
- .github/instructions/dependency-management-policy.instructions.md

Focus on: [specific module/feature/service]
```

---

## Compliance Review Prompts

**Architectural Compliance**:

```prompt
Analyze [repository/folder] for conformance to
vertical slice architecture as defined in
.github/instructions/vertical-slice-architecture.instructions.md

Identify:
- Feature folders not following the structure
- Shared dependencies violating boundaries
- Missing handlers or validators
```

**Security Compliance**:

```prompt
Review [codebase] for security policy violations:
- Hardcoded secrets or credentials
- Missing authentication/authorization
- Vulnerable dependencies (check against policy)
- Non-compliant secret management
```

---

## Interpreting Compliance Results

**AI Output Structure**:

1. **Compliant Areas**: What's working correctly
2. **Violations**: Specific deviations with file/line references
3. **Recommendations**: Actionable fixes
4. **Severity**: Critical, High, Medium, Low

**Example Finding**:

> **Violation**: `Features/Orders/CreateOrder.cs` (Line 45)
>
> **Issue**: Handler directly accesses database context instead of using repository abstraction
>
> **Policy**: Vertical Slice Architecture requires repository pattern for data access
>
> **Recommendation**: Extract data access to `OrderRepository.cs`

---

## Scoped Analysis for Specific Files/Projects

**Why Scope Analysis?**

- Large codebases overwhelm AI context windows
- Focus on changed files in a pull request
- Target known problem areas
- Incremental modernization

**Scoping Strategies**:

- **File-level**: Single file or small file set
- **Folder-level**: Feature module or service
- **Commit-level**: Git diff between commits
- **Issue-level**: Files related to specific GitHub issue

---

## Scoped Analysis Techniques

**Analyzing Changed Files in a PR**:

```bash
gh pr diff 123 --name-only > changed_files.txt
```

Then prompt:

```prompt
Analyze these files for code quality issues:
[paste file list from changed_files.txt]

Check for:
- Code smells and anti-patterns
- Performance bottlenecks
- Security vulnerabilities
- Test coverage gaps
```

---

## Scoped Analysis Techniques (cont.)

**Feature-Specific Analysis**:

```prompt
Analyze the OrderManagement feature in Features/Orders/
for the following concerns:

1. Thread safety in OrderProcessor
2. SQL injection vulnerabilities
3. Missing error handling
4. Incomplete test coverage
5. Compliance with vertical slice architecture

Provide specific file/line references for findings.
```

**Hotspot Identification**:

```prompt
Identify technical hotspots in [folder/service]:
- High cyclomatic complexity (> 10)
- Long methods (> 50 lines)
- Deeply nested conditionals (> 4 levels)
- Duplicate code blocks
```

---

## Advanced Scoping: Git-Based Analysis

**Review Recent Changes**:

```prompt
Using git log, identify files modified in the last 30 days
related to authentication. Analyze those files for:
- Security vulnerabilities
- Breaking changes
- Missing migration scripts
- Test coverage
```

**Compare Branches**:

```prompt
Compare feature-branch with main to identify:
- New dependencies added
- Configuration changes
- Database schema modifications
- API contract changes

Assess risk and required documentation updates.
```

---

## Creating GitHub Issues from Findings

**Automated Issue Creation Workflow**:

1. **Analysis Phase**: AI identifies problems
2. **Issue Drafting**: AI generates structured issue content
3. **Review Phase**: Human validates findings
4. **Creation Phase**: Post issues to GitHub

**Benefits**:

- Consistent issue formatting
- Comprehensive problem documentation
- Traceability from analysis to resolution
- Actionable remediation steps

---

## Issue Template Structure

**Effective AI-Generated Issues Include**:

```markdown
## Problem Description

[Clear explanation of the issue]

## Location

- File: [path]
- Line(s): [line numbers]
- Function/Class: [identifier]

## Impact

- Severity: [Critical|High|Medium|Low]
- Affected Component: [component name]

## Recommendation

[Specific steps to fix]

## Related Policy

[Link to instruction file violated]
```

---

## Example: Creating Issues from Compliance Review

**Step 1: Generate Issue Content**

```prompt
Based on the compliance violations identified, generate
GitHub issue descriptions following this template:
[paste issue template]

Create separate issues for:
1. Critical security findings
2. Architectural violations
3. Documentation gaps

Include labels: 'technical-debt', 'security', 'architecture'
```

---

## Example Issue: Security Violation

**AI-Generated Issue**:

```markdown
## Title

Security: Hardcoded JWT Secret in AuthService

## Description

The JWT signing secret is hardcoded in `Services/AuthService.cs`
at line 34, violating the dependency management policy
(.github/instructions/dependency-management-policy.instructions.md)

## Impact

- **Severity**: Critical
- **Security Risk**: Secret exposed in source control
- **Compliance**: Violates secret management policy

## Recommended Fix

1. Remove hardcoded secret from source
2. Move to Azure Key Vault or environment configuration
3. Implement secret rotation procedure
4. Purge secret from git history using git-filter-repo

## Related Files

- `Services/AuthService.cs` (Line 34)
- `.github/instructions/dependency-management-policy.instructions.md`
```

---

## Posting Issues to GitHub via Copilot

**Method 1: Direct Creation**

```prompt
Create a GitHub issue in repository owner/repo-name
with the following content:
[paste issue content]

Labels: technical-debt, security
Assignees: @security-team
```

**Method 2: Batch Creation**

```prompt
Create GitHub issues for all findings in the analysis.
Group related violations into single issues.
Use appropriate labels and severity markers.
```

**Copilot Integration**: With Pro/Enterprise, assign to @copilot for automated resolution

---

## Assigning Issues to @copilot

**Automated Resolution Workflow**:

1. **Create issue** via Copilot or GitHub UI
2. **Assign to @copilot** in the issue
3. Copilot creates WIP branch automatically
4. Copilot implements fix autonomously
5. Copilot creates pull request when complete
6. Human reviews and merges

**Requirements**:

- GitHub Copilot Pro Plus or Enterprise
- Repository in appropriate organization (for Enterprise)
- Copilot enabled for repository

---

## Best Practices: Issue Management

**Quality Over Quantity**:

- Don't create issues for every minor finding
- Group related violations into themes
- Prioritize by business impact and security risk

**Actionable Issues**:

- Include specific file/line references
- Provide clear reproduction steps (if applicable)
- Suggest concrete remediation approach
- Link to relevant policies/standards

**Tracking Progress**:

- Use labels for categorization (`security`, `tech-debt`, `architecture`)
- Create milestones for remediation sprints
- Link related issues together

---

## Workflow Integration

**Continuous Compliance**:

```yaml
# .github/workflows/compliance-check.yml
name: Compliance Review
on: [pull_request]
jobs:
  compliance:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run Compliance Analysis
        run: |
          gh copilot analyze compliance \
            --instructions .github/instructions/ \
            --scope ${{ github.event.pull_request.changed_files }}
```

**Automated Issue Creation**:

- Integrate with CI/CD pipeline
- Create issues for policy violations automatically
- Block PRs with critical findings

---

## Real-World Example: Technical Debt Sprint

**Scenario**: Legacy codebase modernization

**Phase 1: Discovery** (Scoped Analysis)

```prompt
Analyze Features/Legacy/ folder for:
- Deprecated API usage
- Missing error handling
- Hard-to-test code structures
- Security vulnerabilities
```

**Phase 2: Issue Generation**

- AI generates 15 issues across categories
- Team prioritizes by business impact

**Phase 3: Resolution**

- Critical: 3 security issues assigned to @copilot
- High: 5 architectural issues assigned to developers
- Medium: 7 tech-debt issues backlogged

---

## Measuring Success

**Key Metrics**:

- **Coverage**: % of codebase analyzed
- **Issue Resolution Rate**: Issues closed vs. created
- **Time to Resolution**: Average time from issue creation to closure
- **Compliance Score**: % of files passing compliance checks
- **Technical Debt Reduction**: Trend over time

**Reporting**:

```prompt
Generate a technical debt dashboard summarizing:
- Total issues by category
- Severity distribution
- Resolution progress
- Compliance trend over last 6 months
```

---

## Common Pitfalls and Solutions

**Pitfall 1: Context Window Overload**

- **Problem**: Analyzing entire codebase exceeds AI limits
- **Solution**: Use scoped analysis by folder/feature

**Pitfall 2: False Positives**

- **Problem**: AI flags compliant code as violations
- **Solution**: Refine instruction files with examples

**Pitfall 3: Issue Overload**

- **Problem**: Hundreds of issues overwhelming team
- **Solution**: Filter by severity, batch similar issues

**Pitfall 4: Inconsistent Standards**

- **Problem**: Different devs interpret policies differently
- **Solution**: Centralize instructions in `.github/instructions/`

---

## Advanced Techniques

**Cross-Repository Analysis**:

```prompt
Compare authentication implementation across:
- service-a/Features/Auth/
- service-b/Features/Authentication/
- service-c/Auth/

Identify inconsistencies and recommend standardization.
```

**Trend Analysis**:

```prompt
Analyze git history for the past 6 months to identify:
- Files with highest change frequency (hotspots)
- Modules with most bug fixes
- Areas with declining test coverage
```
