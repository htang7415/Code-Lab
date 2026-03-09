# Context Parallel Attention Bytes

> Track: `ml` | Topic: `systems`

## Concept

Context parallelism splits a long sequence across devices so each device owns fewer query tokens.
The trade-off is that attention still needs remote key/value state from the rest of the sequence.

## Math

$$t_{\mathrm{local}} = \left\lceil \frac{L}{S} \right\rceil$$

$$B_{\mathrm{remote}} = 2 (L - t_{\mathrm{local}}) H b$$

- $L$ -- full sequence length
- $S$ -- number of shards
- $t_{\mathrm{local}}$ -- query tokens handled by one shard
- $H$ -- hidden width per token
- $b$ -- bytes per element
- $B_{\mathrm{remote}}$ -- remote KV bytes a shard must receive for full attention

## Key Points

- Sharding the sequence lowers local activation memory.
- Long-context attention can still be communication-heavy because each shard needs remote K and V tensors.
- This module models first-order bytes, not full overlap or kernel scheduling details.

## Function

```python
def context_parallel_attention_stats(
    sequence_length: int,
    hidden_size: int,
    num_shards: int,
    bytes_per_element: int = 2,
) -> tuple[int, int]:
```

## Run tests

```bash
pytest modules/ml/systems/context-parallelism/python -q
```
