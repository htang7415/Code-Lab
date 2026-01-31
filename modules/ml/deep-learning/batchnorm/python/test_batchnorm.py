from batchnorm import batchnorm


def test_batchnorm_mean():
    out = batchnorm([1.0, 2.0, 3.0])
    assert abs(sum(out)) < 1e-6
