# Davies-Bouldin Index

> Track: `ml` | Topic: `evaluation`

## Concept

Davies-Bouldin averages cluster similarity; lower is better.

## Math

$$DB = \frac{1}{K}\sum_i \max_{j \ne i} \frac{s_i + s_j}{d_{ij}}$$

## Function

```python
def davies_bouldin(si: float, sj: float, dij: float) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/davies-bouldin/python -q
```
