---
marp: true
theme: default
paginate: true
---

﻿---
marp: true
theme: default
paginate: true
title: "AI Assisted Software Development"
subtitle: "From Code to Copilot"
style: |
  section {
    background-color: #0D7FA8;
    color: white;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    padding: 60px;
  }
  h1 {
    font-size: 72px;
    font-weight: 600;
    margin-bottom: 60px;
    color: white;
  }
  .info-box {
    background-color: rgba(255, 255, 255, 0.9);
    color: #333;
    padding: 30px 40px;
    margin: 25px 0;
    border-radius: 12px;
    display: flex;
    align-items: center;
    gap: 30px;
    font-size: 28px;
  }
  .icon {
    font-size: 48px;
    min-width: 60px;
    color: #E67E22;
  }
  .info-text {
    flex: 1;
  }
  .contact-info {
    font-size: 24px;
    margin-top: 10px;
    line-height: 1.6;
  }
  .contact-info a {
    color: #2E86C1;
    text-decoration: none;
  }
  .logo {
    position: absolute;
    top: 40px;
    right: 60px;
    background: white;
    padding: 15px 30px;
    border-radius: 8px;
    font-size: 40px;
    font-weight: bold;
    color: #0D7FA8;
    letter-spacing: 8px;
  }
---

# Welcome to AI-Assisted Software Development

---

<!-- layout: Title Slide -->

## Welcome to AI Assisted Software Development

From Code to Copilot

::: notes
Duration ~00:02

Welcome participants to the AI Assisted Software Development course. This is your opening slide, so set a positive and engaging tone. Introduce the course name and tagline "From Code to Copilot" which emphasizes the journey from traditional software development to AI-augmented practices.

Key talking points:

- Express enthusiasm about the learning journey ahead
- Acknowledge the transformative nature of AI in software development
- Set expectations that this will be hands-on and practical
- Encourage questions and participation throughout

Transition: "Let's start by introducing ourselves..."
:::

---

﻿---
marp: true
theme: default
paginate: true
---
## John Michael Miller

**Principal Software Engineer at CODE**
Played roles of developer, architect, devops engineer, platform engineer, test architect, release manager
AI Practitioner and advocate for effectively using AI to write code

- LinkedIn: [www.linkedin.com/in/johnmichaelmiller](www.linkedin.com/in/johnmichaelmiller)
- Email: [john.miller@codemag.com](john.miller@codemag.com)
- Blog: [codemag.com/blog/AIPractitioner](codemag.com/blog/AIPractitioner)

::: notes
John Michael Miller is a Principal Software Engineer at CODE with over 15 years of experience in software development. He has held various roles including developer, architect, DevOps engineer, platform engineer, test architect, and release manager. John is an AI/ML enthusiast and advocates for effectively using AI to write code. You can connect with him on LinkedIn, reach out via email, or read his blog posts on AI-assisted software development.
- [AI Practitioner Resources](codemag.com/aipractitioner)
:::

---

﻿---
marp: true
theme: default
paginate: true
---

<!-- layout: Centered Two Titles -->

# Course Introductions || Hi, I'm a Developer Who Has Talked to a Robot

::: notes
Duration ~00:01

Opening slide for the introduction section. The centered two-title layout displays "Course Introductions" as the main title and "Hi, I'm a Developer Who Has Talked to a Robot" as the subtitle, creating a friendly and approachable tone for the personal introductions that follow.

Key talking points:

- This is an icebreaker moment
- Set a casual, engaging tone
- The witty subtitle helps create rapport
- Brief pause after displaying to let attendees read

Transition: "Let's go around the room and introduce ourselves..."
:::

---

## Introductions

- Who you are
- Who do you work for
- What you do
- What you've done with AI tools
- What you want to learn

::: notes
Duration ~00:10-15 (depending on class size)

Facilitate round-robin introductions. This is valuable for building rapport and understanding the experience level and expectations of the group.

Facilitation tips:

- Start by modeling with your own introduction
- Keep each person to ~2 minutes
- Note common themes or interests for later reference
- Pay attention to AI experience levels to adjust pace
- Listen for specific learning goals to address during the course

Key observations to note:

- Who has extensive AI coding experience vs. newcomers
- What tools people have tried (Copilot, ChatGPT, Cursor, etc.)
- Common pain points or challenges mentioned
- Areas of particular interest

Transition: "Great to meet everyone! Now let's talk about why we're all here..."
:::

---

﻿---
marp: true
theme: default
paginate: true
---
# About CODE Magazine || Thirty Years and Still Compiling

## About CODE

<img src="marp/images/CODE-30.jpg" style="width: 100%;" />

::: notes
CODE is a custom software company, a staff augmentation company, CODE Magazine for software developers, and training like this webinar. We've been in business for 30 years and the magazine just hit its 25th anniversary. Visit the website at https://www.codemag.com/ for more details.
:::

---

﻿---
marp: true
theme: default
paginate: false
---
# Course Daily Themes || Five Days. One AI. Zero Excuses.

## Daily Themes

| Day       | Theme                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Monday    | AI Guardrails: Instructions, Copilot UI |
| Tuesday   | AI Guardrails: Prompts, Copilot for Teams, Models and Context, LLMs |
| Wednesday | AI Guardrails: Agents, Skills, Managing Context, Instructions vs Prompts vs Agents, Test Automation and Code Quality, MCP                       |
| Thursday  | AI Assisted Brownfield SD: AI Implementation Workflow, Addressing Technical Debt, Building a Backlog, Multi-Implementation Comparison, AI Practitioner Resources |
| Friday    | AI Assisted Greenfield SD: Specification Driven Software Development, Architecture Specification, Technology Specification, Implementation Specification, Implementation Planning, Implementation Prompts, Vertical Slice Implementation, Code Review with GitHub Copilot |

::: notes
Duration ~00:03

Present the week-long course structure. This overview helps participants understand the progression and big-picture organization of the training.

Key talking points:

- Days 1-3 focus on building AI guardrails through instructions, prompts, and agents
- Thursday shifts to brownfield (existing codebases) scenarios
- Friday covers greenfield (new projects) development
- Each day builds on previous concepts
- The progression moves from foundational controls to practical application

Emphasize that guardrails come first because they're essential for safe, effective AI-assisted development. The brownfield/greenfield split acknowledges that these scenarios have different challenges and considerations.

Transition: "Today we'll start with the foundation..."
:::

---

<!-- _class: lead -->

## Course Modules

- Intro
- **▶ AI Assisted Software Development**
- Intro to Copilot
- AI Assistance in Action
- Adding AI Guardrails

---

<!-- _class: lead -->

# AI Assisted Software Development

---

## AI Assisted Software Development

- WTBD - The Core Thesis
- Why AI Assisted Software Development

---

﻿---
ai_generated: true
model: "anthropic/claude-3.5-sonnet@2024-10-22"
operator: "johnmillerATcodemag-com"
chat_id: "marp-deck-wtbd-2026-02-07"
prompt: |
  Create a marp slide deck from the main points in this blog post: https://www.codemag.com/blog/AIPractitioner/WTBD
started: "2026-02-07T16:30:00Z"
ended: "2026-02-07T16:45:00Z"
task_durations:
  - task: "content extraction"
    duration: "00:05:00"
  - task: "slide creation"
    duration: "00:10:00"
total_duration: "00:15:00"
ai_log: "ai-logs/2026/02/07/marp-deck-wtbd-2026-02-07/conversation.md"
source: "johnmillerATcodemag-com"
---

# What's the Big Deal About AI? || The More Things Change, the More They Still Compile

<!-- _class: lead -->

## WTBD - The Core Thesis

> "Programming hasn't changed, but how we go about it has changed, again."

- AI-assisted development is **evolutionary**, not revolutionary
- Programming has always been about **expressing human intent** to machines
- What changes is the **sophistication of our tools** for expressing intent
- The essence remains: bridging the gap between what we want and what machines can do

::: notes
**Opening**: Start with the provocative quote to capture attention. Pause for effect after reading it aloud. **Key Message**: Emphasize that we're not witnessing a revolution but an evolution—AI tools are the latest step in a continuous chain of improvements. **Delivery**: Speak slowly and deliberately on the core thesis. Ask audience: "How many of you thought AI was going to replace programmers?" Acknowledge concerns but pivot to optimism. **Transition**: "To understand why this is evolutionary, let's look at where we've been..."
:::

---

## A Brief History: Machine Code & Assembly (1940s)

- **Machine Code**: Raw binary language executed directly by hardware
- **Physical Programming**:
  - Flipping panel switches
  - Plugging cables
  - Feeding punched cards into IBM readers
  - Threading perforated paper tape

**Assembly Language**: Introduced symbolic mnemonics (MOV, ADD, JMP)

- **Enabling Technology**: Assemblers that translated mnemonics into machine code
- Still mainstream today in embedded systems and OS kernels

::: notes
**Historical Context**: Paint a vivid picture of early programming—physically laborious and error-prone. Mention famous anecdote about Grace Hopper debugging a literal bug (moth) from hardware. **Key Point**: Assembly was the first major abstraction—replacing binary with human-readable mnemonics. **Example**: "MOV AX, BX" is much easier than "10001001 11011000". **Modern Relevance**: Note that assembly is still used today in systems programming, making this history relevant not ancient. **Transition**: "Assembly was a huge leap, but we were still thinking in machine terms. The next step was thinking in human terms..."
:::

---

## High-Level Languages (1950s-1970s)

**The Abstraction Revolution**:

- Math-like and business-oriented syntax
- **Enabling Technologies**: Compilers and interpreters

**Key Languages**:

- **FORTRAN (1957)**: Pioneered scientific programming
- **COBOL (1959)**: Mainstream in business and government
- **C (1972)**: Spread with UNIX thanks to portable compilers

**Sensory Shift**: From mechanical card punches to typewriter-style terminals

::: notes
**Big Picture**: This era marked the shift from "speaking machine" to "speaking math" or "speaking business logic". **FORTRAN Example**: Scientists could write formulas directly rather than translating them into assembly. **COBOL Context**: COBOL's English-like syntax ("ADD SALES TO TOTAL") made programming accessible to business professionals, not just engineers. **C's Significance**: Portability revolution—write once, compile for different hardware. **Sensory Evolution**: Note the shift in human interface—from physical cards to keyboards. Ask audience if anyone has used punch cards. **Transition**: "But even high-level languages required thinking like a computer. The next step was thinking in terms of real-world objects and structures..."
:::

---

## Structured & Object-Oriented Programming (1970s-1980s)

**Focus**: Modularity, reuse, and abstraction

**Key Developments**:

- **Pascal (1970)**: Structured paradigms with compiler innovations
- **C++ (1985)**: Object-oriented compilers supporting inheritance and polymorphism

**Enabling Technologies**:

- Advanced compiler innovations
- Support for inheritance and polymorphism

**Era Experience**: CRT monitors with green text, floppy disks

::: notes
**Conceptual Shift**: This era introduced thinking in terms of real-world objects and relationships. **Pascal**: Emphasized structured programming—breaking code into procedures and functions with clear flow control. **OOP Revolution**: C++ enabled modeling real-world entities as objects with properties and behaviors. **Example**: "Instead of separate functions for customer data, you have a Customer object that knows how to save itself, validate itself, etc." **Memory Lane**: If your audience includes older developers, ask about their experience with green-screen terminals and 5.25" floppy disks. **Transition**: "Objects were powerful, but developers still spent too much time on plumbing. The 90s brought integration..."
:::

---

## IDEs & Libraries (1990s)

**The Integration Era**:

- **IDEs**: Combined compilers, debuggers, and editors in graphical interfaces
- **Visual Studio**: Enabled by faster processors and GUI toolkits
- **Java & JVM (1995)**: "Write once, run anywhere"
- **Reusable Libraries**: Abstracted common functionality

**Enabling Technologies**:

- Faster processors, GUI toolkits, extensible plug-in architectures
- Virtual machines

**Experience**: Mouse clicks, drag-and-drop, desktop computing

::: notes
**Integration Theme**: This era wasn't about new languages but about bringing tools together. **IDE Impact**: No more switching between separate compiler, debugger, and editor windows—everything integrated. **Visual Studio Example**: Drag-and-drop form design, IntelliSense autocomplete—made programming more visual and immediate. **Java's Promise**: "Write once, run anywhere" was revolutionary—JVM abstracted away hardware differences. **Libraries Evolution**: Don't write your own database connector, HTTP client, or encryption—use proven libraries. **Interactive Element**: Ask audience to raise hands if they remember life before IntelliSense. **Transition**: "While desktops became powerful, the internet was about to change everything..."
:::

---

## Web & Scripting Languages (Late 1990s-2000s)

**The Dynamic Web Era**:

- **JavaScript (1995)**: Powered by Netscape, later V8 engine (2008)
- **Python**: Web development in 2000s, data science dominance
- **Ruby on Rails (2004)**: Abstracted web complexity

**Enabling Technologies**:

- Browser engines, dynamic interpreters, frameworks
- Eclipse IDE (2001)

**Experience**: Portable coding on laptops, coffee shop programming

::: notes
**Web Revolution**: Internet shifted computing from desktop applications to browser-based services. **JavaScript Ubiquity**: Initially a toy language, became essential when V8 made it fast enough for serious applications. **Python's Versatility**: Started in web development, evolved into the dominant language for data science and AI/ML. **Rails Magic**: "Convention over configuration"—Rails showed that frameworks could make common tasks trivial. **Portability Shift**: Note the lifestyle change—developers could work from anywhere with WiFi. **Modern Context**: These languages and frameworks still dominate today. **Transition**: "But web apps still ran on physical servers in data centers. Cloud computing changed that..."
:::

---

## Cloud, APIs & Low-Code Platforms (2010s)

**The Orchestration Era**:

