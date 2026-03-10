# Breach Bucket Curvature

> Track: `ml` | Topic: `mlops`

## Concept

Breach bucket curvature measures how much the bucket-share curve bends across adjacent severity buckets.

## Math

If bucket shares are $p_1, \dots, p_K$, define discrete curvature as the total second-difference magnitude:

$$
\mathrm{Curvature} = \sum_{j=2}^{K-1} |p_{j+1} - 2p_j + p_{j-1}|
$$

## Key Points

- Larger values mean the bucket-share curve bends more sharply.
- A flat or linear share profile gives zero curvature.
- This module returns `0.0` when there are too few buckets or no breaches.

## Function

```python
def breach_bucket_curvature(
    observations: list[float],
    capacity: float,
    cutoffs: list[float],
) -> float:
```

## Run tests

```bash
pytest modules/ml/mlops/breach-bucket-curvature/python -q
```
