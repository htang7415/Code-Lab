import pytest

from breach_severity_index import breach_severity_index


def test_breach_severity_index_combines_breach_rate_and_excess_ratio() -> None:
    score = breach_severity_index([0.8, 1.0, 1.3, 0.9, 1.5], capacity=1.0)

    assert score == pytest.approx(0.4 * 1.4)


def test_breach_severity_index_returns_zero_when_nothing_breaches() -> None:
    assert breach_severity_index([0.5, 0.9], capacity=1.0) == pytest.approx(0.0)


def test_breach_severity_index_requires_positive_capacity() -> None:
    with pytest.raises(ValueError, match="positive"):
        breach_severity_index([1.0], capacity=0.0)
