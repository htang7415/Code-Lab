# Root Mean Squared Error

> Track: `ml` | Topic: `deep-learning`

## Concept

RMSE is the square root of MSE.

## Math

$$\mathrm{RMSE} = \sqrt{\mathrm{MSE}}$$

## Function

```python
def rmse(y: list[float], y_hat: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/rmse-loss/python -q
```
