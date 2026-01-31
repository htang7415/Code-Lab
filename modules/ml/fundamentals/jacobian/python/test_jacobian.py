from jacobian import jacobian


def test_jacobian():
    f1 = lambda x, y: x + y
    f2 = lambda x, y: x * y
    j = jacobian(f1, f2, 2.0, 3.0)
    assert abs(j[0][0] - 1.0) < 1e-3
    assert abs(j[1][0] - 3.0) < 1e-3
