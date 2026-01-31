from dbscan import neighbors


def test_neighbors():
    points = [[0.0], [0.1], [2.0]]
    assert neighbors(points, 0, 0.2) == [0, 1]
