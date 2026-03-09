# DBSCAN

> Track: `ml` | Topic: `models`

## Concept

DBSCAN clusters points by density rather than by forcing every point into a
centroid-based partition. Points with enough neighbors become core points and
grow clusters outward through density connectivity.

## Math
$$\mathcal{N}_{\varepsilon}(x) = \{y \mid \mathrm{dist}(x,y) \le \varepsilon\}$$

- $\mathcal{N}_{\varepsilon}(x)$ -- epsilon-neighborhood of point $x$
- $x, y$ -- data points
- $\mathrm{dist}(x,y)$ -- distance between two points
- $\varepsilon$ -- neighborhood radius

## Key Points

- DBSCAN can discover arbitrarily shaped clusters.
- Noise points can remain unassigned instead of being forced into a cluster.
- Cluster quality depends strongly on the choice of `eps` and `min_samples`.

## Function

```python
def neighbors(points: list[list[float]], idx: int, eps: float) -> list[int]:
```

## Run tests

```bash
pytest modules/ml/models/dbscan/python -q
```
