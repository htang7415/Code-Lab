# DBSCAN

> Track: `ml` | Topic: `models`

## Concept

DBSCAN groups points by density using eps-neighborhoods.

## Math

neighbors(x) = {y | dist(x,y) <= eps}

## Function

```python
def neighbors(points: list[list[float]], idx: int, eps: float) -> list[int]:
```

## Run tests

```bash
pytest modules/ml/models/dbscan/python -q
```
