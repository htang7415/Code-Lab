# Jacobian

> Track: `ml` | Topic: `fundamentals`

## Concept

The Jacobian collects all first-order partial derivatives of a vector-valued
function. It tells you how each output coordinate changes when you nudge each
input coordinate.

## Math
$$J_{ij} = \frac{\partial f_i}{\partial x_j}$$

- $f: \mathbb{R}^n \to \mathbb{R}^m$ -- vector-valued function
- $f_i$ -- i-th output component
- $x_j$ -- j-th input component
- $J_{ij}$ -- sensitivity of output $i$ to input $j$
- $J$ -- Jacobian matrix

## Key Points

- Rows correspond to outputs; columns correspond to inputs.
- The Jacobian is the matrix version of a derivative.
- In deep learning, Jacobians describe how local perturbations propagate.

## Function

```python
def jacobian(f1: callable, f2: callable, x: float, y: float, eps: float = 1e-5) -> list[list[float]]:
```

## Run tests

```bash
pytest modules/ml/fundamentals/jacobian/python -q
```
