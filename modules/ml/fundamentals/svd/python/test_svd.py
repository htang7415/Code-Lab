from svd import singular_values_2x2


def test_singular_values():
    vals = singular_values_2x2([[1.0, 0.0], [0.0, 2.0]])
    assert sorted(vals) == [1.0, 2.0]
