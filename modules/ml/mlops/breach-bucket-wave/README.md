# Breach Bucket Wave

> Track: `ml` | Topic: `mlops`

## Concept

Breach bucket wave counts how many times the breach-share curve changes direction across adjacent severity buckets.

## Math

If bucket shares are $p_1, \dots, p_K$, define adjacent differences:

$$
\delta_j = p_j - p_{j-1}
$$

The wave count is the number of sign changes across the non-zero $\delta_j$ sequence.

## Key Points

- This is a discrete direction-change count for the bucket-share profile.
- A monotonic profile has wave `0`.
- Larger values mean the breach-share curve oscillates more across buckets.

## Function

```python
def breach_bucket_wave(
    observations: list[float],
    capacity: float,
    cutoffs: list[float],
) -> int:
```

## Run tests

```bash
pytest modules/ml/mlops/breach-bucket-wave/python -q
```
