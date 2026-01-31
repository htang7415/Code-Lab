# Nesterov Accelerated Gradient

> Track: `ml` | Topic: `optimization`

## Concept

Nesterov uses a lookahead gradient for faster convergence.

## Math

v = μv + grad(w - lr*μv); w = w - lr * v

## Function

```python
def nesterov_step(w: float, grad: float, v: float, lr: float, mu: float) -> tuple[float, float]:
```

## Run tests

```bash
pytest modules/ml/optimization/nesterov/python -q
```
