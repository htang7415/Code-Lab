# Dataset vs Batch vs Epoch

> Track: `ml` | Topic: `data`

## Concept

A dataset is the full collection; a batch is a subset; an epoch is one full pass.

## Math

num_batches = ceil(dataset_size / batch_size)

## Function

```python
def num_batches(dataset_size: int, batch_size: int) -> int:
```

## Run tests

```bash
pytest modules/ml/data/dataset-batch-epoch/python -q
```
