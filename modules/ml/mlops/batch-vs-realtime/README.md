# Batch vs Real-Time Inference

> Track: `ml` | Topic: `mlops`

## Concept

Batching trades latency for throughput.

## Math
$$\mathrm{throughput}_{\text{batch}} > \mathrm{throughput}_{\text{realtime}}$$

- $throughput$ -- requests per unit time

## Function

```python
def choose_mode(batch_size: int) -> str:
```

## Run tests

```bash
pytest modules/ml/mlops/batch-vs-realtime/python -q
```