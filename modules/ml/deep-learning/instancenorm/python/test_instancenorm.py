from instancenorm import instancenorm


def test_instancenorm_mean():
    out = instancenorm([1.0, 2.0, 3.0])
    assert abs(sum(out)) < 1e-6
