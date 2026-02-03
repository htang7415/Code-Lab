# Request Batching

> Track: `ml` | Topic: `mlops`

## Concept

Batch requests to improve throughput.

## Math
$$\text{batches} = \left\lceil \frac{n}{\text{batch\_size}} \right\rceil$$

- $batches$ -- number of batches
- $n$ -- number of requests
- $\mathrm{batch\_size}$ -- requests per batch

## Function

```python
def batch_requests(n: int, batch_size: int) -> int:
```

## Run tests

```bash
pytest modules/ml/mlops/request-batching/python -q
```
