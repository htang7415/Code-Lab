import pytest

from batching_and_n_plus_one_query_costs import (
    batched_query_count,
    n_plus_one_query_count,
    query_cost_summary,
)


def test_batching_collapses_many_child_queries_into_few_round_trips():
    summary = query_cost_summary(parent_count=20, batch_size=20, round_trip_ms=15)

    assert n_plus_one_query_count(20) == 21
    assert batched_query_count(20, 20) == 2
    assert summary["batched_latency_ms"] < summary["n_plus_one_latency_ms"]
    assert summary["saved_round_trips"] == 19


def test_small_batches_still_help_and_invalid_batch_size_raises():
    assert batched_query_count(20, 5) == 5

    with pytest.raises(ValueError):
        batched_query_count(20, 0)
