# TTL And Invalidation

> Track: `databases` | Topic: `caching`

## Concept

TTL bounds staleness by time, while invalidation removes cached entries when the underlying data changes.

## Key Points

- TTL is simple, but it allows stale reads until expiration.
- Invalidation reacts faster to writes, but it needs dependency tracking.
- Tag-based invalidation is useful when one write affects many cached keys.
- Good cache design uses both time-based and write-based freshness controls.

## Minimal Code Mental Model

```python
cache = {}
set_cache_entry(cache, "doc:1", {"title": "Spec"}, now=100, ttl_seconds=30, tags={"workspace:7"})
value = get_if_fresh(cache, "doc:1", now=110)
invalidate_tag(cache, "workspace:7")
```

## Function

```python
def set_cache_entry(
    cache: dict[str, dict[str, object]],
    key: str,
    value: object,
    now: int,
    ttl_seconds: int,
    tags: set[str] | None = None,
) -> None:
def get_if_fresh(
    cache: dict[str, dict[str, object]],
    key: str,
    now: int,
) -> object | None:
def invalidate_key(cache: dict[str, dict[str, object]], key: str) -> None:
def invalidate_tag(cache: dict[str, dict[str, object]], tag: str) -> None:
def stale_keys(cache: dict[str, dict[str, object]], now: int) -> list[str]:
```

## Run tests

```bash
pytest modules/databases/caching/ttl-and-invalidation/python -q
```
