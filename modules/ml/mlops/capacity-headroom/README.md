# Capacity Headroom

> Track: `ml` | Topic: `mlops`

## Concept

Capacity headroom measures how much serving capacity remains before the system reaches its planned limit.

## Math

$$
\mathrm{utilization} = \frac{\mathrm{current\_load}}{\mathrm{max\_capacity}}
$$

$$
\mathrm{headroom} = 1 - \mathrm{utilization}
$$

- $\mathrm{current\_load}$ -- observed request load
- $\mathrm{max\_capacity}$ -- planned maximum sustainable load

## Key Points

- Headroom is a simple safety-margin metric for serving systems.
- Low headroom means there is less room for burst traffic or degradation.
- This pairs naturally with latency and error-budget monitoring.

## Function

```python
def capacity_headroom(current_load: float, max_capacity: float) -> tuple[float, float]:
```

## Run tests

```bash
pytest modules/ml/mlops/capacity-headroom/python -q
```
