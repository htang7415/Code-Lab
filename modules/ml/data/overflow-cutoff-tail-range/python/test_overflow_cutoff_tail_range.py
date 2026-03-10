from __future__ import annotations

import pytest

from overflow_cutoff_tail_range import overflow_cutoff_tail_range


def test_overflow_cutoff_tail_range_returns_range_of_tail_values() -> None:
    lengths = [120, 140, 160, 200]

    assert overflow_cutoff_tail_range(lengths, max_length=100, cutoff=20, quantile=0.5) == pytest.approx(40.0)


def test_overflow_cutoff_tail_range_returns_zero_when_tail_has_single_case() -> None:
    assert overflow_cutoff_tail_range([120, 140], max_length=100, cutoff=20, quantile=0.95) == 0.0


def test_overflow_cutoff_tail_range_rejects_invalid_quantile() -> None:
    with pytest.raises(ValueError, match="quantile"):
        overflow_cutoff_tail_range([120], max_length=100, cutoff=20, quantile=1.1)
