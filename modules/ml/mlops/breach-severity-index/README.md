# Breach Severity Index

> Track: `ml` | Topic: `mlops`

## Concept

Breach severity index combines how often capacity is breached with how large those breaches are on average.

## Math

Let the breach rate be

$$
r = \frac{\sum_{i=1}^{N} \mathbf{1}[x_i > C]}{N}
$$

and the mean excess ratio over breached observations be

$$
e = \frac{1}{B} \sum_{i:x_i > C} \frac{x_i - C}{C}
$$

Then this module reports

$$
\mathrm{BSI} = r(1 + e)
$$

- $x_i$ -- observed load or utilization at time step $i$
- $C$ -- capacity limit
- $B$ -- number of breached observations

## Key Points

- This score is zero when there are no breaches.
- It penalizes both frequent and severe capacity violations.
- This is a compact internal proxy, not a standard benchmark metric.

## Function

```python
def breach_severity_index(observations: list[float], capacity: float) -> float:
```

## Run tests

```bash
pytest modules/ml/mlops/breach-severity-index/python -q
```
