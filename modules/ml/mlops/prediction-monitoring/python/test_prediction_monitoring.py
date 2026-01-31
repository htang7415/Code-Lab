from prediction_monitoring import mean_shift


def test_mean_shift():
    assert mean_shift([0.0, 0.0], [1.0, 1.0]) == 1.0
