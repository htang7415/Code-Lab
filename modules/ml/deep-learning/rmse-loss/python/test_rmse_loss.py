from rmse_loss import rmse


def test_rmse():
    assert abs(rmse([1.0, 2.0], [1.0, 3.0]) - (0.5 ** 0.5)) < 1e-6
