# Gradient Checking

> Track: `ml` | Topic: `deep-learning`

## Concept

Finite differences approximate gradients to validate backprop.

## Math

$$\frac{df}{dx} \approx \frac{f(x+\epsilon) - f(x-\epsilon)}{2\epsilon}$$

## Function

```python
def grad_check(f, x: float, eps: float = 1e-5) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/gradient-checking/python -q
```
