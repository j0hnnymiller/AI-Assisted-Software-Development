# AI-Assisted Software Development with GitHub Copilot (Wed Afternoon)

## Overview

- **Total Duration**: 02:05:38 (2 hours, 5 minutes, 38 seconds)
- **Sections**: 10 major sections
- **Format**: VTT (WebVTT)
- **Primary Speaker**: John Miller
- **Date**: Wednesday Afternoon Session (February 2026)

---

## Section 1: Introduction and Exercise Continuation (Duration: ~00:05:30)

**Time Range**: 00:04:39 - 00:10:00

### Key Topics

- Welcome back and exercise continuation
- Test automation exercise progress check
- Student participation and readiness assessment

### Main Activities

- Instructor checking student progress on ongoing exercise
- Students raising hands to indicate completion status
- Q&A opportunity for students with questions

---

## Section 2: Prompt Guidance Discussion (Duration: ~00:12:30) [x]

**Time Range**: 00:16:41 - 00:29:09

### Key Topics

- Structured prompting for AI-assisted development
- Effective prompt examples for activities
- Avoiding literal copying of activity descriptions

### Key Exchanges

**Student Question (Tom Bui)**: Request for example prompts for activity items

- Problem: Literally typing activity descriptions (e.g., "run linting and architectural checks")
- **Instructor Response**:
  - Suggest prompts like "review the code base for conformance to architectural standards"
  - Look for "deviations between the architecture" or "weaknesses with the architecture"
  - For linting: "review the code base and identify any bad smells"
  - Go beyond what static linting tools can do

### Best Practices

- Phrase prompts to review architectural alignment
- Ask for analysis that goes beyond static tools
- Request identification of architectural improvements

---

## Section 3: Testing Frameworks (Duration: ~00:13:00) [x]

**Time Range**: 00:30:09 - 00:43:09

### Key Topics

- Comprehensive test weeks management
- Test review and validation strategies
- Balancing test coverage with maintainability
- Managing tests over time

### Subsection 3.1: Key Practices for Managing Tests Over Time

#### Core Principles

- **Prune obsolete tests regularly**: Remove tests for old or deprecated functionality
- **Update tests alongside code changes**: Preferably write tests before code (TDD approach)
- **AI enables easier TDD**: Ask AI to write tests first, then ensure implementation passes
- **Clear naming and structure**: Maintain organized test suites
- **Use code coverage reports**: Guide where changes are needed
- **Document test strategy**: Make it part of the codebase

### Subsection 3.2: Test Review and Validation

#### What AI Can Help With

- Detect missing assertions
- Identify redundant tests
- Find edge cases
- Flag inconsistent patterns

#### Critical Testing Principles

- **Validate intent, not implementation**: Test what code should do, not what it does
- **Focus on business logic validation**: Ensure architectural alignment
- **Consider AI-generated code**: If instructions are good, implementation should be close to expectations

### Subsection 3.3: Discussion on AI-Generated Tests

**Student Concern (Dan Blanchard)**: AI creates too many tests

- Problem: "10 tests for a 10-line method"
- Tests are overly verbose

**Instructor Response**:

- Create instruction files with test expectations
- Include value guidance for test importance
- Ask AI to identify tests needing updates for specific code changes
- Focus AI on updating applicable tests only

### Subsection 3.4: Test Validation Debate

**Student Question (Tom Bui)**: How to trust AI test corrections vs. catching real mistakes?

**Instructor Response**:

- Have AI explain what test does
- Use different model for analysis (reduce bias)
- Examine tests to verify accuracy
- Techniques build confidence in tests

### Key Takeaways

- Suggest edge cases for comprehensive coverage
- Validate intents, not just implementations
- Balance thoroughness with maintainability

---

## Section 4: Feature Flags and Test Suites (Duration: ~00:07:00) [x]

**Time Range**: 00:45:12 - 00:52:12

### Key Topics

- Feature flags for managing work-in-progress
- As-Is vs. To-Be test suites
- Safe deployment strategies

### Subsection 4.1: As-Is Test Suites

#### Purpose

- Capture current behavior in tests
- Protect against regressions
- Document expectations for production

#### Core Strategy

- Go to production anytime As-Is tests pass
- New implementations hidden behind feature flags
- High confidence with compiled code + passing As-Is tests

#### Growing the As-Is Suite

- Add tests before making code modifications
- Increase coverage as changes are identified
- Build trust in test suite incrementally

#### Critical Rule

- **Feature flag discipline**: Ensure new code wrapped by feature flags
- **Watch for bleed**: Any unwrapped code will hit production
- **As-Is tests as gate**: These define production readiness

