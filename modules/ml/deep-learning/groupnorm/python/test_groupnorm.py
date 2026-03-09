import pytest

from groupnorm import groupnorm


def test_groupnorm_normalizes_each_group():
    out = groupnorm([1.0, 2.0, 10.0, 12.0], groups=2, eps=1e-12)
    first = out[:2]
    second = out[2:]

    for chunk in (first, second):
        mean = sum(chunk) / len(chunk)
        var = sum((value - mean) ** 2 for value in chunk) / len(chunk)
        assert mean == pytest.approx(0.0, abs=1e-6)
        assert var == pytest.approx(1.0, abs=1e-6)


def test_groupnorm_rejects_uneven_groups():
    with pytest.raises(ValueError, match="divisible"):
        groupnorm([1.0, 2.0, 3.0], groups=2)
