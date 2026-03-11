"""cache_warming_patterns - prefill likely hot keys to avoid predictable cold misses."""

from __future__ import annotations


def recommend_warm_keys(access_counts: dict[str, int], top_n: int) -> list[str]:
    ranked = sorted(access_counts.items(), key=lambda item: (-int(item[1]), item[0]))
    return [key for key, _ in ranked[:max(top_n, 0)]]


def warm_cache(
    store: dict[str, str],
    cache: dict[str, str],
    keys: list[str],
) -> list[str]:
    warmed: list[str] = []
    for key in keys:
        if key in store:
            cache[key] = store[key]
            warmed.append(key)
    return warmed


def serve_requests(
    store: dict[str, str],
    cache: dict[str, str],
    requests: list[str],
) -> tuple[list[str | None], int]:
    responses: list[str | None] = []
    origin_reads = 0
    for key in requests:
        if key in cache:
            responses.append(cache[key])
            continue
        value = store.get(key)
        if value is not None:
            cache[key] = value
            origin_reads += 1
        responses.append(value)
    return responses, origin_reads
