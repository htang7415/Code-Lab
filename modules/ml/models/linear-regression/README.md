# Linear Regression

> Track: `ml` | Topic: `models`

## Concept

Linear regression predicts a target as a linear function of features.

## Math

y = w · x + b

## Function

```python
def predict(x: list[float], w: list[float], b: float) -> float:
```

## Run tests

```bash
pytest modules/ml/models/linear-regression/python -q
```
