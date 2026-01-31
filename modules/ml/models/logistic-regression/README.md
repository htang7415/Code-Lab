# Logistic Regression

> Track: `ml` | Topic: `models`

## Concept

Logistic regression models class probability with a sigmoid.

## Math

$$p = 1/(1+e^{-(w·x+b)})$$

## Function

```python
def predict_proba(x: list[float], w: list[float], b: float) -> float:
```

## Run tests

```bash
pytest modules/ml/models/logistic-regression/python -q
```
