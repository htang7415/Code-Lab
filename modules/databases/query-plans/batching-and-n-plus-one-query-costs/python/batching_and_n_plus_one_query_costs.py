"""batching_and_n_plus_one_query_costs - compare one-query-per-parent with batched fetches."""

from __future__ import annotations

import math


def n_plus_one_query_count(parent_count: int) -> int:
    return 1 + max(parent_count, 0)


def batched_query_count(parent_count: int, batch_size: int) -> int:
    if batch_size <= 0:
        raise ValueError("batch_size must be positive")
    if parent_count <= 0:
        return 1
    return 1 + math.ceil(parent_count / batch_size)


def total_round_trip_ms(query_count: int, round_trip_ms: int) -> int:
    return max(query_count, 0) * max(round_trip_ms, 0)


def query_cost_summary(
    parent_count: int,
    batch_size: int,
    round_trip_ms: int,
) -> dict[str, int]:
    n_plus_one = n_plus_one_query_count(parent_count)
    batched = batched_query_count(parent_count, batch_size)
    return {
        "n_plus_one_queries": n_plus_one,
        "batched_queries": batched,
        "n_plus_one_latency_ms": total_round_trip_ms(n_plus_one, round_trip_ms),
        "batched_latency_ms": total_round_trip_ms(batched, round_trip_ms),
        "saved_round_trips": max(n_plus_one - batched, 0),
    }
