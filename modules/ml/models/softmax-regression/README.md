# Softmax Regression

> Track: `ml` | Topic: `models`

## Concept

Softmax regression generalizes logistic regression to multiple classes.

## Math

p_i = exp(z_i)/Σ exp(z_j)

## Function

```python
def softmax(logits: list[float]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/models/softmax-regression/python -q
```
