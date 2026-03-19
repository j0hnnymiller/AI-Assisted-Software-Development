---
ai_generated: true
model: "anthropic/claude-sonnet-4.6"
operator: "johnmillerATcodemag-com"
chat_id: "large-language-models-20260314"
prompt: |
  create a marp deck describing Large Language Models. How Large Language Models work -
  transformers, tokenization, training process
started: "2026-03-14T15:57:16Z"
ended: "2026-03-14T15:57:40Z"
task_durations:
  - task: "draft"
    duration: "00:00:24"
total_duration: "00:00:24"
ai_log: "ai-logs/2026/03/14/large-language-models-20260314/conversation.md"
source: "johnmillerATcodemag-com"
marp: true
theme: default
paginate: true
---

# Large Language Models

### How they work — and why developers should care

::: notes
Set the stage: LLMs are the engine behind GitHub Copilot, ChatGPT, Claude, and every other AI coding tool. Understanding how they work helps developers use them more effectively and set realistic expectations.

No deep math required — focus on intuition and mental models. This is a conceptual overview, not a research lecture.

Timing: ~30 seconds on title slide.
Transition: "Let's start with the big picture of what an LLM actually is."
:::

---

## What Is a Large Language Model?

> A statistical model trained to **predict the next token** given all preceding tokens.

- Trained on **trillions of tokens** of text (code, books, web pages)
- Learns **patterns, relationships, and structure** in language
- Not a database — it doesn't store facts, it learns **weights**
- Generates output one token at a time, probabilistically

### Key insight

**LLMs don't "know" things — they learn what text tends to follow other text.**

::: notes
This is the most important conceptual slide. Many developers expect LLMs to behave like search engines or databases — they don't.

Key talking points:

- "Next token prediction" sounds simple but at scale it forces the model to learn grammar, logic, context, and even reasoning
- "Weights" are just numbers — billions of floating point values that encode everything the model learned
- Probabilistic output means the same prompt can produce different answers — this is by design, controlled by "temperature"
- Analogy: autocomplete on your phone, but trained on all of human writing

Common misconception to address: "Does Copilot look up my code in a database?" — No. It generates completions based on learned patterns.

Timing: ~2 minutes.
:::

---

## Tokenization — Breaking Text Apart

### Text → Numbers (before the model sees anything)

```
Input:  "Hello, world!"
Tokens: ["Hello", ",", " world", "!"]
IDs:    [15496, 11, 995, 0]
```

```
Input:  "def calculate_tax(income):"
Tokens: ["def", " calculate", "_tax", "(", "income", "):"]
```

- A **token** ≈ ~4 characters or ¾ of a word on average
- The model only ever sees **token IDs**, never raw text
- Tokenization affects **cost**, **context limits**, and **model behavior**
- Rare words split into multiple tokens → less efficient

::: notes
Tokenization is often overlooked but explains many "weird" LLM behaviors.

Key talking points:

- GPT-4 uses ~100,000 tokens in its vocabulary (tiktoken)
- Context window limits (e.g., "128k tokens") are token limits, not character limits
- Why does Copilot sometimes mishandle unusual variable names? Tokenization — rare strings get split awkwardly
- Code tokenization differs from prose — identifiers often split at underscores, camelCase boundaries

Practical implication for developers:

- Long variable names consume more tokens than short ones
- Copy-pasting large files into chat uses tokens fast
- Understanding tokens helps estimate cost when using API

Interactive moment: Ask "How many tokens do you think this slide is?" — good engagement exercise.

Timing: ~2-3 minutes.
:::

---

## The Transformer Architecture

### The breakthrough that made modern LLMs possible (2017)

```
Input Tokens
     ↓
[Embedding Layer]      ← tokens → vectors
     ↓
[Attention Layers] ×N  ← "what matters given what came before?"
     ↓
[Feed-Forward Layers]  ← learn patterns and transformations
     ↓
[Output Layer]         ← probability over next token
```

- **Self-attention** lets every token "look at" every other token
- Processes the **entire context window at once** (not word-by-word)
- Stacked in **layers** — deeper = richer understanding

