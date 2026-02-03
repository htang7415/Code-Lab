# K-Means

> Track: `ml` | Topic: `models`

## Concept

K-Means assigns points to nearest centroid.

## Math
$$c_i = \arg\min_j \lVert x_i - \mu_j \rVert$$

- $\mu$ -- mean
- $x_i$ -- i-th input (feature vector or sample)
- $i$ -- index
- $j$ -- index
- $x$ -- input (feature vector or sample)

- $\mu_j$ -- j-th mean

## Function

```python
def assign(points: list[list[float]], centroids: list[list[float]]) -> list[int]:
```

## Run tests

```bash
pytest modules/ml/models/k-means/python -q
```