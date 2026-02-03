# Vectors and Matrices

> Track: `ml` | Topic: `fundamentals`

## Concept

Vectors and matrices represent data and linear transforms.

## Math

$$y = A x$$

- $y$ -- target/label
- $x$ -- input (feature vector or sample)

- $A$ -- matrix

## Function

```python
def matvec(a: list[list[float]], x: list[float]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/fundamentals/vectors-matrices/python -q
```
