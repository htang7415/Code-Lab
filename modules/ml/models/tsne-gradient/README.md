# t-SNE Point Gradient

> Track: `ml` | Topic: `models`

## Concept

t-SNE moves nearby points together and pushes crowded points apart in a low-dimensional map.
This module computes the gradient contribution for one point from a row of high-dimensional affinities and Student-t low-dimensional similarities.

## Math

$$q_{ij} = \frac{(1 + \lVert y_i - y_j \rVert^2)^{-1}}{\sum_k (1 + \lVert y_i - y_k \rVert^2)^{-1}}$$

$$\nabla_{y_i} C \propto 4 \sum_j (p_{ij} - q_{ij}) (1 + \lVert y_i - y_j \rVert^2)^{-1} (y_i - y_j)$$

- $y_i$ -- low-dimensional point being updated
- $y_j$ -- neighboring low-dimensional points
- $p_{ij}$ -- high-dimensional affinity from point $i$ to $j$
- $q_{ij}$ -- low-dimensional affinity from point $i$ to $j$

## Key Points

- Attraction comes from neighbors with large $p_{ij}$.
- Repulsion comes from points that are too close in the map relative to $p_{ij}$.
- This module focuses on one-point gradient intuition, not the full global normalization.

## Function

```python
def tsne_point_gradient(
    point: list[float],
    other_points: list[list[float]],
    affinities: list[float],
) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/models/tsne-gradient/python -q
```
