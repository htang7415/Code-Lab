# GroupNorm

> Track: `ml` | Topic: `deep-learning`

## Concept

GroupNorm splits channels into groups and normalizes within each group.

## Math

Normalize within each group: y = (x-mean_g)/sqrt(var_g+eps)

## Function

```python
def groupnorm(x: list[float], groups: int, eps: float = 1e-5) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/deep-learning/groupnorm/python -q
```
