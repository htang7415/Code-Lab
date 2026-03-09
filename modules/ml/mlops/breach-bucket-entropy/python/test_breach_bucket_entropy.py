from __future__ import annotations

import math

import pytest

from breach_bucket_entropy import breach_bucket_entropy


def test_breach_bucket_entropy_matches_entropy_of_bucket_shares() -> None:
    entropy = breach_bucket_entropy([0.9, 1.05, 1.2, 1.5], capacity=1.0, cutoffs=[0.1, 0.3])

    assert entropy == pytest.approx(math.log(3.0))


def test_breach_bucket_entropy_returns_zero_when_nothing_breaches() -> None:
    assert breach_bucket_entropy([0.5, 0.8], capacity=1.0, cutoffs=[0.1, 0.3]) == 0.0


def test_breach_bucket_entropy_rejects_unsorted_cutoffs() -> None:
    with pytest.raises(ValueError, match="sorted"):
        breach_bucket_entropy([1.2], capacity=1.0, cutoffs=[0.3, 0.1])
