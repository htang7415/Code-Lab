import pytest

from category_cross_features import category_cross_features


def test_category_cross_features_join_paired_categories() -> None:
    crossed = category_cross_features(left=["red", "blue"], right=["small", "large"])

    assert crossed == ["red__X__small", "blue__X__large"]


def test_category_cross_features_support_custom_separator() -> None:
    crossed = category_cross_features(left=["a"], right=["b"], separator=":")

    assert crossed == ["a:b"]


def test_category_cross_features_require_matching_lengths() -> None:
    with pytest.raises(ValueError, match="same length"):
        category_cross_features(left=["a"], right=["a", "b"])
