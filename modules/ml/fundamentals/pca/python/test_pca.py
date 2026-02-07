from pca import pca_first_component_2d


def test_pca_first_component():
    points = [[-1.0, 0.0], [1.0, 0.0]]
    vec = pca_first_component_2d(points)
    assert abs(abs(vec[0]) - 1.0) < 1e-6
