# LLM Tokenization

Tokenization decides what the model sees as an atomic unit and what the runtime pays for in context length.

## Current Anchors

- Tokenization (`modules/ml/llm/tokenization`)
- Tokenizer comparison (`modules/ml/llm/tokenizer-comparison`)
- Token budgeting under fixed limits (`modules/ml/data/token-budgeting`)

## Concepts to Cover Well

- Character, subword, and byte-level tokenization
- BPE-style merge rules and vocabulary trade-offs
- Byte fallback and out-of-vocabulary behavior
- Why token counts differ across tokenizers on the same text
- Context budgeting, truncation, and billing impact
- Tokenization as a hidden dependency for evaluation and prompting
