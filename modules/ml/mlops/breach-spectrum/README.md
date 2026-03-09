# Breach Spectrum

> Track: `ml` | Topic: `mlops`

## Concept

Breach spectrum counts how many breached observations fall into each severity bucket.

## Math

For normalized breach ratios $r_i = \max(0, (x_i - C) / C)$ and ordered cutoffs
$c_1 \le c_2 \le \dots \le c_K$:

$$
\mathrm{Bucket}_j = \sum_i \mathbf{1}[r_i \in B_j]
$$

- $x_i$ -- observed load or utilization at step $i$
- $C$ -- hard capacity limit
- $B_j$ -- the $j$th severity bucket defined by the cutoffs

## Key Points

- This is a histogram-style summary over breached observations only.
- It shows whether overload is mostly mild, moderate, or severe.
- This module returns raw counts per bucket, not shares.

## Function

```python
def breach_spectrum(observations: list[float], capacity: float, cutoffs: list[float]) -> list[int]:
```

## Run tests

```bash
pytest modules/ml/mlops/breach-spectrum/python -q
```
