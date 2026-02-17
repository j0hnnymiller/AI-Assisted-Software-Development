# AI-Assisted Software Development with GitHub Copilot (Mon Morning) - Content Summary

## Document Overview

- **Title**: AI-Assisted Software Development Course - Day 1 Morning Session
- **Date**: February 2026 (Monday Morning)
- **Instructor**: John Miller (Principal Software Engineer at Code)
- **Format**: Live virtual training session
- **Total Duration**: ~58+ minutes (transcript continues beyond captured content)
- **Main Topics**: Course introduction, LLM fundamentals, AI-first development philosophy

---

## Detailed Outline

### Section 1: Pre-Class Arrival and Small Talk (00:00:57 - 00:09:58)

**Duration**: ~9 minutes

**Key Points**:

- Informal greetings and Super Bowl discussion
- Early arrivals and audio/video setup
- Simeon Hearing from Vanderbilt joining as auditor

---

### Section 2: Course Opening and Welcome (00:09:58 - 00:14:45)

**Duration**: ~5 minutes

**Key Points**:

- Official course start and greetings
- Course title: "AI Assisted Software Development from Code Training"
- Five-day course structure overview:
  - Day 1: Introductory topics
  - Days 2-3: Brownfield development
  - Days 4-5: Greenfield architecture

**Instructor Introduction**:

- John Miller, Principal Software Engineer at Code
- Multiple roles: Developer, architect, DevOps engineer, platform engineer, test architect, release manager
- Over 1 year of AI practitioner experience
- Maintains AI practitioner resources blog
- Contact information and LinkedIn provided

---

### Section 3: Code Organization Overview (00:11:56 - 00:12:52)

**Duration**: ~1 minute

**Company Background**:

- Code is 31+ years old (slide noted as ~1 year old)
- Four divisions:
  - Consulting
  - Staffing
  - Code Magazine (one of few remaining print software development magazines)
  - Code Training

---

### Section 4: Student Introductions (00:12:52 - 00:31:44)

**Duration**: ~19 minutes

**Participants Introduced**:

