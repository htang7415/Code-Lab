# Offline vs Online Inference

> Track: `ml` | Topic: `mlops`

## Concept

Offline runs in batches; online responds per request.

## Math

$$latency_online << latency_batch$$

## Function

```python
def is_online(latency_ms: float, threshold_ms: float = 100.0) -> bool:
```

## Run tests

```bash
pytest modules/ml/mlops/offline-online-inference/python -q
```
