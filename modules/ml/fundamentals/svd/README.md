# SVD

> Track: `ml` | Topic: `fundamentals`

## Concept

SVD factorizes a matrix into $U \Sigma V^{\top}$.

## Math

$$A = U \Sigma V^{\top}$$

## Function

```python
def singular_values_2x2(a: list[list[float]]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/fundamentals/svd/python -q
```
