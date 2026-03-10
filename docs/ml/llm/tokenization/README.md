# LLM Tokenization

Tokenization decides what the model sees as a unit and what the system pays for in context length.

## Purpose

Use this page to understand:
- what a token is
- why tokenizers differ
- how token counts affect prompting, cost, and truncation

## First Principles

- A tokenizer turns raw text into discrete symbols before the model sees it.
- Better tokenization trades vocabulary size against sequence length.
- Different tokenizers change both quality and systems cost because token counts drive context usage.
- Tokenization is part of the model interface, not just preprocessing.

## Core Math

- Tokenized sequence:
  $$
  x \rightarrow (t_1, t_2, \dots, t_n)
  $$
- In transformer-style models, longer tokenized sequences usually mean more memory and attention cost.

## Minimal Code Mental Model

```python
tokens = tokenizer(text)
count = len(tokens)
fits_budget = count <= max_tokens
```

## Canonical Modules

- Core token and representation flow: `token-representation-methods`
- Budgeting impact: `token-budgeting`

## When To Use What

- Start with `token-representation-methods` before token-budget trade-offs.
- Use the token-count comparison inside `token-representation-methods` when the same text behaves differently across tokenizers.
- Use `token-budgeting` when prompting, truncation, or cost is the actual problem.