::: notes
You don't need to explain the math — focus on the intuition of attention.

Key talking points:

- Before Transformers: RNNs processed text sequentially (slow, forgot early context)
- Transformers process everything in parallel — that's why they scale so well on GPUs
- Self-attention intuition: "When I see the word 'it' in a sentence, which earlier word does 'it' refer to?" Attention figures this out
- Layers build up from syntax → semantics → reasoning as you go deeper

Analogy for attention: Imagine reading a legal contract. When you hit a pronoun like "the aforementioned party," your brain jumps back to find who that is. That's attention.

Why this matters for developers: Larger context windows (more tokens processed at once) = Copilot can see more of your codebase at once = better suggestions.

Timing: ~3 minutes. This is the most technical slide — keep it high-level.
:::

---

## Self-Attention — The Core Idea

### How the model decides what to focus on

> **"The trophy didn't fit in the suitcase because it was too big."**
> What does "it" refer to?

- Each token computes **Query**, **Key**, and **Value** vectors
- Attention score = how much each token should influence the current one
- Model learns which relationships matter during training
- Multiple **attention heads** capture different relationship types simultaneously

### In code:

```
"def process(data):"  →  model attends to "def" when predicting
                          what comes after "(data):"
```

::: notes
Use the trophy/suitcase example — it's a classic from the research literature and immediately intuitive.

Key talking points:

- Q/K/V is just a learned lookup mechanism — don't get lost in the math
- Multiple heads: one head might learn syntax relationships, another semantic, another positional
- This is why LLMs understand that a closing brace `}` should match an opening one several lines earlier
- Attention is also why very long prompts can "distract" the model — it has finite attention capacity

Practical tip: When using Copilot, relevant context near your cursor gets higher attention weight. Keep related code nearby when you want better completions.

Timing: ~2-3 minutes.
:::

---

## The Training Process

### Phase 1: Pre-training

```
Raw text (internet, books, code, papers)
          ↓
    Tokenize everything
          ↓
    For each token: predict next token
          ↓
    Compare prediction to actual → compute loss
          ↓
    Backpropagation → update billions of weights
          ↓
    Repeat trillions of times on thousands of GPUs
```

- Months of training, millions of dollars in compute
- Produces a **base model** that completes text — but isn't yet "helpful"

::: notes
Pre-training is where the model learns language, code, and world knowledge.

Key talking points:

- The objective is deceptively simple: predict the next token. But at scale it forces the model to learn everything
- Training data quality matters enormously — garbage in, garbage out
- GitHub Copilot's base model was trained on public GitHub repos (billions of lines of code)
- A "base model" after pre-training will complete text but may write offensive content, refuse nothing, and ramble — it needs the next phase

Scale reference: GPT-3 used 45TB of text data. Training ran on ~10,000 A100 GPUs.

Why developers care: The pre-training corpus determines what languages, frameworks, and patterns the model knows well. Copilot knows React better than a niche internal framework.

Timing: ~2-3 minutes.
:::

---

## The Training Process

### Phase 2: Fine-tuning & Alignment

**Supervised Fine-Tuning (SFT)**

- Train on curated prompt → ideal response pairs
- Teaches the model to be helpful and follow instructions

**Reinforcement Learning from Human Feedback (RLHF)**

- Human raters rank model outputs
- A reward model learns human preferences
- The LLM is optimized to maximize reward score

**Result**: A model that is helpful, harmless, and honest

```
Base model: "The capital of France is Paris. The capital of Spain is..."
Aligned model: "The capital of France is Paris."  ← stops when done
```

::: notes
This phase is what separates "a model that generates text" from "an assistant you can actually use."

Key talking points:

- SFT teaches format and helpfulness; RLHF teaches judgment
- "Hallucinations" happen when the model optimizes for sounding helpful over being accurate
- Safety guardrails (content filters) are also applied at this stage
- GitHub Copilot has additional fine-tuning on high-quality code and developer feedback

