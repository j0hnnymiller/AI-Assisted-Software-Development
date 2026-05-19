# AI-Assisted Software Development with GitHub Copilot (Tuesday Morning Session)

**Recording Date**: February 2026
**Session Duration**: 02:04:14 (2 hours, 4 minutes, 14 seconds)
**Primary Instructor**: John Miller
**Session Type**: Brownfield Development - Advanced Context Techniques

---

## Overview

This morning session focused on brownfield development with GitHub Copilot, emphasizing safety measures, context management, instruction files, and hands-on exercises for creating prompt files and instruction files. The session covered advanced techniques for managing AI-assisted development in existing codebases with a strong emphasis on provenance tracking and reproducible workflows.

**Key Themes**:

- Brownfield vs. Evergreen software development concepts
- Safety measures and guardrails for AI-assisted coding
- Advanced context management techniques
- Instruction files and their role in guiding AI behavior
- Provenance tracking for AI-generated artifacts
- Hands-on prompt file creation exercises

---

## Session Breakdown

### 1. Pre-Session & Introductions

**Duration**: 00:00:24 - 00:06:26 (6:02)

**Content**:

- Small talk about music, guitars, and personal interests
- Participants joining and technical setup
- Casual conversation to warm up the session

**Key Topics**:

- Guitar playing discussion
- Sound check and technical preparation

---

### 2. Session Introduction & Brownfield Overview

**Duration**: 00:06:26 - 00:14:43 (8:17)

**Content**:

- Formal session start and welcome
- Introduction to brownfield development course
- Course agenda overview
- Demo of updated calculator application with Windows-style UI
- Calculator enhancements demonstration (memory buttons, history)
- Workspace compliance review prompt demonstration

**Key Topics**:

- **Brownfield Definition**: Existing systems with history, constraints, real users, deadlines, production requirements
- **Course Agenda**: Understanding brownfield/Evergreen code, safety measures, managing copilot, advanced context techniques, AI guide roles, documentation, backlog building, test automation
- **Calculator Demo**: Windows-style UI created from screenshot prompt, memory storage (MC, MR, M+, M-), calculation history display
- **Evergreen Compliance**: Using AI to review workspace for Evergreen software practices

**Instructor Notes**:

- John Miller emphasized that brownfield code is "shaped by reality" and represents "the best work at the time"
- Demonstrated practical AI use case: reviewing workspace for compliance

---

### 3. Safety Measures & Best Practices [x]

**Duration**: 00:35:29 - 00:58:01 (22:32)

**Content**:

- Safety nets for AI-assisted development
- Testing strategies and code coverage vs. signal quality
- Code review processes treating AI as "eager knowledgeable junior developer"
- Change review workflows
- Keeping change sets small
- Azure DevOps MCP tool mention for PR review automation

**Key Topics**:

- **Feature Flag Removal**: Using AI to safely remove obsolete feature flags
- **Testing Signal Quality**: Emphasizing meaningful tests over coverage metrics alone
- **Change Review Process**:
  - Treat AI output as junior developer work
  - Review everything generated
  - Keep changes small and focused
- **Azure DevOps Integration**: MCP tool for automating PR reviews
- **Small Change Sets**: Benefits of incremental, reviewable changes

**Best Practices Highlighted**:

- Never commit AI-generated code without review
- Test coverage is necessary but not sufficient
- Focus on test quality and signal over percentage metrics
- Use automated tools to assist human reviewers

---

### 4. Managing Copilot & Context Management

**Duration**: 00:42:04 - 00:53:36 (11:32)

**Content**:

- Structure and guardrails for managing copilot
- Context window management and token limits
- Advanced context techniques: summaries, chunking, scoped prompts
- Introduction to instruction files for persistent rules

**Key Topics**:

- **Context Window Limits**:
  - Understanding token consumption
  - Managing large codebases within context constraints
- **Advanced Techniques**:
  - **Summaries** (00:48:05-00:49:35): Condensing large contexts into key information
  - **Chunking** (00:50:00-00:51:01): Breaking down large tasks into manageable pieces
  - **Scoped Prompts** (00:51:02-00:52:18): Focusing AI on specific areas
  - **Instruction Files** (00:52:18-00:53:36): Persistent rules for AI behavior
- **Token Optimization**: Optimizing output for agents vs. humans to reduce token consumption

**Technical Details**:

- Instruction files provide persistent context across sessions
- Meta-prompts that generate other prompts
- Importance of clear, structured guidance for AI

---

### 5. Instruction Files & Provenance Tracking [x]

