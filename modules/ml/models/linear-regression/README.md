# Linear Regression

> Track: `ml` | Topic: `models`

## Concept

Linear regression predicts a target as a linear function of features.

## Math
$$y = w^\top x + b$$

- $y$ -- target/label
- $w$ -- weight parameter
- $x$ -- input (feature vector or sample)
- $b$ -- bias term

## Function

```python
def predict(x: list[float], w: list[float], b: float) -> float:
```

## Run tests

```bash
pytest modules/ml/models/linear-regression/python -q
```