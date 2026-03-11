# Caching And Semantic Caching

Caches reduce latency and cost by serving reused data from a faster copy.

## Purpose

Use this topic to learn classic cache patterns, invalidation trade-offs, and where AI-era semantic caching fits.

## First Principles

- A cache is a copy. The core problem is deciding when that copy is valid enough to trust.
- Read-mostly workloads benefit from cache-aside patterns. Write-heavy workloads often fail when caching is added naively.
- TTL is a freshness policy, not a correctness guarantee.
- Semantic caching helps with repeated LLM requests, but it does not replace authorization checks, grounding checks, or product-specific invalidation.

## Minimal Query Mental Model

```python
value = cache.get(key)
if value is None:
    value = load_from_database(key)
    cache.set(key, value, ttl=300)
return value
```

## Canonical Modules

- `cache-aside`
- `ttl-and-invalidation`
- `write-through-vs-write-behind`
- `client-side-caching`
- `hot-key-and-rate-limit-protection`
- `semantic-caching-basics`

## When To Use What

- Start with cache-aside and explicit invalidation rules.
- Use TTL when stale reads are acceptable for a bounded period.
- Use write-through or write-behind only when the operational trade-off is clear.
- Use semantic caching for repeated retrieval or model-answer patterns with stable permissions and bounded freshness needs.
