from expected_calibration_error import expected_calibration_error


def test_expected_calibration_error_two_bins():
    value = expected_calibration_error(
        confidences=[0.2, 0.4, 0.6, 0.8],
        predictions=[0, 0, 1, 1],
        labels=[0, 1, 1, 1],
        num_bins=2,
    )
    assert value == 0.25


def test_expected_calibration_error_empty_input():
    assert expected_calibration_error([], [], []) == 0.0
