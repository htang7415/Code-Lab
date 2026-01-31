from sgd_momentum import momentum_step


def test_momentum_step():
    w, v = momentum_step(1.0, 1.0, 0.0, 0.1, 0.9)
    assert w == 0.9
    assert v == 1.0
