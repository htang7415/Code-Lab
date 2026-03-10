from __future__ import annotations

import pytest

from breach_bucket_turning_point import breach_bucket_turning_point


def test_breach_bucket_turning_point_returns_local_peak_bucket() -> None:
    bucket = breach_bucket_turning_point([1.05, 1.15, 1.2, 1.25, 1.5], capacity=1.0, cutoffs=[0.1, 0.3])

    assert bucket == 1


def test_breach_bucket_turning_point_returns_minus_one_when_no_turn_exists() -> None:
    assert breach_bucket_turning_point([1.01, 1.05, 1.08, 1.2, 1.5], capacity=1.0, cutoffs=[0.1, 0.3]) == -1


def test_breach_bucket_turning_point_rejects_unsorted_cutoffs() -> None:
    with pytest.raises(ValueError, match="cutoffs"):
        breach_bucket_turning_point([1.2], capacity=1.0, cutoffs=[0.3, 0.1])
