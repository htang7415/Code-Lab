# PCA

> Track: `ml` | Topic: `models`

## Concept

PCA finds directions of maximum variance.

## Math

$$v_1 = \arg\max_{\lVert v \rVert = 1} v^\top \Sigma v$$

## Function

```python
def pca_first_component_2d(points: list[list[float]]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/models/pca/python -q
```
