# MAE vs MSE

> Track: `ml` | Topic: `evaluation`

## Concept

Compare MAE and MSE to see sensitivity to outliers.

## Math

$$MAE uses |e|; MSE uses e^2.$$

## Function

```python
def mae_mse(y: list[float], y_hat: list[float]) -> tuple[float, float]:
```

## Run tests

```bash
pytest modules/ml/evaluation/mae-vs-mse/python -q
```
