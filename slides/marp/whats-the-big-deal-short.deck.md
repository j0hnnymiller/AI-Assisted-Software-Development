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

# What's the Big Deal About AI? || The More Things Change, the More They Still Compile

<!-- _class: lead -->

## The Core Thesis

> "Programming hasn't changed, but how we go about it has changed, again."

- AI-assisted development is **evolutionary**, not revolutionary
- Programming has always been about **expressing human intent** to machines
- What changes is the **sophistication of our tools** for expressing intent
- The essence remains: bridging the gap between what we want and what machines can do

::: notes
**Opening**: Start with the provocative quote to capture attention. Pause for effect after reading it aloud. **Key Message**: Emphasize that we're not witnessing a revolution but an evolution—AI tools are the latest step in a continuous chain of improvements. **Delivery**: Speak slowly and deliberately on the core thesis. Ask audience: "How many of you thought AI was going to replace programmers?" Acknowledge concerns but pivot to optimism. **Transition**: "To understand why this is evolutionary, let's look at where we've been..."
:::

---

## Programming Evolution: Rising Abstraction Layers

| Era           | Abstraction Level     | Key Technology       | Example                   |
| ------------- | --------------------- | -------------------- | ------------------------- |
| **1940s**     | Machine Code/Assembly | Assemblers           | `MOV AX, BX` vs binary    |
| **1950s-70s** | High-Level Languages  | Compilers            | FORTRAN, COBOL, C         |
| **1970s-80s** | Objects & Structures  | OOP Compilers        | Classes, inheritance      |
| **1990s**     | Integrated Tools      | IDEs, Libraries      | Visual Studio, JVM        |
| **2000s**     | Web Frameworks        | Dynamic Interpreters | Rails, Python, JavaScript |
| **2010s**     | Cloud & APIs          | Orchestration        | Microservices, containers |
| **Now**       | Natural Language      | LLMs                 | AI-assisted coding        |

**Pattern**: Each era raised the abstraction, moving from hardware to logic to intent

::: notes
**Narrative Arc**: This compressed history shows the unwavering trajectory—each generation solved the previous era's friction point. **Key Insight to Emphasize**: "We're not abandoning what came before; we're standing on its shoulders. Assembly enabled C. C enabled Python. Python enabled web frameworks. Each step made the developer experience more human-centered." **Transition**: "So when AI arrives, it's not revolutionary—it's the next rung on a ladder we've been climbing for 80 years. The question isn't 'will this replace programming?' but 'what new problems will it let us solve?'"
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
