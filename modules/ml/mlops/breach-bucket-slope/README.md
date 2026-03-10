# Breach Bucket Slope

> Track: `ml` | Topic: `mlops`

## Concept

Breach bucket slope measures the largest adjacent change in breach-share across severity buckets.

## Math

If bucket shares are $p_1, \dots, p_K$:

$$
\mathrm{Slope} = \max_{j=2,\dots,K} |p_j - p_{j-1}|
$$

## Key Points

- This is the strongest single-step change in the bucket-share profile.
- Larger values mean adjacent severity buckets differ sharply in breach share.
- This module returns `0.0` when there are too few buckets or no breaches.

## Function

```python
def breach_bucket_slope(
    observations: list[float],
    capacity: float,
    cutoffs: list[float],
) -> float:
```

## Run tests

```bash
pytest modules/ml/mlops/breach-bucket-slope/python -q
```
