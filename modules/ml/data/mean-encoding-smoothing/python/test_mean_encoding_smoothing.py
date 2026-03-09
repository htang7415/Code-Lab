import pytest

from mean_encoding_smoothing import smoothed_mean_encoding_map


def test_smoothed_mean_encoding_pulls_rare_categories_toward_global_mean() -> None:
    encoding = smoothed_mean_encoding_map(
        categories=["red", "red", "blue", "green"],
        targets=[1.0, 1.0, 0.0, 0.0],
        smoothing=2.0,
    )

    assert encoding == pytest.approx({"red": 0.75, "blue": 1.0 / 3.0, "green": 1.0 / 3.0})


def test_smoothed_mean_encoding_matches_raw_means_when_smoothing_is_zero() -> None:
    encoding = smoothed_mean_encoding_map(
        categories=["a", "a", "b"],
        targets=[1.0, 0.0, 0.0],
        smoothing=0.0,
    )

    assert encoding == pytest.approx({"a": 0.5, "b": 0.0})


def test_smoothed_mean_encoding_requires_non_negative_smoothing() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        smoothed_mean_encoding_map(categories=["a"], targets=[1.0], smoothing=-1.0)
