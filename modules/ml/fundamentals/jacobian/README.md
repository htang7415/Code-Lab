# Jacobian

> Track: `ml` | Topic: `fundamentals`

## Concept

Jacobian contains partial derivatives of vector-valued functions.

## Math

J_ij = ∂f_i/∂x_j

## Function

```python
def jacobian(f1: callable, f2: callable, x: float, y: float, eps: float = 1e-5) -> list[list[float]]:
```

## Run tests

```bash
pytest modules/ml/fundamentals/jacobian/python -q
```
