# InstanceNorm

> Track: `ml` | Topic: `deep-learning`

## Concept

InstanceNorm normalizes per-sample per-channel, often for vision.

## Math

Normalize within a single instance: y = (x-mean)/sqrt(var+eps)

## Function

```python
def instancenorm(x: list[float], eps: float = 1e-5) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/deep-learning/instancenorm/python -q
```
