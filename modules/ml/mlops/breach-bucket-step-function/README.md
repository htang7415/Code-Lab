# Breach Bucket Step Function

> Track: `ml` | Topic: `mlops`

## Concept

Breach bucket step function makes the cumulative breach-share curve explicit at each severity cutoff.

## Math

If breach bucket shares are $p_1, \dots, p_K$ from mild to severe, define the step value at
bucket edge $t_j$ as:

$$
S(t_j) = \sum_{i=1}^{j} p_i
$$

- $p_i$ -- share of breached observations in bucket $i$
- $t_j$ -- severity cutoff for bucket $j$

## Key Points

- This is a right-continuous cumulative step curve over severity buckets.
- The returned curve starts at `(0.0, 0.0)`.
- The final point uses `inf` for the open-ended tail bucket.

## Function

```python
def breach_bucket_step_function(
    observations: list[float],
    capacity: float,
    cutoffs: list[float],
) -> list[tuple[float, float]]:
```

## Run tests

```bash
pytest modules/ml/mlops/breach-bucket-step-function/python -q
```
