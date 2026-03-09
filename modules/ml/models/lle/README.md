# LLE Reconstruction Weights

> Track: `ml` | Topic: `models`

## Concept

Locally Linear Embedding (LLE) represents each point as a weighted combination of its neighbors.
The weights are chosen to reconstruct the point as accurately as possible while summing to one.

## Math

$$\min_w \left\lVert x_i - \sum_j w_j x_j \right\rVert^2 \quad \text{s.t.} \quad \sum_j w_j = 1$$

$$C w = \mathbf{1}, \qquad w \leftarrow \frac{w}{\sum_j w_j}$$

- $x_i$ -- point being reconstructed
- $x_j$ -- neighbor points of $x_i$
- $w_j$ -- reconstruction weights
- $C$ -- local covariance matrix built from neighbor differences

## Key Points

- LLE is a manifold-learning method based on local linear structure.
- The geometry is captured by reconstruction weights, not by global distances alone.
- Small regularization helps when neighbors are nearly collinear.

## Function

```python
def lle_weights(
    point: list[float],
    neighbors: list[list[float]],
    regularization: float = 1e-3,
) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/models/lle/python -q
```
