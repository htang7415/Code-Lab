# Tensor Parallel Linear All-Reduce

> Track: `ml` | Topic: `systems`

## Concept

Tensor parallelism shards a large matrix multiplication across devices.
In a row-parallel linear layer, each shard owns part of the input dimension and produces a partial output that must be summed across shards.

## Math

$$d_{\mathrm{local}} = \frac{d_{\mathrm{in}}}{S}$$

$$B_{\mathrm{allreduce}} = N \, d_{\mathrm{out}} \, b$$

- $d_{\mathrm{in}}$ -- input width
- $d_{\mathrm{out}}$ -- output width
- $S$ -- number of shards
- $d_{\mathrm{local}}$ -- input width stored on one shard
- $N$ -- number of batch tokens
- $b$ -- bytes per output element
- $B_{\mathrm{allreduce}}$ -- output bytes that must be reduced across shards

## Key Points

- Tensor parallelism reduces per-device parameter size.
- Row-parallel layers introduce synchronization because partial outputs must be summed.
- This module models payload size, not collective algorithm constants.

## Function

```python
def row_parallel_linear_stats(
    batch_tokens: int,
    input_dim: int,
    output_dim: int,
    num_shards: int,
    bytes_per_element: int = 2,
) -> tuple[int, int]:
```

## Run tests

```bash
pytest modules/ml/systems/tensor-parallelism/python -q
```
