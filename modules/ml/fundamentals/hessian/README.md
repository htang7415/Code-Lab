# Hessian

> Track: `ml` | Topic: `fundamentals`

## Concept

The Hessian is the matrix of second derivatives of a scalar function. It
describes local curvature: whether the objective bends upward, downward, or
differs by direction.

## Math
$$H_{ij} = \frac{\partial^2 f}{\partial x_i\,\partial x_j}$$

- $f$ -- scalar-valued objective function
- $x_i, x_j$ -- input coordinates
- $H_{ij}$ -- mixed second derivative with respect to coordinates $i$ and $j$
- $H$ -- Hessian matrix

## Key Points

- Positive curvature means the function bends upward locally.
- Negative curvature means it bends downward locally.
- Second-order methods use Hessian information to choose smarter steps.

## Function

```python
def hessian_quadratic(a: float) -> float:
```

## Run tests

```bash
pytest modules/ml/fundamentals/hessian/python -q
```
