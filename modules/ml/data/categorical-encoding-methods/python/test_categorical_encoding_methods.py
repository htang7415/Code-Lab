import pytest

from categorical_encoding_methods import (
    frequency_encoding_map,
    group_rare_categories,
    smoothed_mean_encoding_map,
    target_encoding_map,
    weight_of_evidence,
)


def test_frequency_encoding_returns_relative_counts() -> None:
    out = frequency_encoding_map(["a", "a", "b"])
    assert out == pytest.approx({"a": 2 / 3, "b": 1 / 3})


def test_target_and_smoothed_encoding_maps_are_grouped_by_category() -> None:
    raw = target_encoding_map(["a", "a", "b"], [1.0, 0.0, 1.0])
    smooth = smoothed_mean_encoding_map(["a", "a", "b"], [1.0, 0.0, 1.0], smoothing=2.0)
    assert raw["a"] == pytest.approx(0.5)
    assert smooth["b"] < 1.0


def test_weight_of_evidence_and_rare_grouping_behave_as_expected() -> None:
    assert weight_of_evidence(positive_count=8, negative_count=2, total_positive=10, total_negative=10) > 0.0
    assert group_rare_categories(["a", "a", "b"], min_count=2) == ["a", "a", "__OTHER__"]


def test_invalid_inputs_raise() -> None:
    with pytest.raises(ValueError, match="same length"):
        target_encoding_map(["a"], [])

    with pytest.raises(ValueError, match="non-negative"):
        smoothed_mean_encoding_map(["a"], [1.0], smoothing=-1.0)
