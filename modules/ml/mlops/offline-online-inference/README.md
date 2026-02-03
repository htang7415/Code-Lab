# Offline vs Online Inference

> Track: `ml` | Topic: `mlops`

## Concept

Offline runs in batches; online responds per request.

## Math
$$\mathrm{latency}_{\text{online}} \ll \mathrm{latency}_{\text{batch}}$$

- $latency$ -- response time

## Function

```python
def is_online(latency_ms: float, threshold_ms: float = 100.0) -> bool:
```

## Run tests

```bash
pytest modules/ml/mlops/offline-online-inference/python -q
```