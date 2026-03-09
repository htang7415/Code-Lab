from __future__ import annotations

import pytest

from overflow_cutoff_mean import overflow_cutoff_mean


def test_overflow_cutoff_mean_averages_only_qualifying_overflow() -> None:
    value = overflow_cutoff_mean([64, 120, 111, 200], max_length=100, cutoff=20)

    assert value == pytest.approx(60.0)


def test_overflow_cutoff_mean_returns_zero_when_no_case_reaches_cutoff() -> None:
    assert overflow_cutoff_mean([64, 105, 111], max_length=100, cutoff=20) == 0.0


def test_overflow_cutoff_mean_rejects_negative_lengths() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        overflow_cutoff_mean([64, -1], max_length=100, cutoff=20)
