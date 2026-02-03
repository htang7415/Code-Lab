# Mean Squared Error

> Track: `ml` | Topic: `deep-learning`

## Concept

MSE penalizes squared residuals.

## Math

$$\mathrm{MSE} = \frac{1}{n}\sum_i (y_i - \hat{y}_i)^2$$

- $\mathrm{MSE}$ -- mean squared error
- $\hat{y}$ -- prediction
- $y_i$ -- i-th target/label
- $n$ -- number of samples
- $i$ -- index
- $y$ -- target/label

## Function

```python
def mse(y: list[float], y_hat: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/mse-loss/python -q
```
