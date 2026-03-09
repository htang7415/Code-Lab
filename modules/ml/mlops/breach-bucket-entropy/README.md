# Breach Bucket Entropy

> Track: `ml` | Topic: `mlops`

## Concept

Breach bucket entropy measures how spread breach events are across severity buckets.

## Math

For breach bucket shares $p_1, \dots, p_K$:

$$
\mathrm{Entropy} = -\sum_{j=1}^{K} p_j \log p_j
$$

- $p_j$ -- share of breached observations in severity bucket $j$

## Key Points

- Higher entropy means breaches are spread across more severity bands.
- Lower entropy means breaches are concentrated in a few buckets.
- This module returns `0.0` when there are no breaches.

## Function

```python
def breach_bucket_entropy(observations: list[float], capacity: float, cutoffs: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/mlops/breach-bucket-entropy/python -q
```
