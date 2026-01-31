from bilinear_resizing import bilinear_sample


def test_bilinear_sample():
    assert bilinear_sample(0.0, 1.0, 1.0, 0.0, 0.5, 0.5) == 0.5
