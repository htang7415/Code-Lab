# Breach Heat

> Track: `ml` | Topic: `mlops`

## Concept

Breach heat measures the total squared overload above a hard capacity limit.

## Math

$$
\mathrm{BreachHeat} = \sum_{i=1}^{N} \max\left(0, \frac{x_i - C}{C}\right)^2
$$

- $x_i$ -- observed load or utilization at step $i$
- $C$ -- hard capacity limit

## Key Points

- Squaring makes severe breaches count more than mild ones.
- Summing across time makes repeated breaches accumulate instead of averaging away.
- This is a total batch burden, not a normalized rate.

## Function

```python
def breach_heat(observations: list[float], capacity: float) -> float:
```

## Run tests

```bash
pytest modules/ml/mlops/breach-heat/python -q
```