- **Cloud Computing**: Virtualization and containerization (Docker, Kubernetes)
- **APIs**: REST and GraphQL enabled modular integration
- **Low-Code Platforms**: Mendix, OutSystems, PowerApps with visual compilers

**Transformation**: Programming shifted from hardware-bound tasks to orchestration

**Experience**: Browser dashboards, swiping, clicking, dragging

::: notes
**Orchestration Concept**: Developers became conductors—composing systems from managed services rather than building everything from scratch. **Cloud Impact**: "Need a database? Click button, get database. Need 100 servers? Auto-scale." Infrastructure became code. **API Economy**: Modern apps are mashups—Stripe for payments, Twilio for SMS, Auth0 for authentication. You orchestrate services, not write everything. **Low-Code**: Controversial topic—some see it as dumbing down, others as appropriate tool for business apps. Acknowledge both views. **Key Insight**: This is when programming truly shifted from "making hardware do things" to "composing services and logic". **Transition**: "Cloud and APIs raised the abstraction level. AI assistance raises it even higher..."
:::

---

## The Modern Mainstream Coding Experience

**Intent Interpretation**:

- Developers express intent in higher-level languages, frameworks, and APIs
- Compilers, interpreters, and VMs translate intent into executable code
- Libraries and cloud services provide ready-made building blocks
- Less about micromanaging hardware, more about shaping logic and workflows

**The Core**: Bridging human goals with machine execution through layers of abstraction

::: notes
**Synthesis Point**: This slide ties together the history—every era raised the abstraction level. **Visual Metaphor**: "Think of programming as a ladder—each rung takes you higher above the hardware, making it easier to see the big picture but relying on more layers below." **Modern Developer Reality**: Today's developers rarely think about memory management, CPU registers, or even which physical server runs their code. They think in terms of business logic and user experiences. **Key Question for Audience**: "How many of you have ever written assembly or C code?" Then: "How many wrote Java or Python today?" Shows the abstraction trajectory. **Transition**: "Now here comes AI. It's not a different ladder—it's another rung on the same ladder we've been climbing."
:::

---

## AI-Assisted Coding (Present/Future)

**The Natural Language Era**:

**Enabling Technologies**:

- Large language models trained on vast code repositories
- Contextual intent recognition
- IDE integration

**The Paradigm Shift**: Programming becomes **dialogue**

- Express goals in plain language
- AI generates code, tests, and documentation
- Example: "Create a function that validates email addresses" → Complete implementation

::: notes
**Paradigm Shift**: This is the key slide—AI enables expressing intent in natural language, not just formal syntax. **LLM Training**: Models trained on billions of lines of public code (GitHub, Stack Overflow, etc.) learn patterns and best practices. **IDE Integration**: Copilot, Cursor, Tabnine—AI is embedded in our daily tools, not separate applications. **Dialogue Metaphor**: "Programming becomes conversation. You say what you want, AI suggests how to do it, you refine through iteration." **Live Demo Opportunity**: If appropriate, show quick Copilot example here. **Audience Engagement**: "How many of you have tried GitHub Copilot or ChatGPT for coding?" **Transition**: "This natural language interaction is the crucial breakthrough. Let's explore what that means..."
:::

---

## Natural Language Coding: The Game Changer

**Responsibility Shift**:

- Previously: Coder translates intent into executable code
- Now: Intent expressed in natural language, AI interprets and generates

**New Role of Programmer**:

- **Curator of context**
- **Validator of output**
- **Steward of alignment** between human goals and machine behavior

**Boundary Movement**: Between domain expertise and implementation

::: notes
**Role Evolution**: This is about identity—developers worry "Am I being replaced?" Address this directly. **Curator of Context**: You provide requirements, constraints, examples, test cases. The better the context, the better the AI output. **Validator Role**: AI generates fast, but you must verify it's correct, secure, performant, maintainable. Critical thinking is MORE important, not less. **Steward of Alignment**: Ensuring the code does what users need, not just what you asked for. **Example**: "AI can generate a sorting algorithm, but you decide if sorting is even the right solution." **Reassurance**: "Your expertise shifts from syntax to strategy, from typing to thinking." **Transition**: "Let's look at specific examples of how AI understands intent..."
:::

---

## AI Understands Intent—Not Just Commands

**Beyond Parsing**: AI understands what you mean

- "Make this faster" → Performance optimizations
- "Add error handling" → Proper exception management
- "Log the output" → Appropriate logging implementation

**New Interaction Modes**:

- Sketches and examples as expressions of intent
- Test cases and bug reports → Code generation
- Conversational iteration like human collaboration

::: notes
**Intent Understanding**: This is what makes AI different from traditional autocomplete or code snippets. **Examples Walkthrough**: Go through each example slowly. "Make this faster" could mean caching, algorithm optimization, database indexing—AI considers context to choose. **Test-Driven Development**: "You can write tests first, AI generates implementation that passes tests. TDD on steroids!" **Bug Reports as Input**: Show how AI can read a bug report ("Users getting 500 error when submitting form") and suggest fixes. **Conversational Iteration**: "Too much like code that..." "Actually, make it more like..." — Natural back-and-forth refinement. **Live Example Opportunity**: If time permits, demonstrate a conversational refinement with AI. **Transition**: "This sounds revolutionary, but remember—it's just another tool in a long line of tools..."
:::

---

## It's Just Another Tool

**Historical Perspective**:

- **IDEs**: Auto-complete and debugging
- **Libraries**: Reusable components
- **AI**: Intelligent scaffolding, pattern recognition, code generation

**Reality Check**:

- AI is not replacing developers
- It's helping them move faster and think bigger
- Following the same pattern as previous innovations

::: notes
**Reassurance Slide**: This slide is the antidote to hype and fear. Speak with calm authority. **Historical Pattern**: Every new tool was feared—"High-level languages will make us lazy!" "IDEs will dumb down programmers!" Didn't happen. **Tool, Not Replacement**: Hammer didn't replace carpenters. Calculator didn't replace mathematicians. AI won't replace developers. **Speed and Scale**: "AI lets you work faster, tackle bigger problems, spend more time on creative and strategic work rather than boilerplate." **Personal Testimony**: If you have personal experience where AI helped you—share it. Humanizes the technology. **Address Anxiety**: Acknowledge that change is uncomfortable but emphasize continuity. **Transition**: "But this doesn't mean we can skip the hard parts..."
:::

---

## Verification Still Matters

**Unchanged Responsibilities**:

- **Testing, review, and validation** still required
- **Architecture, correctness, security, ethics** remain developer duties
- Critical thinking is still essential

**What Changed**: How we express our goals
**What Didn't Change**: Whether we need to think critically

::: notes
**Critical Reality Check**: This slide balances the optimism. AI is powerful but not infallible. **Testing Remains Essential**: AI-generated code needs the same rigorous testing as human-written code. Maybe more, since you didn't write it. **Security Responsibility**: AI doesn't understand your threat model, compliance requirements, or security policies. You do. **Ethics and Bias**: AI trained on public code may reproduce problematic patterns (hardcoded credentials, insecure practices, biased algorithms). You're the filter. **Architecture Decisions**: AI can implement patterns, but you choose which patterns fit your system's needs. **Analogy**: "GPS tells you the route, but you still drive the car. You watch for hazards, make judgment calls, take responsibility." **Transition**: "So what does the future actually look like?"
:::

---

## The Future Is Still Intent-Driven Development

**Continuity**:

- Core goal remains: getting computers to do what we need
- Instead of writing/debugging code → creating prompts and refining context
- Same learning curve pattern as all previous improvements

**Essential Truth**: AI assistance is just another improvement in the long line of programming evolution

::: notes
**Future Vision**: This slide looks forward while maintaining historical perspective. **Intent-Driven Continuity**: From assembly to C to Python to AI prompts—each step made intent clearer, implementation more abstracted. **Skills Evolution**: "Learning Python took time. Learning prompt engineering will take time. But it's the same kind of skill acquisition we've always done." **Learning Curve Reality**: Don't sugarcoat—there will be frustration, mistakes, and learning. But also breakthroughs and productivity gains. **Continuity Message**: "You're not starting over. You're building on everything you know. Your domain knowledge, debugging skills, design sense—all still essential." **Encouragement**: "This is an exciting time to be a developer. AI removes drudgery, letting us focus on the interesting problems." **Transition**: "Let me wrap up with the key takeaways..."
:::

---

## Conclusion

**The Fundamental Truth**:

- Programming has **always** been about translating human intent into machine action
- From punch cards to Python to AI prompts—the core challenge remains unchanged
- What evolves is not the essence of programming, but the sophistication of our tools

**AI's Role**:

- Latest chapter in the ongoing story
- More intuitive ways to communicate with computers
- Preserves essential human responsibilities: design, validation, ethical oversight

**The Future**: Not abandoning programming, but refining it—making it more accessible and efficient while keeping human creativity and judgment at the center.

::: notes
**Closing Message**: This is your mic-drop moment. Speak with conviction and optimism. **Core Thesis Callback**: Circle back to opening quote—"Programming hasn't changed, but how we go about it has changed, again." **Fundamental Continuity**: Emphasize that this entire journey (70+ years) has been about expressing intent with increasing ease. AI is the latest, not the last, step. **Human Centrality**: "AI is a tool we wield, not a replacement for our judgment. We remain at the center—designers, validators, ethical stewards." **Accessibility Point**: AI will bring more people into programming by lowering barriers. That's a good thing. **Call to Action**: "The future belongs to developers who embrace these tools while maintaining the critical thinking and expertise that makes great software." **Ending Note**: Pause briefly after final sentence, let it land, then invite questions. **Optional**: If time, ask "What questions do you have?" and address 2-3 before moving on.
:::

---

﻿---
ai_generated: false
operator: "johnmillerATcodemag-com"
source: "johnmillerATcodemag-com"
---

# The AI Revolution in Software Development || With Great Token Budget Comes Great Responsibility

---

## Why AI Assisted Software Development

If used effectively, it will give you superpowers

- The courage to
  - Take on codebases that few would touch
  - Use technologies you should know but don't
  - Write more high-quality code than you have ever written before
  - Take on the nice to haves

::: notes
Career Transformation: - Those who adapt: become 10x more productive, tackle bigger challenges, expand skill sets - Those who resist: may find themselves struggling with modern development expectations - New roles emerging: AI prompt engineers, AI code reviewers, AI-assisted architects

Superpowers Explained: - Legacy codebases: AI can quickly understand and explain complex, undocumented systems - New technologies: Learn frameworks/languages faster with AI as a coding partner - Code quality: AI suggests improvements, catches bugs, generates comprehensive tests - Nice to haves: Features that were “too time-consuming” become feasible

Examples to share: - Developer who used AI to modernize a 15-year-old PHP codebase in weeks instead of months - Team that adopted a new framework (React to Vue) with AI assistance in days - 80% reduction in boilerplate code writing time - Comprehensive test suites generated automatically

Key message: AI doesn't replace developers—it amplifies their capabilities
:::

---

## AI-First & Prompt-First

AI-First Development
- A software engineering philosophy where AI is embedded across the entire SDLC–requirements, design, implementation, testing, documentation, compliance, and maintenance.
Prompt-First Development
- A workflow pattern where prompts, instruction files, and chat modes are treated as first-class, version-controlled artifacts.

::: notes
AI-First is the broad philosophy. Prompt-First is the tactical layer that enables predictable AI behavior. You can do Prompt-First without being AI-First, but not the reverse.
:::

---

## What Each Optimizes For

| Focus Area    | AI-First                  | Prompt-First                       |
| ------------- | ------------------------- | ---------------------------------- |
| Scope         | Entire SDLC               | Interaction layer                  |
| Goal          | Lifecycle integration     | Deterministic AI behavior          |
| Optimization  | Velocity, governance      | Prompt quality, reproducibility    |
| Risk Controls | Human-in-loop, provenance | Versioned prompts, context control |

::: notes
This table is the heart of the comparison. AI-First is about organizational and architectural change. Prompt-First is about artifact discipline and predictable outputs.
:::

---

## How They Treat Artifacts

AI-First
  - Requirements written with AI collaboration in mind
  - AI-generated scaffolds, tests, docs
  - Provenance enforced across all AI outputs
  - Architecture assumes AI participation

Prompt-First
  - Prompts and instruction files are version-controlled
  - Prompts define behavioral contracts
  - Reusable prompt modules
  - Chat modes define safe, predictable interactions

::: notes
AI-First changes what you build and how you build it. Prompt-First changes how you communicate intent to the AI.
:::

---

## Relationship Between the Two

Prompt-First is a subset of AI-First.
Prompt-First = mechanics
AI-First = philosophy + architecture + lifecycle integration

::: notes
This is the conceptual hierarchy. Prompt-First is necessary but not sufficient for AI-First maturity.
:::

---

<!-- layout: Two Content -->

## AI First Software Development

Building software where AI is a core capability, not an add-on.

**Why AI-First**
  - Software requirements are increasingly expressed in natural language.
  - AI copilots accelerate architecture, coding, testing, and documentation.
  - Teams shift from writing code to designing intent and validating outputs.
**Outcomes**
  - Faster iteration cycles
  - Better documentation and test coverage

::: column

**Core principles**
  - **Prompt-First Design** — workflows expressed as structured prompts
  - **AI-Native Architecture** — modular boundaries and deterministic interfaces
  - **Human-in-the-Loop** — review, validation, and traceability everywhere
  - **Continuous Verification** — tests, analysis, and guardrails on every output
  - **Lifecycle Governance** — versioning, provenance, and risk-based controls

- Reduced cognitive load on developers
- More resilient, adaptable systems

::: notes
This slide frames what we mean by AI-First development. The key idea is that AI isn't an add-on or a productivity booster—it becomes a core capability of the software lifecycle. When we design systems today, we assume AI will participate in requirements, architecture, coding, testing, and documentation.

