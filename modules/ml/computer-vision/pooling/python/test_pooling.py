from pooling import max_pool, avg_pool


def test_pooling():
    assert max_pool([1, 3, 2]) == 3
    assert avg_pool([1, 3]) == 2
