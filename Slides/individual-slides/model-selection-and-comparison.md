---
marp: true
theme: default
paginate: true
---

## Model Selection & Comparison

Available models vary over time (Jan 18, 2026)
Multipliers vary with Copilot Subscription level
Name | Input Context Size | Output Context Size | Capabilities | Multiplier
--- | --- | --- | --- | ---
Claude Haiku 4.5 | 128K | 16K | Tools, Vision | 0.33x
Claude Opus 4.1 | 68K | 16K | Vision | 10x
Claude Opus 4.5 | 128K | 16K | Tools, Vision | 3x
Claude Sonnet 4 | 128K | 16K | Tools, Vision | 1x
Claude Sonnet 4.5 | 128K | 16K | Tools, Vision | 1x
Gemini 2.5 P Gemini 3 Flash (Preview) | 109K | 64K | Tools, Vision | 1x
Gemini 3 Flash (Preview) | 109K | 64K | Tools, Vision | 0.33x
Gemini 3 Pro (Preview) | 109K | 64K | Tools, Vision | 1x
GPT-4.1 | 111K | 16K | Tools, Vision | 0x
GPT-4o | 64K | 4K | Tools, Vision | 0x
GPT-5 | 128K | 128K | Tools, Vision | 1x
GPT-5 mini | 128K | 64K | Tools, Vision | 0x
GPT-5-Codex (Preview) | 128K | 128K | Tools, Vision | 1x
GPT-5.1 | 128K | 64K | Tools, Vision | 1x
GPT-5.1-Codex | 128K | 128K | Tools, Vision | 1x
GPT-5.1-Codex-Max | 128K | 128K | Tools, Vision | 1x
GPT-5.1-Codex-Mini (Preview) | 128K | 128K | Tools, Vision | 0.33x
GPT-5.2 | 128K | 64K | Tools, Vision | 1x
GPT-5.2-Codex | 272K | 128K | Tools, Vision | 1x
Grok Code Fast 1 | 109K | 64K | Tools | 0x
Raptor mini (Preview) | 200K | 64K | Tools, Vision | 0x

---

## Public Leaderboards

- Where to See Model-to-Model Comparisons
- LLM-Stats Coding Leaderboard
  - Aggregates 20+ coding benchmarks
  - Shows top performers across HumanEval, LiveCodeBench, etc.
- TechRadar's Coding LLM Guide
  - Editorial comparison of strengths (debugging, test generation, etc.)
- Zencoder's 2026 Model Comparison
  - Breaks down accuracy, reasoning, and context window-

---

## Core Benchmarks

- What Models Are Actually Tested On
- HumanEval
  - Classic functional-correctness benchmark for Python
- LiveCodeBench
  - Contamination-free, holistic benchmark for modern LLMs
- MBPP (Mostly Basic Programming Problems)
  - Simple algorithmic tasks across languages
- SWE-Bench
  - Real-world GitHub issue resolution
- DevQualityEval
  - Evaluates test generation for Java and Go

---

## Surveys & Deep-Dive Research

Understanding the Landscape
Academic Surveys (arXiv)

- Comprehensive overviews of techniques, benchmarks, and model families
  Benchmark Explainers (Vellum, Analytics Vidhya)
- Strengths and weaknesses of each benchmark
- How to interpret results
  Specialized Benchmarks
- SwiftEval, domain-specific coding evaluations, etc

---

## Evaluation Frameworks

- Tools for Running Your Own Tests
  - Symflower DevQualityEval
    - Open-source framework for code and test generation evaluation
  - CodeArena (HuggingFace)
    - Collective evaluation platform for coding tasks
  - Automatic Benchmark Generation Tools
    - Research into LLM-generated benchmarks and judge reliability

---

## Selecting Models

Select benchmarks aligned with your workflow
Combine leaderboards + hands-on evaluation
Build a repeatable internal benchmark suite
Track contamination-free benchmarks for reliability

::: notes
Contamination-Free Benchmarks
Why They Matter — and How They Work
Contamination-free benchmarks exist because modern LLMs are trained on massive, scraped corpora that often include the very benchmarks used to evaluate them. If a model has already seen the test set during training, its score is inflated — sometimes dramatically — and no longer reflects real reasoning or coding ability
A contamination-free benchmark is designed to eliminate that inflation and give you a score you can actually trust.
:::
