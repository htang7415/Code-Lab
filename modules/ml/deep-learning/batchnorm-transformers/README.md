# Why BatchNorm is Bad for Transformers

> Track: `ml` | Topic: `deep-learning`

## Concept

BatchNorm mixes statistics across batch/time, which conflicts with sequence modeling.

## Math

$$\mu_B = \frac{1}{BT}\sum_{b=1}^{B}\sum_{t=1}^{T} x_{b,t}$$

- $\mu$ -- mean
- $x_b$ -- input (feature vector or sample) for b
- $b$ -- bias term
- $t$ -- timestep or iteration
- $x$ -- input (feature vector or sample)

- $\mu_B$ -- mean for B
- $B$ -- matrix
- $T$ -- number of steps

## Function

```python
def batch_stats(matrix: list[list[float]]) -> tuple[float, float]:
```

## Run tests

```bash
pytest modules/ml/deep-learning/batchnorm-transformers/python -q
```
