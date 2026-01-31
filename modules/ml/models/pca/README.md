# PCA

> Track: `ml` | Topic: `models`

## Concept

PCA finds directions of maximum variance.

## Math

First principal component = eigenvector of covariance matrix.

## Function

```python
def pca_first_component_2d(points: list[list[float]]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/models/pca/python -q
```
