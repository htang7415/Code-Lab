import math

from pca import first_principal_component_2d


def test_pca_axis_aligned():
    points = [[-2.0, 0.0], [0.0, 0.0], [3.0, 0.0]]
    v = first_principal_component_2d(points)
    assert math.isclose(abs(v[0]), 1.0, rel_tol=1e-6)
    assert math.isclose(abs(v[1]), 0.0, abs_tol=1e-6)


def test_pca_diagonal():
    points = [[0.0, 0.0], [1.0, 1.0], [2.0, 2.0]]
    v = first_principal_component_2d(points)
    assert math.isclose(abs(v[0]), abs(v[1]), rel_tol=1e-6)
