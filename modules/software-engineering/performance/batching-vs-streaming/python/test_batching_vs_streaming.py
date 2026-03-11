from __future__ import annotations

import pytest

from batching_vs_streaming import batch_cost_per_item, preferred_delivery_mode, streaming_worth_it


def test_preferred_delivery_mode_depends_on_early_result_need() -> None:
    assert preferred_delivery_mode(needs_early_results=True, amortization_priority=False) == "streaming"
    assert preferred_delivery_mode(needs_early_results=False, amortization_priority=True) == "batching"


def test_batch_cost_per_item_amortizes_batch_latency() -> None:
    assert batch_cost_per_item(total_batch_ms=120, batch_size=6) == pytest.approx(20.0)


def test_streaming_worth_it_checks_time_to_first_result_against_total_completion() -> None:
    assert streaming_worth_it(time_to_first_result_ms=100, full_completion_ms=900) is True
    assert streaming_worth_it(time_to_first_result_ms=300, full_completion_ms=900) is False
