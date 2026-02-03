# Jacobian

> Track: `ml` | Topic: `fundamentals`

## Concept

Jacobian contains partial derivatives of vector-valued functions.

## Math
$$J_{ij} = \frac{\partial f_i}{\partial x_j}$$

- $J_ij$ -- objective for ij
- $x_j$ -- j-th input (feature vector or sample)
- $J$ -- objective
- $x$ -- input (feature vector or sample)
- $j$ -- index

## Function

```python
def jacobian(f1: callable, f2: callable, x: float, y: float, eps: float = 1e-5) -> list[list[float]]:
```

## Run tests

```bash
pytest modules/ml/fundamentals/jacobian/python -q
```