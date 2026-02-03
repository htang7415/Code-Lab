# Gaussian Process Regression

> Track: `ml` | Topic: `models`

## Concept

Gaussian Process Regression (GPR) places a GP prior over functions and uses
kernel-based similarity to produce a predictive distribution.

## Math
$$k(x,x') = \exp\left(-\frac{\lVert x-x' \rVert^2}{2\ell^2}\right)$$

$$\mu_* = K_*^{\top} K^{-1} y,\quad \Sigma_* = K_{**} - K_*^{\top} K^{-1} K_*$$

- $k$ -- index or number of neighbors
- $x$ -- input (feature vector or sample)
- $\mu$ -- mean
- $\Sigma$ -- covariance matrix
- $K$ -- key matrix or kernel
- $y$ -- target/label

## Function

```python
def gp_posterior_predict(
    x_train: list[list[float]],
    y_train: list[float],
    x_test: list[list[float]],
    length_scale: float,
    noise: float,
) -> tuple[list[float], list[float]]:
```

## Run tests

```bash
pytest modules/ml/models/gaussian-process-regression/python -q
```
