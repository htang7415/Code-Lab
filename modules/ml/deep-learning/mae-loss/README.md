# Mean Absolute Error

> Track: `ml` | Topic: `deep-learning`

## Concept

MAE penalizes absolute residuals.

## Math

MAE = (1/n) Σ |y - ŷ|

## Function

```python
def mae(y: list[float], y_hat: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/mae-loss/python -q
```
