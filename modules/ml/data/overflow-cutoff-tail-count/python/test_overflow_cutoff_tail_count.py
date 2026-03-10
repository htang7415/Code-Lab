from __future__ import annotations

import pytest

from overflow_cutoff_tail_count import overflow_cutoff_tail_count


def test_overflow_cutoff_tail_count_counts_cases_in_upper_tail() -> None:
    lengths = [120, 140, 160, 200]

    assert overflow_cutoff_tail_count(lengths, max_length=100, cutoff=20, quantile=0.5) == 2


def test_overflow_cutoff_tail_count_returns_zero_when_nothing_qualifies() -> None:
    assert overflow_cutoff_tail_count([105, 110], max_length=100, cutoff=20) == 0


def test_overflow_cutoff_tail_count_rejects_invalid_quantile() -> None:
    with pytest.raises(ValueError, match="quantile"):
        overflow_cutoff_tail_count([120], max_length=100, cutoff=20, quantile=-0.1)
