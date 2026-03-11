# Cache TTL Jitter

> Track: `databases` | Topic: `caching`

## Concept

TTL jitter spreads expirations so many keys do not all expire at the same second and stampede the origin together.

## Key Points

- Fixed TTLs can synchronize expirations across large key sets.
- Jitter adds a small deterministic or random offset around the base TTL.
- The goal is to spread expiration times, not to make caching unpredictable.
- Jitter works especially well on hot fleets of similar keys.
- The base TTL should stay positive; negative TTLs turn jitter into already-expired noise.

## Minimal Code Mental Model

```python
keys = ["k1", "k2", "k3", "k4"]
expirations = jittered_expirations(keys, now=100, base_ttl=60, jitter_ratio=0.2)
buckets = expiration_bucket_counts(expirations)
```

## Function

```python
def validate_base_ttl(base_ttl: int) -> None:
def stable_jitter_seconds(key: str, base_ttl: int, jitter_ratio: float) -> int:
def expiration_time(
    key: str,
    now: int,
    base_ttl: int,
    jitter_ratio: float,
) -> int:
def jittered_expirations(
    keys: list[str],
    now: int,
    base_ttl: int,
    jitter_ratio: float,
) -> dict[str, int]:
def expiration_bucket_counts(expirations: dict[str, int]) -> dict[int, int]:
def max_bucket_load(expirations: dict[str, int]) -> int:
```

## Run tests

```bash
pytest modules/databases/caching/cache-ttl-jitter/python -q
```
