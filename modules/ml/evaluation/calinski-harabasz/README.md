# Calinski-Harabasz Index

> Track: `ml` | Topic: `evaluation`

## Concept

Calinski-Harabasz compares between- and within-cluster dispersion.

## Math

$$CH = (B/(k-1)) / (W/(n-k))$$

## Function

```python
def calinski_harabasz(b: float, w: float, k: int, n: int) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/calinski-harabasz/python -q
```
