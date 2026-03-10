# Breach Bucket Inflection

> Track: `ml` | Topic: `mlops`

## Concept

Breach bucket inflection identifies the bucket with the strongest discrete change in curvature.

## Math

If bucket shares are $p_1, \dots, p_K$, define the discrete second difference at bucket $j$ as:

$$
\Delta_j = p_{j+1} - 2p_j + p_{j-1}
$$

The inflection bucket is the one with the largest $|\Delta_j|$.

## Key Points

- This localizes where the bucket-share curve bends most strongly.
- It differs from total curvature by returning one bucket index.
- This module returns `-1` when no inflection can be identified.

## Function

```python
def breach_bucket_inflection(
    observations: list[float],
    capacity: float,
    cutoffs: list[float],
) -> int:
```

## Run tests

```bash
pytest modules/ml/mlops/breach-bucket-inflection/python -q
```
