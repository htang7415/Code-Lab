# BatchNorm

> Track: `ml` | Topic: `deep-learning`

## Concept

BatchNorm normalizes activations across the batch.

## Math

$$y = \frac{x - \mu_B}{\sqrt{\sigma_B^2 + \epsilon}}$$

- $x$ -- input features
- $y$ -- normalized output
- $\mu_B$ -- batch mean
- $\sigma_B$ -- batch standard deviation
- $\epsilon$ -- small constant for numerical stability

## Function

```python
def batchnorm(x: list[float], eps: float = 1e-5) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/deep-learning/batchnorm/python -q
```