### Subsection 4.2: To-Be Test Suites

#### Purpose

- Define future behavior
- Validate work-in-progress features
- Track implementation progress

#### Workflow

1. Implement feature flag around code to modify
2. When flag ON: Execute new behavior
3. Write tests that only run when feature flag ON
4. Separate test execution strategy in pipeline

#### Automation Strategy

**Phase 1**: As-Is Tests

- Set flags to match production state
- Run current behavior tests
- Look for regressions

**Phase 2**: To-Be Tests

- Turn on appropriate flags
- Execute To-Be testing
- Assess progress toward completion

#### Benefits

- Smaller To-Be suite for check-in procedures
- Guide modernization efforts
- Validate new practices and architectures

#### Maintenance Requirement

**After Production Release**:

- Move To-Be tests into As-Is suite
- Tests become part of regression suite
- Maintain consistency with production state

### Subsection 4.3: Feature Flag Retirement

**AI-Assisted Approach**:

- Before AI: Create pull request to implement flag, merge, retire later
- With AI: Ask to "identify changes needed to remove this feature flag"
- AI effectively removes feature flags from codebase

---

## Section 5: Testing in Production (Duration: ~00:07:00)

**Time Range**: 00:50:55 - 00:57:55

### Key Topics

- Safe production testing strategies
- Shadow traffic and canary releases
- Observability and automated rollback
- Beta testing groups

### Subsection 5.1: Engineered Production Testing

#### Core Principle

- Hide features behind flags until ready
- Test in real environment with real loads

#### Techniques

- **Shadow traffic**: Test with production-like traffic without user impact
- **Canary releases**: Gradual rollout to subset of users
- **Observability dashboards**: Real-time monitoring of issues
- **Automated rollback**: Auto-disable features exceeding error budgets

### Subsection 5.2: Error Budget Management

#### Automatic Feature Disabling

- Set error threshold for features
- Monitor error rate over time window
- Auto-disable if threshold exceeded
- Notify team for investigation

**Example**: "If more than X errors in Y minutes for this feature, disable and alert"

### Subsection 5.3: Beta Testing Strategy

#### Implementation

- Create pool of internal users or beta testers
- Enable features for specific user groups
- Test in production environment with real data
- Gather feedback before wider rollout

#### Benefits

- Real-world validation with actual loads
- Early detection of edge cases
- User behavior often unexpected
- Reduces risk of full-scale failure

### Subsection 5.4: Discussion on Database Schema Changes

**Student Question (Dan Blanchard)**: Can feature flags get complicated with database schema updates?

**Instructor Response**:

- Acknowledged complexity exists
- Suggested this is a valid concern requiring careful planning
- (Discussion appears to have continued but was not fully captured in transcript sample)

---

## Section 6: Addressing Technical Debt (Duration: ~00:08:00) [x]

**Time Range**: 00:59:49 - 01:07:49

### Key Topics

- Prompting Copilot to address technical debt
- Security vulnerability remediation
- JWT secret management
- Implementation planning

### Subsection 6.1: Technical Debt Remediation Example

#### Scenario

Working with technical debt issue (JWT secrets hardcoded in code)

#### Approach

**Before Implementation**: Ask AI for proposed implementation

- "Propose implementation to address Question #1"
- Review plan before execution
- Validate completeness

### Subsection 6.2: JWT Secret Security Fix

#### Issue Identified

- JWT secret hardcoded in source control
- Security vulnerability requiring immediate remediation

#### Recommended Fix Components

**Phase 1: Immediate Remediation**

1. Remove secret from source control
2. Replace with placeholder in code
3. Add configuration validation logic
4. Detect placeholder value and throw exception
5. Validate secret length and format

**Phase 2: Secure Configuration**

1. Initialize user secrets for local development
2. Use .NET user secrets command
3. Set new rotated secret value
4. Configure production environment variables
5. Store in secure secret management

**Phase 3: Enterprise-Grade Security**

1. Move from configuration to Key Vault (Azure Key Vault)
2. Configure secret in Key Vault
3. Retrieve from Key Vault in application
4. Implement interface for token retrieval

**Phase 4: Git History Cleanup**

1. Install git-filter-repo command
2. Search app settings files for secrets
3. Purge secret from repository history
4. Create new secret for rotation

**Phase 5: Testing Strategy**

1. Validation tests for secret configuration
2. Integration tests for secret retrieval
3. Environment configuration tests
4. Quality metrics and success criteria
5. Deployment checklist

### Subsection 6.3: Key Observations

**Instructor Notes**:

