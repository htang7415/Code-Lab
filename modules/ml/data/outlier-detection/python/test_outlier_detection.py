import pytest

from outlier_detection import z_score_outliers


def test_z_score_outliers_flags_large_deviation() -> None:
    indices = z_score_outliers([10.0, 11.0, 9.0, 10.0, 10.0, 40.0], threshold=2.0)

    assert indices == [5]


def test_z_score_outliers_returns_empty_for_constant_values() -> None:
    assert z_score_outliers([3.0, 3.0, 3.0]) == []


def test_z_score_outliers_requires_positive_threshold() -> None:
    with pytest.raises(ValueError, match="threshold"):
        z_score_outliers([1.0, 2.0], threshold=0.0)
