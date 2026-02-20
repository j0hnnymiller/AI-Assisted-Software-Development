# AI-Assisted Software Development with GitHub Copilot (Friday Afternoon)

## Overview

- **Total Duration**: 01:23:39
- **Sections**: 8
- **Format**: VTT (WebVTT)
- **Primary Instructor**: John Miller
- **Participants**: Chris Bishop, Dan Blanchard, Christopher Rockwell, Matt Hoffman, Lyle Ubben, Al (mentioned)

---

## Section 1: Session Opening & Vertical Slice Review (00:01:59 - 00:07:11)

**Duration**: 05:12

### Key Topics

- Welcome back after break
- Review of vertical slice diagram showing parallel implementation capabilities
- Discussion of VSO 2 (basic arithmetic capability) and VSO 3 dependencies
- Critical path identification for slice implementation
- Task assignment for vertical slices
- Al reported completing slices 1-10

### Subsections

#### Vertical Slice Dependency Review

- VSO 1 (completed) enables parallel implementation of multiple slices
- VSO 2 identified as good candidate to unblock VSO 3 on critical path
- Discusses slices numbered 7, 8, 13, 16 as first-tier candidates

---

## Section 2: Issue Identification & Diagram Corrections (00:07:11 - 00:15:07)

**Duration**: 07:56

### Key Topics

- Matt Hoffman identifies slices 6 and 7 are swapped in diagram
- AI review of slice numbering inconsistencies
- Use of AI to verify and correct slice titles in diagram
- Multiple iterations to fix parsing errors in Mermaid diagram
- Successfully rendered corrected diagram

### Subsections

#### AI-Assisted Diagram Validation

- Copilot used to analyze slice title discrepancies
- VSO 6: "Delete the last digit (backspace)" vs VSO 7: "Keyboard input"
- AI confirms titles were swapped in diagram
- Iterative debugging of Mermaid rendering issues

---

## Section 3: Slice 4 Showcase - Order of Operations (00:15:07 - 00:22:00)

**Duration**: 06:53

### Key Topics

- Chris Bishop demonstrates VSO 4 implementation (equals and result)
- Testing order of operations: 3 \* 2 + 5 = 11
- Edge case testing: division by zero error handling
- Float/precision testing
- Implementation completed using Cursor AI tool
- Discussion of AI doing development work vs. human specification

### Subsections

#### Test Scenarios Demonstrated

- Basic addition: 5 + 3 = 8
- Order of operations: 3 \* 2 + 5 = 11
- Edge case: 10 / 0 (error message displayed)
- Float precision: decimal calculations verified

#### Key Insight on Development Skills

- LinkedIn post discussion: value shifting from coding skills to specification/intent skills
- Chris notes he "didn't have to do any development myself"
- John emphasizes critical thinking and intent expression becoming primary skill

---

## Section 4: GitHub Code Review with Copilot (00:22:00 - 00:40:06)

**Duration**: 18:06

### Key Topics

- GitHub Copilot code review process for PR #4
- Review identified 8 comments/issues
- Unicode character usage in comparisons
- State management issues with error clearing
- Missing AI provenance metadata
- Unused constants and functions
- Commit suggestion feature demonstration

### Subsections

#### Code Review Findings

- **Unicode issues**: Minus sign character recommendations
- **State management**: Error state clearing leaves expression tokens intact
- **Compliance**: AI provenance header missing from previously compliant files
- **Dead code**: Unused constants and functions identified
- **Testing gaps**: Subtraction test coverage noted

#### Review Process Observation

- Copilot "thinking process" visible during review
- Manual resolution of comments required
- Discussion of using review output to improve instruction files
- Suggestion to tighten instruction files to prevent recurring issues

---

## Section 5: Slice 3 Showcase - Clear Button (00:40:06 - 00:54:22)

**Duration**: 14:16

### Key Topics

- Christopher Rockwell demonstrates VSO 3 implementation
- Merged Chris Bishop's VSO 4 work first
- Clear button functionality: resets calculator to zero
- Minimal new code - primarily integration work
- Discussion of merge conflicts from shared files

