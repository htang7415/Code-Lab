from __future__ import annotations

import pytest

from overflow_cutoff_tail_skew import overflow_cutoff_tail_skew


def test_overflow_cutoff_tail_skew_returns_population_skew_for_tail_values() -> None:
    lengths = [120, 120, 140, 180]

    assert overflow_cutoff_tail_skew(lengths, max_length=100, cutoff=20, quantile=0.0) == pytest.approx(0.81649658)


def test_overflow_cutoff_tail_skew_returns_zero_when_tail_has_no_variation() -> None:
    assert overflow_cutoff_tail_skew([120, 120, 120], max_length=100, cutoff=20, quantile=0.0) == 0.0


def test_overflow_cutoff_tail_skew_rejects_invalid_quantile() -> None:
    with pytest.raises(ValueError, match="quantile"):
        overflow_cutoff_tail_skew([120], max_length=100, cutoff=20, quantile=1.1)
