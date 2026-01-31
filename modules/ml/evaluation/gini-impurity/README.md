# Gini Impurity

> Track: `ml` | Topic: `evaluation`

## Concept

Gini impurity measures class mixing in a node.

## Math

$$\mathrm{Gini} = 1 - \sum_c p_c^2$$

## Function

```python
def gini(labels: list[int]) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/gini-impurity/python -q
```
