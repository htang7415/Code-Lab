# Request Batching

> Track: `ml` | Topic: `mlops`

## Concept

Batch requests to improve throughput.

## Math

batches = ceil(n / batch_size)

## Function

```python
def batch_requests(n: int, batch_size: int) -> int:
```

## Run tests

```bash
pytest modules/ml/mlops/request-batching/python -q
```
