# Isolation Forest Score

> Track: `ml` | Topic: `models`

## Concept

Isolation Forest detects anomalies by asking how quickly a point becomes isolated under random partitioning.
Shorter path lengths indicate easier isolation and therefore more anomalous points.

## Math

$$s(x, n) = 2^{-E[h(x)] / c(n)}$$

$$c(n) = 2 H_{n-1} - \frac{2(n-1)}{n}$$

- $E[h(x)]$ -- average path length for point $x$
- $c(n)$ -- normalizing average path length for sample size $n$
- $H_{n-1}$ -- harmonic number
- $s(x, n)$ -- anomaly score

## Key Points

- Short path lengths imply anomalous behavior.
- The score is normalized by expected path length at sample size $n$.
- Scores closer to $1$ are more anomalous.

## Function

```python
def average_path_length(sample_size: int) -> float:
def isolation_score(avg_path_length: float, sample_size: int) -> float:
```

## Run tests

```bash
pytest modules/ml/models/isolation-forest/python -q
```
