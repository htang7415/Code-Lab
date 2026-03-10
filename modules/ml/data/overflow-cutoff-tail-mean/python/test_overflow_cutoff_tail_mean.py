from __future__ import annotations

import pytest

from overflow_cutoff_tail_mean import overflow_cutoff_tail_mean


def test_overflow_cutoff_tail_mean_returns_mean_of_upper_tail() -> None:
    lengths = [120, 140, 160, 200]

    assert overflow_cutoff_tail_mean(lengths, max_length=100, cutoff=20, quantile=0.5) == pytest.approx(80.0)


def test_overflow_cutoff_tail_mean_returns_zero_when_nothing_qualifies() -> None:
    assert overflow_cutoff_tail_mean([105, 110], max_length=100, cutoff=20) == 0.0


def test_overflow_cutoff_tail_mean_rejects_invalid_quantile() -> None:
    with pytest.raises(ValueError, match="quantile"):
        overflow_cutoff_tail_mean([120], max_length=100, cutoff=20, quantile=1.2)
