from linear_regression import predict


def test_predict():
    assert predict([1.0, 2.0], [0.5, 1.0], 0.0) == 2.5
