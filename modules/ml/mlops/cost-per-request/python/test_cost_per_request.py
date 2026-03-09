import pytest

from cost_per_request import cost_per_request


def test_cost_per_request_divides_total_cost_by_request_count() -> None:
    assert cost_per_request(total_cost=12.5, request_count=50) == pytest.approx(0.25)


def test_cost_per_request_can_be_zero() -> None:
    assert cost_per_request(total_cost=0.0, request_count=10) == pytest.approx(0.0)


def test_cost_per_request_requires_positive_request_count() -> None:
    with pytest.raises(ValueError, match="positive"):
        cost_per_request(total_cost=1.0, request_count=0)
