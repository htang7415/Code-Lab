import pytest

from capacity_headroom import capacity_headroom


def test_capacity_headroom_reports_utilization_and_remaining_fraction() -> None:
    utilization, headroom = capacity_headroom(current_load=75.0, max_capacity=100.0)

    assert utilization == pytest.approx(0.75)
    assert headroom == pytest.approx(0.25)


def test_capacity_headroom_clamps_headroom_at_zero_when_over_capacity() -> None:
    utilization, headroom = capacity_headroom(current_load=120.0, max_capacity=100.0)

    assert utilization == pytest.approx(1.2)
    assert headroom == pytest.approx(0.0)


def test_capacity_headroom_requires_positive_capacity() -> None:
    with pytest.raises(ValueError, match="positive"):
        capacity_headroom(current_load=10.0, max_capacity=0.0)
