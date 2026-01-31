# Gini Impurity

> Track: `ml` | Topic: `evaluation`

## Concept

Gini impurity measures class mixing in a node.

## Math

Gini = 1 - Σ p_c^2

## Function

```python
def gini(labels: list[int]) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/gini-impurity/python -q
```
