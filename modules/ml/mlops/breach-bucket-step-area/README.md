# Breach Bucket Step Area

> Track: `ml` | Topic: `mlops`

## Concept

Breach bucket step area measures the discrete area under the cumulative breach-share step curve across the severity buckets.

## Math

If cumulative bucket shares are $c_1, \dots, c_K$:

$$
\mathrm{StepArea} = \sum_{j=1}^{K} c_j
$$

## Key Points

- This is a discrete unit-width area under the cumulative step curve.
- Larger values mean breach mass accumulates earlier across the severity buckets.
- This module returns `0.0` when there are no breaches.

## Function

```python
def breach_bucket_step_area(
    observations: list[float],
    capacity: float,
    cutoffs: list[float],
) -> float:
```

## Run tests

```bash
pytest modules/ml/mlops/breach-bucket-step-area/python -q
```
