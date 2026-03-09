# KV Cache Size

> Track: `ml` | Topic: `llm`

## Concept

Autoregressive transformers cache key and value tensors from previous tokens so they do not recompute attention over the full prefix at every decode step.

## Math

$$\mathrm{bytes} = B \cdot L \cdot T \cdot H_{kv} \cdot D \cdot 2 \cdot s$$

- $B$ -- batch size
- $L$ -- number of layers
- $T$ -- cached tokens
- $H_{kv}$ -- number of key-value heads
- $D$ -- head dimension
- $2$ -- one tensor for keys and one for values
- $s$ -- bytes per stored element

## Key Points

- KV cache memory scales linearly with context length.
- Multi-query or grouped-query attention reduces cache size by shrinking $H_{kv}$.
- Memory pressure from the cache often drives serving decisions.

## Function

```python
def kv_cache_bytes(
    num_layers: int,
    num_tokens: int,
    num_kv_heads: int,
    head_dim: int,
    bytes_per_element: int,
    batch_size: int = 1,
) -> int:
```

## Run tests

```bash
pytest modules/ml/llm/kv-cache/python -q
```
