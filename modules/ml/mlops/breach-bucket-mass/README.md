# Breach Bucket Mass

> Track: `ml` | Topic: `mlops`

## Concept

Breach bucket mass measures what fraction of total normalized overload falls into each breach severity bucket.

## Math

For normalized breach ratios $r_i = \max(0, (x_i - C) / C)$ and ordered cutoffs
$c_1 \le c_2 \le \dots \le c_K$:

$$
\mathrm{Mass}_j = \frac{\sum_i r_i \mathbf{1}[r_i \in B_j]}{\sum_i r_i}
$$

- $x_i$ -- observed load or utilization at step $i$
- $C$ -- hard capacity limit
- $B_j$ -- the $j$th severity bucket defined by the cutoffs

## Key Points

- This weights breaches by severity, not just count.
- It is the mass-weighted analogue of breach bucket share.
- This module returns zeros when there is no overload mass.

## Function

```python
def breach_bucket_mass(observations: list[float], capacity: float, cutoffs: list[float]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/mlops/breach-bucket-mass/python -q
```
