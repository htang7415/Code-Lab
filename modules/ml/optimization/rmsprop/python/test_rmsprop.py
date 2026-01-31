from rmsprop import rmsprop_step


def test_rmsprop_step():
    w, v = rmsprop_step(1.0, 1.0, 0.0, 0.1, 0.9, 1e-8)
    assert w < 1.0
    assert v > 0.0
