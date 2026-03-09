import pytest

from bootstrap_intervals import bootstrap_percentile_interval


def test_bootstrap_percentile_interval_matches_interpolated_percentiles() -> None:
    lower, upper = bootstrap_percentile_interval([1.0, 2.0, 3.0, 4.0, 5.0], alpha=0.2)

    assert lower == pytest.approx(1.4)
    assert upper == pytest.approx(4.6)


def test_bootstrap_percentile_interval_handles_sorted_or_unsorted_inputs() -> None:
    lower, upper = bootstrap_percentile_interval([3.0, 1.0, 2.0], alpha=0.5)

    assert lower == pytest.approx(1.5)
    assert upper == pytest.approx(2.5)


def test_bootstrap_percentile_interval_requires_multiple_values() -> None:
    with pytest.raises(ValueError, match="at least two"):
        bootstrap_percentile_interval([1.0])
