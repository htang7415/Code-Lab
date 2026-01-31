from k_means import assign


def test_assign():
    points = [[0.0], [10.0]]
    centroids = [[0.0], [5.0]]
    assert assign(points, centroids) == [0, 1]