Why AI-First
“Teams increasingly express requirements in natural language. AI can interpret those requirements and generate scaffolding, code, tests, and documentation.”
“This shifts the developer's role from writing every line of code to defining intent, constraints, and quality expectations.”
“The goal isn't to replace engineering judgment—it's to amplify it.”

Core Principles

Prompt-First Design
“We start with structured prompts that capture behaviors, invariants, and interfaces. These become durable artifacts, just like design docs.”

AI-Native Architecture
“We design modules with clear boundaries so AI-generated components remain predictable and testable. Deterministic interfaces are essential.”

Human-in-the-Loop
“AI accelerates creation, but humans validate correctness, safety, and alignment with business intent. Review is built into the workflow.”

Continuous Verification
“Every AI-generated artifact—code, tests, docs—runs through automated checks. Static analysis, unit tests, and guardrails catch drift early.”

Lifecycle Governance
“We treat prompts, outputs, and revisions as versioned assets. Provenance and traceability matter for compliance, debugging, and long-term maintainability.”

Outcomes
“Teams iterate faster because intent moves directly into working prototypes.”
“Documentation and test coverage improve because AI can generate them continuously.”
“Developers spend more time on architecture and correctness, less on boilerplate.”
“The result is software that's more adaptable and resilient over time.”
:::

---

<!-- layout: Two Content -->

## Prompt-First Software Development

Design the intent first — let AI generate the implementation.

**Why Prompt-First**
  - Behaviors and constraints are expressed in structured natural language.
  - Prompts become first-class source-of-truth artifacts.
  - Teams shift from writing functions to defining outcomes, invariants, and interfaces.

**Benefits**
  - Faster iteration from idea to working software
  - Higher consistency across generated components

::: column

**Core practices**
  - **Structured Prompts** — templates for features, APIs, data models, tests, and refactors
  - **Instruction Files** — persistent, versioned guidance for code generation
  - **Deterministic Boundaries** — clear contracts keep outputs predictable
  - **Validation Loops** — tests plus human review ensure correctness and safety
  - **Prompt Versioning** — track intent evolution just like code changes

- Reduced cognitive load on developers
- Better alignment between business intent and implementation

::: notes
“This slide introduces the core idea behind Prompt-First development. Instead of starting with code, we start with intent. Prompts become the primary design artifact, and AI becomes the mechanism that turns intent into implementation.”

Why Prompt-First
“Modern development increasingly begins with natural-language descriptions of behavior. Prompt-First formalizes that by treating prompts as first-class inputs to the software lifecycle.”
“The developer's role shifts from writing code line-by-line to defining outcomes, constraints, invariants, and interfaces.”
“This creates a tighter alignment between business intent and the resulting system.”

Core Practices

Structured Prompts
“We don't rely on ad-hoc prompting. We use templates for features, APIs, data models, tests, and refactors. This creates consistency and reduces ambiguity.”

Instruction Files
“These are durable, versioned prompt artifacts that guide AI generation. They act like living design documents that the AI reads every time it produces code.”

Deterministic Boundaries
“We design modules with clear contracts so AI-generated code stays predictable. The AI can generate the internals, but the interfaces remain stable and human-controlled.”

Validation Loops
“Every AI-generated artifact goes through automated tests and human review. The goal is to catch drift early and ensure correctness.”

Prompt Versioning
“Prompts evolve just like code. Tracking changes helps with debugging, reproducibility, and compliance.”

Benefits
“Teams move from idea to working software much faster because intent flows directly into generation.”
“Generated components become more consistent because they're driven by structured prompts, not one-off instructions.”
“Developers spend more time on architecture and correctness, less on boilerplate.”
“The end result is a system that's easier to maintain and adapt over time.”
:::

---

<!-- _class: lead -->

## Course Modules

- Intro
- AI Assisted Software Development
- **▶ Intro to Copilot**
- AI Assistance in Action
- Adding AI Guardrails

---

<!-- _class: lead -->

# Intro to Copilot

---

## Intro to Copilot

- Hands-On with GitHub Copilot

---

﻿---
ai_generated: true
model: "openai/gpt-5.3-codex@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "exercise-repository-fork-clone-deck-20260322"
prompt: |
  create an exercise marp slide deck using the slides\exercise-template.pptx template for the following:


  ## Exercise: Clone the AI-Assisted-Software-Development Repository

  Prerequisites: Git, GitHub account
  Objectives
  Fork the AI-Assisted-Software-Development repo
  Activities
  Clone the git@github.com:johnmillerATcodemag-com/AI-Assisted-Software-Development.gitrepository
  Switch to the brownfield branch
  Success Criteria
  Cloned repository exists locally

  ::: notes
  Duration ~00:10

  Objective: Fork the course repos Tasks
  Search GitHub for
  AI-Assisted-Software-Development
  Fork this repo
  This will create a personal copy under your GitHub account
  You can make changes without affecting the original repo
  :::

  ---

  ## Exercise: Fork the AIASD-20260209-BF Repo

  Objectives
    - Explore an unfamiliar codebase
  Activities
    - Fork this repo https://github.com/j0hnnymiller/AIASD-20260209-BF.git
    - Clone the forked repo
    - Create a GitHub PAT https://github.com/settings/tokens
    - Store the PAT in the GITHUB_TOKEN environment variable

  ::: column

  Success Criteria
    - Repo is available locally

  ::: notes
  Duration ~00:20

  Guide participants through creating a fork of the brownfield exercise repository, cloning it locally, and creating a GitHub PAT for authenticated access. Emphasize that this setup work enables the later brownfield labs.
  :::

---

# Exercise: Fork and Clone Repositories || Exercise: Your First git clone of Many

## Exercise: Clone the AI-Assisted-Software-Development Repository

**Setup and Objectives**

Prerequisites
  - Git
  - GitHub account

Objectives
  - Fork the AI-Assisted-Software-Development repository
  - Clone your fork to your local machine
  - Switch to the brownfield branch to confirm branch navigation

**Activities and Success Criteria**

Activities
  1. Search GitHub for AI-Assisted-Software-Development.
  2. Fork the repository into your GitHub account.
  3. Clone your fork locally with SSH or HTTPS.
  4. Open a terminal in the cloned repository.
  5. Switch to the brownfield branch.

::: column

```bash
git clone git@github.com:<your-username>/AI-Assisted-Software-Development.git
cd AI-Assisted-Software-Development
git checkout brownfield
```

Success Criteria
  - Repository is forked under your GitHub account
  - Cloned repository exists locally
  - Brownfield branch is checked out successfully

::: notes
Duration ~00:10

Set the context by explaining that this is foundational setup for all later course tasks. Guide participants to fork first, then clone their own fork, so they have push access and can safely make changes without affecting the original repository. If students hit authentication issues, pause briefly to confirm whether they are using SSH keys or HTTPS credentials and help them choose one method consistently. Close by asking everyone to run 'git branch --show-current' so they can verify they are on the brownfield branch before moving forward.
:::

---

## Exercise: Fork the 20260330-aiasd-ge Repo

**Objectives**

- Explore an unfamiliar codebase with a safe personal fork
- Clone and validate local access to the brownfield exercise repository
- Configure PAT-based authentication for GitHub operations

::: column

**Activities and Success Criteria**

Activities

1. Open https://github.com/j0hnnymiller/20260330-aiasd-ge.git.
2. Fork the repository to your personal GitHub account.
3. Clone the forked repository locally.
4. Create a GitHub PAT at https://github.com/settings/tokens.
5. Store the token in the 'GITHUB_TOKEN' environment variable.

```bash
$env:GITHUB_TOKEN = "<your-pat>"

export GITHUB_TOKEN="<your-pat>"
```

Success Criteria

- Forked repository exists in your GitHub account
- Repository is available locally and can be opened in VS Code
- 'GITHUB_TOKEN' is set in the current shell session

::: notes
Duration ~00:20

Frame this as brownfield readiness work and explain that a clean setup now prevents workflow friction later. Walk students through forking and cloning first, then move to PAT creation with a reminder to use least-privilege token scopes and never commit tokens to source control. During the hands-on period, check that everyone can authenticate successfully before they continue into subsequent labs. Transition by emphasizing that local clone plus PAT setup is the baseline for future repository analysis and change workflows.
:::

---

## Exercise: Fork the Repos

**Objective**

- Fork the course repositories needed for independent practice

::: column

**Activities and Success Criteria**

Activities

1. Search GitHub for the following repositories:
   - AI-Assisted-Software-Development
   - zeus.academia.3b
2. Fork both repositories into your GitHub account.
3. Confirm each fork appears under your account.
4. Optional: clone each fork locally for offline work.

Success Criteria

- Both repositories are forked to your GitHub account
- You can identify the original upstream repositories
- You can explain why forking protects the source repositories

::: notes
Duration ~00:10

Use this slide as a consolidation exercise to reinforce the fork-first workflow pattern across multiple repositories. Encourage participants to describe the difference between upstream and origin in their own words, because that understanding reduces merge and push mistakes later in the course. If time permits, have learners quickly clone one of the forks and verify remotes using 'git remote -v' as a confidence check. End with a short recap that forking gives each participant a safe workspace while preserving the integrity of the course-owned repositories.
:::

---

﻿---
marp: true
theme: default
paginate: true
---

# Hands-On with GitHub Copilot in VS Code || Getting Your Pair Programmer to Stop Guessing

---

## Hands-On with GitHub Copilot

Installation and configuration

- Installing the extension
- Setting up authentication
- Configuring settings
  - Sharing configuration across an organization
- Shared configuration templates (e.g., .copilot/settings.json) can be distributed across projects to standardize behavior.
  - https://www.codemag.com/Blog/AI/AIASD-install-guide

::: notes
Walk through installation, auth, and a quick coding session; encourage participants to follow along.
:::

---

## Prompt Specificity

Add error handling to my code

- Result: Generic response asking what type of errors, what language, what code?
  Add error handling to my JavaScript function that calls an external API. I want to handle network timeouts, 404 errors, and JSON parsing failures. Return user-friendly error messages.
- Result: Better, but still generic without seeing actual code structure
  @file:api-client.js Add comprehensive error handling to the fetchUserData function. Handle network timeouts (>5s), HTTP errors (404, 500, etc.), and JSON parsing failures.   Return user-friendly error messages that match our existing error format in @file:error-types.js
- Result: Specific implementation that matches existing code patterns\*

::: notes
Duration ~00:04

**Delivery Instructions:**
This slide demonstrates the progression from terrible to excellent prompts—walk through each example deliberately.

**Example 1 (Bad):** "Add error handling to my code" - Read this with a slightly exasperated tone. Point out: What code? What language? What kind of errors? Copilot literally has no context to work with. This is like asking a contractor to "fix your house" with no other information.

**Example 2 (Better):** Read the second prompt and note improvements: specifies JavaScript, specifies function purpose (external API call), lists specific error types (network timeouts, 404, JSON parsing). But emphasize the problem: "still generic without seeing actual code structure." Copilot doesn't know your coding patterns, your existing error handling approach, or your project structure.

**Example 3 (Best):** Read the third prompt slowly, highlighting key improvements:

- Uses '@file:api-client.js' to reference specific file (Copilot can see the actual code)
- Names the exact function ('fetchUserData')
- Provides precise timeout threshold (>5s, not just "timeouts")
- Lists specific HTTP codes (404, 500, etc.)
- References another file '@file:error-types.js' for consistency with existing patterns

**Key Teaching Point:** "The difference between prompt 1 and prompt 3 is the difference between Copilot asking YOU 10 clarifying questions versus Copilot just doing exactly what you need. Specificity saves time."

**Audience Interaction:** Ask: "How many of you have written prompts like example 1? Don't worry—we all start there. By the end of today, you'll be writing prompts like example 3 automatically."

**Transition:** "Now let's practice this in a hands-on lab where you'll learn to add context using @ symbols..."
:::

---

﻿---
ai_generated: true
model: "openai/gpt-5.3-codex@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "exercise-github-copilot-vscode-workflows-20260322"
prompt: |
  create an exercise marp slide deck using the slides\exercise-template.pptx template for the provided GitHub Copilot labs (getting started, context management, chat workflow, and modes)
started: "2026-03-22T00:00:00Z"
ended: "2026-03-22T00:20:00Z"
task_durations:
  - task: "exercise deck authoring"
    duration: "00:12:00"
  - task: "provenance logging"
    duration: "00:05:00"
  - task: "readme update"
    duration: "00:03:00"
total_duration: "00:20:00"
ai_log: "ai-logs/2026/03/22/exercise-github-copilot-vscode-workflows-20260322/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---

# Exercise: Getting Started with GitHub Copilot in VS Code || Exercise: Your AI Copilot Reports for Duty

---

<!-- layout: Two Content -->

## Exercise: Getting Started with GitHub Copilot

Objectives
  - Install and configure GitHub Copilot
  - Verify authentication with your GitHub account
  - Explore core Copilot UI components in VS Code

Activities
  1. Install the GitHub Copilot extension from the VS Code marketplace.
  2. Sign in with your GitHub account and verify Copilot access.

::: column

3. Locate and explore:
  - Chat window and chat history
  - New chat button
  - Quick chat feature and keyboard shortcut
  - Settings menu
  - Model selection dropdown
4. Check your premium token usage bar.
5. Create a new chat and experiment with the interface.

Success Criteria
  - Copilot extension is installed and authenticated
  - You can open and close chat windows
  - You can explain main chat versus quick chat
  - You can find and use chat history

::: notes
Duration ~00:30

Use this lab as the onboarding checkpoint for all remaining Copilot exercises. Start by confirming everyone has VS Code open and can reach the extension marketplace, then walk the room while participants sign in and complete authentication. Pause after each interface element so learners can find it before moving forward, especially quick chat and model selection since these are easy to miss for first-time users. Close by asking each participant to start one test chat so you can confirm readiness before transitioning to context management.
:::

