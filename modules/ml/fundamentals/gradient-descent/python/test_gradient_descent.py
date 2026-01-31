from gradient_descent import gd_step


def test_gd_step():
    assert gd_step(1.0, 0.5, 0.1) == 0.95