**Duration**: 00:52:18 - 01:30:46 (38:28)

**Content**:

- Deep dive into instruction files vs. prompt files vs. chat modes
- Provenance metadata requirements for AI-generated artifacts
- Template structures and YAML front matter
- Validation checklists and quality gates
- Enforcing compliance through instruction files
- Discussion of regulatory requirements (FDA guidance)
- Iterative refinement of instruction files

**Key Topics**:

- **Instruction Files**: Persistent rules applied to AI interactions within scope
- **Prompt Files**: Reusable templates for specific tasks
- **Chat Modes**: Interactive guidance for specific workflows
- **Provenance Metadata**:
  - AI-generated flag
  - Model identification (provider/model@version)
  - Operator identification
  - Timestamps and durations
  - Conversation log references
  - Source attribution
- **Compliance & Auditability**:
  - Chain of custody for AI artifacts
  - Protecting against orphaned/unverifiable artifacts
  - Team collaboration and compliance support
- **FDA Guidance Discussion**:
  - Preliminary guidance on AI-generated software exists
  - Not yet finalized with specific detail requirements
  - Process demonstration and explanation requirements
  - Treating AI like any other development process

**Example Structures**:

- YAML front matter for provenance
- Conversation log templates (`ai-logs/yyyy/mm/dd/<chat-id>/conversation.md`)
- Summary file templates for session documentation

**Important Clarifications**:

- Buddy Toups asked about workflow definition vs. built-in features
- John clarified these are custom instructions added via instruction files
- Not natively supported by Copilot but effective workaround

**Validation Technique Demo**:

- Using Ctrl+I to ask AI to explain its interpretation of instruction files
- Comparing AI understanding across different models
- Refining instructions based on interpretation feedback

---

### 6. Hands-On Exercise: Creating Prompt Files [x]

**Duration**: 01:35:07 - 01:57:29 (22:22)

**Content**:

- Exercise introduction: Create prompt file that creates instruction file
- First attempt without instruction files (baseline)
- Adding instruction files to repository
- Second attempt with instruction files (comparison)
- Comparing results from both iterations
- Discussion of non-deterministic behavior and consistency

**Exercise Objectives**:

- Understand prompt structure
- Practice defining intent, constraints, and success criteria
- Create reusable, clear, scoped prompts
- Observe the impact of instruction files on output quality

**Exercise Steps**:

1. **Phase 1 - Without Instructions**:
   - Create prompt to generate Evergreen software development instruction file
   - No guidance from existing instruction files
   - Save output for comparison
2. **Phase 2 - With Instructions**:
   - John pushed instruction files to repository
   - Participants pulled updates
   - Cleared chat context (new chat window)
   - Re-ran same prompt with instruction files available
   - Compared differences
3. **Phase 3 - Comparison**:
   - Use AI to compare the two generated files
   - Identify significant differences
   - Report findings

**Exercise Findings**:

- **Chris Bishop's Results**: AI recommended merging core principles from original document with new document, suggested including conceptual foundation, provided comparison table
- **Rockwell Christopher's Results**: Extensive differences including mode declaration, model specification, log creation requirements, interesting distinction between AI-generated vs. manual checklists
- **General Observations**:
  - Non-deterministic nature of AI output without guidance
  - Significant improvement in consistency with instruction files
  - More complete metadata and provenance with instructions
  - Better adherence to repository standards

**Key Discussion Points**:

- Reproducibility and dependability of AI output
- Reducing scrutiny burden through better guidance
- Making AI-generated code more predictable
- Trade-offs between verbose human-readable vs. terse AI-optimized instruction files

**Token Optimization Discussion**:

- John's experience with context window limitations
- Evolution from verbose human-targeted to terse AI-targeted instructions
- Requirement to "minimize token consumption while maintaining clarity"
- Creating separate human-readable documentation vs. AI instruction files

**Clarifications During Exercise**:

- Boris Giterman asked about sequence of instruction files (which to use first)
- John clarified the exercise is about creating a prompt that creates a prompt that creates an instruction
- Dan Blanchard asked about file location (.github/copilot/Promptfiles vs .github/instructions)
- Confusion resolved: prompt files go in /prompts, instruction files in /instructions

---

### 7. Creating Instruction Files from Prompts [x]

**Duration**: 01:57:34 - 02:04:14 (6:40)

**Content**:

- Running the prompt files created in previous exercise
- Generating instruction files from prompts
- Review of generated instruction files
- Discussion of inference and AI knowledge leveraging
- Prompt-first approach benefits

