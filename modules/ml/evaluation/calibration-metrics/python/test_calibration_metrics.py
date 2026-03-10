import pytest

from calibration_metrics import brier_score, expected_calibration_error, isotonic_calibration


def test_expected_calibration_error_is_zero_for_perfectly_calibrated_points() -> None:
    ece = expected_calibration_error(
        confidences=[1.0, 1.0, 1.0, 1.0],
        predictions=[1, 0, 1, 0],
        labels=[1, 0, 1, 0],
        num_bins=2,
    )
    assert ece == pytest.approx(0.0)


def test_brier_score_matches_mean_squared_probability_error() -> None:
    assert brier_score([1, 0], [0.8, 0.3]) == pytest.approx(((0.8 - 1.0) ** 2 + (0.3 - 0.0) ** 2) / 2.0)


def test_isotonic_calibration_returns_monotone_outputs_in_sorted_score_order() -> None:
    scores = [0.8, 0.1, 0.4, 0.2]
    labels = [0, 0, 1, 1]

    calibrated = isotonic_calibration(scores, labels)
    sorted_pairs = sorted(zip(scores, calibrated), key=lambda pair: pair[0])
    sorted_outputs = [value for _, value in sorted_pairs]

    assert sorted_outputs == sorted(sorted_outputs)


def test_invalid_inputs_raise() -> None:
    with pytest.raises(ValueError, match="same length"):
        expected_calibration_error([0.5], [1], [])

    with pytest.raises(ValueError, match="binary"):
        brier_score([2], [0.5])

    with pytest.raises(ValueError, match="binary"):
        isotonic_calibration([0.1], [3])
