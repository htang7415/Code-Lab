from __future__ import annotations

import pytest

from breach_bucket_step_area import breach_bucket_step_area


def test_breach_bucket_step_area_returns_discrete_area_under_cumulative_curve() -> None:
    value = breach_bucket_step_area([1.05, 1.15, 1.2, 1.25, 1.5], capacity=1.0, cutoffs=[0.1, 0.3])

    assert value == pytest.approx(2.0)


def test_breach_bucket_step_area_returns_zero_when_no_breaches_exist() -> None:
    assert breach_bucket_step_area([0.8, 0.9], capacity=1.0, cutoffs=[0.1, 0.3]) == 0.0


def test_breach_bucket_step_area_rejects_unsorted_cutoffs() -> None:
    with pytest.raises(ValueError, match="cutoffs"):
        breach_bucket_step_area([1.2], capacity=1.0, cutoffs=[0.3, 0.1])
