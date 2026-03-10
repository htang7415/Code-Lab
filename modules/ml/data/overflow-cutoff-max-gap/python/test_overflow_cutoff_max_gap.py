from __future__ import annotations

import pytest

from overflow_cutoff_max_gap import overflow_cutoff_max_gap


def test_overflow_cutoff_max_gap_returns_gap_between_top_two_qualifying_overflow_values() -> None:
    value = overflow_cutoff_max_gap([64, 120, 130, 200], max_length=100, cutoff=20)

    assert value == pytest.approx(70.0)


def test_overflow_cutoff_max_gap_returns_zero_when_fewer_than_two_cases_qualify() -> None:
    assert overflow_cutoff_max_gap([64, 120, 111], max_length=100, cutoff=20) == 0.0


def test_overflow_cutoff_max_gap_rejects_negative_lengths() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        overflow_cutoff_max_gap([64, -1], max_length=100, cutoff=20)
