from __future__ import annotations

import pytest

from overflow_cutoff_tail_gini import overflow_cutoff_tail_gini


def test_overflow_cutoff_tail_gini_returns_gini_for_upper_tail() -> None:
    lengths = [120, 140, 160, 200]

    assert overflow_cutoff_tail_gini(lengths, max_length=100, cutoff=20, quantile=0.25) == pytest.approx(0.2)


def test_overflow_cutoff_tail_gini_returns_zero_when_tail_has_single_case() -> None:
    assert overflow_cutoff_tail_gini([120, 140], max_length=100, cutoff=20, quantile=0.95) == 0.0


def test_overflow_cutoff_tail_gini_rejects_invalid_quantile() -> None:
    with pytest.raises(ValueError, match="quantile"):
        overflow_cutoff_tail_gini([120], max_length=100, cutoff=20, quantile=-0.1)
