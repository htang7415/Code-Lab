from zero_gradients import zero_grad


def test_zero_grad():
    assert zero_grad([1.0, -1.0]) == [0.0, 0.0]
