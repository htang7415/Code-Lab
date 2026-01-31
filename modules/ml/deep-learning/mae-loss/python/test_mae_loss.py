from mae_loss import mae


def test_mae():
    assert mae([1.0, 2.0], [1.0, 3.0]) == 0.5
