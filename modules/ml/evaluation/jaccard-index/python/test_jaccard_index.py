from jaccard_index import jaccard


def test_jaccard():
    assert jaccard({1, 2}, {2, 3}) == 1 / 3