---

<!-- layout: Two Content -->

## Exercise: Understanding Context Management

Objectives
  - Learn to add context using @ symbols
  - Understand context window limitations
  - Practice writing effective prompts

Activities
1. Basic context addition:
  - Use '@workspace' to search your codebase
  - Use '@file' to reference specific files
  - Use '@terminal' to include command output
  - Use '@vscode' for VS Code product questions

::: column

2. Prompt practice:
  - Write a vague prompt and observe the result
  - Rewrite with specific context and compare quality
  - Add file references to improve accuracy
3. Context window experiment:
  - Run a longer single conversation
  - Observe when early context gets dropped
  - Start a new chat when topic focus changes

Success Criteria
  - You can use all four @ context types
  - You can identify when to start a fresh chat
  - You can show quality improvements from specific prompts

::: notes
Duration ~00:20

Frame this as the first skill that directly improves Copilot output quality without changing tools or models. During the @ symbol walkthrough, have participants perform each step live and explain what new information Copilot gains from each context type. For the prompt comparison, ask learners to keep the same goal and only change context quality so the difference is obvious and measurable. End by normalizing context window limits as expected behavior, then reinforce the habit that new topic equals new chat.
:::

---

<!-- layout: Two Content -->

## Exercise: Chat Management and Workflow

Objectives
  - Organize chat sessions effectively
  - Use chat history as a working reference
  - Develop efficient workflow patterns with main and quick chat

Activities
1. Chat organization:
  - Review current chat history
  - Identify conversations that should have been separate
  - Practice starting new chats at natural topic boundaries
2. Context preservation:
  - Run one focused feature chat
  - Add only relevant context files
  - Complete work without context overflow
3. Quick chat practice:
  - Keep main chat for primary task flow
  - Use quick chat for side questions
  - Return to main chat with context preserved
4. Chat history review:
  - Locate previous high-quality solutions
  - Identify prompts that worked well
  - Capture repeatable prompt patterns

Success Criteria
  - Chat history is organized and meaningful
  - You can quickly find and reuse previous solutions
  - You can use multiple chat windows without losing primary context

::: notes
Duration ~00:20

Introduce this lab as productivity hygiene that prevents context fatigue and low-quality responses later in the day. Coach participants to separate work streams by topic, and use quick chat for interruptions so their main conversation remains coherent and reusable. During the history review, have each learner identify one prompt that worked well and explain why it worked, which helps them build a personal prompting playbook. Finish with the context window management bullets as operational rules they can apply in every future session.
:::

---

<!-- _class: lead -->

## Course Modules

- Intro
- AI Assisted Software Development
- Intro to Copilot
- **▶ AI Assistance in Action**
- Adding AI Guardrails

---

<!-- _class: lead -->

# AI Assistance in Action

---

## AI Assistance in Action

- Collaborating on a Solution
- The Pull Request Lifecycle
- Multi-Model Implementation Comparison
- Core Evergreen Principles

---

﻿---
marp: true
theme: default
paginate: true
---
# Vibe Coding: Collaborative AI Development || One Keyboard, Many Opinions, One Calculator

## Collaborating on a Solution

- Basic Arithmetic - Addition, subtraction, multiplication, division
- Clear / Reset Function - Quickly resets the current input or entire calculation
- Decimal Support - Allows entry and computation with decimal numbers
- Sign Toggle (+/–) - Switches values between positive and negative
- Percentage Function - Converts values to percentages for quick calculations
- Memory Functions (M+, M–, MR, MC) - Store, recall, add to, or clear memory values
- Error Handling - Displays errors such as division by zero
- Simple, Intuitive Interface - Numeric keypad, operation buttons, and display screen
- Test Automation
  - Code Coverage
- Dependency Management
- Comparing Implementations
- Chat Management
- Intro to Evergreen Software Development

::: notes
This slide outlines the collaborative development process we'll follow for building our calculator application — and mob programming will be central to how we work together.

Except for Project Setup and Basic Arithmetic functions, the mob controls the direction of the implementation. The other labs are optional and can be used when the mob directs the development of that feature or as suggestions should the mob struggle for direction.

We begin with Project Setup, where the team configures the environment, aligns on goals, and prepares the repo. This is done as a mob — one keyboard, one screen, and everyone contributing ideas in real time. It ensures shared understanding from the start.

At the end of the day, we introduce Evergreen Software Development — a mindset of continuous improvement.

Random ideas:
Implementing Observability

Scaffold a new C# command line project using .NET. The project should include:
A Program.cs file with a simple "Hello, World!" example.
A .csproj file configured for a console application.
A README.md with build and run instructions.
The project should be ready to build and run from the command line.
:::

---

﻿---
ai_generated: true
model: "openai/gpt-5.3-codex@2026-03-16"
operator: "johnmillerATcodemag-com"
chat_id: "calculator-project-exercise-deck-20260317"
prompt: |
  create an exercise slide deck, using the #file:exercise-template.md, for the provided calculator project exercise content.
started: "2026-03-17T03:28:00Z"
ended: "2026-03-17T03:36:00Z"
task_durations:
  - task: "content normalization"
    duration: "00:03:00"
  - task: "deck authoring"
    duration: "00:05:00"
total_duration: "00:08:00"
ai_log: "ai-logs/2026/03/17/calculator-project-exercise-deck-20260317/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---

# Exercise: Calculator Project Setup || Exercise: The Calculator That Launched a Thousand Prompts

---

<!-- layout: Two Content -->

## Exercise: Calculator Project - Setup and Basic Implementation

Objectives
  - Use AI to generate starter code for arithmetic operations
  - Understand how to validate AI-generated logic
  - Integrate addition, subtraction, multiplication, and division functions

Activities
1. Project Initialization:
  - Prompt AI to create a new project
  - Review generated project structure
  - Verify build configuration
2. Implement Basic Operations:
  - Prompt AI to add methods for addition, subtraction, multiplication, and division

::: column

3. Review the Code:
  - Check correctness and edge cases
4. Build and Run:
  - Use Copilot to help with build commands
  - Troubleshoot compilation errors with Copilot
  - Run the application

Success Criteria
  - Working calculator with 4 basic operations
  - Application compiles and runs successfully
  - Generated code is critically reviewed

::: notes
Duration ~01:00

---

## Setup and Basic Implementation Exercise Instructions

**Prerequisites:** Calculator project context available

### Objectives
- Scaffold core operations with AI assistance.
- Validate generated logic before accepting changes.
- Deliver a working baseline calculator.

### Activities

- Build project skeleton, implement 4 operations, and verify behavior.
- Emphasize manual review of AI output before merge.

### Success Criteria

- Four operations work end-to-end.
- Build is green.
- Team can explain logic and edge-case handling.
  :::

---

<!-- layout: Two Content -->

## Exercise: Calculator Project - Clear / Reset

Objectives
  - Use AI to scaffold state-management logic
  - Implement CE (clear entry) and C (clear all) behaviors
  - Understand UI state transitions

Activities
  1. Ask AI to outline the difference between CE and C
  2. Generate code for clearing current input vs full state
  3. Integrate logic into calculator state object
  4. Test transitions with sample input sequences

::: column

Success Criteria
  - CE clears only the active entry
  - C resets the entire calculator state

::: notes
Duration ~00:15

## Clear / Reset Exercise Instructions

**Prerequisites:** Basic calculator state model

### Objectives

- Separate entry-level clear from full reset behavior.
- Verify expected transitions from each action.

### Activities

- Use focused prompts and test state transitions quickly.

### Success Criteria

- CE and C behaviors are consistent and explainable.
  :::

---

<!-- layout: Two Content -->

## Exercise: Calculator Project - Decimal Input

Objectives
  - Use AI to generate input-validation logic
  - Prevent multiple decimal points
  - Ensure decimals flow through arithmetic operations

Activities
  1. Ask AI for a decimal input strategy
  2. Generate code to block duplicate decimals in one number
  3. Integrate decimal support into input parser
  4. Test decimal operations with AI-generated test cases

::: column

Success Criteria
  - Decimal input works without duplication errors
  - Arithmetic with decimals is correct
  - Validation logic is explainable

::: notes
Duration ~00:12

## Decimal Input Exercise Instructions

**Prerequisites:** Input parser in place

### Objectives

- Implement robust decimal parsing and validation.

### Activities

- Target parser rules, then validate with focused tests.

### Success Criteria

- No duplicate decimal points accepted.
- Decimal math behaves correctly.
  :::

---

## Exercise: Calculator Project - Sign Toggle (+/-)

Objectives
  - Use AI to generate sign-toggle logic
  - Understand effect on active input and stored value

Activities
  1. Ask AI to generate toggle-sign function for active value
  2. Integrate into input workflow
  3. Test before and after digit entry

Success Criteria
  - Sign toggle works for integers and decimals
  - Learner can explain stored vs active value impact

::: notes
Duration ~00:08

## Sign Toggle Exercise Instructions

**Prerequisites:** Numeric input flow functioning

### Objectives

- Add predictable sign toggling.

### Activities

- Keep implementation minimal and test transitions.

### Success Criteria

- Toggle is stable across value states.
  :::

---

<!-- layout: Two Content -->

## Exercise: Calculator Project - Percentage

Objectives
  - Use AI to clarify percentage interpretation rules
  - Implement percentage logic for common patterns
  - Validate behavior with AI-generated examples

Activities
  1. Ask AI how percentage should behave in a standard calculator
  2. Generate code for:
    - X x Y%
    - Y + X%
    - Y - X%
3. Test each pattern with AI-generated values

::: column

Success Criteria
  - Percentage operations match standard calculator behavior
  - Learner can articulate percentage interpretation rules

::: notes
Duration ~00:15

## Percentage Exercise Instructions

**Prerequisites:** Core arithmetic implemented

### Objectives

- Align percentage behavior with user expectations.

### Activities

- Compare generated logic with known calculator semantics.

### Success Criteria

- Three key percentage patterns operate correctly.
  :::

---

<!-- layout: Two Content -->

## Exercise: Calculator Project - Memory Functions (M+, M-, MR, MC)

Objectives
  - Use AI to design memory subsystem
  - Implement memory add, subtract, recall, and clear
  - Validate memory across multiple operations

Activities
  1. Ask AI for memory-state structure
  2. Generate functions for M+, M-, MR, MC
  3. Integrate memory operations into calculator flow
  4. Test memory persistence over sequences

::: column

Success Criteria
  - Memory functions behave as expected
  - Learner can explain memory state updates

::: notes
Duration ~00:18

## Memory Functions Exercise Instructions

**Prerequisites:** Calculator state architecture defined

### Objectives

- Add reliable memory operations.

### Activities

- Ensure memory state is explicit and testable.

### Success Criteria

- Memory operations are consistent and validated.
  :::

---

<!-- layout: Two Content -->

## Exercise: Calculator Project - Error Handling

Objectives
  - Use AI to identify common error conditions
  - Implement error messages and recovery logic
  - Ensure graceful reset after errors

Activities
  1. Ask AI to list calculator errors (for example divide by zero)
  2. Generate error detection and display logic
  3. Implement reset path after an error
  4. Test error scenarios with AI-generated tests

::: column

Success Criteria
  - Errors are detected and displayed correctly
  - Calculator recovers cleanly
  - Learner can explain error-handling flow

::: notes
Duration ~00:10

## Error Handling Exercise Instructions

**Prerequisites:** Core operations implemented

### Objectives

- Build robust error paths without breaking user flow.

### Activities

- Validate both error detection and post-error recovery.

### Success Criteria

- Error handling is visible, predictable, and recoverable.
  :::

---

<!-- layout: Two Content -->

## Exercise: Calculator Project - Add Trigonometric Functions

Objectives
  - Integrate trigonometric operations
  - Use AI for math wrappers and parsing logic
  - Handle degrees vs radians correctly

Activities
  1. Ask AI to generate sin, cos, tan functions using language math library
  2. Ask AI for degree/radian mode strategy
  3. Implement UI bindings or command triggers
  4. Generate sample input/output table with AI and validate

::: column

Success Criteria
  - Trig results are correct for selected angle mode
  - Degree/radian switching works consistently
  - UI or commands correctly call trig functions
  - Learner can explain validation and refinement steps

::: notes
Duration ~00:15

## Trigonometric Functions Exercise Instructions

**Prerequisites:** Advanced operation framework available

### Objectives

- Add trig support with explicit angle-mode handling.

### Activities

- Implement and validate both behavior and mode switching.

### Success Criteria

- Trig pipeline works end-to-end with tested expectations.
  :::

---

<!-- layout: Two Content -->

## Exercise: Calculator Project - UI

Objectives
  - Use AI to scaffold UI event handlers
  - Connect UI controls to logic functions
  - Validate end-to-end workflow

Activities
  1. Ask AI to generate event-binding code for numeric/operator controls
  2. Integrate logic functions from prior exercises
  3. Test full workflow:
    - Enter decimal
    - Toggle sign
    - Apply percentage
    - Store result in memory

::: column

Success Criteria
  - UI triggers all calculator functions correctly
  - End-to-end workflow completes without errors
  - Learner can explain UI-to-logic mapping

::: notes
Duration ~00:15

## UI Exercise Instructions

**Prerequisites:** Core logic stable and testable

### Objectives

- Wire UI interactions cleanly to existing logic.

### Activities

- Prioritize event mapping clarity over visual polish.

### Success Criteria

- Workflow passes from input to output with no breaks.
  :::

---

<!-- layout: Two Content -->

## Exercise: Calculator Project - Testing

Objectives
  - Generate unit tests with AI assistance
  - Identify quality issues in generated tests
  - Understand why generated tests require review

