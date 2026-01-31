# Decision Trees

> Track: `ml` | Topic: `models`

## Concept

Decision trees split data to reduce impurity.

## Math

Gini = 1 - Σ p_c^2

## Function

```python
def gini_impurity(labels: list[int]) -> float:
```

## Run tests

```bash
pytest modules/ml/models/decision-trees/python -q
```
