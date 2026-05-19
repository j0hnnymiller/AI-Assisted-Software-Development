---
marp: true
theme: default
paginate: true
---

# Model Selection and Comparison || So Many Models, So Few Context Windows

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

- Select benchmarks aligned with your workflow
- Combine leaderboards + hands-on evaluation
- Build a repeatable internal benchmark suite
- Track contamination-free benchmarks for reliability

::: notes
Contamination-Free Benchmarks
Why They Matter — and How They Work
Contamination-free benchmarks exist because modern LLMs are trained on massive, scraped corpora that often include the very benchmarks used to evaluate them. If a model has already seen the test set during training, its score is inflated — sometimes dramatically — and no longer reflects real reasoning or coding ability
A contamination-free benchmark is designed to eliminate that inflation and give you a score you can actually trust.
:::
