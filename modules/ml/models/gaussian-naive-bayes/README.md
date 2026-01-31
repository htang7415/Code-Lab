# Gaussian Naive Bayes

> Track: `ml` | Topic: `models`

## Concept

Gaussian NB assumes features are independent Gaussians per class.

## Math

$$p(x|y)=\prod_i \mathcal{N}(x_i;\mu_i,\sigma_i^2)$$

## Function

```python
def gaussian_log_likelihood(x: list[float], mean: list[float], var: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/models/gaussian-naive-bayes/python -q
```
