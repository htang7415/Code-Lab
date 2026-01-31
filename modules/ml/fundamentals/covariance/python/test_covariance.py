from covariance import covariance


def test_covariance():
    assert covariance([1, 2], [1, 2]) == 0.25
