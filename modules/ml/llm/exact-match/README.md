# Normalized Exact Match

> Track: `ml` | Topic: `llm`

## Concept

Exact match for text answers is usually computed after lightweight normalization so casing, punctuation, and articles do not create fake mismatches.

## Math

$$\mathrm{EM} = \frac{1}{n} \sum_{i=1}^{n} \mathbb{I}[\mathrm{norm}(\hat{y}_i) = \mathrm{norm}(y_i)]$$

- $n$ -- number of evaluated answers
- $\hat{y}_i$ -- predicted answer string
- $y_i$ -- gold answer string
- $\mathrm{norm}$ -- normalization function applied before comparison

## Key Points

- Exact match is stricter than similarity metrics such as BLEU or ROUGE.
- Normalization policy matters and should be fixed before comparing models.
- This module uses a simple SQuAD-style normalization baseline.

## Function

```python
def exact_match_score(predictions: list[str], labels: list[str]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/exact-match/python -q
```
