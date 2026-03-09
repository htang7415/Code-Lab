from __future__ import annotations

import pytest

from overflow_cutoff_rate import overflow_cutoff_rate


def test_overflow_cutoff_rate_counts_examples_at_or_above_cutoff() -> None:
    rate = overflow_cutoff_rate([64, 120, 111, 200], max_length=100, cutoff=20)

    assert rate == pytest.approx(0.5)


def test_overflow_cutoff_rate_returns_zero_for_empty_input() -> None:
    assert overflow_cutoff_rate([], max_length=100, cutoff=20) == 0.0


def test_overflow_cutoff_rate_rejects_negative_lengths() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        overflow_cutoff_rate([64, -1], max_length=100, cutoff=20)