- Implementation plan more comprehensive than original issue
- Good opportunity to attach detailed plan to issue
- Can add steps as sub-issues or tasks
- Track implementation progress incrementally
- Some non-coding steps required (rotation, etc.)

**Critical Step**:

- **Rotate secret** after exposure in git
- Difficult to truly remove from git history
- Rotation is essential security practice

---

## Section 7: Implementation Review (Duration: ~00:04:00) [ ]

**Time Range**: 01:07:50 - 01:11:50

### Key Topics

- Selecting appropriate issues to implement
- Evaluating implementation complexity
- Issue selection criteria

### Activities

- Reviewed multiple technical debt issues
- Selected issue #5 (error handling improvements)
- Identified issues requiring non-coding steps
- Discussed try-catch improvements

### Implementation Decision

- Issue #1 (JWT secrets): Too many manual steps for demonstration
- Issue #5 (error handling): Better suited for live demonstration
- Plan to ask AI for implementation proposal first

---

## Section 8: AI Implementation Workflow (Duration: ~00:10:00)

**Time Range**: 01:11:51 - 01:21:50

### Key Topics

- Getting AI implementation proposals
- Verifying AI understanding of issues
- Starting implementation execution
- Implementation monitoring

### Subsection 8.1: Implementation Request Process

#### Best Practice Workflow

1. **Request Proposal First**: Don't execute immediately
   - "Propose implementation to address issue"
   - Review what AI thinks it will do
   - Verify understanding before execution

2. **Review Proposed Fix**
   - AI reads issue description
   - AI proposes specific fix
   - Human reviews for completeness

3. **Identify Gaps**
   - Check for missing steps
   - Example: JWT issue didn't include GitHub removal steps
   - Add requirements before proceeding

4. **Proceed with Implementation**
   - "Go ahead with the implementation"
   - Can reference conversation on different machine later
   - Save implementation plan as reference

### Subsection 8.2: Multi-Tasking with AI

**Concurrent Work**:

- Can start implementation in one session
- Continue with other tasks
- Monitor progress via notifications
- AI works autonomously once started

### Preview of Next Topic

**Instructor Note**: Will demonstrate multi-implementation comparison

- Technique for evaluating pros and cons
- Compare different solutions to problems
- Find and evaluate alternatives

---

## Section 9: Effective Prompts for Technical Debt (Duration: ~00:08:30)

**Time Range**: 01:22:35 - 01:31:05

### Key Topics

- Crafting effective technical debt prompts
- GitHub issue management
- Copilot integration with GitHub
- Issue creation and assignment

### Subsection 9.1: Prompt Components

#### Required Elements

- **Clear description of debt**: What problem exists
- **Constraints and architectural rules**: Beyond instruction files
- **Expected outcomes**: What success looks like
- **Required test updates**: Testing strategy
- **Documentation updates**: Required documentation
- **Provenance requirements**: Not in instruction files

#### Benefits

- Faster remediation
- Consistent application of fixes
- Reduced manual effort
- Standardized approach

### Subsection 9.2: GitHub Integration

#### Issue Management via Copilot

**Method 1: Direct Issue Creation**

- Command: "Post issue #6 to the GitHub [repo]"
- Copilot creates issue in GitHub
- Can specify labels, assignees, etc.

**Challenges Encountered**:

- Wrong repository selected initially
- Required full repository name format: `owner/repository`
- Need to enable issues in repository settings

**Resolution**:

- Provide explicit repository path
- Verify settings in GitHub
- Use format: `owner/repository-name`

#### Assigning Issues to Copilot

**Paid Subscription Feature**:

1. Create issue in GitHub
2. Assign to @copilot
3. Copilot creates work-in-progress branch
4. Implements solution autonomously
5. Sends notifications on progress
6. Creates pull request when complete

**Requirements**:

- Enterprise license OR
- Pro Plus subscription
- Repository in appropriate organization (for Enterprise)

**Student Discussion**:

- Free plan users cannot access this feature
- Enterprise repos must be in enterprise org
- Chris Bishop confirmed org requirement

### Subsection 9.3: Live Demonstration

**Example Workflow**:

1. Created issue from file content
2. Attempted to post to GitHub
3. Encountered repository selection issue
4. Corrected repository reference
5. Issue successfully created
6. Assigned to @copilot
7. Copilot began autonomous implementation

**Observations**:

- Parallel execution: Issue #5 implementation running simultaneously
- Notifications received as work progresses
- WIP (work-in-progress) branch created automatically

---

## Section 10: Hands-On Exercise (Duration: ~00:17:00)

**Time Range**: 01:47:24 - 02:04:33

### Key Topics

- Student implementation practice
- Pull request workflow
- GitHub Actions and workflow approvals
- Troubleshooting

