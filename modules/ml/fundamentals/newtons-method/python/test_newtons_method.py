from newtons_method import newton_step


def test_newton_step():
    assert newton_step(1.0, 2.0, 4.0) == 0.5
