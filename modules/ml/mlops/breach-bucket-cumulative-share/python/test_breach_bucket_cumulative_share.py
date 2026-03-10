from __future__ import annotations

import pytest

from breach_bucket_cumulative_share import breach_bucket_cumulative_share


def test_breach_bucket_cumulative_share_returns_cumulative_bucket_shares() -> None:
    shares = breach_bucket_cumulative_share([0.9, 1.05, 1.2, 1.5], capacity=1.0, cutoffs=[0.1, 0.3])

    assert shares == pytest.approx([1 / 3, 2 / 3, 1.0])


def test_breach_bucket_cumulative_share_returns_zeros_when_nothing_breaches() -> None:
    assert breach_bucket_cumulative_share([0.5, 0.8], capacity=1.0, cutoffs=[0.1, 0.3]) == [0.0, 0.0, 0.0]


def test_breach_bucket_cumulative_share_rejects_unsorted_cutoffs() -> None:
    with pytest.raises(ValueError, match="sorted"):
        breach_bucket_cumulative_share([1.2], capacity=1.0, cutoffs=[0.3, 0.1])
