from hybrid_search import (
    cosine_similarity,
    hybrid_score,
    lexical_overlap_score,
    rank_documents,
)


DOCUMENTS = [
    {
        "id": "keyword-doc",
        "text": "pgvector permissions filter",
        "vector": [0.6, 0.8],
    },
    {
        "id": "semantic-doc",
        "text": "semantic ranking only",
        "vector": [1.0, 0.0],
    },
]


def test_cosine_similarity_is_one_for_identical_vectors() -> None:
    assert cosine_similarity([1.0, 2.0], [1.0, 2.0]) == 1.0


def test_lexical_overlap_rewards_exact_query_terms() -> None:
    assert lexical_overlap_score("pgvector permissions", "pgvector permissions filter") == 1.0
    assert lexical_overlap_score("pgvector permissions", "semantic ranking only") == 0.0


def test_hybrid_ranking_shifts_when_lexical_weight_matters_more() -> None:
    lexical_heavy = rank_documents(
        "pgvector permissions",
        [1.0, 0.0],
        DOCUMENTS,
        alpha=0.4,
    )
    semantic_heavy = rank_documents(
        "pgvector permissions",
        [1.0, 0.0],
        DOCUMENTS,
        alpha=0.9,
    )

    assert lexical_heavy[0][0] == "keyword-doc"
    assert semantic_heavy[0][0] == "semantic-doc"
    assert hybrid_score(
        "pgvector permissions",
        [1.0, 0.0],
        "pgvector permissions filter",
        [0.6, 0.8],
        alpha=0.4,
    ) > hybrid_score(
        "pgvector permissions",
        [1.0, 0.0],
        "semantic ranking only",
        [1.0, 0.0],
        alpha=0.4,
    )
