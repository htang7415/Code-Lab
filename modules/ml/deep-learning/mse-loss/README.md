# Mean Squared Error

> Track: `ml` | Topic: `deep-learning`

## Concept

MSE penalizes squared residuals.

## Math

MSE = (1/n) Σ (y - ŷ)^2

## Function

```python
def mse(y: list[float], y_hat: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/mse-loss/python -q
```
