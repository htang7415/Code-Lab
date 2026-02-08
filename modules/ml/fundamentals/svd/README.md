# SVD

> Track: `ml` | Topic: `fundamentals`

## Concept

SVD factorizes a matrix into orthonormal bases and non-negative singular values.

## Math

$$A = U \Sigma V^{\top}$$

For a $2\times2$ matrix, we can compute $V$ and $\Sigma$ by diagonalizing
$B = A^{\top}A$ with one Jacobi rotation, then set $U = A V \Sigma^{-1}$.

- $U$ -- left singular vectors (orthonormal)
- $\Sigma$ -- diagonal singular values (non-negative, sorted)
- $V$ -- right singular vectors (orthonormal)
- $B$ -- $A^{\top}A$ (symmetric)
- $A$ -- input matrix

## Function

```python
def svd_2x2(a: list[list[float]]) -> tuple[list[list[float]], list[float], list[list[float]]]:
```

```python
def singular_values_2x2(a: list[list[float]]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/fundamentals/svd/python -q
```