Activities
  1. Generate Initial Tests:
    - Prompt: "Create unit tests for the calculator operations"
    - Review generated test structure
    - Verify tests call calculator code
  2. Fix Test Issues:
    - If tests are trivial (for example 1 + 1 only), identify issue
    - Prompt: "Update tests to call Calculator class methods"
    - Verify improved test quality

::: column

  3. Run Tests:
    - Execute test suite
    - Review output
    - Debug failing tests with Copilot
  4. Add Edge Cases:
    - Prompt: "Add tests for edge cases like division by zero"
    - Verify exception handling tests

Success Criteria
  - Minimum 8 test cases
  - Tests call actual calculator methods
  - Edge cases and error conditions included
  - All tests pass

::: notes
Duration ~01:00

## Testing Exercise Instructions

**Prerequisites:** Calculator logic implemented

### Objectives

- Improve test quality, not just test count.

### Activities

- Review generated tests critically before accepting.

### Success Criteria

- Test suite is meaningful, comprehensive, and green.
  :::

---

<!-- layout: Two Content -->

## Exercise: Code Coverage

Objectives
  - Set up code coverage reporting
  - Interpret coverage data
  - Improve coverage based on identified gaps

Activities
  1. Enable Coverage Collection:
    - Prompt: "Add code coverage reporting to my test project"
    - Review dependencies added
    - Resolve NuGet/dependency issues with Copilot
  2. Generate Coverage Report:
    - Run tests with coverage
    - Review percentage
    - Identify uncovered paths

::: column

  3. Improve Coverage:
    - Add tests for uncovered methods
    - Re-run coverage and verify improvement
    - Discuss if 100% coverage is necessary

Success Criteria
  - Coverage reporting configured successfully
  - Coverage reports can be generated and interpreted
  - Reasonable coverage achieved (>80% line coverage)
  - Learner understands what coverage metrics mean

::: notes
Duration ~00:40

## Code Coverage Exercise Instructions

**Prerequisites:** Stable test suite

### Objectives

- Use coverage as a guide for targeted testing.

### Activities

- Treat uncovered code as investigation points, not automatic defects.

### Success Criteria

- Coverage setup works and leads to actionable improvements.
  :::

---

<!-- layout: Two Content -->

## Exercise: Calculator Project - Encapsulate Core Logic

Objectives
  - Separate UI concerns from computational logic
  - Use AI to scaffold standalone core logic module/class
  - Ensure UI communicates through a clean API
  - Validate improved testability and maintainability

Activities
  1. Ask AI to generate dedicated component (for example CalculatorEngine or CalculatorCore) containing:
    - Arithmetic operations
    - State management
    - Trig/percentage/memory logic where implemented

::: column

  2. Review and refine API surface (naming, inputs, outputs)
  3. Replace UI-embedded logic with component calls

Success Criteria
  - All features route through external logic component
  - UI contains only event handling/display updates
  - Learner can explain modularity and reuse benefits

::: notes
Duration ~00:15

## Encapsulate Core Logic Exercise Instructions

**Prerequisites:** UI and logic currently coupled

### Objectives

- Improve architecture through separation of concerns.

### Activities

- Create clear, testable boundaries between UI and engine.

### Success Criteria

- Core logic is isolated and reusable.
  :::

---

<!-- layout: Two Content -->

## Exercise: Security Review

Objectives
  - Systematically review code for security issues
  - Address discovered vulnerabilities
  - Strengthen input validation and safe patterns

Activities
  1. Security Review:
    - Prompt: "Review this code for security vulnerabilities"
    - Address identified issues
    - Add input validation where missing

::: column

  2. Validate Fixes:
    - Write tests for fixed vulnerabilities
    - Review fixes with peers
    - Document rationale for security decisions

Success Criteria
  - No obvious security issues remain
  - AI recommendations are critically evaluated and validated

::: notes
Duration ~00:40

## Security Review Exercise Instructions

**Prerequisites:** Functional calculator project

### Objectives

- Apply practical security checks to working code.

### Activities

- Validate fixes with tests and review, not assumptions.

### Success Criteria

- Security posture improves with documented rationale.
  :::

---

<!-- layout: Two Content -->

## Exercise: Documentation

Objectives
  - Add and improve project documentation
  - Review AI-generated docs for accuracy and completeness

Activities
  1. Documentation:
    - Ask Copilot to generate XML/doc comments
    - Review and refine for correctness

::: column

    - Add README usage instructions
    - Ask AI to update existing documentation sections

Success Criteria
  - Documentation is comprehensive and accurate
  - AI-generated content is critically reviewed before acceptance

::: notes
Duration ~00:40

## Documentation Exercise Instructions

**Prerequisites:** Stable code to document

### Objectives

- Produce maintainable, user-focused documentation.

### Activities

- Treat generated docs as drafts requiring technical review.

### Success Criteria

- Docs are complete, correct, and actionable.
  :::

---

<!-- layout: Two Content -->

## Exercise: Refactoring

Objectives
  - Apply refactoring best practices
  - Compare alternative implementations
  - Evaluate trade-offs before choosing changes

Activities
  1. Refactoring Exercise:
    - Ask Copilot for alternative implementations
    - Compare readability, complexity, and maintainability
    - Discuss trade-offs and select best approach

::: column

  2. Implement Refactor:
    - Apply selected refactor
    - Ensure tests still pass
    - Review code quality improvements

Success Criteria
  - At least one refactoring improvement implemented
  - Code quality and maintainability improved
  - AI suggestions critically evaluated

::: notes
Duration ~00:40

## Refactoring Exercise Instructions

**Prerequisites:** Existing implementation with improvement opportunities

### Objectives

- Use AI for option generation, then apply engineering judgment.

### Activities

- Compare alternatives using explicit criteria.

### Success Criteria

- Selected refactor improves clarity without regressions.

:::

---

﻿---
ai_generated: true
model: "openai/gpt-5.3-codex@2026-03-16"
operator: "johnmillerATcodemag-com"
chat_id: "lab2-test-coverage-improvement-exercise-20260317"
prompt: |
  create an exercise slide, using the #file:exercise-template.md, for Lab 2: Test Coverage Improvement.
started: "2026-03-17T03:19:00Z"
ended: "2026-03-17T03:23:00Z"
task_durations:
  - task: "template alignment"
    duration: "00:01:00"
  - task: "exercise authoring"
    duration: "00:03:00"
total_duration: "00:04:00"
ai_log: "ai-logs/2026/03/17/lab2-test-coverage-improvement-exercise-20260317/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---
# Exercise: Test Coverage Improvement || Exercise: From "It Works on My Machine" to Actually Tested

## Exercise: Test Coverage Improvement

Objectives

- Analyze code coverage reports
- Use Copilot to intelligently add tests
- Achieve target coverage percentage
- Balance quantity vs. quality of tests

Activities

1. Review Current Coverage:

- Run tests with coverage reporting
- Identify uncovered code paths
- Analyze coverage percentage by file/class

2. Targeted Test Generation:

- Prompt: "Add tests to increase code coverage to [X]%"
- Observe how Copilot identifies gaps
- Review generated tests for quality

3. Strategic Coverage Improvement:

- Prompt: "Add tests for edge cases in division operation"
- Prompt: "Add tests for corner cases like divide by zero"
- Prompt: "Add integration tests for evaluate arithmetic method"

4. Verify Test Quality:

- Confirm tests call real implementation code
- Confirm tests verify expected behavior, not just execution
- Confirm edge cases are properly handled

5. Re-run Coverage:

- Execute test suite with coverage
- Compare before/after percentages
- Identify remaining gaps

Success Criteria

- Code coverage increased by at least 20 percentage points
- All new tests are meaningful and test actual implementation
- Tests include edge cases and error conditions
- Coverage report shows improved metrics
- Understanding of test quality vs. quantity trade-offs

::: notes
Duration ~00:45

## Test Coverage Improvement Exercise Instructions

**Prerequisites:** Lab 1 completed, existing test suite

### Objectives

- Analyze code coverage reports
- Use Copilot to intelligently add tests
- Achieve target coverage percentage
- Balance quantity vs. quality of tests

### Activities

1. Review current coverage metrics and identify weak areas by file/class.
2. Use Copilot prompts to generate targeted tests for uncovered code paths.
3. Improve strategically with edge-case and integration-focused prompts.
4. Validate test quality to ensure behavior is truly verified.
5. Re-run coverage and compare before/after outcomes.

### Success Criteria

- Coverage increases by at least 20 percentage points.
- New tests are meaningful and exercise actual implementation logic.
- Edge cases and error conditions are covered.
- Coverage reporting clearly shows improvement.
- Participants can explain quality vs. quantity trade-offs.

### Key Learning Point

As discovered in the session, asking Copilot to "increase coverage to 50%" can work because it can intelligently identify which code paths need testing. This can be more efficient than manually finding every gap, but quality checks are still required.
:::

---

﻿---
ai_generated: true
model: "openai/gpt-5.3-codex@2026-03-16"
operator: "johnmillerATcodemag-com"
chat_id: "lab3-test-driven-development-exercise-20260317"
prompt: |
  create an exercise slide, using the #file:exercise-template.md, for Lab 3: Test-Driven Development (TDD) with Copilot.
started: "2026-03-17T03:21:00Z"
ended: "2026-03-17T03:25:00Z"
task_durations:
  - task: "template mapping"
    duration: "00:01:00"
  - task: "exercise authoring"
    duration: "00:03:00"
total_duration: "00:04:00"
ai_log: "ai-logs/2026/03/17/lab3-test-driven-development-exercise-20260317/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---

# Exercise: Test-Driven Development with Copilot || Exercise: Write the Test First. Trust the Process.

---

<!-- layout: Two Content -->

## Exercise: Test-Driven Development (TDD) with Copilot

Objectives
  - Practice TDD workflow with AI assistance
  - Write failing tests before implementation
  - Use tests to drive design decisions
  - Understand red-green-refactor cycle

Activities
  1. Define New Feature:
    - Choose a feature (for example, memory operations for calculator)
    - Store current result (ANS/answer functionality)
    - Recall previous result
    - Handle "ANS + 5" style operations
  2. Write Failing Tests First:
    - Prompt: "Using TDD, create tests for a memory/answer feature in the calculator. DO NOT implement the feature yet."
    - Review generated tests
    - Verify tests reference methods that do not exist yet
  3. Run Tests (Expect Failures):
    - Execute test suite
    - Observe compilation errors or test failures
    - Document what is missing
  4. Implement Feature to Pass Tests:
    - Prompt: "Implement the memory/answer feature to make the tests pass"
    - Review generated implementation
    - Run tests again
    - Verify all tests now pass
  5. Refactor:
    - With tests passing, ask for improvements
    - Prompt: "Refactor the answer implementation for better readability"
    - Verify tests still pass after refactoring

Success Criteria
  - Tests written before implementation
  - Initial test run shows failures (red phase)
  - Implementation makes all tests pass (green phase)
  - Code refactored while maintaining passing tests
  - Understanding of TDD benefits and workflow

::: notes
Duration ~00:60

## Test-Driven Development (TDD) with Copilot Exercise Instructions

**Prerequisites:** Understanding of TDD principles

### Objectives

- Practice TDD workflow with AI assistance
- Write failing tests before implementation
- Use tests to drive design decisions
- Understand red-green-refactor cycle

### Activities

1. Select a small feature and define expected behavior.
2. Ask Copilot for tests only, and confirm the implementation is still missing.
3. Run tests and capture failures to validate the red phase.
4. Implement the minimum code required to satisfy tests.
5. Refactor for readability and maintainability while keeping tests green.

### Success Criteria

- Tests are authored before implementation code.
- The first execution clearly fails (red).
- Feature implementation makes tests pass (green).
- Refactoring preserves passing tests.
- Participants can explain the value of TDD in AI-assisted development.

### TDD Cycle

1. **Red:** Write a failing test.
2. **Green:** Write minimal code to make it pass.
3. **Refactor:** Improve code while keeping tests green.
   :::

---

﻿---
ai_generated: true
model: "anthropic/claude-sonnet-4.6"
operator: "johnmillerATcodemag-com"
chat_id: "ai-assisted-pr-marp-20260314"
prompt: |
  create a marp deck describing AI assistance in creating github pull requests
started: "2026-03-14T20:03:48Z"
ended: "2026-03-14T20:10:00Z"
task_durations:
  - task: "content structuring"
    duration: "00:02:00"
  - task: "slide creation"
    duration: "00:05:00"
  - task: "speaker notes"
    duration: "00:03:00"
total_duration: "00:10:00"
ai_log: "ai-logs/2026/03/14/ai-assisted-pr-marp-20260314/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---

# AI-Assisted Pull Request Workflows || Pull Requests That Actually Get Reviewed

::: notes
Duration ~00:01

Welcome to this session on using AI to improve the pull request workflow. GitHub Copilot and related AI tools can dramatically reduce the friction of creating, reviewing, and merging pull requests.

**Key Points**:

- PRs are a critical communication artifact in software development
- AI can help at every stage: drafting, describing, reviewing, and summarizing
- The goal is not to replace human judgment but to reduce toil

**Delivery**: Open by asking the audience how much time they spend writing PR descriptions or waiting for code review. Frame AI assistance as a way to reclaim that time.

**Transition**: "Let's look at where AI fits in the pull request lifecycle."
:::

---

## The Pull Request Lifecycle

| Stage               | AI Assistance                  |
| ------------------- | ------------------------------ |
| Writing code        | Copilot completions            |
| Drafting the PR     | Generated description          |
| Code review         | Inline suggestions & summaries |
| Addressing feedback | Guided fixes                   |
| Final merge         | Automated checks               |

::: notes
Duration ~00:02

**Key Points**:

