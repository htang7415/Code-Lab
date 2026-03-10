from __future__ import annotations

import pytest

from overflow_cutoff_upper_tail import overflow_cutoff_upper_tail


def test_overflow_cutoff_upper_tail_returns_high_quantile_for_qualifying_overflow() -> None:
    lengths = [120, 130, 160, 200]

    assert overflow_cutoff_upper_tail(lengths, max_length=100, cutoff=20, quantile=0.75) == pytest.approx(70.0)


def test_overflow_cutoff_upper_tail_returns_zero_when_nothing_qualifies() -> None:
    assert overflow_cutoff_upper_tail([105, 110], max_length=100, cutoff=20) == 0.0


def test_overflow_cutoff_upper_tail_rejects_invalid_quantile() -> None:
    with pytest.raises(ValueError, match="quantile"):
        overflow_cutoff_upper_tail([120], max_length=100, cutoff=20, quantile=1.2)
