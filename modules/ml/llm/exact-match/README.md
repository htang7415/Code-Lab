# Normalized Exact Match

> Track: `ml` | Topic: `llm`

## Purpose

Use this module to score answer correctness when references are strong and
string equality is the main criterion after light normalization.

## First Principles

- Exact match is stricter than overlap metrics.
- In practice, text answers are usually normalized before comparison so punctuation, casing, and articles do not create fake mismatches.
- This makes exact match useful for QA-style tasks with deterministic reference answers.

## Core Math

$$
\mathrm{EM} = \frac{1}{n} \sum_{i=1}^{n} \mathbb{I}[\mathrm{norm}(\hat{y}_i) = \mathrm{norm}(y_i)]
$$

- $n$ -- number of evaluated answers
- $\hat{y}_i$ -- predicted answer string
- $y_i$ -- gold answer string
- $\mathrm{norm}$ -- normalization function applied before comparison

## Minimal Code Mental Model

```python
score = exact_match_score(predictions, labels)
```

## Function

```python
def exact_match_score(predictions: list[str], labels: list[str]) -> float:
```

## When To Use What

- Use exact match when a normalized reference answer is the real success criterion.
- Use answer verification when multiple acceptable references or looser matching rules matter.
- Fix the normalization policy before comparing models.

## Run tests

```bash
pytest modules/ml/llm/exact-match/python -q
```
