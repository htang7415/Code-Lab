# Breach Burden

> Track: `ml` | Topic: `mlops`

## Concept

Breach burden measures the total normalized amount by which observations exceed a hard capacity.

## Math

$$
\mathrm{BreachBurden} = \sum_{i=1}^{N} \max\left(0, \frac{x_i - C}{C}\right)
$$

- $x_i$ -- observed load or utilization at time step $i$
- $C$ -- hard capacity limit

## Key Points

- This captures both how many breaches occurred and how large they were.
- It differs from a breach rate because repeated small breaches and one large breach both add to the burden.
- This module returns an unbounded batch total.

## Function

```python
def breach_burden(observations: list[float], capacity: float) -> float:
```

## Run tests

```bash
pytest modules/ml/mlops/breach-burden/python -q
```
