# Cost Per Request

> Track: `ml` | Topic: `mlops`

## Concept

Cost per request measures how much serving spend is consumed, on average, for each handled request.

## Math

$$
\mathrm{cost\_per\_request} = \frac{\mathrm{total\_cost}}{\mathrm{request\_count}}
$$

- $\mathrm{total\_cost}$ -- total serving cost over the measurement window
- $\mathrm{request\_count}$ -- number of served requests

## Key Points

- This is a simple serving economics primitive.
- It pairs naturally with latency, throughput, and quality metrics.
- High request volume can still be undesirable if unit economics are poor.

## Function

```python
def cost_per_request(total_cost: float, request_count: int) -> float:
```

## Run tests

```bash
pytest modules/ml/mlops/cost-per-request/python -q
```
