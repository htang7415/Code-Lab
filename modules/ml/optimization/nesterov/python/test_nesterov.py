from nesterov import nesterov_step


def test_nesterov_step():
    w, v = nesterov_step(1.0, 1.0, 0.0, 0.1, 0.9)
    assert w < 1.0
    assert v == 1.0
