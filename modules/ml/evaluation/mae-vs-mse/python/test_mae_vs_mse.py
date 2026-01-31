from mae_vs_mse import mae_mse


def test_mae_mse():
    mae, mse = mae_mse([1.0, 2.0], [1.0, 3.0])
    assert mae == 0.5
    assert mse == 0.5
