from adam import adam_step


def test_adam_step():
    w, m, v = adam_step(1.0, 1.0, 0.0, 0.0, 0.1, 0.9, 0.999, 1e-8)
    assert w < 1.0
    assert m > 0.0
    assert v > 0.0
