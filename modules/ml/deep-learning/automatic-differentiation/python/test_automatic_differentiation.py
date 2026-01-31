from automatic_differentiation import forward_grad


def test_forward_grad():
    assert forward_grad(3.0) == 6.0
