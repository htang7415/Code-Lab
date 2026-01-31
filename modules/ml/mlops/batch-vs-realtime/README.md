# Batch vs Real-Time Inference

> Track: `ml` | Topic: `mlops`

## Concept

Batching trades latency for throughput.

## Math

$$throughput_batch > throughput_realtime$$

## Function

```python
def choose_mode(batch_size: int) -> str:
```

## Run tests

```bash
pytest modules/ml/mlops/batch-vs-realtime/python -q
```
