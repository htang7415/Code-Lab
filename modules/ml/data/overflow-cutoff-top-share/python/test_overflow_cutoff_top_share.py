from __future__ import annotations

import pytest

from overflow_cutoff_top_share import overflow_cutoff_top_share


def test_overflow_cutoff_top_share_returns_share_of_largest_qualifying_case() -> None:
    lengths = [120, 140, 160, 200]

    assert overflow_cutoff_top_share(lengths, max_length=100, cutoff=20) == pytest.approx(100 / 220)


def test_overflow_cutoff_top_share_returns_zero_when_nothing_qualifies() -> None:
    assert overflow_cutoff_top_share([105, 110], max_length=100, cutoff=20) == 0.0


def test_overflow_cutoff_top_share_rejects_negative_lengths() -> None:
    with pytest.raises(ValueError, match="lengths"):
        overflow_cutoff_top_share([120, -1], max_length=100, cutoff=20)
