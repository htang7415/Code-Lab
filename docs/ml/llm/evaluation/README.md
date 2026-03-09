# LLM Evaluation

LLM evaluation mixes language-model likelihood, task scoring, and model-judge style comparisons.

## Current Anchors

- Perplexity (`modules/ml/llm/perplexity`)
- MMLU-style evaluation (`modules/ml/llm/mmlu-evaluation`)
- Pass@k (`modules/ml/llm/pass-at-k`)

## Concepts to Cover Well

- Perplexity and token-level likelihood
- Exact match and normalized string matching
- Pass@k for code and reasoning tasks
- Benchmark-style scoring such as MMLU variants
- Judge-based and pairwise preference evaluation
