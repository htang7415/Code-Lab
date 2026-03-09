import pytest

from feature_scaling import feature_scale


def test_feature_scale_standardizes_values() -> None:
    scaled = feature_scale([1.0, 2.0, 3.0], method="zscore")

    assert scaled == pytest.approx([-1.224744871391589, 0.0, 1.224744871391589])


def test_feature_scale_minmax_scales_to_zero_one_range() -> None:
    scaled = feature_scale([2.0, 4.0, 6.0], method="minmax")

    assert scaled == pytest.approx([0.0, 0.5, 1.0])


def test_feature_scale_rejects_unknown_method() -> None:
    with pytest.raises(ValueError, match="method"):
        feature_scale([1.0], method="unknown")
