from softmax_regression import softmax


def test_softmax_sum():
    assert abs(sum(softmax([1.0, 1.0])) - 1.0) < 1e-6
