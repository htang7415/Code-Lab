from mixed_precision import scale_gradients


def test_scale_gradients():
    assert scale_gradients([1.0, 2.0], 2.0) == [2.0, 4.0]
