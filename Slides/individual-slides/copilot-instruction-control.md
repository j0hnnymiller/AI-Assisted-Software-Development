---
marp: true
theme: default
paginate: true
---
## Controlling GitHub Copilot Instruction Files

Understanding Context Submission in AI-Assisted Development

::: notes
Duration ~00:20

Welcome to this session on controlling GitHub Copilot instruction files. This is a critical topic for teams implementing AI-assisted development workflows, as understanding how instructions are submitted with every prompt is essential for maintaining consistency, reducing token costs, and ensuring the right context reaches your AI assistant.

Today we'll cover four key areas: how the automatic inclusion system works through the applyTo field, how prompt files interact with instructions, how chat modes affect instruction submission, and practical strategies for controlling your context.

This session assumes you're familiar with basic GitHub Copilot usage and have worked with instruction files before. If you haven't, we recommend reviewing the “Creating Instruction Files” session first.
:::

---




## The Core Concept

Every Copilot prompt includes relevant instruction files automatically

```markdown
# .github/instructions/security.instructions.md
---
applyTo: "**/*.{ts,js,py}"
---
# Security Best Practices
...
```

When you work on src/api.ts → Security instructions automatically included

::: notes
Let's start with the fundamental concept: GitHub Copilot includes instruction files with every prompt you send, but it's not random - it's controlled by pattern matching.

The key mechanism is the applyTo field in the YAML front matter of instruction files. This field contains a glob pattern that determines which files trigger automatic inclusion of that instruction file.

In this example, we have security instructions that apply to TypeScript, JavaScript, and Python files. When you open or edit any file matching this pattern - like src/api.ts - these security instructions are automatically included in the context sent to the AI model.

This is incredibly powerful because it means:

Instructions follow the files they're relevant to

You don't need to manually reference instructions every time

Different file types can have different instruction contexts

Token usage is optimized by only including relevant instructions

Think of it like having domain experts looking over your shoulder, but only when you're working in their domain. You wouldn't want your database architect reviewing your CSS files, and you wouldn't want your UI designer reviewing your SQL queries. The applyTo field ensures the right expertise is present at the right time.
:::

---




## The applyTo Field: Pattern Matching

Three Levels of Scope Control

```yaml
# Global - Everything
applyTo: "**/*"

# Directory-Specific - Slides only
applyTo: "Slides/individual-slides/**"

# Type-Specific - Code files only
applyTo: "**/*.{cs,ts,js,py,java,go,rb}"
```

Result: Only matching instruction files are included in context

::: notes
The applyTo field uses glob patterns, which give you three levels of granularity for controlling instruction scope.

Level 1: Global patterns like “*/” apply to every file in your repository. Use this sparingly for truly universal instructions like AI provenance requirements or company-wide coding standards. The ai-assisted-output.instructions.md file is a perfect example - it applies everywhere because every AI-generated output needs provenance metadata.

Level 2: Directory-specific patterns like “Slides/individual-slides/**” target a specific folder hierarchy. This is ideal for instructions that only make sense in certain parts of your codebase. Marp slide instructions only matter when you're creating slides, so they target that directory exclusively.

Level 3: Type-specific patterns like “*/.{cs,ts,js}” apply to specific file extensions regardless of location. This is perfect for language-specific instructions, architectural patterns, or technology-specific guidelines. Vertical slice architecture instructions might only apply to backend code files.

The matching happens automatically when you:

Open a file in the editor

Reference a file in chat

Run a command that targets specific files

Pro tip: You can combine these patterns. For example, “src/*/.test.{ts,js}” would only match test files in the src directory. This allows very precise control over which instructions apply where.

One important caveat: If an instruction file has NO applyTo field, it won't be automatically included at all. You'd need to manually reference it with @-mentions.
:::

---




## Prompt Files: Reference, Don't Control

Prompt files execute tasks, they don't control instruction inclusion

```markdown
<!-- .github/prompts/create-api.prompt.md -->

**CRITICAL**: All AI-generated artifacts MUST comply with
`.github/instructions/ai-assisted-output.instructions.md`
```

Key Distinction:
✅ Can reference instruction requirements in content
❌ Don't control which instructions auto-include
🎯 The target file's applyTo matching still determines inclusion

::: notes
This is a common source of confusion, so let's clarify: prompt files and instruction files serve different purposes and work in different ways.

Prompt files are executable tasks - they're like scripts you run to accomplish specific goals. They contain the prompt text, expected deliverables, and requirements. When you execute a prompt file, you're asking the AI to perform a specific task following specific guidelines.

However, prompt files don't control the automatic inclusion of instruction files. What happens instead is:

You execute a prompt file (say, create-api.prompt.md)

The prompt content itself can mention or reference instruction files

The AI reads those references as part of the prompt

But the automatic inclusion of instruction files is still controlled by the applyTo patterns matching the files being created or modified

Here's a practical scenario: You run a prompt to create a new TypeScript API file. The prompt mentions that security instructions must be followed. The security.instructions.md file has applyTo: “*/.ts”. When the AI creates the new .ts file:

