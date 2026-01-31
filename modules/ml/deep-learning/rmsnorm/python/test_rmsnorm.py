from rmsnorm import rmsnorm


def test_rmsnorm_rms():
    out = rmsnorm([3.0, 4.0])
    rms = (sum(v * v for v in out) / len(out)) ** 0.5
    assert abs(rms - 1.0) < 1e-6
