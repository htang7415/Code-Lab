from convex_vs_nonconvex import is_convex_quadratic


def test_is_convex_quadratic():
    assert is_convex_quadratic(1.0)
    assert not is_convex_quadratic(-1.0)
