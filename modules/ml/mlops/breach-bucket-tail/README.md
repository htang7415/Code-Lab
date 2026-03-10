# Breach Bucket Tail

> Track: `ml` | Topic: `mlops`

## Concept

Breach bucket tail measures how much breach share lies in the most severe buckets.

## Math

If breach bucket shares are $p_1, \dots, p_K$ from mild to severe and the tail uses
the last $T$ buckets:

$$
\mathrm{TailMass} = \sum_{j=K-T+1}^{K} p_j
$$

- $p_j$ -- share of breached observations in severity bucket $j$
- $T$ -- number of most severe buckets to include

## Key Points

- This focuses on the severe end of the breach distribution.
- It complements breach bucket entropy with a directional severity summary.
- This module returns `0.0` when there are no breaches.

## Function

```python
def breach_bucket_tail(
    observations: list[float],
    capacity: float,
    cutoffs: list[float],
    tail_buckets: int = 1,
) -> float:
```

## Run tests

```bash
pytest modules/ml/mlops/breach-bucket-tail/python -q
```
