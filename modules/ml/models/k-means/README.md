# K-Means

> Track: `ml` | Topic: `models`

## Concept

K-Means assigns points to nearest centroid.

## Math

$$c_i = \arg\min_j \lVert x_i - \mu_j \rVert$$

## Function

```python
def assign(points: list[list[float]], centroids: list[list[float]]) -> list[int]:
```

## Run tests

```bash
pytest modules/ml/models/k-means/python -q
```
