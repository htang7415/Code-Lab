# Batch Iterator

> Track: `ml` | Topic: `data`

## Concept

A batch iterator yields index ranges for mini-batches.

## Math

$$b_i = \left[iB, \min\left((i+1)B, N\right)\right)$$

## Function

```python
def batch_indices(n: int, batch_size: int) -> list[list[int]]:
```

## Run tests

```bash
pytest modules/ml/data/batch-iterator/python -q
```
