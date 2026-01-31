from xavier_initialization import xavier_uniform


def test_xavier_length():
    weights = xavier_uniform(2, 3, seed=1)
    assert len(weights) == 6
