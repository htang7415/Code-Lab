from __future__ import annotations

import pytest

from overflow_cutoff_count import overflow_cutoff_count


def test_overflow_cutoff_count_counts_examples_at_or_above_cutoff() -> None:
    count = overflow_cutoff_count([64, 120, 111, 200], max_length=100, cutoff=20)

    assert count == 2


def test_overflow_cutoff_count_returns_zero_for_empty_input() -> None:
    assert overflow_cutoff_count([], max_length=100, cutoff=20) == 0


def test_overflow_cutoff_count_rejects_negative_lengths() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        overflow_cutoff_count([64, -1], max_length=100, cutoff=20)
