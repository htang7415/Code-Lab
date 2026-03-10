from __future__ import annotations

import pytest

from breach_bucket_knee import breach_bucket_knee


def test_breach_bucket_knee_returns_bucket_with_largest_slope_change() -> None:
    bucket = breach_bucket_knee([1.01, 1.05, 1.08, 1.2, 1.5], capacity=1.0, cutoffs=[0.1, 0.3])

    assert bucket == 1


def test_breach_bucket_knee_returns_minus_one_when_no_breaches_exist() -> None:
    assert breach_bucket_knee([0.8, 0.9], capacity=1.0, cutoffs=[0.1, 0.3]) == -1


def test_breach_bucket_knee_rejects_unsorted_cutoffs() -> None:
    with pytest.raises(ValueError, match="cutoffs"):
        breach_bucket_knee([1.2], capacity=1.0, cutoffs=[0.3, 0.1])
