# Gradient Checking

> Track: `ml` | Topic: `deep-learning`

## Concept

Finite differences approximate gradients to validate backprop.

## Math

df/dx ≈ (f(x+ε) - f(x-ε)) / (2ε)

## Function

```python
def grad_check(f, x: float, eps: float = 1e-5) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/gradient-checking/python -q
```