The prompt content enforces the requirement

The applyTo pattern causes automatic inclusion

Both work together, but through different mechanisms

Think of it this way: Prompt files are the “what to do”, instruction files are the “how to do it”, and applyTo patterns are the “when to apply the how”.

The prompt metadata can specify output paths, which helps the system know what file types to expect and therefore which instructions might become relevant, but it's still the applyTo matching that does the heavy lifting.
:::

---




## Chat Modes: Persona, Not Pattern Control

Chat modes create specialized contexts, not instruction filters

```markdown
# .github/chatmodes/security-analyzer.chatmode.md
# Focus: Code security, vulnerability detection
```

Interaction Model:
graph LR
    A[File Being Edited] --> B{applyTo Match?}
    B -->|Yes| C[Auto-Include Instructions]
    B -->|No| D[Skip Instructions]
    C --> E[Add Chat Mode Persona]
    D --> E
    E --> F[Generate Response]

::: notes
Chat modes are often misunderstood as another way to control instruction inclusion, but they actually serve a different purpose. Let's clarify their role in the context submission system.

Chat modes create specialized AI personas with domain expertise. When you activate a chat mode, you're essentially telling the AI “act as a security expert” or “act as a documentation specialist”. The chat mode defines:

The role and mission of the AI

Core areas of expertise

Communication style and tone

Specialized commands or workflows

Response formatting preferences

But here's the key: chat modes don't override or control the applyTo pattern matching system. Instead, they layer on top of it. Let's walk through the flow:

You're editing a TypeScript file (src/auth.ts)

applyTo patterns are evaluated - security.instructions.md matches

The security instructions are auto-included in context

You have the “Security Analyzer” chat mode active

The chat mode persona is added to the context

The AI now has: the file, the security instructions, AND the security expert persona

The diagram shows this flow. The file type drives instruction inclusion through pattern matching, and the chat mode adds a specialized persona layer on top. They're complementary, not competitive.

A practical benefit: You could have security instructions that are very technical and rule-based, while the security analyzer chat mode adds conversational expertise and interactive commands. The instructions say “what to check”, the chat mode says “how to explain findings”.

One important note: If your chat mode references specific instruction files in its content, those references work like any other reference - they become part of the conversation, but they don't change the automatic inclusion patterns.
:::

---




## The Control Hierarchy

Understanding the complete context assembly
1. 📝 File Being Edited (e.g., src/api.ts)
          ↓
2. 🎯 Instruction Files (applyTo pattern matching)
          ↓
3. 🎭 Active Chat Mode (if any - adds persona/context)
          ↓
4. 📋 Prompt Files (can reference additional instructions)
          ↓
5. 👤 Manual @-mentions (explicit instruction references)

::: notes
Now let's bring it all together with the complete control hierarchy. This shows the order in which different elements contribute to the context that gets submitted with your Copilot prompts.

Level 1: The Foundation - The File Being Edited Everything starts with the actual file you're working on. This could be a file you have open, a file you're creating, or files you reference in conversation. This establishes the base context and triggers the pattern matching system.

Level 2: Automatic Layer - Instruction Files Based on the file from level 1, the system evaluates all applyTo patterns in your instruction files. Every instruction file whose pattern matches your current file is automatically included. This happens silently in the background - you don't see it, but it's there. This is the primary control mechanism we've been discussing.

Level 3: Persona Layer - Active Chat Mode If you have a chat mode active, its persona definition, methodology, and guidelines are added to the context. This doesn't replace the instructions from level 2, it augments them. Think of this as the “personality” that interprets and applies the technical instructions.

Level 4: Task Layer - Prompt Files When you execute a prompt file, its content becomes part of the conversation. Any references to instruction files in the prompt text are processed. The prompt often specifies what type of output to create, which can trigger additional applyTo matching for the target files.

Level 5: Explicit Layer - Manual @-mentions Finally, you can always manually reference specific instruction files using @-mentions in your chat. This overrides the automatic system - if an instruction file doesn't have an applyTo match but you @-mention it, it gets included anyway.

Understanding this hierarchy helps you:

Debug why certain instructions aren't being applied

Optimize token usage by avoiding redundant inclusion

Design better instruction file patterns

Structure your workflow for maximum efficiency

Pro tip: Use levels 1-2 for 90% of your work (file-driven automatic inclusion), level 3 for specialized domains (chat modes), and levels 4-5 for exceptional cases (specific tasks or overrides).
:::

---




## Practical Control Strategies

