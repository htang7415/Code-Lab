# Preference Learning

> Track: `ml` | Topic: `llm`

## Concept

Preference learning optimizes models with pairwise comparisons between outputs.

## Math

Pairwise logistic loss: L = -log(sigmoid(score_chosen - score_rejected)).

## Function

```python
def preference_loss(score_chosen: float, score_rejected: float) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/preference-learning/python -q
```
