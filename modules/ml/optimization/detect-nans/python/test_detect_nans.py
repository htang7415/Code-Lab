from detect_nans import has_nan


def test_has_nan():
    assert has_nan([0.0, float("nan")])
