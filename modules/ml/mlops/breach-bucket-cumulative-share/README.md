# Breach Bucket Cumulative Share

> Track: `ml` | Topic: `mlops`

## Concept

Breach bucket cumulative share measures the cumulative share of breaches up to each severity bucket.

## Math

If breach bucket shares are $p_1, \dots, p_K$ from mild to severe:

$$
\mathrm{CumShare}_j = \sum_{i=1}^{j} p_i
$$

- $p_i$ -- share of breached observations in severity bucket $i$

## Key Points

- This is the cumulative-share version of breach bucket share.
- It shows how much breach mass is covered as severity thresholds increase.
- This module returns zeros when there are no breaches.

## Function

```python
def breach_bucket_cumulative_share(
    observations: list[float],
    capacity: float,
    cutoffs: list[float],
) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/mlops/breach-bucket-cumulative-share/python -q
```
