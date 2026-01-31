# Gradient Descent

> Track: `ml` | Topic: `fundamentals`

## Concept

Gradient descent updates parameters along negative gradient.

## Math

$$x = x - lr * grad$$

## Function

```python
def gd_step(x: float, grad: float, lr: float) -> float:
```

## Run tests

```bash
pytest modules/ml/fundamentals/gradient-descent/python -q
```
