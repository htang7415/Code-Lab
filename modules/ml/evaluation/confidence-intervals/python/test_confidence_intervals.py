import pytest

from confidence_intervals import mean_confidence_interval


def test_mean_confidence_interval_matches_normal_approximation() -> None:
    lower, upper = mean_confidence_interval([1.0, 2.0, 3.0, 4.0])

    assert lower == pytest.approx(1.2348254402389105)
    assert upper == pytest.approx(3.7651745597610895)


def test_mean_confidence_interval_collapses_for_constant_samples() -> None:
    lower, upper = mean_confidence_interval([5.0, 5.0, 5.0], z=1.0)

    assert lower == 5.0
    assert upper == 5.0


def test_mean_confidence_interval_requires_two_samples() -> None:
    with pytest.raises(ValueError, match="at least two"):
        mean_confidence_interval([1.0])
