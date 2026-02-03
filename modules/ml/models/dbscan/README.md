# DBSCAN

> Track: `ml` | Topic: `models`

## Concept

DBSCAN groups points by density using eps-neighborhoods.

## Math
$$\mathcal{N}_arepsilon(x) = \{y \mid \mathrm{dist}(x,y) \le arepsilon\}$$

- $\mathcal{N}$ -- normal (Gaussian) distribution
- $x$ -- input (feature vector or sample)
- $y$ -- target/label

## Function

```python
def neighbors(points: list[list[float]], idx: int, eps: float) -> list[int]:
```

## Run tests

```bash
pytest modules/ml/models/dbscan/python -q
```