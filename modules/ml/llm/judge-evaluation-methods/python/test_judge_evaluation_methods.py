import pytest

from judge_evaluation_methods import judge_agreement_matrix, judge_calibration_gap, pairwise_judge_rates


def test_pairwise_judge_rates_returns_win_loss_tie_fractions() -> None:
    win_rate, loss_rate, tie_rate = pairwise_judge_rates([1, 1, 0, -1])

    assert win_rate == 0.5
    assert loss_rate == 0.25
    assert tie_rate == 0.25


def test_pairwise_judge_rates_handles_empty_input() -> None:
    assert pairwise_judge_rates([]) == (0.0, 0.0, 0.0)


def test_pairwise_judge_rates_validates_outcome_values() -> None:
    with pytest.raises(ValueError, match="only -1, 0, or 1"):
        pairwise_judge_rates([2])


def test_judge_calibration_gap_is_small_for_well_aligned_confidences() -> None:
    gap = judge_calibration_gap(confidences=[0.9, 0.2, 0.8], correctness=[1, 0, 1])

    assert gap == pytest.approx((0.1 + 0.2 + 0.2) / 3.0)


def test_judge_calibration_gap_penalizes_overconfidence() -> None:
    gap = judge_calibration_gap(confidences=[0.95], correctness=[0])

    assert gap == pytest.approx(0.95)


def test_judge_calibration_gap_requires_binary_correctness() -> None:
    with pytest.raises(ValueError, match="binary"):
        judge_calibration_gap(confidences=[0.5], correctness=[2])


def test_judge_agreement_matrix_reports_pairwise_match_rates() -> None:
    matrix = judge_agreement_matrix(
        [
            [1, 1, 0, -1],
            [1, 0, 0, -1],
            [-1, -1, 0, 1],
        ]
    )

    assert matrix[0] == pytest.approx([1.0, 0.75, 0.25])
    assert matrix[1] == pytest.approx([0.75, 1.0, 0.25])
    assert matrix[2] == pytest.approx([0.25, 0.25, 1.0])


def test_judge_agreement_matrix_returns_empty_for_no_judges() -> None:
    assert judge_agreement_matrix([]) == []


def test_judge_agreement_matrix_requires_same_number_of_items() -> None:
    with pytest.raises(ValueError, match="same number of items"):
        judge_agreement_matrix([[1, 0], [1]])


def test_judge_agreement_matrix_requires_valid_decisions() -> None:
    with pytest.raises(ValueError, match="-1, 0, or 1"):
        judge_agreement_matrix([[2], [1]])
