from __future__ import annotations

import pytest

from overflow_cutoff_skew import overflow_cutoff_skew


def test_overflow_cutoff_skew_returns_population_skew_for_qualifying_overflow() -> None:
    lengths = [120, 120, 140, 180]

    assert overflow_cutoff_skew(lengths, max_length=100, cutoff=20) == pytest.approx(0.81649658)


def test_overflow_cutoff_skew_returns_zero_when_qualifying_overflow_has_no_variation() -> None:
    assert overflow_cutoff_skew([120, 120, 120], max_length=100, cutoff=20) == 0.0


def test_overflow_cutoff_skew_rejects_negative_lengths() -> None:
    with pytest.raises(ValueError, match="lengths"):
        overflow_cutoff_skew([120, -1], max_length=100, cutoff=20)
