from __future__ import annotations

import math

import pytest

from breach_bucket_step_function import breach_bucket_step_function


def test_breach_bucket_step_function_returns_right_continuous_curve() -> None:
    curve = breach_bucket_step_function([0.9, 1.05, 1.2, 1.5], capacity=1.0, cutoffs=[0.1, 0.3])

    assert curve[0] == (0.0, 0.0)
    assert curve[1][0] == pytest.approx(0.1)
    assert curve[1][1] == pytest.approx(1 / 3)
    assert curve[2][0] == pytest.approx(0.3)
    assert curve[2][1] == pytest.approx(2 / 3)
    assert math.isinf(curve[3][0])
    assert curve[3][1] == 1.0


def test_breach_bucket_step_function_returns_zero_curve_when_no_breach_occurs() -> None:
    curve = breach_bucket_step_function([0.5, 0.8], capacity=1.0, cutoffs=[0.1])

    assert curve == [(0.0, 0.0), (0.1, 0.0), (float("inf"), 0.0)]


def test_breach_bucket_step_function_rejects_unsorted_cutoffs() -> None:
    with pytest.raises(ValueError, match="cutoffs"):
        breach_bucket_step_function([1.2], capacity=1.0, cutoffs=[0.3, 0.1])
