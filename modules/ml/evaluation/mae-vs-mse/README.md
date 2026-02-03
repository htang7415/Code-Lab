# MAE vs MSE

> Track: `ml` | Topic: `evaluation`

## Concept

Compare MAE and MSE to see sensitivity to outliers.

## Math
$$\mathrm{MAE} = \frac{1}{n}\sum_{i=1}^{n} |e_i|,\quad \mathrm{MSE} = \frac{1}{n}\sum_{i=1}^{n} e_i^2$$

- $\mathrm{MAE}$ -- mean absolute error
- $\mathrm{MSE}$ -- mean squared error
- $n$ -- number of samples
- $i$ -- index

## Function

```python
def mae_mse(y: list[float], y_hat: list[float]) -> tuple[float, float]:
```

## Run tests

```bash
pytest modules/ml/evaluation/mae-vs-mse/python -q
```