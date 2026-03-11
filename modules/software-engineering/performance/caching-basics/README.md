# Caching Basics

> Track: `software-engineering` | Topic: `performance`

## Concept

Caching is useful when repeated reads are common and the system can tolerate some freshness lag without violating correctness.

## Key Points

- A cache is only as good as its invalidation and freshness rules.
- High mutation rates increase stale-data risk.
- Hit rate is the main signal for whether the cache is paying for itself.

## Minimal Code Mental Model

```python
worth_it = should_cache(read_frequency=1000, mutation_frequency=5, freshness_tolerance_s=60)
hit_rate = cache_hit_rate(hits=900, lookups=1000)
risk = stale_risk(mutation_frequency=20, freshness_tolerance_s=5)
```

## Function

```python
def should_cache(read_frequency: int, mutation_frequency: int, freshness_tolerance_s: int) -> bool:
def cache_hit_rate(hits: int, lookups: int) -> float:
def stale_risk(mutation_frequency: int, freshness_tolerance_s: int) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/performance/caching-basics/python -q
```
