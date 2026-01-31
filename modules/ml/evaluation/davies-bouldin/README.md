# Davies-Bouldin Index

> Track: `ml` | Topic: `evaluation`

## Concept

Davies-Bouldin averages cluster similarity; lower is better.

## Math

DB = (1/K) Σ max_{j!=i} (s_i + s_j) / d_{ij}

## Function

```python
def davies_bouldin(si: float, sj: float, dij: float) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/davies-bouldin/python -q
```
