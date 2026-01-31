# K-Nearest Neighbors

> Track: `ml` | Topic: `models`

## Concept

KNN predicts by majority vote of nearest points.

## Math

argmax_c Σ 1[y_i=c] for k nearest

## Function

```python
def knn_predict(distances: list[float], labels: list[int], k: int) -> int:
```

## Run tests

```bash
pytest modules/ml/models/knn/python -q
```
