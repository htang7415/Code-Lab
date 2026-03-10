from __future__ import annotations

import pytest

from overflow_cutoff_iqr import overflow_cutoff_iqr


def test_overflow_cutoff_iqr_returns_interquartile_range_of_qualifying_overflow() -> None:
    value = overflow_cutoff_iqr([64, 120, 130, 200], max_length=100, cutoff=20)

    assert value == pytest.approx(40.0)


def test_overflow_cutoff_iqr_returns_zero_when_fewer_than_two_cases_qualify() -> None:
    assert overflow_cutoff_iqr([64, 120, 111], max_length=100, cutoff=20) == 0.0


def test_overflow_cutoff_iqr_rejects_negative_lengths() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        overflow_cutoff_iqr([64, -1], max_length=100, cutoff=20)
