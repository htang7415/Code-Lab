# Gaussian Process Regression

> Track: `ml` | Topic: `models`

## Concept

Gaussian Process Regression (GPR) places a GP prior over functions and uses
kernel-based similarity to produce a predictive distribution.

## Math

$$k(x,x') = \exp\left(-\frac{\lVert x-x' \rVert^2}{2\ell^2}\right)$$

$$f(x) \sim \mathcal{GP}(0, k), \quad y = f(x) + \varepsilon,\ \varepsilon \sim \mathcal{N}(0, \sigma_n^2)$$

$$K = K(X,X) + \sigma_n^2 I,\quad K_* = K(X, X_*),\quad K_{**} = K(X_*, X_*)$$

$$\mu_* = K_*^\top K^{-1} y,\quad \Sigma_* = K_{**} - K_*^\top K^{-1} K_*$$

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
