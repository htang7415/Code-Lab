# RMSNorm

> Track: `ml` | Topic: `deep-learning`

## Concept

RMSNorm normalizes by root-mean-square without centering.

## Math

$$y = \frac{x}{\sqrt{\frac{1}{d}\sum_{i=1}^{d} x_i^2 + \epsilon}}$$

- $\epsilon$ -- small constant or noise term
- $x_i$ -- i-th input (feature vector or sample)
- $y$ -- target/label
- $d$ -- dimension
- $i$ -- index
- $x$ -- input (feature vector or sample)

## Function

```python
def rmsnorm(x: list[float], eps: float = 1e-5) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/deep-learning/rmsnorm/python -q
```
