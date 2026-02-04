# SVD (2x2)

> Track: `ml` | Topic: `representation`

## Concept

Singular Value Decomposition factorizes a matrix into rotations and scaling.
For a 2x2 matrix, singular values are the square roots of the eigenvalues of $A^T A$.

## Function

```python
def singular_values_2x2(matrix: list[list[float]]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/representation/svd/python -q
```
