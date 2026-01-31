# Mean Squared Error

> Track: `ml` | Topic: `deep-learning`

## Concept

MSE penalizes squared residuals.

## Math

$$\mathrm{MSE} = \frac{1}{n}\sum_i (y_i - \hat{y}_i)^2$$

## Function

```python
def mse(y: list[float], y_hat: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/mse-loss/python -q
```
