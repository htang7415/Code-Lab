from layernorm import layernorm


def test_layernorm_mean():
    out = layernorm([1.0, 2.0, 3.0])
    assert abs(sum(out)) < 1e-6
