# Calinski-Harabasz Index

> Track: `ml` | Topic: `evaluation`

## Concept

Calinski-Harabasz compares between- and within-cluster dispersion.

## Math

$$CH = (B/(k-1)) / (W/(n-k))$$

- $B$ -- between-cluster dispersion
- $k$ -- number of clusters
- $W$ -- within-cluster dispersion
- $n$ -- number of samples

## Function

```python
def calinski_harabasz(b: float, w: float, k: int, n: int) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/calinski-harabasz/python -q
```