1. The PR lifecycle is a feedback loop, not a one-way street
2. Most developers focus on the code-writing stage but spend significant time on communication tasks
3. AI assistance compresses the non-coding parts of the cycle

**Examples to Share**:

- A developer who writes great code but struggles with clear PR descriptions benefits from AI drafting
- A reviewer who is overwhelmed with large PRs benefits from AI summaries

**Audience Interaction**: "Which stage do you find most time-consuming or frustrating?"

**Transition**: "Let's start with where most of the AI value is—creating the PR itself."
:::

---

## AI-Generated PR Descriptions

GitHub Copilot can **draft your PR description** based on your diff:

- Summarizes **what changed** and **why**
- Suggests **testing instructions**
- Highlights **breaking changes**
- Links related **issues and tickets**

> Use 'gh pr create' with Copilot in the CLI, or the **GitHub web editor** with AI suggestions

::: notes
Duration ~00:03

**Key Points**:

1. Copilot analyzes the diff and generates a structured description automatically
2. Good PR descriptions save reviewers time and reduce back-and-forth questions
3. The AI draft is a starting point—always review and personalize it

**Demo Tip**: If demoing live, show 'gh pr create' in the terminal and trigger Copilot suggestions in the description field.

**Common Pitfall**: AI descriptions can be verbose. Encourage developers to trim and focus on the "why" rather than just the "what."

**Audience Interaction**: "How many of you write a detailed PR description every time? How many leave it mostly empty?"

**Transition**: "Once the PR is open, AI continues to help on the review side."
:::

---

## AI-Powered Code Review

GitHub Copilot assists reviewers with:

- **Inline explanations** of complex code
- **Suggested improvements** with rationale
- **Security vulnerability** detection
- **Test coverage** gap identification
- **Style and convention** enforcement

> Use '@workspace' in Copilot Chat to ask questions across the entire PR diff

::: notes
Duration ~00:03

**Key Points**:

1. AI doesn't replace human reviewers—it reduces the cognitive load so reviewers can focus on design and logic
2. Copilot Chat in the PR view lets reviewers ask questions like "What does this function do?" without leaving the review
3. Security scanning tools (GitHub Advanced Security + Copilot Autofix) can suggest fixes for flagged issues

**Examples to Share**:

- Reviewer asks: "Is there a simpler way to write this?" → Copilot suggests a refactored version
- Reviewer asks: "Does this handle null input?" → Copilot analyzes and flags a potential null reference

**Audience Interaction**: "Have you used Copilot Chat during a code review? What kinds of questions did you ask?"

**Transition**: "Beyond individual comments, AI can also summarize entire PRs."
:::

---

## Copilot PR Summaries

GitHub Copilot can **summarize large PRs** automatically:

- Condenses hundreds of lines of diff into a **paragraph**
- Categorizes changes: _features, fixes, refactors_
- Flags **high-risk areas** that need closer review
- Generates a **changelog entry** from the summary

```
GitHub.com → Pull Request → Copilot Summary button
```

::: notes
Duration ~00:02

**Key Points**:

1. This feature is particularly valuable for large PRs with many files changed
2. Summaries help async teams where reviewers may not have full context
3. The summary can be copied directly into release notes or changelogs

**Demo Tip**: Show the Copilot summary button on GitHub.com if doing a live demo. Highlight how it categorizes changes.

**Pro Tip**: Teams can require a Copilot summary as part of their PR checklist to ensure all PRs are self-documenting.

**Transition**: "Now let's look at how Copilot helps you respond to review feedback."
:::

---

## Responding to Review Feedback

AI accelerates **addressing reviewer comments**:

1. Copilot suggests **code fixes** inline from review comments
2. Ask Copilot Chat: _"How do I fix this review comment?"_
3. Copilot **Autofix** resolves flagged security issues
4. Batch-address similar comments across files

> 🔁 The feedback loop closes faster when AI drafts the fix and the human approves it

::: notes
Duration ~00:03

**Key Points**:

1. The most time-consuming part of PR iteration is addressing multiple review comments
2. Copilot can read a review comment and suggest the corresponding code change
3. Autofix is especially powerful for security alerts—it not only flags the issue but provides the patched code

**Workflow to Describe**:

1. Reviewer leaves a comment: "This should use a parameterized query"
2. Developer clicks Copilot suggestion next to the comment
3. Copilot generates the parameterized version
4. Developer reviews and commits

**Audience Interaction**: "How many review cycles does a typical PR go through on your team? Could AI reduce that?"

**Transition**: "Let's talk about automating the checks that run on every PR."
:::

---

# Multi-Model Implementation Comparison || Ask Three AIs, Get Four Opinions

---

## Multi-Model Implementation Comparison

- Implementing changes with different AI models
- Comparing approaches and outcomes
- Risk assessment and quality evaluation
- Best practice synthesis
- Exercises for hands-on practice

::: notes
Introduce this module as a way to help teams understand how different AI models behave when given the same task. Emphasize that multi-model comparison is a powerful guardrail: it reduces hallucinations, improves quality, and helps teams choose the right model for the right job.
:::

---

## Implementing Changes With Different AI Models

- Why use multiple models?
- Different reasoning styles
- Different strengths (refactoring, documentation, architecture)
- Cross-validation reduces risk
- Helps detect missing context or contradictions
- Typical use cases
  - Refactoring comparisons
  - Documentation consistency checks
  - Architecture proposal validation

::: notes
Explain that no single model is perfect. Using multiple models gives teams a broader perspective and helps catch errors or blind spots that one model alone might miss.
:::

---

## Comparing Approaches & Outcomes

What to compare
  - Code structure and clarity
  - Architectural alignment
  - Test quality
  - Documentation completeness
  - Risk level of proposed changes

Benefits
  - Identifies the safest implementation
  - Surfaces hidden assumptions
  - Highlights model-specific biases

::: notes
Encourage participants to treat model outputs like multiple drafts from different engineers. The goal is not to pick a winner — it's to synthesize the best ideas.
:::

---

## Risk Assessment & Quality Evaluation

Risk indicators
  - Missing tests
  - Large or unnecessary refactors
  - Violations of instruction files
  - Unclear or undocumented behavior

Quality indicators
  - Small, incremental changes
  - Clear reasoning
  - Strong test coverage
  - Alignment with evergreen principles

::: notes
Reinforce that risk assessment is essential in brownfield systems. Even if a model produces elegant code, it may be too risky without proper guardrails.
:::

---

## Exercise: Prompt Copilot to Address Technical Debt

Objectives
Practice writing high-signal prompts
Apply architectural constraints
Produce safe, incremental remediation requests
Activities
Select a small piece of technical debt.
Write a prompt that includes:
  - Description of the debt
  - Constraints and rules
  - Expected behavior
  - Required tests and documentation
Ask Copilot to propose a remediation.
Review the output for correctness.
Success Criteria
Prompt is clear, scoped, and actionable
Copilot produces a safe, incremental change
Output aligns with architectural rules
Provenance metadata is included

::: notes
Duration ~00:10

Encourage participants to choose a real example from their brownfield system. The goal is clarity and safety, not complexity.
:::

---

<!-- layout: two-column -->

## Exercise: Prompt Multiple Models to Address Technical Debt

Objectives
  - Compare outputs from different models
  - Identify strengths and weaknesses
  - Evaluate risk and quality

Activities
  - Select a small technical debt item.
  - Prompt two or more models to propose a fix.

::: column

  - Compare outputs for:
    - Safety
    - Clarity
    - Test coverage
    - Architectural alignment
  - Synthesize the best elements into a final solution.

Success Criteria
  - Differences between models are clearly identified
  - Risks and strengths are evaluated
  - Final synthesized solution is safe and incremental
  - Provenance metadata is included

::: notes
Duration ~00:15

Encourage participants to think like reviewers comparing multiple PRs. The goal is to understand model behavior, not to pick a favorite.
:::

---

﻿---
marp: true
theme: default
paginate: true
---

# Evergreen Software Core Principles || Code That Doesn't Rot: A Love Story

---

<!-- layout: Two Content -->

## Core Evergreen Principles

**Design and interface principles**
  - **Intent-First Design**
    Define purpose, invariants, and boundaries before writing code.
  - **Stable Interfaces, Evolving Internals**
    Keep contracts predictable while implementations improve.
  - **Lifecycle Governance**
    Maintain quality through tests, versioning, and human validation.

::: column

**Regeneration principles**
  - **Continuous Regeneration with Guardrails**
    Use AI safely with tests, specs, and architectural constraints.
  - **Modular, Replaceable Components**
    Structure the system so parts can be regenerated or swapped without cascading breakage.

::: notes
Duration ~00:05

Introduce Evergreen Software Development as a philosophy for building systems that can evolve indefinitely without degrading. This is crucial for AI-assisted development.

Explain each principle:

1. Intent-First Design: Document WHY before WHAT. AI can regenerate code but needs clear intent.
2. Stable Interfaces: Public contracts stay stable while implementations improve continuously.
3. Continuous Regeneration: AI can safely rewrite components when guardrails (tests, specs) exist.
4. Modular Components: Any piece can be regenerated without breaking the system.
5. Lifecycle Governance: Quality maintained through automation and human oversight.

Key insight: Traditional software rots over time. Evergreen software is designed to be continuously regenerated and improved.

Transition: "Let's see why software fails to be evergreen..."
:::

---

<!-- layout: Two Content -->

## Why Software Fails to Be Evergreen

**Design failures**
- **Intent Rot**
  - Purpose, constraints, and invariants are undocumented or lost.
- **Unstable or Leaky Interfaces**
  - APIs and boundaries change unpredictably.
- **Tightly Coupled Architecture**
  - Components depend on each other's internals.

::: column

**Safety failures**
- **Insufficient Guardrails**
  - Missing tests and validation make safe regeneration impossible.
- **One-Off Patches and Drift**
  - Ad-hoc fixes pull the system away from intended design.

::: notes
Duration ~00:05

Explain the common anti-patterns that prevent software from being evergreen. These are the enemies of long-term maintainability.

1. Intent Rot: Documentation becomes outdated or nonexistent. AI can't regenerate code when it doesn't know the purpose.
2. Unstable Interfaces: Breaking changes cascade through the system. AI regeneration requires stable contracts.
3. Tight Coupling: Changes in one component break others. AI can't safely regenerate tightly coupled code.
4. Insufficient Guardrails: Without tests and specs, AI-generated code can't be validated.
5. Drift: Ad-hoc fixes create divergence from the design. The system becomes unpredictable.

Real-world examples:

- Legacy system with no documentation (intent rot)
- Microservices with frequently changing APIs (unstable interfaces)
- Monolith with circular dependencies (tight coupling)

Transition: "Let's see how to avoid these pitfalls..."
:::

---

<!-- _class: lead -->

## Course Modules

- Intro
- AI Assisted Software Development
- Intro to Copilot
- AI Assistance in Action
- **▶ Adding AI Guardrails**

---

<!-- _class: lead -->

# Adding AI Guardrails

---

## Adding AI Guardrails

- Adding AI Guardrails
- What Are Instruction Files?
- Scoped `<name>.instructions.md` files
- Instruction File `applyTo` Patterns
- Core Instructions
- Organizational vs. Repository Instruction Files
- Technology Inventory & Instruction Generation Exercise Instructions

---

# Adding AI Guardrails || Teaching Your AI to Color Inside the Lines

---

## Adding AI Guardrails

- What are instructions, prompts, and Agents
- Creating instruction, prompt, and Agent files
- Meta prompts that generate these files
- Instructions for generating artifacts
- Enforcing provenance for AI-assisted artifacts

::: notes
Introduce this module as the foundation for safe, predictable AI-assisted development.

Guardrails ensure that AI output is intentional, reviewable, and aligned with architectural and organizational standards.

These practices turn AI from a novelty into a disciplined engineering tool.
:::

---

## Instructions for Generating Artifacts

- Best practices
  - Define the artifact type
  - Specify required sections
  - Provide examples or templates
  - Include acceptance criteria
  - Require the model to restate constraints

::: notes
When asking AI to generate an artifact, be explicit about structure and constraints.

This prevents drift and ensures the output is usable without heavy editing.
:::

---

## Enforcing Provenance for AI Artifacts

- AI involvement
- Model used
- Date generated
- Human reviewer
  - Store provenance in headers, footers, or side cars
  - Track revisions in version control

::: notes
Provenance is essential for conformance, auditability, and long-term maintainability.

It ensures teams know which artifacts were AI-generated, which were human-generated, and which were hybrid.
:::

---

## Instructions for AI Generated Artifacts

The one instruction file that rules them all

::: notes
Provenance is essential for conformance, auditability, and long-term maintainability.

It ensures teams know which artifacts were AI-generated, which were human-generated, and which were hybrid.
:::

---

## AI-Assisted Output Instructions

- Ensures provenance and logging for all AI-assisted outputs
- Defines required metadata, logging workflow, and quality gates
- Protects code quality and enables audits

::: notes
This slide introduces the purpose of the AI-Assisted Output Instructions file: to enforce traceability, quality, and compliance for all AI-generated artifacts in the repository.
:::

---

## Required Provenance Metadata

Every AI-assisted artifact must include:

```yaml
ai_generated: true
model: provider/model@version
operator: username
chat_id: unique chat identifier
prompt: exact prompt text
started/ended: timestamps
task_durations & total_duration
ai_log: path to conversation log
source: who/what created the file
```

::: notes
This slide lists the mandatory metadata fields that must be embedded in every AI-generated file.

These fields ensure each artifact can be traced back to its origin, model, and operator.
:::

---

## Metadata Placement Policy

- Use YAML front matter for Markdown and similar formats
- For binaries/images, use a sidecar <artifact>.meta.md
- Never use sidecars for Markdown

::: notes
This slide explains where and how to place provenance metadata.

