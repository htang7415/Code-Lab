# Breach Bucket Knee

> Track: `ml` | Topic: `mlops`

## Concept

Breach bucket knee identifies the bucket where the cumulative breach-share curve changes slope most sharply.

## Math

If bucket shares are $p_1, \dots, p_K$, the step-function slope change entering bucket $j$ is:

$$
\Delta_j = |p_j - p_{j-1}|
$$

The knee is the bucket with the largest $\Delta_j$.

## Key Points

- This is a discrete knee heuristic over severity buckets.
- Larger values mean the breach-share curve changes slope more abruptly.
- This module returns `-1` when no knee can be identified.

## Function

```python
def breach_bucket_knee(
    observations: list[float],
    capacity: float,
    cutoffs: list[float],
) -> int:
```

## Run tests

```bash
pytest modules/ml/mlops/breach-bucket-knee/python -q
```
