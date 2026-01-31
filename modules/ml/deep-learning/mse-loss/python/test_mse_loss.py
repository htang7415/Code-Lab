from mse_loss import mse


def test_mse():
    assert mse([1.0, 2.0], [1.0, 3.0]) == 0.5
