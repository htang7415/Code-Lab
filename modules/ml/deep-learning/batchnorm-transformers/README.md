# Why BatchNorm is Bad for Transformers

> Track: `ml` | Topic: `deep-learning`

## Concept

BatchNorm mixes statistics across batch/time, which conflicts with sequence modeling.

## Math

$$\mu_B = \frac{1}{BT}\sum_{b=1}^{B}\sum_{t=1}^{T} x_{b,t}$$

## Function

```python
def batch_stats(matrix: list[list[float]]) -> tuple[float, float]:
```

## Run tests

```bash
pytest modules/ml/deep-learning/batchnorm-transformers/python -q
```
