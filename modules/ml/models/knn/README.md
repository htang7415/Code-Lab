# K-Nearest Neighbors

> Track: `ml` | Topic: `models`

## Concept

KNN predicts by majority vote of nearest points.

## Math
$$\hat{c} = \arg\max_c \sum_{i \in \mathcal{N}_k} \mathbb{I}[y_i=c]$$

- $\mathbb{I}$ -- indicator function
- $\mathcal{N}$ -- normal (Gaussian) distribution
- $y_i$ -- i-th target/label
- $i$ -- index
- $k$ -- index or number of neighbors
- $y$ -- target/label

## Function

```python
def knn_predict(distances: list[float], labels: list[int], k: int) -> int:
```

## Run tests

```bash
pytest modules/ml/models/knn/python -q
```