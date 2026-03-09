# Gaussian Process Regression

> Track: `ml` | Topic: `models`

## Concept

Gaussian Process Regression (GPR) places a GP prior over functions and uses
kernel-based similarity to produce a predictive distribution.

## Math
$$k(x,x') = \exp\left(-\frac{\lVert x-x' \rVert^2}{2\ell^2}\right)$$

$$\mu_* = K_*^{\top}(K + \sigma_n^2 I)^{-1} y,\quad \Sigma_* = K_{**} - K_*^{\top}(K + \sigma_n^2 I)^{-1} K_*$$

- $k(x, x')$ -- kernel measuring similarity between inputs
- $\ell$ -- kernel length scale
- $K$ -- training-training kernel matrix
- $K_*$ -- training-test kernel matrix
- $K_{**}$ -- test-test kernel matrix
- $\sigma_n^2$ -- observation noise variance
- $y$ -- observed training targets
- $\mu_*$ -- predictive mean
- $\Sigma_*$ -- predictive covariance

## Key Points

- Nearby inputs have strongly correlated function values under the RBF kernel.
- The posterior mean interpolates smoothly between observed targets.
- The posterior covariance expresses uncertainty, which is one of GPR's main
  advantages over point-estimate regressors.

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
