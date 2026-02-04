import math

from svd import singular_values_2x2


def test_svd_diagonal():
    s1, s2 = singular_values_2x2([[3.0, 0.0], [0.0, 4.0]])
    assert math.isclose(s1, 4.0, rel_tol=1e-6)
    assert math.isclose(s2, 3.0, rel_tol=1e-6)


def test_svd_rank_one():
    s1, s2 = singular_values_2x2([[1.0, 0.0], [0.0, 0.0]])
    assert math.isclose(s1, 1.0, rel_tol=1e-6)
    assert math.isclose(s2, 0.0, abs_tol=1e-6)
