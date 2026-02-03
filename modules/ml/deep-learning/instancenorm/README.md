# InstanceNorm

> Track: `ml` | Topic: `deep-learning`

## Concept

InstanceNorm normalizes per-sample per-channel, often for vision.

## Math

$$y = \frac{x - \mu_I}{\sqrt{\sigma_I^2 + \epsilon}}$$

- $x$ -- input features
- $y$ -- normalized output
- $\mu_I$ -- mean for instance $I$
- $\sigma_I$ -- standard deviation for instance $I$
- $\epsilon$ -- small constant for numerical stability

## Function

```python
def instancenorm(x: list[float], eps: float = 1e-5) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/deep-learning/instancenorm/python -q
```
