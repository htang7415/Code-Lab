from precision_recall import precision_recall


def test_precision_recall():
    p, r = precision_recall([1, 0, 1], [1, 1, 0])
    assert p == 0.5
    assert r == 0.5
