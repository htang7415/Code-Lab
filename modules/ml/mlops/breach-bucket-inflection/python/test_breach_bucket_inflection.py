from __future__ import annotations

import pytest

from breach_bucket_inflection import breach_bucket_inflection


def test_breach_bucket_inflection_returns_bucket_with_largest_second_difference() -> None:
    bucket = breach_bucket_inflection([1.05, 1.15, 1.2, 1.25, 1.5], capacity=1.0, cutoffs=[0.1, 0.3])

    assert bucket == 1


def test_breach_bucket_inflection_returns_minus_one_when_no_breaches_exist() -> None:
    assert breach_bucket_inflection([0.8, 0.9], capacity=1.0, cutoffs=[0.1, 0.3]) == -1


def test_breach_bucket_inflection_rejects_unsorted_cutoffs() -> None:
    with pytest.raises(ValueError, match="cutoffs"):
        breach_bucket_inflection([1.2], capacity=1.0, cutoffs=[0.3, 0.1])