1. **Otto Dobretsberger** - Code software engineer (20 years), preparing to teach custom versions of this course
2. **Chris Bishop** - Field Boss (HVAC/elevator software), Senior Systems Engineer, created AI agent for customization pipeline assessment
3. **Simeon Hearing** - Vanderbilt University Medical Center, coordinating larger organizational course
4. **Christopher Rockwell** - Vanderbilt University, application developer, uses Copilot and Claude Code
5. **Tom Bui** - MKS (laser drilling equipment for circuits), Principal Software Engineer, interested in legacy code
6. **Peter Goostree** - MKS architect, distributed data ingestion platform, uses AI for unit tests and scaffolding, interested in multi-agent workflows
7. **Alex Myachin** - MKS, Principal Software Engineer, laser manufacturing software, using Copilot for peer reviews and unit tests
8. **Dan Blanchard** - Independent software architect, 20-year client, wants to learn about maintaining existing code bases and training models
9. **Richard LaVorgna** - 20th Judicial Circuit (South Florida), programming analyst, exploring AI for Windows applications
10. **Stephen Childs** - CIO, 20th Judicial Circuit, former developer staying current with technology
11. **Rigoberto Llorens-Leon** - 20th Judicial Circuit, web developer, interested in faster/better application development
12. **Lyle Ubben** - Gene by Gene (Family Tree DNA parent), B2B ordering system, uses Copilot for PR reviews
13. **Buddy Toups** - Gene by Gene (Family Tree DNA consumer), Software Development Manager, working on context-as-code for 40+ repositories
14. **Al Torres** - Infosoft Consulting (Philippines), ERP customization with Acumatica (C#), seeking formal AI training
15. **Boris Giterman** - Dell Senior Director, Global Cyber Security Engineering (ISG), 2 years with AI code assistants, interested in full SDLC artifacts
16. **Matt Hoffman** - Outlier Technologies (SansRay compliance software for Health and Human Services), lead developer

---

### Section 5: Course Agenda and Five-Day Overview (00:31:44 - 00:35:14)

**Duration**: ~3.5 minutes

**Daily Breakdown**:

- **Day 1**:
  - Morning: Core concepts
  - Afternoon: Hands-on coding in VS Code
- **Days 2-3**: Brownfield development
  - Read-only understanding of code bases
  - Technical debt measurement
  - Moving from Brownfield to Evergreen
- **Days 4-5**: Greenfield development
  - Requirements through implementation
  - Complete architecture exercise

**Day 1 Specific Agenda**:

1. AI-assisted software development overview
2. LLMs and code generation (2 sections)
3. Team considerations and code base protection
4. GitHub Copilot UI overview and context management
5. Mob programming introduction
6. Hands-on coding with Copilot

---

### Section 6: AI-Assisted Development Philosophy (00:35:14 - 00:44:00)

**Duration**: ~9 minutes

#### 6.1: Programming Evolution

**Key Concepts**:

- Programming hasn't changed, but HOW we program has evolved
- Historical progression from switch panels to natural language
- AI-assisted development is evolutionary, not revolutionary
- Core remains: expressing human intent to machines

#### 6.2: Why AI-Assisted Development

**Benefits Highlighted**:

- Gives developers "superpowers"
- Courage to tackle difficult code bases
- Use unfamiliar technologies confidently
- Write higher quality code
- **Tackle "nice to haves"** - Major insight: Backlogs continually grow, only "must haves" get implemented
- AI enables teams to address more items beyond critical requirements

#### 6.3: AI-First vs Prompt-First Development

**AI-First Development**:

- **Scope**: Entire SDLC integration
- **Philosophy**: Life cycle integration with AI embedded throughout
- **Optimization**: Velocity and governance
- **Focus**: Human-in-the-loop, provenance tracking
- **Artifacts**: Requirements written with AI, scaffolds, tests, documentation, architecture assumes AI participation

**Prompt-First Development**:

- **Scope**: Interaction layer (how we interact with AI)
- **Mechanics**: Deterministic AI behavior
- **Optimization**: Prompt quality and reproducibility
- **Focus**: Version prompts and context control
- **Artifacts**: Instruction files, prompt files, agents, behavioral contracts, reusable modules, chat modes

**Relationship**: Prompt-first handles mechanics; AI-first provides philosophy and architecture

---

### Section 7: Large Language Models (LLMs) - Part 1 (00:44:00 - 00:47:00)

**Duration**: ~3 minutes

#### 7.1: Conceptual Overview

**Training and Processing**:

- Trained on massive datasets of code and natural language
- Nearly all published internet content consumed
- Uses **transformer architecture** to understand patterns
- **Token-based processing** - code broken into tokens
- **Attention mechanisms** focus on relevant context
- **Probabilistic next-token prediction** based on training patterns

**Critical Understanding**:

- **No true understanding** - only pattern matching at scale
- Statistical prediction from one token to the next
- The scale and sophistication produce remarkable results

---

### Section 8: Large Language Models (LLMs) - Part 2: Capabilities (00:47:00 - 00:50:14)

**Duration**: ~3 minutes

**LLM Code Generation Capabilities**:

1. Code completion
2. Code generation
3. Refactoring
4. Code optimization
5. Bug detection and remediation
6. Granular documentation
7. Test case generation
8. Code explanation and commenting
9. Multi-language support and translation

**Current Limitations** _(with caveat: these are improving)_:

1. **No real-time knowledge** - Some models now supplement with web search
2. **Generate statistically correct but logically flawed code** - Syntactically valid but execution flaws
3. **Hallucinations** - Making up information
4. **Limited context windows** - Finite memory (continually expanding)
5. **No business logic understanding** - Appears to understand but lacks true comprehension
6. **Cannot extend reasoning** beyond provided context
7. **Security vulnerabilities** - Can introduce if not careful
8. **Training data bias** - Demonstrated bias toward own generated code

---

### Section 9: LLM Architecture for Code Generation (00:50:14 - 00:53:00)

**Duration**: ~3 minutes

#### 9.1: Architecture Diagram Walkthrough

**Processing Pipeline**:

1. **Developer Input**: Natural language + code context
2. **Tokenization**: Text converted to tokens
3. **Embedding**: Tokens transformed into vectors
4. **Transformer Layer**:
   - Attention and feed-forward logic applied
   - Incorporates training data, code repositories, documentation
   - Fine-tuning/code-specific training
5. **Context Window**: Limited memory buffer for understanding requests
6. **Pattern Recognition**: Code patterns and syntax understanding
7. **Probability Distribution**: Next-token prediction
8. **Decoding Strategy**: Greedy beam search sampling
9. **Code Generation**: Tokens converted to text output
10. **Post-processing**: Validation and accuracy improvements (increasing focus area)
11. **Developer Review**: Accept or refine prompt and retry

---

### Section 10: Model Selection and Capabilities (00:53:00 - 00:58:00+)

**Duration**: ~5+ minutes _(transcript continues)_

#### 10.1: Available Models in GitHub Copilot

**Model Characteristics Displayed**:

- Multiple models available (snapshot from several weeks prior)
- Specific capabilities: Tool support, vision, media output
- **Input context size limits**
- **Output context size limits**
- Example: Claude Sonnet 3.5 - 128K input / 64K output context window

**Context Window Importance**:

- Exceeding limits introduces variability and unpredictability
- Models and versions continually change
- Specific versions come and go

**Subscription Impact**:

- Multipliers vary by subscription level
- "Premium requests" allocated monthly
- Usage caps require waiting for reset period

---

## Summary Statistics

- **Total Recorded Sections**: 10 major sections
- **Average Section Length**: ~5-6 minutes
- **Longest Section**: Student Introductions (~19 minutes)
- **Shortest Section**: Code Organization Overview (~1 minute)
- **Format**: Lecture with Q&A opportunities

---

## Key Learning Objectives (Day 1 Morning)

### Conceptual Foundation

1. Understanding AI-assisted development as evolution, not revolution
2. Distinction between AI-first (philosophy) and prompt-first (mechanics)
3. LLM fundamentals: Transformers, tokens, attention, probabilistic prediction
4. Current capabilities and honest limitations

### Practical Insights

1. AI enables tackling "nice to haves" - expanding beyond must-have features
2. Importance of context management and token limitations
3. Developer remains in review/validation role
4. Multiple models available with different capabilities

### Team Context

- Diverse participant backgrounds: healthcare, legal, manufacturing, genetics, consulting
- Common interests: Legacy code management, test generation, process automation, agent workflows
- Experience levels: From minimal AI exposure to 2 years of active use

---

## Notable Quotes and Insights

> "Programming really hasn't changed, but how we go about it has changed." - John Miller

> "AI will give you superpowers. It will give you the courage to take on code bases that few people would touch." - John Miller

> "There is no true understanding - it's pattern matching at matching scale. It's really statistical prediction from one token to the next." - John Miller (on LLMs)

> "The only things that actually ever get implemented up until now would have been the must haves... AI allows us to take on more things that we were not able to take on before." - John Miller

---

## Question Interactions

### Q&A Highlights:

1. **Dan Blanchard** (00:45:00): Clarifying AI-first vs prompt-first distinction
   - AI-first = SDLC-wide approach, agents and skills
   - Prompt-first = Specific artifact generation with instruction files

2. **Chris Bishop** (00:50:00): Real-time knowledge limitation relevance
   - Acknowledged improving with web search integration
   - Less of a limitation as models evolve

---

## Technical Terms Introduced

- **LLM**: Large Language Model
- **Transformer Architecture**: Neural network design for pattern understanding
- **Tokenization**: Breaking text/code into processable units
- **Context Window**: Limited memory buffer for AI processing
- **Attention Mechanisms**: Focusing on relevant parts of context
- **Hallucination**: AI generating plausible but incorrect information
- **Greenfield**: New development projects
- **Brownfield**: Existing/legacy code bases
- **Evergreen**: Well-maintained, modern code state
- **SDLC**: Software Development Life Cycle
- **Premium Requests**: Higher-capability model usage in subscription tiers

---

## Resumability Context

**Course Progression**: This is Day 1 morning session establishing foundational concepts before hands-on work in the afternoon.

**Next Session Topics** (anticipated):

- GitHub Copilot UI deep dive
- Context management techniques
- Mob programming exercise
- Hands-on coding session

**Prerequisites for Next Session**:

- Understanding of AI-first vs prompt-first distinction
- Awareness of LLM capabilities and limitations
- Recognition of context window constraints

---

**Summary Generated**: 2026-02-17
**Source**: `AI-Assisted Software Development with GitHub Copilot (Mon Morning).vtt`
**Format**: WebVTT transcript with speaker identification
**Coverage**: Complete structured analysis of morning session
