# Cache Consistency Patterns

> Track: `databases` | Topic: `caching`

## Concept

Caches are fast because they are copies. Consistency patterns define how the copy stays aligned with the source of truth.

## Key Points

- Cache-aside fills the cache on demand but can go stale if writes skip invalidation.
- Write-through updates the source and cache together for tighter freshness.
- Invalidate-on-write drops the cache entry so the next read repopulates from the source.
- The safest pattern depends on whether read freshness or write simplicity is more important.

## Minimal Code Mental Model

```python
store = {"doc:1": "old"}
cache = {}
cache_aside_read(store, cache, "doc:1")
invalidate_on_write_update(store, cache, "doc:1", "new")
fresh = cache_aside_read(store, cache, "doc:1")
```

## Function

```python
def cache_aside_read(
    store: dict[str, str],
    cache: dict[str, str],
    key: str,
) -> str | None:
def write_through_update(
    store: dict[str, str],
    cache: dict[str, str],
    key: str,
    value: str,
) -> None:
def invalidate_on_write_update(
    store: dict[str, str],
    cache: dict[str, str],
    key: str,
    value: str,
) -> None:
def stale_cache_keys(
    store: dict[str, str],
    cache: dict[str, str],
) -> list[str]:
```

## Run tests

```bash
pytest modules/databases/caching/cache-consistency-patterns/python -q
```
