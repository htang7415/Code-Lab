# Breach Bucket CDF

> Track: `ml` | Topic: `mlops`

## Concept

Breach bucket CDF measures the cumulative share of breaches up to each severity bucket.

## Math

If breach bucket shares are $p_1, \dots, p_K$ from mild to severe:

$$
\mathrm{CDF}_j = \sum_{i=1}^{j} p_i
$$

- $p_i$ -- share of breached observations in severity bucket $i$

## Key Points

- This shows how quickly breach mass accumulates as severity increases.
- It is a cumulative version of breach bucket share.
- This module returns zeros when there are no breaches.

## Function

```python
def breach_bucket_cdf(observations: list[float], capacity: float, cutoffs: list[float]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/mlops/breach-bucket-cdf/python -q
```
