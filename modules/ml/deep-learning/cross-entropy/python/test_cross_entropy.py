from cross_entropy import cross_entropy


def test_cross_entropy_low():
    loss = cross_entropy([3.0, 0.0], 0)
    assert loss < 0.1
