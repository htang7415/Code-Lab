# Prefix Cache Savings

> Track: `ml` | Topic: `systems`

## Concept

Prefix caching is only useful when it saves meaningful prefill work across a workload.
This module turns per-request prefix hit lengths into aggregate saved-token metrics.

## Math

$$T_{\mathrm{saved}} = \sum_i h_i$$

$$r_{\mathrm{saved}} = \frac{T_{\mathrm{saved}}}{\sum_i L_i}$$

- $L_i$ -- prompt length for request $i$
- $h_i$ -- cached prefix hit length for request $i$
- $T_{\mathrm{saved}}$ -- total prefill tokens skipped by cache hits
- $r_{\mathrm{saved}}$ -- fraction of prompt tokens saved across the workload

## Key Points

- Hit length matters more than hit count.
- Saved-token fraction is a better first-order serving metric than a raw cache-hit boolean.
- This metric only captures prefill savings, not decode latency or cache lookup overhead.

## Function

```python
def prefix_cache_savings(
    prompt_lengths: list[int],
    hit_lengths: list[int],
) -> tuple[int, float]:
```

## Run tests

```bash
pytest modules/ml/systems/prefix-cache-metrics/python -q
```