Why alignment matters for developers: It's why Copilot suggests reasonable code instead of technically-valid-but-insane solutions. It's also why it refuses to help with malicious code.

Common question: "Can I fine-tune Copilot on my codebase?" — GitHub Enterprise Copilot offers custom fine-tuning on private repos.

Timing: ~2-3 minutes.
:::

---

## Context Window — The Model's Working Memory

| Model             | Context Window               |
| ----------------- | ---------------------------- |
| GPT-3.5           | 16k tokens (~12,000 words)   |
| GPT-4o            | 128k tokens (~96,000 words)  |
| Claude 3.5 Sonnet | 200k tokens (~150,000 words) |
| Gemini 1.5 Pro    | 1M tokens (~750,000 words)   |

- Everything the model "knows" during a conversation fits here
- Once exceeded, **earlier content is forgotten**
- GitHub Copilot uses the context window for: open files, cursor position, recent edits, instruction files
- Larger context = can see more code, but also slower & more expensive

::: notes
Context window is one of the most practically important LLM concepts for developers using Copilot.

Key talking points:

- The context window is not persistent memory — every new conversation starts fresh
- Copilot automatically fills the context window with relevant code from open tabs and recent edits
- This is why opening related files improves Copilot suggestions — they get included in context
- Instruction files (`.github/instructions/`) consume some of the context window — keep them concise

Practical tip: If Copilot seems to "forget" something you told it, it likely scrolled out of the context window. Repeat the key constraints.

Timing: ~2 minutes.
:::

---

## Temperature & Sampling

### How the model chooses its next token

```
Token probabilities after "def calculate_":
  "tax"      → 35%
  "total"    → 28%
  "price"    → 18%
  "discount" → 12%
  other...   → 7%
```

| Temperature | Behavior                         | Use case           |
| ----------- | -------------------------------- | ------------------ |
| 0.0         | Always picks highest probability | Deterministic code |
| 0.3–0.5     | Mostly top tokens, some variety  | Code completion    |
| 0.7–1.0     | More creative, less predictable  | Brainstorming      |
| > 1.0       | Random / incoherent              | Rarely useful      |

::: notes
Temperature demystifies why LLMs give different answers to the same question.

Key talking points:

- Temperature = how "flat" or "peaked" the probability distribution is before sampling
- Copilot uses a low temperature (~0.2-0.4) for code — you want predictable, correct completions
- ChatGPT uses higher temperature for conversational responses — feels more natural
- When Copilot gives you alternates (Alt+] to cycle), it's sampling different tokens

Developer implication: If you're using the Copilot API or OpenAI API directly, lower temperature for code generation tasks, higher for creative tasks like writing test descriptions.

Timing: ~2 minutes.
:::

---

## Key Takeaways

- 🔤 **Tokenization** — text is broken into tokens; everything is numbers
- 🔍 **Transformers** — attention lets every token relate to every other
- 🎓 **Pre-training** — learns from trillions of tokens of text & code
- 🎯 **Fine-tuning** — makes the model helpful, safe, and task-specific
- 📏 **Context window** — the model's working memory; bigger = better
- 🌡️ **Temperature** — controls creativity vs. determinism

### The bottom line for developers:

> LLMs are powerful pattern matchers. Give them **clear context**, **good examples**, and **specific instructions** — and they'll surprise you.

::: notes
Wrap up by connecting the technical concepts back to practical developer behavior.

Key points to reinforce:

- You don't need to understand the math to use LLMs effectively
- Understanding tokens helps you write better prompts and manage costs
- Understanding context helps you structure your workspace for better Copilot suggestions
- Understanding temperature explains why results vary

For Q&A, be prepared for:

- "How does Copilot know about my private code?" — It doesn't unless you're using Enterprise Knowledge Bases
- "Why does it make things up?" — Hallucination: the model is optimized to produce plausible-sounding text, not verified facts
- "What's the difference between Copilot and ChatGPT?" — Same underlying technology; different fine-tuning, context, and integration

Timing: Spend remaining session time on Q&A.
:::