Markdown files must use embedded YAML front matter; only non-embeddable formats use sidecar files.

Note: Instructions files have limited support for metadata and must use sidecar files
:::

---

## AI Chat Logging Workflow

- Each chat creates a unique log folder: 'ai-logs/yyyy/mm/dd/<chat-id>/'
- Required files:
  - 'conversation.md' (full transcript)
  - 'summary.md' (objectives, decisions, outcomes)
  - 'artifacts/' (optional)
- Never reuse chat logs between sessions

::: notes
This slide describes the logging structure for AI chats.

Each session gets its own folder, transcript, and summary, ensuring clear separation and traceability.
:::

---

## Quality & PR Checklist

- Metadata complete and correct
- Conversation and summary logs exist
- 'README.md' updated for notable artifacts
- No sensitive data in outputs
- All AI-generated content traces to a chat log

::: notes
This slide summarizes the quality gates and PR requirements.

Artifacts must be fully documented, logs must exist, and sensitive data must be avoided.
:::

---

## Copilot Integration Requirements

- Copilot must auto-manage chat IDs and logs
- Metadata injected automatically
- Block artifact creation if chat context is missing
- Enforce provenance before file creation

::: notes
This slide highlights the requirements for GitHub Copilot integration.

Copilot should automate chat management, metadata injection, and enforce compliance before generating files.
:::

---

## Enforcement & Remediation

- PRs blocked if provenance is incomplete
- Missing logs or metadata must be added before merge
- Orphaned artifacts require reconstruction of logs and metadata

::: notes
This slide explains enforcement:

PRs are blocked if requirements are not met.

Any missing provenance must be remediated before merging.
:::

---

## Core Instruction files

'agent-file.instructions.md'
  - Defines the structure and contents of agents

'instruction-files.instructions.md'
  - Defines the structure and contents of instruction files

'prompt-file.instructions.md'
  - Defines the structure and contents of prompts

'instruction-prompt-files.instructions.md'
  - Defines the structure and contents of prompts that create instruction files

---

<!-- layout: Two Content -->

## Exercise: Copy the Core Instructions

Objectives
  - Understand file organization for AI-assisted output policies
  - Practice copying files between repositories
  - Ensure compliance with output metadata requirements

Activities
  1. Locate '.github/instructions/ai-assisted-output.instructions.md' in the AI-Assisted-Software-Development repository
  2. Copy the file into the '.github/instructions' folder of the current repository
  3. Copy these files as well:
    - 'chatmode-file.instructions.md'
    - 'instruction-files.instructions.md'
    - 'instruction-prompt-files.instructions.md'
    - 'prompt-file.instructions.md'

::: column

  4. Verify the copied files matches the original
  5. Review the instructions

Success Criteria:
  - The files are present in the current repo
  - The content matches the source file
  - No metadata or formatting is lost

::: notes
Duration ~00:10

This exercise reinforces the importance of maintaining consistent AI-assisted output policies across repositories. By copying the instructions file, participants learn to manage compliance and provenance requirements for AI-generated artifacts. Ensure the copied file is identical and properly placed to support future AI work.
:::

---

<!-- layout: Two Content -->

## Exercise: Create an Instruction File for Evergreen Development

Objectives
  - Capture evergreen principles
  - Define architectural boundaries
  - Specify modernization rules

Activities
  1. Submit the Evergreen Instructions prompt
  2. Review the instructions

::: column

Success Criteria
  - Instruction file is stable and reusable
  - Reflects evergreen development values
  - Provides clear guardrails

::: notes
Duration ~00:15

This reinforces the evergreen mindset and produces a reusable artifact for future AI-assisted work.

Prompt: Submit the prompt #file:create-evergreen-software-instructions.prompt.md
:::

---

## Exercise: Context-Related Issues

Objectives
  - Identify missing context
  - Detect token overflow risks
  - Improve prompt scoping

Activities
  1. Copy the check-context.prompt.md file from the AIASD repository
  2. Review the prompt
  3. Submit the prompt
  4. Review the output

::: column

Success Criteria
  - Correctly identified context gaps

::: notes
Duration ~00:10

This exercise builds intuition for context management—one of the most important AI-era engineering skills.
:::

---

## Exercise: Delegating Work to Copilot

Objectives
Practice delegating multi-step tasks
Ensure Copilot follows architectural rules
Validate AI-generated remediation plans
Activities
Select a multi-step technical debt item.
Ask Copilot to:
  - Analyze the problem
  - Propose a remediation plan
  - Generate code changes
  - Update tests
  - Update documentation
Review Copilot's output.
Identify missing context or risks.
Success Criteria
Delegation prompt is complete and structured
Copilot produces a multi-step plan
Output is safe, incremental, and reversible
Human review identifies any gaps

::: notes
Duration ~00:15

This exercise builds confidence in delegating larger tasks while maintaining safety and architectural alignment. Emphasize that humans remain the final reviewers.
:::

---

## Exercise: Assigning an Issue to Copilot

Objectives
Convert technical debt into a structured issue
Provide Copilot with actionable context
Practice writing acceptance criteria
Activities
Select a technical debt item.
Create a GitHub-style issue with:
  - Title
  - Description
  - Impact and risk
  - Acceptance criteria
  - Provenance metadata
Assign the issue to Copilot.
Review Copilot's proposed remediation.
Success Criteria
Issue is clear and well-structured
Acceptance criteria are testable
Copilot produces a relevant draft
Provenance metadata is present

::: notes
Duration ~00:10

This exercise reinforces the workflow of treating Copilot as a junior developer who receives tasks and produces drafts.
:::

---

﻿---
marp: true
theme: default
paginate: true
---

# Instruction Files || The .editorconfig for Your AI's Soul

::: notes

**Opening**: This is the title slide introducing the concept of instruction files. **Keep It Brief**: Simply say "Let's talk about instruction files—a powerful way to guide AI behavior persistently across your projects." **Visual Cue**: Let the title appear, pause for 2-3 seconds. **No Content Yet**: Don't explain what they are—that's the next slide's job. **Transition**: "First, let me frame what we mean by 'persistent AI behavioral guidelines'..."

**Frame the Concept**: This subtitle slide sets up the key mental model. **Persistent**: Emphasize that unlike one-time prompts, these rules stay active across multiple interactions. **Behavioral**: These files tell AI _how_ to work, not _what_ to build. **Guidelines vs Commands**: "Think of instruction files as automated code review rules that apply every time AI generates code." **Analogy**: "Like .editorconfig or .eslintrc files, but for AI behavior instead of code formatting." **Transition**: "So what exactly are instruction files? Let's define them..."
:::

---

## What Are Instruction Files?

- Persistent configuration files that define AI behavior patterns
- Applied automatically across multiple interactions
- Establish consistent working standards and constraints

Key Characteristics
- Scope: Repository-wide or context-specific
- Persistence: Active across all relevant AI interactions
- Purpose: Define “how” AI should work, not “what” to do

::: notes
**Definition Emphasis**: Read the definition slowly—this is foundational. **Configuration Metaphor**: "Just like you configure your IDE or linter, you configure your AI assistant with instruction files." **Automatic Application**: Key point: once created, they're automatically applied. No need to paste instructions repeatedly. **Standards Example**: "Example: All Azure code must use managed identities, no hardcoded keys. Put that in azure-dev.instructions.md, and AI will follow it automatically." **Scope Explanation**: Can apply broadly ('applyTo: "**"') or narrowly ('applyTo: "*.cs"'). **How vs What**: Clarify: Instructions define _style_ ("use dependency injection") not _tasks_ ("build a login system"). **Audience Check**: "Does this distinction make sense—how versus what?" **Transition**: "Let me show you what one looks like..."
:::

---

## Instruction Files: Use Cases

Perfect For:
- Coding Standards → Consistent style across projects
- Security Policies → Enforce security practices
- Quality Gates → Define testing and review requirements
- Technology Constraints → Specify approved frameworks/tools

Examples:
- azure-development.instructions.md
- testing-standards.instructions.md
- security-requirements.instructions.md

::: notes
**Use Cases Overview**: These are the "why" behind instruction files. **Coding Standards**: "Every team has style preferences—indentation, naming, file organization. Instruction files codify this for AI." **Security Example**: "You can mandate: 'Never log passwords', 'Always sanitize user input', 'Use parameterized queries'. AI will follow these rules automatically." **Quality Gates**: "Require test coverage thresholds, code review checklists, documentation standards." **Technology Constraints**: "Enterprise scenario: only approved libraries/frameworks allowed. Instruction file enforces this." **Real Examples**: Point to each example filename and briefly explain: azure-development covers cloud-specific patterns, testing-standards defines test structure, security-requirements enforces security policies. **Team Benefit**: "This is especially powerful for teams—everyone's AI assistant follows the same rules, producing consistent output." **Transition**: "Before we move on, let me share some best practices..."
:::

---

# Scoped vs Non‑Scoped Instructions || Choosing the Right Instruction File Type

---

## Scoped '<name>.instructions.md' files

- Apply **only** when 'applyTo' matches
- Can **exclude** paths
- For **language‑, framework‑, or domain‑specific rules**
- Ideal for precision control
- Best for **targeted, contextual guidance**

---

## Repo‑level '.md' files

- Apply **everywhere** in the repo
- Always included
- For **universal rules**: style, security, logging, architecture
- No 'applyTo' / 'exclude' support
- Best for **global, evergreen guidance**

---

## Decision Rule

- If it should apply **repo‑wide** → use '.md'
- If it should apply **only in certain paths** → use '.instructions.md'
- If you need **exclusions** → must use '.instructions.md'

::: notes
This slide summarizes the functional difference between the two instruction file types GitHub Copilot supports inside '.github/instructions/'.
Repo‑level '.md' files are unconditional and always included.
Scoped '.instructions.md' files are conditional, support 'applyTo' and 'exclude', and only activate when relevant.
The decision rule gives teams a simple, auditable way to choose the correct mechanism.
:::

---

## 'exclude:' in Practice

```yaml
applyTo:
  - "src/**"
exclude:
  - "src/experimental/**"
  - "src/legacy/*.js"
```

- Scope instructions to 'src/' but carve out experimental and legacy paths
- Only available with '.instructions.md' files (not repo‑level '.md')

---

﻿---
ai_generated: true
model: "anthropic/claude-3.5-sonnet@2024-10-22"
operator: "johnmillerATcodemag-com"
chat_id: "applyto-patterns-marp-deck-20260303"
prompt: |
  create a marp deck that explains the applyTo options. include speaker notes in the pandoc format
started: "2026-03-03T00:00:00Z"
ended: "2026-03-03T00:15:00Z"
task_durations:
  - task: "content structure and outline"
    duration: "00:03:00"
  - task: "slide content creation"
    duration: "00:10:00"
  - task: "speaker notes and refinement"
    duration: "00:02:00"
total_duration: "00:15:00"
ai_log: "ai-logs/2026/03/03/applyto-patterns-marp-deck-20260303/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---

# Instruction File applyTo Patterns || Glob Patterns: The Bouncer at Your AI's Door

---

## Instruction File 'applyTo' Patterns

**Understanding Glob Pattern Matching**

Controlling When Instructions Apply to Your Code

::: notes
Duration ~00:01

Welcome to this presentation on instruction file applyTo patterns. This is a critical concept for managing GitHub Copilot's behavior across your codebase. By the end of this session, you'll understand how to precisely control which files your instruction files apply to using glob patterns.

**Key Point**: This is about precision - getting Copilot to apply the right rules to the right files
**Transition**: "Let's start by understanding what the applyTo field actually does"
:::

---

## Where 'appliesTo' Fits

The filtering mechanism for instruction files.

'appliesTo' is a **selector** that determines _when_ an instruction file is included in the stack.

**Common selectors**

- **repositories** -- specific repos only
- **languages** -- certain languages only
- **filePatterns** -- specific files only
- **tools** -- certain Copilot features only
- **scopes** -- chat only, editor only, and similar contexts

::: notes
'appliesTo' is not a guardrail itself. It's a routing
rule. It prevents irrelevant instructions from polluting the stack and
keeps the assistant focused.
:::

---

## How 'appliesTo' Interacts with the Stack

Filtering happens _before_ merging

1.  Copilot discovers all instruction files in scope
2.  Copilot filters them using 'appliesTo'
3.  Copilot merges the remaining files into the stack

::: notes
This means you can have many instruction files in
'.github/instructions/', but only the ones whose 'appliesTo' match the
current context will be included.
:::

---

## Universal Application

Apply instructions to **all files** in the repository:

```yaml
applyTo: "**"        # All files
applyTo: "**/*"      # All files (explicit)
```

**Use Cases:**
  - AI-assisted output policies
  - General code quality standards
  - Repository-wide conventions
  - Copilot behavior guidelines

**Caution:** Use sparingly - can create conflicts with more specific instructions

::: notes
Duration ~00:02

The double asterisk wildcard is the universal matcher. Use this for repository-wide policies that should apply everywhere - things like your AI-assisted output instructions, general quality standards, or compliance requirements.

**Important warning**: Overusing universal patterns is a common mistake. Every universal instruction adds to the context Copilot needs to process for every file. If you have 10 instruction files all using "\*\*", Copilot has to load all 10 for every single file you open.

**Best practice**: Reserve universal patterns for truly universal policies. Most instructions should be more specific.

**Real example from the repo**: The ai-assisted-output.instructions.md uses "\*_/_" because AI provenance metadata requirements apply to all AI-generated content regardless of file type.

**Ask audience**: "How many instruction files do you think should realistically use universal patterns? Usually no more than 2-3."
:::

---

## 📝 File Extension Matching

Target specific file types using extension patterns:

```yaml
## Single extension
applyTo: "**/*.md"

## Multiple extensions (brace expansion)
applyTo: "**/*.{cs,ts,js}"

## Specific file naming pattern
applyTo: "**/*.instructions.md"
```

