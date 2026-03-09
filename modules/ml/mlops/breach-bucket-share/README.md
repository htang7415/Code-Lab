# Breach Bucket Share

> Track: `ml` | Topic: `mlops`

## Concept

Breach bucket share measures what fraction of breached observations falls into each severity bucket.

## Math

For normalized breach ratios $r_i = \max(0, (x_i - C) / C)$ and ordered cutoffs
$c_1 \le c_2 \le \dots \le c_K$:

$$
\mathrm{Share}_j = \frac{\sum_i \mathbf{1}[r_i \in B_j]}{\sum_i \mathbf{1}[r_i > 0]}
$$

- $x_i$ -- observed load or utilization at step $i$
- $C$ -- hard capacity limit
- $B_j$ -- the $j$th severity bucket defined by the cutoffs

## Key Points

- This is the normalized version of breach spectrum.
- It focuses on how breach events are distributed across severity bands.
- This module returns zeros when there are no breached observations.

## Function

```python
def breach_bucket_share(observations: list[float], capacity: float, cutoffs: list[float]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/mlops/breach-bucket-share/python -q
```
