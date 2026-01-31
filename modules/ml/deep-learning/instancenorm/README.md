# InstanceNorm

> Track: `ml` | Topic: `deep-learning`

## Concept

InstanceNorm normalizes per-sample per-channel, often for vision.

## Math

$$y = \frac{x - \mu_I}{\sqrt{\sigma_I^2 + \epsilon}}$$

## Function

```python
def instancenorm(x: list[float], eps: float = 1e-5) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/deep-learning/instancenorm/python -q
```
