from activation_failure_modes import dead_relu_fraction


def test_dead_relu_fraction():
    assert dead_relu_fraction([-1.0, 0.0, 2.0]) == 2 / 3
