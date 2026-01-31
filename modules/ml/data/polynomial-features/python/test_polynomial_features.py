from polynomial_features import poly_features


def test_poly_features():
    assert poly_features(2.0, 3) == [2.0, 4.0, 8.0]
