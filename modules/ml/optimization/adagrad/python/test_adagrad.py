from adagrad import adagrad_step


def test_adagrad_step():
    w, g2 = adagrad_step(1.0, 1.0, 0.0, 0.1, 1e-8)
    assert w < 1.0
    assert g2 > 0.0
