from __future__ import annotations

import pytest

from breach_bucket_quantile import breach_bucket_quantile


def test_breach_bucket_quantile_returns_bucket_at_target_quantile() -> None:
    bucket = breach_bucket_quantile([0.9, 1.05, 1.2, 1.5], capacity=1.0, cutoffs=[0.1, 0.3], quantile=0.5)

    assert bucket == 1


def test_breach_bucket_quantile_returns_minus_one_when_nothing_breaches() -> None:
    assert breach_bucket_quantile([0.5, 0.8], capacity=1.0, cutoffs=[0.1, 0.3], quantile=0.5) == -1


def test_breach_bucket_quantile_rejects_invalid_quantile() -> None:
    with pytest.raises(ValueError, match="quantile"):
        breach_bucket_quantile([1.2], capacity=1.0, cutoffs=[0.1], quantile=0.0)
