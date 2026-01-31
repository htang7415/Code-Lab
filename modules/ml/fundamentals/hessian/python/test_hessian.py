from hessian import hessian_quadratic


def test_hessian_quadratic():
    assert hessian_quadratic(3.0) == 6.0
