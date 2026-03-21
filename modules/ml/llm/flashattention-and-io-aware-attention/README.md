# FlashAttention and IO-Aware Attention

> Track: `ml` | Topic: `llm`

## Purpose

Use this module to understand why FlashAttention speeds up attention by
reducing memory traffic instead of changing the exact attention result.

## First Principles

- Standard attention often materializes a full score matrix of size $L \times L$.
- FlashAttention tiles the score computation so only a small working block has
  to live in fast memory at once.
- The main gain is lower IO between HBM and on-chip memory, not fewer FLOPs in
  the attention formula itself.
- FlashAttention-2 keeps the same exactness goal while improving work partitioning.

## Core Math

Full score-matrix bytes:

$$
\mathrm{FullBytes} = B \cdot H \cdot L^2 \cdot s
$$

Per-tile scratch bytes:

$$
\mathrm{TileBytes} = B \cdot H \cdot T_q \cdot T_k \cdot s
$$

Tile rounds:

$$
\mathrm{Rounds} = \left\lceil \frac{L}{T_q} \right\rceil \left\lceil \frac{L}{T_k} \right\rceil
$$

- $B$ -- batch size
- $H$ -- number of heads
- $L$ -- sequence length
- $T_q, T_k$ -- query and key tile sizes
- $s$ -- bytes per attention score

## From Math To Code

- Estimate the full score-matrix footprint first.
- Estimate the scratch space for one tile.
- Compare full materialization against tiled scratch space.
- Count tile rounds to see how longer sequences increase the amount of tiled work.

## Minimal Code Mental Model

```python
full = attention_score_matrix_bytes(sequence_length=4096, bytes_per_score=2, heads=32)
tile = attention_tile_bytes(query_tile=128, key_tile=128, bytes_per_score=2, heads=32)
rounds = attention_tile_rounds(sequence_length=4096, query_tile=128, key_tile=128)
gain = flashattention_memory_reduction_factor(
    sequence_length=4096,
    query_tile=128,
    key_tile=128,
    bytes_per_score=2,
    heads=32,
)
```

## Function

```python
def attention_score_matrix_bytes(
    sequence_length: int,
    bytes_per_score: int = 2,
    batch_size: int = 1,
    heads: int = 1,
) -> int:
def attention_tile_bytes(
    query_tile: int,
    key_tile: int,
    bytes_per_score: int = 2,
    batch_size: int = 1,
    heads: int = 1,
) -> int:
def attention_tile_rounds(sequence_length: int, query_tile: int, key_tile: int) -> int:
def flashattention_memory_reduction_factor(
    sequence_length: int,
    query_tile: int,
    key_tile: int,
    bytes_per_score: int = 2,
    batch_size: int = 1,
    heads: int = 1,
) -> float:
```

## When To Use What

- Use `attention_score_matrix_bytes` to see why standard attention becomes memory-heavy at long length.
- Use `attention_tile_bytes` to estimate the tiled working-set size instead.
- Use `attention_tile_rounds` when reasoning about scheduler pressure from longer sequences.
- Use `flashattention_memory_reduction_factor` when you want one number comparing full materialization with tiled scratch space.

## References

- Dao et al. (2022). [FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://arxiv.org/abs/2205.14135)
- Dao (2023). [FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning](https://arxiv.org/abs/2307.08691)

## Run tests

```bash
pytest modules/ml/llm/flashattention-and-io-aware-attention/python -q
```