### Subsection 10.1: Student Progress Monitoring

**Activities**:

- Instructor monitoring student progress
- Students raising hands when still working
- Individual help for questions
- Notifications tracking completed work

### Subsection 10.2: Workflow Approval Issues

**Student Question (Dan Blanchard)**: Workflow awaiting approval

**Issue**:

- Pull requests showing "1 workflow awaiting approval"
- Required manual approval for workflows
- Appeared on multiple pull requests

**Discussion**:

- Unclear if setting or security requirement
- Option to approve workflows manually
- "Learn more" link available for details

### Subsection 10.3: Copilot PR Review Issues

**Student Question (Matt Hoffman)**: @copilot not reviewing PRs

**Issue**:

- Tagged @copilot in PR like instructor demonstrated
- No action taken by Copilot
- Suspected organizational/subscription limitation

**Instructor Response**:

- Likely free plan limitation
- Not available on free tier
- Should work with Pro Plus (confirmed working)

**Additional Context (Chris Bishop)**:

- Enterprise requires repo in enterprise org
- Copilot code review needs Enterprise license
- Special organizational URL for enterprise repos
- Further isolation and additional features

---

## Section 11: Session Wrap-Up and Preview (Duration: ~00:01:05)

**Time Range**: 02:04:33 - 02:05:38

### Key Topics

- Exercise completion check
- Preview of next session topics
- Closing remarks

### Next Session Preview

**Topic: Multi-Implementation Comparison**

- Technique for evaluating pros and cons
- Compare different implementations
- Find multiple solutions to problems
- Evaluate alternatives systematically

**Transition Announcement**:

- Moving into Greenfield part of course
- Workspace cleanup needed
- Questions can be addressed in morning

### Closing

- Encouragement to continue practicing
- Morning pickup for any remaining questions
- Session officially concluded

**Farewells**:

- Multiple students thanking instructor
- Professional sign-offs
- End of Wednesday afternoon session

---

## Summary Statistics

- **Total major sections**: 11
- **Average section length**: ~11:30 minutes
- **Longest section**: Testing Frameworks (~13 minutes)
- **Shortest section**: Session Wrap-Up (~1 minute)
- **Total hands-on time**: ~17 minutes (Section 10)
- **Total lecture/demonstration**: ~1:47 hours

---

## Key Themes Throughout Session

### 1. **AI-Assisted Test Automation**

- Writing tests with AI assistance
- Managing test suites effectively
- Balancing coverage with maintainability

### 2. **Feature Flag Strategy**

- As-Is and To-Be test suites
- Safe deployment practices
- Production testing with feature flags

### 3. **Technical Debt Management**

- Using AI to propose remediation
- Security vulnerability fixes
- Comprehensive implementation planning

### 4. **GitHub Integration**

- Issue creation and tracking
- Assigning work to Copilot
- Automated implementation workflows

### 5. **Best Practices**

- Effective prompting strategies
- Validation before execution
- Incremental implementation approach

---

## Speaker Engagement Summary

### Primary Speaker

**John Miller** (Instructor)

- Led all major discussions
- Demonstrated technical workflows
- Answered student questions
- Provided implementation guidance

### Active Student Participants

- **Tom Bui**: Prompt guidance questions, test validation concerns
- **Dan Blanchard**: AI test generation concerns, feature flag complexity, workflow approvals
- **Chris Bishop**: GitHub enterprise clarifications
- **Matt Hoffman**: Copilot PR review issues
- **Christopher L Rockwell**: Technical assistance during demos
- **Lyle Ubben**: Brief interaction
- **Stephen Childs**: Confirmation responses

---

## Technical Topics Covered

### Development Practices

- Test-driven development with AI
- Code review and validation
- Architectural alignment checking
- Linting and code quality

### Security

- Secret management
- JWT security best practices
- Key vault integration
- Git history cleanup

### DevOps

- CI/CD pipeline integration
- Feature flag management
- Canary releases
- Observability and monitoring

### AI Tools

- GitHub Copilot
- Copilot Workspace
- Automated issue resolution
- Pull request automation

---

## Learning Outcomes

By the end of this session, participants should understand:

1. How to craft effective prompts for test automation
2. Strategies for managing test suites over time
3. Using feature flags for safe deployments
4. Testing in production safely
5. Addressing technical debt with AI assistance
6. Integrating AI tools with GitHub workflows
7. Best practices for AI-assisted development
8. Common challenges and solutions with AI tools

---

**Document Generated**: 2026-02-17
**Format**: Structured Markdown Summary
**Source**: VTT Transcript Analysis
**Total Content**: ~2 hours of training material