**Key Concepts**:

- **Inference as Friend**: AI leveraging vast embedded knowledge to fill in details
- **Prompt-First Approach**:
  - Easier to delete than create from scratch
  - Start with comprehensive AI-generated content
  - Edit down to precise requirements
  - Reduces initial authoring burden
- **Two Editing Approaches**:
  1. Edit instruction file directly
  2. Modify prompt file and regenerate (preferred for version control)

**Benefits of Prompt-File Approach**:

- Changes preserved in source control
- Prompt evolution tracked
- Reproducible instruction file generation
- Better provenance: detailed prompt vs. simple directive
- Example: Instead of just "create instruction file for Evergreen development", have detailed prompt with structure, requirements, constraints

**Generated Content Discussion**:

- Peter Goostree: "Amazed at what it created. Architectural context. It's crazy."
- Demonstrated how much detail AI can infer from minimal guidance
- Instruction files leverage model's built-in knowledge of patterns and conventions

**Session Conclusion**:

- Exercise deemed successful
- Break announced (one hour)
- John offered to answer questions in chat before afternoon session
- Reminder to join new chat for afternoon session (new context)

---

## Key Participants & Contributions

**Primary Instructor**:

- **John Miller**: Led entire session, provided demonstrations, answered all technical questions, facilitated exercises

**Active Participants**:

- **Dan Blanchard**: Asked about FDA regulatory requirements, commit message auto-generation, file organization
- **Buddy Toups**: Questioned workflow definition vs. built-in features, model differences in instruction file interpretation
- **Chris Bishop**: Shared comparison results showing core principles recommendations
- **Rockwell Christopher L**: Provided detailed analysis of instruction file differences
- **Goostree Peter**: Expressed amazement at generated architectural context
- **Giterman Boris**: Asked about instruction file sequence and order
- **Matt Hoffman**: Participated in exercises

---

## Technical Topics Covered

### Development Concepts

- Brownfield vs. Evergreen software development
- Code maintainability and longevity
- Technical debt management
- Feature flag lifecycle management

### AI-Assisted Development

- GitHub Copilot usage patterns
- Context management strategies
- Token optimization techniques
- Prompt engineering best practices
- Meta-prompts (prompts that generate prompts)

### Safety & Quality

- Code review workflows for AI-generated code
- Testing strategies (signal quality vs. coverage)
- Change management and small change sets
- Validation and verification techniques

### Instruction File System

- Types: Instruction files, prompt files, chat modes
- Structure: YAML front matter, markdown content
- Metadata: Provenance tracking requirements
- Validation: Checklists and quality gates
- Optimization: AI-targeted vs. human-readable formats

### Provenance & Compliance

- Required metadata fields (11 fields mentioned)
- Conversation logging (`ai-logs/` structure)
- FDA preliminary guidance on AI-generated software
- Audit trails and chain of custody
- Team collaboration requirements

---

## Tools & Technologies Mentioned

- **GitHub Copilot**: Primary AI coding assistant
- **VS Code**: Development environment
- **Azure DevOps MCP Tool**: PR review automation
- **Git**: Version control and provenance tracking
- **YAML**: Metadata and configuration format
- **Markdown**: Documentation and instruction format

---

## Files & Resources Referenced

### Repository Structure

- `.github/instructions/` - Instruction files directory
- `.github/copilot/Promptfiles/` - Prompt files directory
- `ai-logs/yyyy/mm/dd/<chat-id>/` - Conversation logs
- `ai-logs/yyyy/mm/dd/<chat-id>/conversation.md` - Full transcript
- `ai-logs/yyyy/mm/dd/<chat-id>/summary.md` - Session summary

### Instruction Files Discussed

- AI-assisted output instructions (main provenance policy)
- Prompt file creation instructions
- Instruction file creation instructions
- Chat mode file instructions
- Evergreen software development instructions (exercise output)

### Prompt Files Created (Exercise)

- Create instruction file for Evergreen development (participant-generated)

---

## Best Practices & Recommendations

### For AI-Assisted Development

1. Always review AI-generated code as you would junior developer work
2. Keep change sets small and focused
3. Use instruction files for consistent, repeatable guidance
4. Track provenance for all AI-generated artifacts
5. Optimize instruction files for token efficiency

### For Instruction Files

1. Target AI agents, not humans (reduce token consumption)
2. Use clear, structured YAML front matter
3. Include validation checklists where appropriate
4. Test interpretation across different models
5. Store human-readable docs separately from AI instructions

