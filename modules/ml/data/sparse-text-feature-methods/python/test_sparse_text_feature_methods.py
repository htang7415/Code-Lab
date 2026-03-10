import pytest

from sparse_text_feature_methods import (
    chi_square_feature_score,
    count_vector,
    hashed_feature_counts,
    prune_rare_tokens,
    tf_idf_weights,
)


def test_count_vector_and_pruning_cover_basic_sparse_lexical_flow() -> None:
    assert count_vector(["a", "b", "a"], ["a", "b", "c"]) == [2, 1, 0]
    assert prune_rare_tokens(["a", "a", "b"], min_count=2) == ["a", "a", "__UNK__"]


def test_tfidf_weights_emphasize_rarer_terms() -> None:
    weights = tf_idf_weights(["rare", "common"], {"rare": 1, "common": 5}, num_documents=10)
    assert weights["rare"] > weights["common"]


def test_hash_trick_and_chi_square_return_valid_outputs() -> None:
    buckets = hashed_feature_counts(["x", "y", "x"], num_buckets=4)
    assert sum(buckets) == 3
    assert chi_square_feature_score(8, 2, 2, 8) > 0.0


def test_invalid_inputs_raise() -> None:
    with pytest.raises(ValueError, match="unique"):
        count_vector(["a"], ["a", "a"])

    with pytest.raises(ValueError, match="positive"):
        hashed_feature_counts(["a"], num_buckets=0)
