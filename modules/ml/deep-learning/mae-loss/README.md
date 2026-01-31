# Mean Absolute Error

> Track: `ml` | Topic: `deep-learning`

## Concept

MAE penalizes absolute residuals.

## Math

$$\mathrm{MAE} = \frac{1}{n}\sum_i |y_i - \hat{y}_i|$$

## Function

```python
def mae(y: list[float], y_hat: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/mae-loss/python -q
```
