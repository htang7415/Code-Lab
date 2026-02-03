# Hessian

> Track: `ml` | Topic: `fundamentals`

## Concept

Hessian is the matrix of second derivatives.

## Math
$$H_{ij} = \frac{\partial^2 f}{\partial x_i\,\partial x_j}$$

- $x_i$ -- i-th input (feature vector or sample)
- $x_j$ -- j-th input (feature vector or sample)
- $x$ -- input (feature vector or sample)
- $i$ -- index
- $j$ -- index

## Function

```python
def hessian_quadratic(a: float) -> float:
```

## Run tests

```bash
pytest modules/ml/fundamentals/hessian/python -q
```