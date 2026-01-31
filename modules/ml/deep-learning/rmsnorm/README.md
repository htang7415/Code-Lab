# RMSNorm

> Track: `ml` | Topic: `deep-learning`

## Concept

RMSNorm normalizes by root-mean-square without centering.

## Math

y = x / sqrt(mean(x^2)+eps)

## Function

```python
def rmsnorm(x: list[float], eps: float = 1e-5) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/deep-learning/rmsnorm/python -q
```
