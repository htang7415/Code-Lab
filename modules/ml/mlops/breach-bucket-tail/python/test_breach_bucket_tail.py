from __future__ import annotations

import pytest

from breach_bucket_tail import breach_bucket_tail


def test_breach_bucket_tail_returns_share_in_most_severe_bucket() -> None:
    tail = breach_bucket_tail([0.9, 1.05, 1.2, 1.5], capacity=1.0, cutoffs=[0.1, 0.3])

    assert tail == pytest.approx(1 / 3)


def test_breach_bucket_tail_can_sum_multiple_tail_buckets() -> None:
    tail = breach_bucket_tail([0.9, 1.05, 1.2, 1.5], capacity=1.0, cutoffs=[0.1, 0.3], tail_buckets=2)

    assert tail == pytest.approx(2 / 3)


def test_breach_bucket_tail_rejects_non_positive_tail_bucket_count() -> None:
    with pytest.raises(ValueError, match="positive"):
        breach_bucket_tail([1.2], capacity=1.0, cutoffs=[0.1], tail_buckets=0)
