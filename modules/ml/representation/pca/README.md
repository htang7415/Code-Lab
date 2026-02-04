# PCA (2D)

> Track: `ml` | Topic: `representation`

## Concept

Principal Component Analysis finds the direction of maximum variance.
In 2D, this is the first principal component of the covariance matrix.

## Math

Given centered points $x$, the covariance is $C = \frac{1}{n}\sum x x^T$.
The first component is the eigenvector of $C$ with the largest eigenvalue.

## Function

```python
def first_principal_component_2d(points: list[list[float]]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/representation/pca/python -q
```
