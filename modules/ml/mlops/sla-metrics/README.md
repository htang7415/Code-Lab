# SLA Metrics

> Track: `ml` | Topic: `mlops`

## Concept

SLA metrics track latency or error thresholds.

## Math
$$\mathrm{violation\_rate} = \frac{\text{violations}}{\text{total}}$$

- $\mathrm{violation\_rate}$ -- fraction of SLA violations
- $violations$ -- number of SLA violations
- $total$ -- total requests or samples

## Function

```python
def violation_rate(violations: int, total: int) -> float:
```

## Run tests

```bash
pytest modules/ml/mlops/sla-metrics/python -q
```
