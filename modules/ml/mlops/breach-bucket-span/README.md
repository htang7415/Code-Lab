# Breach Bucket Span

> Track: `ml` | Topic: `mlops`

## Concept

Breach bucket span measures the spread between the largest and smallest bucket shares.

## Math

If bucket shares are $p_1, \dots, p_K$:

$$
\mathrm{Span} = \max_i p_i - \min_i p_i
$$

## Key Points

- Larger values mean breach severity is concentrated unevenly across buckets.
- A perfectly even bucket-share profile has span `0`.
- This module returns `0.0` when there are no breaches.

## Function

```python
def breach_bucket_span(
    observations: list[float],
    capacity: float,
    cutoffs: list[float],
) -> float:
```

## Run tests

```bash
pytest modules/ml/mlops/breach-bucket-span/python -q
```
