# Loss Functions

> Track: `ml` | Topic: `deep-learning`

## Purpose

Use this module to compare the core loss families that matter in modern ML:
classification losses, regression losses, and robust losses.

## First Principles

- A loss tells the model what kind of error matters.
- Cross-entropy is the default classification loss because it rewards correct probability mass.
- Focal loss is a variant of cross-entropy for imbalanced classification with many easy examples.
- Hinge loss is margin-based rather than probability-based.
- MSE, MAE, RMSE, and Huber are regression-style losses that differ mainly in how strongly they punish large residuals.

## Core Math

$$
L_{\text{CE}} = -\log p_{\text{target}},
\quad
L_{\text{focal}} = -(1-p)^\gamma \log p
$$

$$
L_{\text{hinge}} = \max(0, 1-y \cdot s)
$$

$$
\mathrm{MAE} = \frac{1}{n}\sum_i |y_i-\hat y_i|,
\quad
\mathrm{MSE} = \frac{1}{n}\sum_i (y_i-\hat y_i)^2
$$

Huber loss:

$$
L_\delta(r) =
\begin{cases}
\frac{1}{2}r^2 & |r| \le \delta \\
\delta(|r| - \frac{1}{2}\delta) & |r| > \delta
\end{cases}
$$

## From Math To Code

- Convert logits to probabilities before cross-entropy.
- Compute residuals before regression losses.
- Use Huber when you want a quadratic loss near zero and a linear loss in the tails.

## Minimal Code Mental Model

```python
probs = softmax_probs(logits)
ce = cross_entropy(logits, target)
err = residuals(y_true, y_pred)
reg = mse(y_true, y_pred)
robust = huber(y_true_scalar, y_pred_scalar, delta=1.0)
```

## Function

```python
def softmax_probs(logits: list[float]) -> list[float]:
def cross_entropy(logits: list[float], target: int) -> float:
def focal_loss(p: float, gamma: float = 2.0) -> float:
def hinge_loss(score: float, label: int) -> float:
def huber(y: float, y_hat: float, delta: float = 1.0) -> float:
def residuals(y: list[float], y_hat: list[float]) -> list[float]:
def mae(y: list[float], y_hat: list[float]) -> float:
def mse(y: list[float], y_hat: list[float]) -> float:
def rmse(y: list[float], y_hat: list[float]) -> float:
```

## When To Use What

- Use cross-entropy for most classification setups.
- Use focal loss when class imbalance creates many easy negatives.
- Use hinge loss when you want a margin-based classifier rather than calibrated probabilities.
- Use MSE for standard regression, MAE for more outlier robustness, RMSE when you want the error back on the original scale, and Huber when you want a smooth compromise.

## References

- Shannon (1948). [A Mathematical Theory of Communication](https://doi.org/10.1002/j.1538-7305.1948.tb01338.x)
- Cortes and Vapnik (1995). [Support-vector networks](https://link.springer.com/article/10.1007/BF00994018)
- Huber (1964). [Robust Estimation of a Location Parameter](https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-35/issue-1/Robust-Estimation-of-a-Location-Parameter/10.1214/aoms/1177703732.full)
- Lin et al. (2017). [Focal Loss for Dense Object Detection](https://arxiv.org/abs/1708.02002)

## Run tests

```bash
pytest modules/ml/deep-learning/loss-functions/python -q
```
