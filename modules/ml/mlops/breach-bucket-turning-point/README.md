# Breach Bucket Turning Point

> Track: `ml` | Topic: `mlops`

## Concept

Breach bucket turning point identifies the interior bucket where breach-share growth turns into decline.

## Math

If bucket shares are $p_1, \dots, p_K$, a turning point at bucket $j$ satisfies:

$$
p_j \ge p_{j-1} \quad \text{and} \quad p_j > p_{j+1}
$$

## Key Points

- This looks for a local peak in the bucket-share sequence.
- It is stricter than a knee heuristic because it requires an actual turn.
- This module returns `-1` when no turning point exists.

## Function

```python
def breach_bucket_turning_point(
    observations: list[float],
    capacity: float,
    cutoffs: list[float],
) -> int:
```

## Run tests

```bash
pytest modules/ml/mlops/breach-bucket-turning-point/python -q
```
