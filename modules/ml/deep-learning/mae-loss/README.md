# Mean Absolute Error

> Track: `ml` | Topic: `deep-learning`

## Concept

MAE penalizes absolute residuals.

## Math

$$\mathrm{MAE} = \frac{1}{n}\sum_i |y_i - \hat{y}_i|$$

- $\mathrm{MAE}$ -- mean absolute error
- $\hat{y}$ -- prediction
- $y_i$ -- i-th target/label
- $n$ -- number of samples
- $i$ -- index
- $y$ -- target/label

## Function

```python
def mae(y: list[float], y_hat: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/mae-loss/python -q
```
