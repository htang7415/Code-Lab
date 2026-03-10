from __future__ import annotations

import pytest

from overflow_cutoff_range import overflow_cutoff_range


def test_overflow_cutoff_range_returns_span_of_qualifying_overflow() -> None:
    value = overflow_cutoff_range([64, 120, 130, 200], max_length=100, cutoff=20)

    assert value == pytest.approx(80.0)


def test_overflow_cutoff_range_returns_zero_when_fewer_than_two_cases_qualify() -> None:
    assert overflow_cutoff_range([64, 120, 111], max_length=100, cutoff=20) == 0.0


def test_overflow_cutoff_range_rejects_negative_lengths() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        overflow_cutoff_range([64, -1], max_length=100, cutoff=20)
