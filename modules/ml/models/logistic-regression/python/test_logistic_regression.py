from logistic_regression import predict_proba


def test_predict_proba():
    p = predict_proba([0.0], [1.0], 0.0)
    assert abs(p - 0.5) < 1e-6
