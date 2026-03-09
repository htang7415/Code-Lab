# Gaussian Mixture Model EM Step

> Track: `ml` | Topic: `models`

## Concept

A Gaussian mixture model (GMM) explains data as a weighted sum of Gaussian components.
Expectation-Maximization (EM) alternates between soft assignment of points to components and parameter updates from those assignments.

## Math

$$r_{ik} = \frac{\pi_k \, \mathcal{N}(x_i \mid \mu_k, \sigma_k^2)}{\sum_{j=1}^{K} \pi_j \, \mathcal{N}(x_i \mid \mu_j, \sigma_j^2)}$$

$$\mu_k' = \frac{\sum_i r_{ik} x_i}{\sum_i r_{ik}}$$

- $r_{ik}$ -- responsibility of component $k$ for point $i$
- $\pi_k$ -- mixture weight of component $k$
- $\mu_k$ -- mean of component $k$
- $\sigma_k^2$ -- variance of component $k$
- $K$ -- number of components

## Key Points

- GMM uses soft cluster membership instead of hard assignments.
- EM increases data likelihood by alternating E-step and M-step updates.
- Initialization matters because EM can converge to local optima.

## Function

```python
def em_step_1d(
    data: list[float],
    weights: list[float],
    means: list[float],
    variances: list[float],
) -> tuple[list[float], list[float], list[float]]:
```

## Run tests

```bash
pytest modules/ml/models/gaussian-mixture-model-em/python -q
```