### For Context Management

1. Use summaries to condense large contexts
2. Chunk work into manageable pieces
3. Scope prompts to specific areas
4. Leverage instruction files for persistent rules
5. Be mindful of context window limits

### For Provenance Tracking

1. Always include complete metadata (11 required fields)
2. Log conversations in structured format
3. Link artifacts to their generating conversations
4. Track model, operator, timestamps, and durations
5. Maintain audit trail for regulatory compliance

---

## Exercise Results & Insights

### Without Instruction Files (Baseline)

- Generated content varied significantly between participants
- Some elements inferred from model's general knowledge
- Inconsistent metadata and structure
- Variable quality and completeness

### With Instruction Files (Enhanced)

- More consistent output across participants
- Better adherence to repository standards
- Complete provenance metadata included automatically
- Improved structure and organization
- Greater predictability and reliability

### Key Learning

The instruction files made AI output significantly more:

- **Consistent**: Reduced variation across runs
- **Complete**: Included all required metadata
- **Compliant**: Adhered to repository standards
- **Predictable**: More deterministic behavior
- **Maintainable**: Easier to review and validate

---

## Questions & Answers

**Q (Buddy Toups)**: These aren't built-in features to copilot, right? You're defining a workflow with instruction files?
**A (John Miller)**: Correct. These are instructions we're giving that copilot currently doesn't support natively, allowing us to create provenance information with artifacts.

**Q (Buddy Toups)**: Have you seen different models interpret instruction files differently? Is "explain" a good way to diagnose model understanding?
**A (John Miller)**: Yes, it's a good technique. You can use it to understand how AI thinks about the work, especially when seeing different effects between models. Use the explanation to fine-tune instruction files for accurate interpretation across models.

**Q (Dan Blanchard)**: Is the regulatory chain of custody required now? We have FDA cleared products.
**A (John Miller)**: FDA has preliminary guidance but not finalized with specific detail requirements. They require demonstrating a process you follow and can explain. Treat AI like any other development process - need to explain how output was generated and your understanding of it. Provenance helps with resumability and conversation history. Having that header information and session files is useful.

**Q (Boris Giterman)**: Which instruction file should be first in the sequence?
**A (John Miller)**: We're creating a prompt to prompt copilot to create a prompt file. That prompt file creates an instruction file. Just creating a profile that contains guidance for creating an instruction file for Evergreen software development.

**Q (Dan Blanchard)**: When you committed, did it auto-generate your commit messages?
**A (John Miller)**: Yes, the sparkle button generates commit messages from file changes. Mostly reliable but sometimes generic. Break into smaller commits for better messages. Stage only files you want commit message for - it only looks at staged files.

**Q (Dan Blanchard)**: Should we open a new chat window for second exercise run?
**A (John Miller)**: Yes, clear your context so nothing bleeds over from first run.

---

## Summary Statistics

- **Total Duration**: 2 hours, 4 minutes, 14 seconds
- **Number of Major Sections**: 7
- **Primary Instructor**: John Miller
- **Active Participants**: 7+ (Dan Blanchard, Buddy Toups, Chris Bishop, Rockwell Christopher L, Goostree Peter, Giterman Boris, Matt Hoffman, and others)
- **Hands-On Exercises**: 2 major exercises
- **Key Concepts Introduced**: 15+ (brownfield, Evergreen, instruction files, prompt files, provenance, context management, etc.)
- **Files/Directories Referenced**: 10+ repository paths and structures

---

## Longest Sections

1. **Instruction Files & Provenance Tracking**: 38:28 (most comprehensive topic)
2. **Hands-On Exercise: Creating Prompt Files**: 22:22 (practical application)
3. **Safety Measures & Best Practices**: 22:32 (foundational concepts)

## Shortest Sections

1. **Pre-Session & Introductions**: 6:02 (warm-up)
2. **Creating Instruction Files from Prompts**: 6:40 (final exercise)
3. **Session Introduction & Brownfield Overview**: 8:17 (context setting)

---

## Next Steps (Afternoon Session Preview)

John mentioned the session would continue after a one-hour break with:

- Further hands-on exercises
- Additional brownfield development techniques
- More advanced topics from the course agenda

**Important Reminder**: Join new chat/call for afternoon session (new context)

---

**Document Generated**: Via AI summarization of VTT transcript
**Source File**: `AI-Assisted Software Development with GitHub Copilot (Tue Morning).vtt`
**Total Lines Processed**: 7,441 lines
**Summary Created**: 2026-02-17
