import pytest

from tail_latency_budget import tail_latency_budget_status


def test_tail_latency_budget_reports_usage_and_remaining_fraction() -> None:
    usage, remaining = tail_latency_budget_status(observed_tail_ms=180.0, budget_ms=200.0)

    assert usage == pytest.approx(0.9)
    assert remaining == pytest.approx(0.1)


def test_tail_latency_budget_clamps_remaining_fraction_at_zero_when_over_budget() -> None:
    usage, remaining = tail_latency_budget_status(observed_tail_ms=250.0, budget_ms=200.0)

    assert usage == pytest.approx(1.25)
    assert remaining == pytest.approx(0.0)


def test_tail_latency_budget_requires_positive_budget() -> None:
    with pytest.raises(ValueError, match="positive"):
        tail_latency_budget_status(observed_tail_ms=10.0, budget_ms=0.0)
