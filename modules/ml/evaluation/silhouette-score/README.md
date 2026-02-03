# Silhouette Score

> Track: `ml` | Topic: `evaluation`

## Concept

Silhouette compares intra-cluster to nearest-cluster distance.

## Math

$$s = \frac{b - a}{\max(a,b)}$$

- $s$ -- silhouette score
- $a$ -- mean intra-cluster distance
- $b$ -- mean nearest-cluster distance

## Function

```python
def silhouette(a: float, b: float) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/silhouette-score/python -q
```
