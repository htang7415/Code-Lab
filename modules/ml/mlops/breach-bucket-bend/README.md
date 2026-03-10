# Breach Bucket Bend

> Track: `ml` | Topic: `mlops`

## Concept

Breach bucket bend measures the average discrete curvature of the breach-share curve across interior severity buckets.

## Math

If bucket shares are $p_1, \dots, p_K$, define the mean absolute second difference:

$$
\mathrm{Bend} = \frac{1}{K-2} \sum_{j=2}^{K-1} |p_{j+1} - 2p_j + p_{j-1}|
$$

## Key Points

- This normalizes total curvature by the number of interior buckets.
- A flat or linear bucket-share profile has bend `0`.
- This module returns `0.0` when there are too few buckets or no breaches.

## Function

```python
def breach_bucket_bend(
    observations: list[float],
    capacity: float,
    cutoffs: list[float],
) -> float:
```

## Run tests

```bash
pytest modules/ml/mlops/breach-bucket-bend/python -q
```
