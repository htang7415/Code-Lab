from groupnorm import groupnorm


def test_groupnorm_length():
    out = groupnorm([1.0, 2.0, 3.0, 4.0], groups=2)
    assert len(out) == 4
