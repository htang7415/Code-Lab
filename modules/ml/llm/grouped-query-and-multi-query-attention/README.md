# Grouped-Query and Multi-Query Attention

> Track: `ml` | Topic: `llm`

## Purpose

Use this module to compare standard multi-head attention with grouped-query
attention (GQA) and multi-query attention (MQA) for faster decoding.

## First Principles

- Standard multi-head attention gives every query head its own key-value head.
- MQA shares one key-value head across all query heads.
- GQA is the middle ground: several query heads share each key-value head.
- The main gain is lower KV-cache size and lower memory-bandwidth cost during decoding.

## Core Math

Queries per key-value head:

$$
\mathrm{QPerKV} = \frac{H_q}{H_{kv}}
$$

KV-cache fraction relative to full multi-head attention:

$$
\mathrm{KVFraction} = \frac{H_{kv}}{H_q}
$$

KV-cache reduction:

$$
\mathrm{Reduction} = 1 - \frac{H_{kv}}{H_q}
$$

- $H_q$ -- number of query heads
- $H_{kv}$ -- number of key-value heads

## From Math To Code

- Start from the full number of query heads.
- Pick the number of key-value heads implied by the layout.
- Compute how many query heads share each key-value head.
- Translate that shared layout into a cache-size reduction ratio.

## Minimal Code Mental Model

```python
kv_mha = kv_heads_for_layout(num_query_heads=16, layout="mha")
kv_mqa = kv_heads_for_layout(num_query_heads=16, layout="mqa")
kv_gqa = kv_heads_for_layout(num_query_heads=16, layout="gqa", grouped_kv_heads=4)
shared = queries_per_kv_head(num_query_heads=16, num_kv_heads=4)
saved = kv_cache_reduction_ratio(num_query_heads=16, num_kv_heads=4)
```

## Function

```python
def kv_heads_for_layout(
    num_query_heads: int,
    layout: str,
    grouped_kv_heads: int | None = None,
) -> int:
def queries_per_kv_head(num_query_heads: int, num_kv_heads: int) -> int:
def kv_cache_fraction(num_query_heads: int, num_kv_heads: int) -> float:
def kv_cache_reduction_ratio(num_query_heads: int, num_kv_heads: int) -> float:
```

## When To Use What

- Use `kv_heads_for_layout` to compare MHA, MQA, and GQA as architecture choices.
- Use `queries_per_kv_head` when you want to see how much sharing each KV head carries.
- Use `kv_cache_fraction` and `kv_cache_reduction_ratio` when the main question is inference memory or bandwidth.

## References

- Shazeer (2019). [Fast Transformer Decoding: One Write-Head is All You Need](https://arxiv.org/abs/1911.02150)
- Ainslie et al. (2023). [GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints](https://arxiv.org/abs/2305.13245)

## Run tests

```bash
pytest modules/ml/llm/grouped-query-and-multi-query-attention/python -q
```
