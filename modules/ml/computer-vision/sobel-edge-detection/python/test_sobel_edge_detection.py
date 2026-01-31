from sobel_edge_detection import sobel_center


def test_sobel_center():
    patch = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert sobel_center(patch) == 0.0
