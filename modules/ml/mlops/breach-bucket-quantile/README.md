# Breach Bucket Quantile

> Track: `ml` | Topic: `mlops`

## Concept

Breach bucket quantile identifies the severity bucket reached at a target breach quantile.

## Math

If breach bucket shares are $p_1, \dots, p_K$ from mild to severe, find the smallest
bucket index $j$ such that:

$$
\sum_{i=1}^{j} p_i \ge q
$$

- $p_i$ -- share of breached observations in severity bucket $i$
- $q$ -- target quantile in `(0, 1]`

## Key Points

- This turns a cumulative breach distribution into one bucket index.
- Lower returned buckets mean most breaches are mild.
- This module returns `-1` when there are no breaches.

## Function

```python
def breach_bucket_quantile(
    observations: list[float],
    capacity: float,
    cutoffs: list[float],
    quantile: float,
) -> int:
```

## Run tests

```bash
pytest modules/ml/mlops/breach-bucket-quantile/python -q
```
