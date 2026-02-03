# Davies-Bouldin Index

> Track: `ml` | Topic: `evaluation`

## Concept

Davies-Bouldin averages cluster similarity; lower is better.

## Math

$$DB = \frac{1}{K}\sum_i \max_{j \ne i} \frac{s_i + s_j}{d_{ij}}$$

- $DB$ -- Davies-Bouldin index
- $K$ -- number of clusters
- $s_i$ -- scatter within cluster $i$
- $s_j$ -- scatter within cluster $j$
- $d_{ij}$ -- distance between cluster centroids $i$ and $j$

## Function

```python
def davies_bouldin(si: float, sj: float, dij: float) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/davies-bouldin/python -q
```
