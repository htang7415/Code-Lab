from __future__ import annotations

import pytest

from overflow_cutoff_tail_variance import overflow_cutoff_tail_variance


def test_overflow_cutoff_tail_variance_returns_population_variance_of_tail() -> None:
    lengths = [120, 140, 160, 200]

    assert overflow_cutoff_tail_variance(lengths, max_length=100, cutoff=20, quantile=0.5) == pytest.approx(400.0)


def test_overflow_cutoff_tail_variance_returns_zero_when_tail_has_single_case() -> None:
    assert overflow_cutoff_tail_variance([120, 140], max_length=100, cutoff=20, quantile=0.95) == 0.0


def test_overflow_cutoff_tail_variance_rejects_invalid_quantile() -> None:
    with pytest.raises(ValueError, match="quantile"):
        overflow_cutoff_tail_variance([120], max_length=100, cutoff=20, quantile=-0.1)