### Subsections

#### Implementation Details

- Clear button implementation: 2 + 3 + 6, then clear → 0, then 3 \* 3 = 9
- Successfully handled merge conflicts from VSO 4
- Copilot resolved conflicts on first try
- Some duplicate button issues found and fixed
- Provenance metadata issue identified in review

#### Merge Conflict Lessons

- Multiple slices modifying same files causes conflicts
- Suggestion to modularize code to reduce conflicts
- Acknowledge simple architecture makes separation challenging

---

## Section 6: GitHub CLI & PR Management (00:54:22 - 01:05:34)

**Duration**: 11:12

### Key Topics

- Discussion of default merge strategy (squash vs. merge commit)
- GitHub settings navigation for pull request configuration
- Requesting Copilot code reviews via GitHub web interface
- GitHub CLI commands for resolving PR comments
- Personal access token permissions for CLI operations

### Subsections

#### GitHub PR Tools & Extensions

- GitHub Pull Requests extension for VS Code
- Viewing PRs directly in IDE for easier context management
- Lyle Ubben explores resolving comments programmatically via CLI
- John investigates `gh pr comment` commands for resolution

#### Permission & Access Issues

- Personal access token scope restrictions
- Classic tokens vs. fine-grained tokens discussion
- Need for proper permissions to use CLI review features

---

## Section 7: Development Process Q&A (01:05:34 - 01:11:21) [ ]

**Duration**: 05:47

### Key Topics

- Question about merge conflict resolution strategies
- Dan asks about best practices (VS Code vs. GitHub web)
- Question from Al about creating requirements documents (PRD files)
- Discussion of when AI can generate requirements vs. domain expertise needs

### Subsections

#### Merge Conflict Best Practices

- Accept current vs. incoming changes typically resolves most conflicts
- VS Code merge editor recommended
- Architecture should minimize conflicts through module isolation
- Acknowledgment that simple single-file architecture increases conflicts

#### Requirements Document Creation

- AI can assist but cannot replace domain expertise
- Teams must build requirements for their specific problem domain
- AI useful for structure and refinement, not domain knowledge
- Reference to previous day's calculator PRD generation exercise

---

## Section 8: Adoption Strategy & Wrap-up (01:11:21 - 01:23:39)

**Duration**: 12:18

### Key Topics

- Dan asks about takeaways and organizational adoption
- John outlines step-by-step adoption strategy
- Greenfield vs. Brownfield approaches
- Iterative improvement process for instruction files
- Real-world experience emphasis

### Subsections

#### Step 1: Build Instruction Files

- Start with core instruction files to govern development process
- Use provided instruction files as starting point
- Add technology-specific instructions
- Review and customize metadata requirements

#### Step 2: Brownfield Analysis

- Use AI to interrogate existing codebase
- Identify deviations from standards and conventions
- Build backlog of technical debt
- Prioritize improvements through AI analysis

#### Step 3: Greenfield Setup

- Bring in core instructions
- Add technology stack-specific instruction files
- Build requirements documents
- Use agents to break down features into implementation prompts

#### Step 4: Iterative Refinement

- Review AI-generated output quality
- Update instruction files based on review feedback
- Repeat generation to validate improvements
- Build on successful patterns for new capabilities

#### Key Philosophy

- Iterating on guardrails and prompts, not just code
- Similar to code iteration but at instruction/prompt level
- Continuous improvement of instruction files
- Build knowledge base over time

---

## Summary Statistics

- **Total sections**: 8
- **Average section length**: 10:27
- **Longest section**: Code Review with Copilot (18:06)
- **Shortest section**: Session Opening (05:12)
- **Primary activities**: Code review, demonstrations, Q&A, process discussion
- **Slices showcased**: VSO 3 (Clear button), VSO 4 (Order of operations)
- **Pull requests reviewed**: 2
- **Participants actively demonstrating**: 2 (Chris Bishop, Christopher Rockwell)
