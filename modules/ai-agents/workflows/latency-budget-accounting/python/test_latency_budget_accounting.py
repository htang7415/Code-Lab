from __future__ import annotations

import pytest

from latency_budget_accounting import (
    latency_budget_route,
    per_step_latency_budget,
    remaining_latency_budget,
)


def test_latency_budget_accounting_tracks_remaining_and_step_budget() -> None:
    remaining = remaining_latency_budget(
        total_budget_ms=1200,
        elapsed_ms=350,
        reserved_response_ms=200,
    )

    assert remaining == 650
    assert per_step_latency_budget(remaining, remaining_steps=2) == 325
    assert latency_budget_route(
        step_latency_ms=320,
        step_budget_ms=325,
        can_stream=True,
        can_fallback=True,
    ) == "continue"


def test_latency_budget_accounting_routes_overruns_to_stream_fallback_or_review() -> None:
    assert latency_budget_route(380, step_budget_ms=325, can_stream=True, can_fallback=True) == "stream"
    assert latency_budget_route(380, step_budget_ms=325, can_stream=False, can_fallback=True) == "fallback"
    assert latency_budget_route(380, step_budget_ms=325, can_stream=False, can_fallback=False) == "review"
    assert remaining_latency_budget(1000, elapsed_ms=950, reserved_response_ms=100) == 0


def test_latency_budget_accounting_validation() -> None:
    with pytest.raises(ValueError):
        remaining_latency_budget(total_budget_ms=500, elapsed_ms=-1)
    with pytest.raises(ValueError):
        remaining_latency_budget(total_budget_ms=500, elapsed_ms=0, reserved_response_ms=500)
    with pytest.raises(ValueError):
        per_step_latency_budget(remaining_budget_ms=100, remaining_steps=0)
    with pytest.raises(ValueError):
        latency_budget_route(step_latency_ms=10, step_budget_ms=0, can_stream=True, can_fallback=False)