Four approaches to managing instruction context
Strategy | Use Case | Example
--- | --- | ---
Specific Patterns | Domain-specific guidance | src/**/*.ts for backend TypeScript
No applyTo | Manual inclusion only | Docs that need explicit opt-in
Global with Overrides | Base + specialized | **/* + specific overrides
Directory Isolation | Project sections | frontend/** vs backend/**

::: notes
Let's conclude with four practical strategies you can use to manage instruction context effectively. These are patterns we've seen work well in real development teams.

Strategy 1: Specific Patterns (Recommended for Most Cases) Use precise glob patterns that match only the files where instructions are relevant. For example, if you have vertical slice architecture instructions, apply them only to your backend code: “src/backend/*/.{cs,ts,py}”. This keeps your context clean and focused. It also reduces token costs since irrelevant instructions aren't included.

When to use: This should be your default strategy. Be specific about where instructions apply. Think about the actual files developers will be editing and match those patterns.

Strategy 2: No applyTo Field (For Specialized Use) Some instruction files shouldn't automatically include anywhere. These are typically:

Very specialized instructions that rarely apply

Experimental guidelines you're testing

Documentation that needs explicit consent to follow

Instructions with high token costs that should be opt-in

When to use: For instructions that might cause confusion if automatically included, or that are so specialized that automatic inclusion would rarely be appropriate. Developers must @-mention these explicitly.

Strategy 3: Global with Overrides (Advanced) Start with global instructions that apply everywhere (like AI provenance requirements), then create more specific instruction files that override or extend them for particular domains. For example:

ai-assisted-output.instructions.md: applyTo: “*/”

ai-assisted-code-output.instructions.md: applyTo: “*/.{code}” The more specific file can provide additional requirements that layer on top of the global ones.

When to use: When you have a base set of universal requirements but need domain-specific extensions. Be careful not to create conflicting instructions.

Strategy 4: Directory Isolation (For Large Projects) In large monorepos or projects with distinct sections, isolate instructions by directory. Frontend, backend, mobile, docs, infrastructure - each gets its own instruction files with directory-specific patterns. This prevents cross-contamination of concerns.

When to use: Projects with clear architectural boundaries, multi-team codebases, or when different parts of your system have fundamentally different requirements.

Implementation tip: Document your strategy in your repository's README so the team understands the pattern matching approach you're using. Include examples of which files trigger which instructions.

Remember: You can see which instructions are active by checking the Copilot context window or by asking Copilot “which instruction files are currently active?”
:::

---




## Real-World Examples

From your current workspace

```markdown
# ai-assisted-output.instructions.md
applyTo: "**/*"
# ✅ Applies everywhere - fundamental provenance requirements

# vertical-slice-implementation.instructions.md
applyTo: "**/*.{cs,ts,js,py,java,go,rb}"
# ✅ Code files only - architectural guidance

# marp-slides.instructions.md
applyTo: "Slides/individual-slides/**"
# ✅ Specific directory - presentation formatting

# chatmode-file.instructions.md
applyTo: "**/*.chatmode.md"
# ✅ Specific file type - chat mode creation rules
```

::: notes
Let's look at real examples from your actual workspace to see these strategies in action. These are live instruction files that demonstrate the patterns we've discussed.

Example 1: Universal Requirements The ai-assisted-output.instructions.md file uses the global pattern “*/”. This makes sense because every AI-generated artifact in your repository needs complete provenance metadata - the chat ID, model used, timestamps, operator, etc. There's no file type that should be exempt from these requirements. This is a perfect use case for global application.

Example 2: Language-Specific Guidance The vertical-slice-implementation.instructions.md file applies to code files across multiple languages. Notice the pattern includes cs, ts, js, py, java, go, and rb extensions. This instruction file contains architectural guidance about implementing vertical slice architecture, which is relevant to any programming language but not relevant to markdown docs, config files, or slides. By targeting only code files, it stays out of the way when you're writing documentation.

