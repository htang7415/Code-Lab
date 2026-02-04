from embeddings import mean_pool


def test_mean_pool():
    vectors = [[1.0, 2.0], [3.0, 4.0]]
    assert mean_pool(vectors) == [2.0, 3.0]


def test_mean_pool_empty():
    assert mean_pool([]) == []
