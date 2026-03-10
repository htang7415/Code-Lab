# Breach Bucket Arc

> Track: `ml` | Topic: `mlops`

## Concept

Breach bucket arc measures the excess arc length of the breach-share curve across severity buckets.

## Math

If bucket shares are $p_1, \dots, p_K$, define the excess arc as:

$$
\mathrm{Arc} = \sum_{j=2}^{K} \left(\sqrt{1 + (p_j - p_{j-1})^2} - 1\right)
$$

## Key Points

- A flat bucket-share profile has arc `0`.
- Larger values mean the bucket-share curve changes more across adjacent buckets.
- This is a geometric alternative to curvature-style summaries.

## Function

```python
def breach_bucket_arc(
    observations: list[float],
    capacity: float,
    cutoffs: list[float],
) -> float:
```

## Run tests

```bash
pytest modules/ml/mlops/breach-bucket-arc/python -q
```
