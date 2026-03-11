from pooling import max_pool, avg_pool


def test_pooling():
    assert max_pool([1, 3, 2]) == 3
    assert avg_pool([1, 3]) == 2


def test_pooling_requires_non_empty_window():
    import pytest

    with pytest.raises(ValueError, match="non-empty"):
        max_pool([])
    with pytest.raises(ValueError, match="non-empty"):
        avg_pool([])
