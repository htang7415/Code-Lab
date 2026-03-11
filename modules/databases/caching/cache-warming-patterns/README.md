# Cache Warming Patterns

> Track: `databases` | Topic: `caching`

## Concept

Cache warming fills likely-hot keys before the first user request so the system avoids predictable cold misses.

## Key Points

- Warming is useful when the hot set is predictable.
- The goal is to reduce origin reads on the first request burst.
- Warming only helps if the warmed keys actually get requested soon after.
- The hot-key selection logic matters as much as the preload step.
- `top_n` and access counts should stay non-negative; negative values are input bugs, not cache signals.

## Minimal Code Mental Model

```python
warm_keys = recommend_warm_keys({"doc:1": 100, "doc:2": 20, "doc:3": 5}, top_n=2)
cache = {}
warm_cache(store, cache, warm_keys)
responses, origin_reads = serve_requests(store, cache, ["doc:1", "doc:1", "doc:2"])
```

## Function

```python
def validate_top_n(top_n: int) -> None:
def recommend_warm_keys(access_counts: dict[str, int], top_n: int) -> list[str]:
def warm_cache(
    store: dict[str, str],
    cache: dict[str, str],
    keys: list[str],
) -> list[str]:
def serve_requests(
    store: dict[str, str],
    cache: dict[str, str],
    requests: list[str],
) -> tuple[list[str | None], int]:
```

## Run tests

```bash
pytest modules/databases/caching/cache-warming-patterns/python -q
```
