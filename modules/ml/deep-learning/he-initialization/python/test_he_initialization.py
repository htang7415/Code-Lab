from he_initialization import he_normal


def test_he_length():
    weights = he_normal(2, 3, seed=1)
    assert len(weights) == 6