Example 3: Directory-Specific Rules The marp-slides.instructions.md file uses “Slides/individual-slides/**” to target only the specific directory where slide content is created. Marp formatting rules, speaker note syntax, and presentation structure guidance only makes sense for slide files. If this pattern was broader, you'd get slide-specific instructions while writing code, which would be confusing and waste tokens.

Example 4: File Type Specialization The chatmode-file.instructions.md file applies only to files ending in .chatmode.md. This is hyper-specific because the instructions are about creating chat mode definition files - they're only relevant when you're actually authoring a chat mode. This prevents developers from seeing chat mode creation instructions when they're working on normal documentation.

The pattern: Start with the question “When would a developer need this guidance?” Then write the most specific pattern that matches those situations. Too broad and you waste tokens and cause confusion. Too narrow and the instructions won't be there when needed.

You can examine your own instruction files and ask: “Is this applyTo pattern optimal? Could it be more specific? Is it too specific and causing instructions to be missed?”
:::

---




## Key Takeaways

applyTo field controls automatic inclusion via glob patterns
Prompt files reference but don't control instruction selection
Chat modes add personas, not pattern overrides
Hierarchy determines context: File → Instructions → Persona → Task → Manual
Be intentional with patterns to optimize context and token usage
Remember: Specificity is your friend - match patterns to actual use cases

::: notes
Let's wrap up with the five key takeaways you should remember from this session.

First and most important: The applyTo field is your primary control mechanism. This glob pattern in the instruction file's YAML front matter determines when that file automatically includes in context. Master glob patterns and you master context control. If you remember nothing else from this session, remember this point.

Second: Prompt files are not instruction controllers. They're task executors that can reference instructions in their content, but they don't override or control the applyTo pattern matching system. Think of prompts as “what to do” and instructions as “how to do it” - they're complementary, not competitive.

Third: Chat modes create specialized AI personas that layer on top of the instruction system. They don't replace or filter instructions; they add context, expertise, and communication style. Use chat modes to add personality and specialized workflows, not to control instruction inclusion.

Fourth: Understanding the hierarchy helps you debug and optimize. When something unexpected happens - instructions not being applied, wrong context being included, token limits being hit - trace through the hierarchy: What file am I working on? What patterns match? What chat mode is active? What prompt am I running? What did I manually @-mention?

Fifth: Specificity beats generality. It's tempting to use broad patterns like “*/” for everything, but resist that temptation. Specific patterns mean:

Lower token costs (only relevant context)

Faster responses (less to process)

Better quality (more focused guidance)

Fewer conflicts (clearer which rules apply)

A well-designed instruction file system uses specific patterns that precisely match the files where guidance is needed.

Action items for after this session:

Audit your instruction files - check every applyTo pattern

Test what happens when you edit different file types

Document your pattern strategy for your team

Consider creating directory-specific or type-specific instruction files if you currently have too many global patterns

Questions to consider:

Are your patterns too broad or too narrow?

Do you have instructions without applyTo fields that should have them?

Are there conflicting instructions applying to the same files?

Could you reduce token usage with more specific patterns?

Thank you for your attention. Let's open it up for questions.
:::

---




## Questions & Discussion

Common Questions:
How do I see which instructions are active for my current file?
Can I temporarily disable an instruction file?
What happens when two instruction files conflict?
How can I debug unexpected instruction inclusion?
Resources:
.github/instructions/instruction-files.instructions.md
.github/instructions/copilot-instructions.md
.github/instructions/ai-assisted-output.instructions.md

::: notes
This final slide is for the Q&A portion. Let me provide you with answers to the most common questions we receive about instruction file control, so you're prepared for the discussion.

Question 1: “How do I see which instructions are active for my current file?” Answer: You can explicitly ask GitHub Copilot in chat: “Which instruction files are currently active?” or “What instructions are you following right now?” Copilot will list the instruction files in its context. You can also check the Copilot context panel if your IDE supports it. Some teams also create a test prompt that lists all applyTo patterns and their match status.

Question 2: “Can I temporarily disable an instruction file?” Answer: There are a few approaches:

Rename the file temporarily (remove .instructions.md extension)

Comment out the applyTo field in the YAML front matter

Move the file outside the .github/instructions/ directory

Use @-mentions to explicitly include only the instructions you want for a specific task Remember to document why you're disabling it and when you plan to re-enable it.

Question 3: “What happens when two instruction files conflict?” Answer: Both files are included in context, and the AI attempts to reconcile them. However, explicit conflicts (like “always do X” vs “never do X”) should be resolved by:

Making applyTo patterns mutually exclusive

Using one file as the base and another as an override with clear precedence rules

Merging the conflicting files into a single coherent instruction set Good naming and clear scope help prevent conflicts.

Question 4: “How can I debug unexpected instruction inclusion?” Answer: Follow this debugging process:

Ask Copilot what instructions are active

Check the applyTo patterns in those files

Verify what file type you're working with

Test the glob pattern using a pattern tester

Check if you have any global patterns that might be catching this file

Look for recently added instruction files that might have overly broad patterns

Additional discussion points:

Share examples of instruction patterns that worked well for your team

Discuss challenges with token limits and how specific patterns helped

Talk about the process for creating new instruction files

Review the governance model for instruction file approval

The resources listed are the canonical documentation files in your repository. Encourage your team to read these for deeper understanding of the instruction file system.

For ongoing support, consider:

Creating a team channel for instruction file discussions

Establishing a regular review cycle for instruction files

Assigning an “instruction file owner” who maintains the system

Building tools to visualize instruction coverage across your codebase

Thank you all for participating. I'll stick around for individual questions after we adjourn.
:::
