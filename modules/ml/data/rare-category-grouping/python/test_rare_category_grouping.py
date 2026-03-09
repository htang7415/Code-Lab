import pytest

from rare_category_grouping import group_rare_categories


def test_group_rare_categories_replaces_infrequent_values() -> None:
    grouped = group_rare_categories(
        categories=["red", "blue", "red", "green"],
        min_count=2,
    )

    assert grouped == ["red", "__OTHER__", "red", "__OTHER__"]


def test_group_rare_categories_keeps_frequent_values() -> None:
    grouped = group_rare_categories(
        categories=["a", "a", "b", "b"],
        min_count=2,
    )

    assert grouped == ["a", "a", "b", "b"]


def test_group_rare_categories_requires_positive_threshold() -> None:
    with pytest.raises(ValueError, match="positive"):
        group_rare_categories(categories=["a"], min_count=0)
