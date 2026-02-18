# AI-Assisted Software Development with GitHub Copilot (Friday Morning Session)
## Session Summary

**Date**: February 2026
**Duration**: ~1 hour 41 minutes (00:00:57 - 01:41:24)
**Speakers**: John Miller (Instructor), Dan Blanchard, Christopher L Rockwell, Chris Bishop, Buddy Toups
**Format**: Hands-on workshop with live demonstration and pair programming

---

## Table of Contents
1. [Opening and Introductions](#1-opening-and-introductions)
2. [AI Practitioner Resources Overview](#2-ai-practitioner-resources-overview)
3. [AI-First Development Methodology](#3-ai-first-development-methodology)
4. [GitHub Project Workflow Exploration](#4-github-project-workflow-exploration)
5. [Dependency Analysis and Planning](#5-dependency-analysis-and-planning)
6. [Vertical Slice Implementation](#6-vertical-slice-implementation)
7. [Pull Request and Code Review](#7-pull-request-and-code-review)

---

## 1. Opening and Introductions
**Time**: 00:00:57 - 00:04:10
**Duration**: ~3 minutes

Brief greetings and session setup. John Miller welcomes participants and prepares to share screen for the day's agenda.

**Key Points**:
- Morning greetings from all participants
- Session preparation and technical setup

---

## 2. AI Practitioner Resources Overview
**Time**: 00:04:10 - 00:14:05
**Duration**: ~10 minutes

John Miller introduces and demonstrates the "AI Practitioner Resources" application - a custom tool he created to manage AI-related resources and processes.

**Topics Covered**:
- **00:04:10 - 00:05:25**: Introduction to the AI Practitioner Resources page
  - Only three slides for the day
  - Application has significant bearing on the course content

- **00:05:25 - 00:06:38**: Questions about optional tools
  - Discussion about Pandoc and Marp (markdown presentation tools)
  - Clarification that these are optional, not required for the course

- **00:06:42 - 00:14:05**: Detailed walkthrough of AI resources functionality
  - GitHub Actions integration for gist storage
  - Risk scoring mechanism for AI-generated content
  - Repository structure and organization
  - Storage and retrieval of AI prompts and responses

**Key Concepts**:
- Gist-based storage system for AI artifacts
- Automated risk assessment
- Integration with GitHub workflows

---

## 3. AI-First Development Methodology
**Time**: 00:14:05 - 00:18:00
**Duration**: ~4 minutes

Discussion of the AI-first and prompt-first development philosophy that guides the course approach.

**Topics Covered**:
- Definition of AI-first development approach
- Prompt-first methodology: creating prompts before implementation
- How AI artifacts are tracked and managed
- Relationship between prompts, issues, and implementation

**Key Principles**:
- Start with clear prompts that define requirements
- Use AI to generate implementation plans
- Track provenance of all AI-generated artifacts
- Maintain transparency in AI-assisted development

---

## 4. GitHub Project Workflow Exploration
**Time**: 00:18:00 - 00:45:00
**Duration**: ~27 minutes

Comprehensive exploration of GitHub project structure, contributor workflows, and issue management.

**Topics Covered**:
- **00:18:00 - 00:25:00**: GitHub repository structure
  - Project organization and file layout
  - Contributor guidelines
  - Workflow documentation

- **00:25:00 - 00:31:00**: Issue creation and management
  - How to create issues from AI-generated plans
  - Issue templates and structure
  - Linking issues to implementation work

- **00:31:00 - 00:36:00**: Implementation planning review
  - Reviewing AI-generated implementation plans
  - Discussion of vertical slices (30 slices identified)
  - Removing sprint and duration estimates to focus on continuous flow

- **00:36:00 - 00:45:00**: Diagram generation and visualization
  - Using AI to generate dependency diagrams
  - Troubleshooting diagram rendering issues
  - Mermaid diagram syntax and common errors

**Key Points**:
- Implementation plan contains 30 vertical slices
- Focus on continuous delivery rather than time-boxed sprints
- Start with foundational slices and progress through dependencies
- AI tools can generate visual diagrams but often need refinement

---

## 5. Dependency Analysis and Planning
**Time**: 00:45:00 - 00:48:30
**Duration**: ~3.5 minutes

Brief discussion of dependency graphs and how they inform implementation sequencing.

**Topics Covered**:
- Reading and interpreting dependency diagrams
- Understanding which slices must be completed before others
- Identifying the critical path through implementation
- Foundational vs. dependent features

**Key Insights**:
- Dependency graphs help visualize implementation order
- Some slices can be parallelized, others are sequential
- Foundational work must be completed first

---

## 6. Vertical Slice Implementation
**Time**: 00:48:30 - 01:30:00
**Duration**: ~41.5 minutes

Hands-on implementation of the first vertical slice using AI assistance and pair programming.

**Topics Covered**:
- **00:48:30 - 01:00:00**: Setting up for implementation
  - Selecting the first slice to implement
  - Reviewing acceptance criteria
  - Setting up Git branches and workspace

- **01:00:00 - 01:09:00**: Issue review and scope verification
  - Comparing implementation prompt to generated issue
  - Identifying scope mismatches
  - Discussion of rescoping or splitting issues
  - Prompt refinement considerations

- **01:09:00 - 01:20:00**: Live coding with AI assistance
  - Using GitHub Copilot for code generation
  - Reviewing generated code
  - Discussing file organization (webcat-frontend folder structure)
  - Implementation of foundational web components

- **01:20:00 - 01:30:00**: Manual verification steps discussion
  - AI-generated implementation includes manual verification checklist
  - Discussion of automating vs. manual verification
  - Improving prompts to favor automated testing
  - Reviewing verification requirements

**Key Technical Details**:
- Vertical slice: "Implement Foundational WebCat"
- File structure: webcat-frontend folder with component organization
- Question about whether implementation plan should be updated when issues are split
- Focus on automated testing rather than manual verification steps

---

## 7. Pull Request and Code Review
**Time**: 01:30:00 - 01:41:24
**Duration**: ~11.5 minutes

Creating pull request, initiating code reviews (both human and AI), and addressing feedback.

**Topics Covered**:
- **01:30:00 - 01:33:00**: Creating the pull request
  - Branch naming: "slice-1"
  - Git workflow: commit, push, create PR
  - Associating PRs with issues (development section)

- **01:33:00 - 01:36:00**: Code review process
  - Assigning reviewers (Christopher)
  - Initiating GitHub Copilot code review
  - Waiting for AI-generated review comments
  - Assigning issue to implementer (Dan Blanchard)

- **01:36:00 - 01:39:00**: Reviewing AI feedback
  - AI identifies missing AI provenance metadata in markdown files
  - Discussion of DOM element access patterns
  - Multiple code quality issues flagged

- **01:39:00 - 01:41:24**: Addressing review comments
  - How to reference specific review comments
  - Copy-paste vs. direct AI interaction with comments
  - Fixing issues: AI metadata, code patterns
  - Discussion of when to implement vs. ignore certain suggestions

**Key Issues Identified**:
- **Markdown files missing AI provenance metadata**: AI reviewer caught missing metadata that should track the generation source
- **DOM element access patterns**: Suggestions for improved DOM manipulation
- **Multiple other code quality concerns**: Various improvements suggested by AI reviewer

**Process Insights**:
- GitHub Copilot can be added as code reviewer
- AI review takes a few minutes to complete
- Review comments can be addressed individually or in batch
- Some AI suggestions may be contextual and require judgment
- Manual reviewers work in parallel with AI reviewers

---

## Summary Statistics

**Total Duration**: ~1 hour 41 minutes
**Number of Major Topics**: 7
**Number of Speakers**: 5
**Primary Activities**:
- Lecture/Demo: ~35% (AI resources, methodology, project structure)
- Live Implementation: ~40% (vertical slice coding)
- Code Review: ~15% (PR creation and review process)
- Q&A/Discussion: ~10% (scattered throughout)

**Key Concepts Introduced**:
1. AI Practitioner Resources application
2. AI-first and prompt-first development
3. Vertical slice architecture (30 slices for project)
4. Continuous flow vs. sprint-based planning
5. AI-assisted code review
6. Provenance tracking for AI-generated artifacts

**Technical Tools Used**:
- GitHub (Issues, Projects, Pull Requests)
- GitHub Copilot (coding assistance and code review)
- VS Code (development environment)
- Mermaid (diagram generation)
- Git (version control workflow)

**Learning Outcomes**:
- Understanding AI-first development workflow
- Creating and managing vertical slices
- Using AI for implementation and review
- Balancing AI assistance with human judgment
- Proper provenance tracking for AI artifacts
- Git workflow for AI-assisted development

---

## Notable Quotes

> "Today we're going to start off with AI practitioner resources. This is an application I created that I has, I think, a lot of bearing on what we're doing in the course." - John Miller (00:04:20)

> "I asked it to remove a Sprint and duration estimates because... I instead wanted to treat this as a continuous stream of work, you know, without any time boxing around the work." - John Miller (00:36:19)

> "The implementation prompts should be automated... we should be able to determine at the very end that the based on the verification steps that are automated that it's working correctly." - John Miller (01:27:54)

---

## Next Steps and Follow-up Items

Based on the session content:

1. **Prompt Refinement**: Update implementation prompts to emphasize automated testing over manual verification steps
2. **Issue Management**: Determine how to handle scope mismatches between prompts and generated issues
3. **Implementation Plan**: Consider whether plan should be updated when issues are split or rescoped
4. **Code Reviews**: Address AI-generated feedback, particularly around provenance metadata
5. **Continue Implementation**: Move to next vertical slice after completing PR review and merge

---

**End of Summary**

*This summary was generated from WebVTT transcript: "AI-Assisted Software Development with GitHub Copilot (Fri Morning).vtt"*
*Session recorded: February 2026*
