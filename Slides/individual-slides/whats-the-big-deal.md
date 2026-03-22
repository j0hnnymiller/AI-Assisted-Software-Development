---
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
