import pytest

from queue_utilization import queue_utilization


def test_queue_utilization_reports_fraction_and_saturation_flag() -> None:
    utilization, saturated = queue_utilization(queue_depth=8, queue_capacity=10)

    assert utilization == pytest.approx(0.8)
    assert not saturated


def test_queue_utilization_marks_full_queue_as_saturated() -> None:
    utilization, saturated = queue_utilization(queue_depth=12, queue_capacity=10)

    assert utilization == pytest.approx(1.2)
    assert saturated


def test_queue_utilization_requires_positive_capacity() -> None:
    with pytest.raises(ValueError, match="positive"):
        queue_utilization(queue_depth=1, queue_capacity=0)
