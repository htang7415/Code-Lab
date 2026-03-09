# Queue Utilization

> Track: `ml` | Topic: `mlops`

## Concept

Queue utilization measures how full a serving queue is relative to its configured capacity.

## Math

$$
\mathrm{utilization} = \frac{\mathrm{queue\_depth}}{\mathrm{queue\_capacity}}
$$

- $\mathrm{queue\_depth}$ -- current number of queued requests
- $\mathrm{queue\_capacity}$ -- maximum intended queue size

## Key Points

- High queue utilization often precedes latency spikes.
- This is a simple saturation metric for serving pipelines.
- The module returns both utilization and a saturation flag.

## Function

```python
def queue_utilization(queue_depth: int, queue_capacity: int) -> tuple[float, bool]:
```

## Run tests

```bash
pytest modules/ml/mlops/queue-utilization/python -q
```
