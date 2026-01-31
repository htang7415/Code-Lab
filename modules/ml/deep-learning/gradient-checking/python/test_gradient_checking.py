from gradient_checking import grad_check


def test_grad_check_square():
    f = lambda x: x * x
    approx = grad_check(f, 3.0)
    assert abs(approx - 6.0) < 1e-3
