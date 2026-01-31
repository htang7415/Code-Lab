# RMSNorm

> Track: `ml` | Topic: `deep-learning`

## Concept

RMSNorm normalizes by root-mean-square without centering.

## Math

$$y = \frac{x}{\sqrt{\frac{1}{d}\sum_{i=1}^{d} x_i^2 + \epsilon}}$$

## Function

```python
def rmsnorm(x: list[float], eps: float = 1e-5) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/deep-learning/rmsnorm/python -q
```
