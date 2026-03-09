import pytest

from judge_calibration import judge_calibration_gap


def test_judge_calibration_gap_is_small_for_well_aligned_confidences() -> None:
    gap = judge_calibration_gap(confidences=[0.9, 0.2, 0.8], correctness=[1, 0, 1])

    assert gap == pytest.approx((0.1 + 0.2 + 0.2) / 3.0)


def test_judge_calibration_gap_penalizes_overconfidence() -> None:
    gap = judge_calibration_gap(confidences=[0.95], correctness=[0])

    assert gap == pytest.approx(0.95)


def test_judge_calibration_gap_requires_binary_correctness() -> None:
    with pytest.raises(ValueError, match="binary"):
        judge_calibration_gap(confidences=[0.5], correctness=[2])
