from dropout import dropout


def test_dropout_length():
    out = dropout([1.0, 2.0, 3.0], p=0.5, seed=1)
    assert len(out) == 3
