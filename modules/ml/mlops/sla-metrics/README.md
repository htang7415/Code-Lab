# SLA Metrics

> Track: `ml` | Topic: `mlops`

## Concept

SLA metrics track latency or error thresholds.

## Math

$$violation_rate = violations / total$$

## Function

```python
def violation_rate(violations: int, total: int) -> float:
```

## Run tests

```bash
pytest modules/ml/mlops/sla-metrics/python -q
```