**Most Common:**
  - '**/*.md' - All Markdown files
  - '**/*.{cs,ts,js,py}' - Multiple programming languages
  - '**/*.test.js' - Test files
  - '**/*.instructions.md' - Instruction files

::: notes
Duration ~00:02

File extension matching is probably the most common pattern you'll use. The key syntax here is the brace expansion - that's the curly braces with comma-separated extensions.

**Walking through the examples**:

1. "\*_/_.md" - Double star means any directory depth, forward slash, star means any filename, dot md means must end with .md
2. The brace expansion lets you list multiple extensions without repeating the pattern
3. You can be even more specific with compound extensions like .instructions.md

**Pro tip**: When you need to apply instructions to code files across multiple languages, use the brace expansion. In this repo, vertical slice architecture instructions use "\*_/_.{cs,ts,js,py,java,go,rb}" to cover all supported languages.

**Common mistake**: Forgetting the **/ at the start means only files in the root directory match
**Correct**: "**/_.md" matches all markdown files recursively
**Incorrect**: "_.md" only matches markdown files in root directory

**Demonstrate**: Show how the pattern breaks down visually
:::

---

## 📁 Directory-Specific Patterns

Limit instructions to specific directories:

```yaml
## All files in a directory
applyTo: "slides/marp/**"

## Specific file type in directory
applyTo: "src/Features/**/*.cs"

## Multiple directory levels
applyTo: ".github/instructions/**/*.md"
```

**Benefits:**
  - Isolate concerns (slides vs code vs docs)
  - Different rules for different project areas
  - Clearer instruction purpose

::: notes
Duration ~00:02

Directory-specific patterns are crucial for organizing large codebases. They let you say "these architecture rules only apply to source code" or "these formatting rules only apply to slides."

**Breaking down the syntax**:

- "slides/marp/**" - Note there's no leading slash or asterisks. This matches the specific directory path, then /** means everything underneath it
- "src/Features/\*_/_.cs" - Combines directory path with file extension filter
- The pattern is always relative to the repository root

**Real-world example from this repo**: The marp-slides.instructions.md uses "slides/marp/\*\*" because those formatting rules should only apply to presentation slides, not to other markdown files like README.md or documentation.

**Another example**: You might have vertical-slice.instructions.md with "src/Features/\*_/_.cs" so those architectural patterns only apply to feature code, not to infrastructure or configuration code.

**Visual aid**: If possible, show the repository structure and how the pattern matches
**Transition**: "Let's dive deeper into the glob syntax itself"
:::

---

## Glob Pattern Syntax

**Core wildcards**
  - '*' -- any characters except '/'
  - '**' -- zero or more directory levels
  - '?' -- exactly one character

**Pattern sets**
  - '[abc]' -- one character from a set
  - '[a-z]' -- one character from a range
  - '{a,b}' -- one of several alternatives

**Examples**
  - '*.md' -> 'README.md'
  - '**/*.md' -> 'docs/guide.md'
  - '*.{js,ts}' -> 'app.ts'

::: notes
Duration ~00:03

This slide is your reference guide for glob pattern syntax. Let's walk through each one with careful attention to the distinctions:

**Single asterisk (\*)**:

- Matches any characters EXCEPT forward slash
- "\*.md" matches "README.md" in the current directory
- Does NOT match "docs/README.md" - the slash breaks the match
- Think of it as "wildcard within one directory level"

**Double asterisk (**)\*\*:

- This is the recursive directory matcher
- Can match zero or more directory levels
- "\*_/_.md" matches files at any depth
- Critical: It must be its own path segment - "**/" not "**/file.md"

**Question mark (?)**:

- Exactly one character (useful for versioned files)
- "config?.json" matches "config1.json" and "configA.json"
- Does NOT match "config10.json" (that's two characters)

**Brackets [abc] and [a-z]**:

- Character classes - match one character from the set
- Useful for version numbers or variant files
- "file[123].md" matches file1.md, file2.md, file3.md

**Braces {a,b}**:

- This is alternation - match any of the alternatives
- Most commonly used for file extensions
- "\*.{js,ts,jsx,tsx}" matches all JavaScript/TypeScript files
- Each alternative can itself be a pattern

**Demonstrate**: Show 2-3 concrete examples with actual files
**Transition**: "Now let's see these patterns in action with real examples from this repository"
:::

---

## Pattern Matching Rules

**Key Points to Remember:**
  - Patterns are evaluated when files are opened
  - Multiple instruction files can match the same file
  - More specific patterns take precedence (in terms of clarity, not override)
  - Patterns are relative to repository root
  - Case sensitivity depends on file system (Windows: no, Linux: yes)

**When Copilot Evaluates Patterns:**
  1. File opened in editor → Check all instruction files
  2. Load matching instructions into context
  3. Apply rules during code generation

::: notes
Duration ~00:03

Let's consolidate the technical details about how pattern matching actually works in practice:

**Evaluation Timing**:
Pattern matching happens dynamically. When you open a file, VS Code/Copilot:

1. Scans all instruction files in the workspace
2. Evaluates each applyTo pattern against the current file path
3. Loads matching instructions into Copilot's context window
4. This context is then used for all Copilot operations in that file

This is important because it means pattern matching is NOT a one-time operation at startup - it happens constantly as you switch between files.

**Multiple Matches**:
It's perfectly valid for multiple instruction files to match the same file. Copilot will try to follow all applicable instructions. This is why avoiding conflicts is so important - if two instructions contradict each other, Copilot will struggle.

**Example of intentional multiple matches**:

- general-coding-standards.instructions.md with "\*_/_.cs"
- vertical-slice-architecture.instructions.md with "src/Features/\*_/_.cs"
- A file at "src/Features/Users/CreateUser.cs" matches both
- Both instruction sets apply (general standards + architecture patterns)
- This works if the instructions are complementary

**Specificity and Precedence**:
Unlike CSS, there's no formal "specificity" calculation where more specific patterns override less specific ones. Instead, ALL matching instructions are loaded. The idea of "precedence" is more about human clarity - more specific patterns make intent clearer, but don't technically override anything.

**Repository Root**:
All patterns are relative to the workspace root (where .git directory is located). There's no way to use absolute paths, which is good for portability.

**Case Sensitivity**:
Critical detail - this depends on the underlying file system:

- Windows: case-insensitive ("\*.MD" matches "file.md")
- Linux: case-sensitive ("\*.MD" matches "file.MD" but not "file.md")
- macOS: depends on file system format (usually case-insensitive)

Best practice: Always use lowercase in patterns and standardize file naming to lowercase to avoid cross-platform issues.

**Important**: "The dynamic evaluation means you can test instruction changes immediately - just close and reopen a file"
:::

---

﻿---
marp: true
theme: default
paginate: true
---

# Core Instruction Files || The Constitution of Your AI Republic

---

<!-- layout: Two Content -->

## Core Instructions

**Artifact and workflow rules**

'ai-assisted-output.instructions.md'
  - Guidance for AI-generated artifacts

'chatmode-file.instructions.md'
  - Guidance for generating chat modes

'instruction-files.instructions.md'
  - Guidance for generating instruction files

::: column

**Prompt-related rules**

'prompt-file.instructions.md'
  - Guidance for generating prompt files
'instruction-prompt-files.instructions.md'
  - Guidance for prompts that generate instruction files

::: notes
Duration ~00:03

Present the core instruction files that govern AI-assisted development in this repository. These files are the foundation of the guardrails system.

Explain each file's purpose:

- ai-assisted-output.instructions.md: The master policy for ALL AI-generated content, covering provenance, logging, and compliance
- chatmode-file.instructions.md: Defines how to create custom chat modes for specific development workflows
- instruction-files.instructions.md: Meta-instructions for creating new instruction files
- prompt-file.instructions.md: Guidelines for creating reusable prompt files
- instruction-prompt-files.instructions.md: Meta-prompts that generate instruction files

Emphasize the hierarchical nature: ai-assisted-output is the root policy that all others reference.

Transition: "Let's dive into how to use these..."
:::

---

﻿---
ai_generated: true
model: "openai/gpt-5.3-codex@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "organizational-vs-repository-instruction-files-20260317"
prompt: |
  create a marp deck with the title "Organizational vs. Repository Instruction Files"

  That covers this material: Business/Enterprise tier capabilities; Path-scoped instruction files; Folder-level technology-specific rules
started: "2026-03-17T08:20:17.2570320-07:00"
ended: "2026-03-17T08:32:00.0000000-07:00"
task_durations:
  - task: "requirements and instruction review"
    duration: "00:06:00"
  - task: "deck authoring"
    duration: "00:05:00"
  - task: "provenance and README updates"
    duration: "00:01:00"
total_duration: "00:12:00"
ai_log: "ai-logs/2026/03/17/organizational-vs-repository-instruction-files-20260317/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---

# Organizational vs. Repository Instruction Files || Corporate Rules vs. Your Team's Rules

---

## Organizational vs. Repository Instruction Files

- Business/Enterprise tier capabilities
- Path-scoped instruction files
- Folder-level technology-specific rules

::: notes
Frame this as a layering strategy, not an either-or choice. The audience should leave with a practical model for deciding what belongs at enterprise scope versus repository scope. Keep this opening to about 60-90 seconds.
:::

---

## Why Two Instruction Layers Exist

- Enterprise instructions enforce baseline policy and governance
- Repository instructions optimize for project context and implementation detail
- Together they balance consistency and local autonomy

**Key Idea**

Define global guardrails once, then narrow behavior where code lives.

::: notes
Explain that teams usually fail by over-centralizing or over-fragmenting. Centralize non-negotiables, decentralize implementation guidance. Emphasize this prevents policy drift while keeping day-to-day delivery fast.
:::

---

## Business/Enterprise Tier Capabilities

- Organization-wide safety and compliance standards
- Approved model and tool usage policy
- Mandatory provenance and audit requirements
- Security and legal baselines (secret handling, license constraints)
- Shared quality gates for CI/CD

**Typical Scope**

All repositories, all teams, all environments.

::: notes
Call out that enterprise-tier files should be stable and short. They should define constraints, not feature behavior. Give examples: required metadata fields, approved hosts, restricted operations, and mandatory security checks.
:::

---

﻿---
ai_generated: true
model: "openai/gpt-5.3-codex@unknown"
operator: "johnmillerATcodemag-com"
chat_id: "exercise-technology-inventory-instruction-generation-20260317"
prompt: |
  create an exercise marp deck using the slides\marp\exercise-template.deck.md template with the title "Exercise: Technology Inventory & Instruction Generation"

  That covers this material: Creating inventory of project technologies; Background sessions for concurrent work; Generating multiple instruction files simultaneously; Session management interface
started: "2026-03-17T08:37:22.0000000-07:00"
ended: "2026-03-17T08:42:00.0000000-07:00"
task_durations:
  - task: "template mapping"
    duration: "00:01:30"
  - task: "exercise authoring"
    duration: "00:02:30"
  - task: "provenance and catalog updates"
    duration: "00:01:00"
total_duration: "00:05:00"
ai_log: "ai-logs/2026/03/17/exercise-technology-inventory-instruction-generation-20260317/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---

<!-- layout: Two Content -->

# Exercise: Technology Inventory and Instruction Generation || Exercise: Take Stock Before You Start Spending Tokens

Objectives
  - Create a clear inventory of project technologies across the repository
  - Use background sessions to run concurrent analysis and drafting work
  - Generate multiple instruction files simultaneously from the inventory results
  - Practice session management interface workflows for parallel task control

Activities
  1. Technology Inventory Build:
    - Scan the repository and list languages, frameworks, build tools, and test stacks
    - Group technologies by folder ownership and lifecycle criticality
    - Identify missing or outdated instruction coverage per technology area
  2. Background Session Orchestration:
    - Start parallel background sessions for discovery, drafting, and validation
    - Assign one focused outcome per session (inventory, file generation, review)
    - Capture each session's outputs and merge findings into one working backlog

::: column

  3. Simultaneous Instruction Generation:
    - Generate multiple instruction files for high-priority technology folders
    - Apply path-scoped patterns to each generated instruction file
    - Validate that each file is targeted, non-overlapping, and implementation-ready
  4. Session Management Interface Review:
    - Track session state, ownership, and completion status
    - Resolve collisions between concurrently generated instruction outputs
    - Close sessions with a summarized decision log and next-step actions

Success Criteria
  - Technology inventory includes stack, location, and risk/priority attributes
  - At least three instruction files are generated concurrently and scoped correctly
  - Background sessions are documented with clear responsibilities and outcomes
  - Session management process is repeatable for future multi-stream work

::: notes
Duration ~00:30

## Technology Inventory & Instruction Generation Exercise Instructions

**Prerequisites:** Access to repository tree, instruction conventions, and team roles for parallel work

### Objectives

- Build a practical technology inventory that informs instruction planning.
- Execute concurrent work safely with background sessions.
- Produce multiple scoped instruction files in one coordinated workflow.
- Use the session management interface to maintain control and traceability.

### Activities

1. Build a structured inventory first; avoid writing instruction files until the landscape is clear.
2. Split participants into concurrent roles: inventory lead, instruction generator, and session coordinator.
3. Generate scoped instruction files in parallel, then run a conflict review before acceptance.
4. Finalize with a short session-management retrospective: what scaled, what collided, what to improve.

### Success Criteria

- Inventory coverage is complete enough to drive instruction priorities.
- Parallel sessions finish with non-conflicting outputs.
- Generated instruction files include clear scoping and ownership boundaries.
- Team can reproduce the same workflow on another repository without redesigning the process.

### Facilitation Tip

Use a visible board (status: active, blocked, complete) for each session stream so the team can rebalance quickly when one stream stalls.
:::