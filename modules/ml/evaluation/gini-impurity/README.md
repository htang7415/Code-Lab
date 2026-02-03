# Gini Impurity

> Track: `ml` | Topic: `evaluation`

## Concept

Gini impurity measures class mixing in a node.

## Math

$$\mathrm{Gini} = 1 - \sum_c p_c^2$$

- $p_c$ -- probability for c
- $p$ -- probability

## Function

```python
def gini(labels: list[int]) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/gini-impurity/python -q
```
