import pytest

from entity_embedding_intuition import pooled_entity_embedding


def test_pooled_entity_embedding_averages_selected_rows() -> None:
    pooled = pooled_entity_embedding(
        entity_ids=[0, 2],
        embedding_table=[[1.0, 2.0], [10.0, 20.0], [3.0, 4.0]],
    )

    assert pooled == pytest.approx([2.0, 3.0])


def test_pooled_entity_embedding_returns_zero_vector_for_no_ids() -> None:
    pooled = pooled_entity_embedding(entity_ids=[], embedding_table=[[1.0, 2.0]])

    assert pooled == pytest.approx([0.0, 0.0])


def test_pooled_entity_embedding_requires_valid_indices() -> None:
    with pytest.raises(ValueError, match="valid embedding rows"):
        pooled_entity_embedding(entity_ids=[1], embedding_table=[[1.0, 2.0]])
