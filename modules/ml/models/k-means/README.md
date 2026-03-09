# K-Means

> Track: `ml` | Topic: `models`

## Concept

K-Means alternates between assigning each point to its nearest centroid and
updating centroids to the mean of their assigned points. It is one of the
simplest clustering algorithms.

## Math
$$c_i = \arg\min_j \lVert x_i - \mu_j \rVert$$

- $x_i$ -- i-th data point
- $\mu_j$ -- centroid of cluster $j$
- $c_i$ -- cluster assignment for point $i$
- $i$ -- index
- $j$ -- index

## Key Points

- Assignment uses nearest-centroid distance.
- Update moves each centroid to the average of its assigned points.
- K-Means prefers compact, roughly spherical clusters.

## Function

```python
def assign(points: list[list[float]], centroids: list[list[float]]) -> list[int]:
```

## Run tests

```bash
pytest modules/ml/models/k-means/python -q
```
