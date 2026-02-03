# Gaussian Naive Bayes

> Track: `ml` | Topic: `models`

## Concept

Gaussian NB assumes features are independent Gaussians per class.

## Math
$$p(x\mid y)=\prod_i \mathcal{N}(x_i;\mu_i,\sigma_i^2)$$

- $\mathcal{N}$ -- normal (Gaussian) distribution
- $\mu$ -- mean
- $\sigma$ -- standard deviation
- $x_i$ -- i-th input (feature vector or sample)
- $p$ -- probability
- $x$ -- input (feature vector or sample)
- $y$ -- target/label
- $i$ -- index

- $\mu_i$ -- i-th mean
- $\sigma_i$ -- i-th standard deviation

## Function

```python
def gaussian_log_likelihood(x: list[float], mean: list[float], var: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/models/gaussian-naive-bayes/python -q
```