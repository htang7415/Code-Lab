# PCA

> Track: `ml` | Topic: `models`

## Concept

PCA finds directions of maximum variance.

## Math
$$v_1 = \arg\max_{\lVert v \rVert = 1} v^\top \Sigma v$$

- $\Sigma$ -- covariance matrix
- $v_1$ -- first principal component
- $v$ -- direction vector

## Function

```python
def pca_first_component_2d(points: list[list[float]]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/models/pca/python -q
```