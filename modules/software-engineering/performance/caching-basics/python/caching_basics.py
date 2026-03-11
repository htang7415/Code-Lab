from __future__ import annotations


def should_cache(read_frequency: int, mutation_frequency: int, freshness_tolerance_s: int) -> bool:
    if read_frequency < 0 or mutation_frequency < 0 or freshness_tolerance_s < 0:
        raise ValueError("inputs must be non-negative")
    if read_frequency == 0:
        return False
    return read_frequency >= max(1, mutation_frequency * 10) and freshness_tolerance_s > 0


def cache_hit_rate(hits: int, lookups: int) -> float:
    if hits < 0 or lookups <= 0 or hits > lookups:
        raise ValueError("hits must be between 0 and lookups, and lookups must be positive")
    return hits / lookups


def stale_risk(mutation_frequency: int, freshness_tolerance_s: int) -> str:
    if mutation_frequency < 0 or freshness_tolerance_s < 0:
        raise ValueError("inputs must be non-negative")
    if freshness_tolerance_s == 0:
        return "high"
    if mutation_frequency == 0:
        return "low"
    if mutation_frequency * freshness_tolerance_s >= 100:
        return "high"
    if mutation_frequency * freshness_tolerance_s >= 20:
        return "medium"
    return "low"
