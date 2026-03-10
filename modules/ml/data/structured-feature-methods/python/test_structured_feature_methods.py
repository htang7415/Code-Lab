import pytest

from structured_feature_methods import bucketize, category_cross_features, pooled_entity_embedding


def test_bucketize_assigns_values_to_expected_bins() -> None:
    buckets = bucketize(values=[-1.0, 0.5, 2.0, 5.0], boundaries=[0.0, 2.0, 4.0])

    assert buckets == [0, 1, 2, 3]


def test_category_cross_features_join_paired_categories() -> None:
    crossed = category_cross_features(left=["red", "blue"], right=["small", "large"])

    assert crossed == ["red__X__small", "blue__X__large"]


def test_pooled_entity_embedding_averages_selected_rows() -> None:
    pooled = pooled_entity_embedding(
        entity_ids=[0, 2],
        embedding_table=[[1.0, 2.0], [10.0, 20.0], [3.0, 4.0]],
    )

    assert pooled == pytest.approx([2.0, 3.0])


def test_structured_feature_methods_validate_common_errors() -> None:
    with pytest.raises(ValueError, match="same length"):
        category_cross_features(left=["a"], right=["a", "b"])
    with pytest.raises(ValueError, match="sorted"):
        bucketize(values=[1.0], boundaries=[2.0, 1.0])
    with pytest.raises(ValueError, match="valid embedding rows"):
        pooled_entity_embedding(entity_ids=[1], embedding_table=[[1.0, 2.0]])
