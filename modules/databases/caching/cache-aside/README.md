# Cache Aside

> Track: `databases` | Topic: `caching`

## Concept

Cache-aside reads from a fast cache first and only falls back to the database when the cached copy is missing or stale.

## Key Points

- A cache is a copy, so freshness rules matter as much as speed.
- Cache-aside keeps the source of truth in the database and treats the cache as an optimization layer.
- TTL limits staleness but does not guarantee correctness by itself.
- Explicit invalidation is often simpler than trying to update every cached copy perfectly.

## Minimal Code Mental Model

```python
cache = {}
value = read_through_cache(cache, "user:42", loader=load_user, now=100, ttl_seconds=30)
invalidate(cache, "user:42")
fresh_value = read_through_cache(cache, "user:42", loader=load_user, now=120, ttl_seconds=30)
```

## Function

```python
def read_through_cache(
    cache: dict[str, tuple[object, int | None]],
    key: str,
    loader: Callable[[], object],
    now: int,
    ttl_seconds: int | None = None,
) -> object:
def invalidate(cache: dict[str, tuple[object, int | None]], key: str) -> None:
```

## Run tests

```bash
pytest modules/databases/caching/cache-aside/python -q
```
