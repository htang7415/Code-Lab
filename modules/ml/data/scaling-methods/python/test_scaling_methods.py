import pytest

from scaling_methods import clip_features, feature_scale, robust_scale


def test_zscore_scaling_centers_values() -> None:
    out = feature_scale([1.0, 2.0, 3.0], method="zscore")
    assert sum(out) == pytest.approx(0.0)


def test_minmax_scaling_bounds_values() -> None:
    assert feature_scale([2.0, 4.0, 6.0], method="minmax") == pytest.approx([0.0, 0.5, 1.0])


def test_robust_scaling_uses_median_and_iqr() -> None:
    out = robust_scale([1.0, 2.0, 100.0])
    assert out[1] == pytest.approx(0.0)


def test_clipping_caps_extremes() -> None:
    assert clip_features([-5.0, 0.5, 10.0], min_value=0.0, max_value=1.0) == [0.0, 0.5, 1.0]


def test_invalid_inputs_raise() -> None:
    with pytest.raises(ValueError, match="zscore"):
        feature_scale([1.0], method="bad")

    with pytest.raises(ValueError, match="less than or equal"):
        clip_features([1.0], min_value=2.0, max_value=1.0)
