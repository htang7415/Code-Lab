from reranking_pipelines import (
    initial_retrieve,
    pipeline_rank,
    rerank_candidates,
)


DOCUMENTS = [
    {
        "id": "generic-safety",
        "text": "tool safety and review workflows",
        "retrieval_score": 0.95,
    },
    {
        "id": "approval-gated-actions",
        "text": "approval gated actions for destructive tools",
        "retrieval_score": 0.92,
    },
    {
        "id": "semantic-caching",
        "text": "semantic caching for repeated model responses",
        "retrieval_score": 0.90,
    },
]

QUERY = "approval gated actions"


def test_initial_retrieval_uses_the_coarse_retrieval_score() -> None:
    candidates = initial_retrieve(DOCUMENTS, candidate_k=2)

    assert [document["id"] for document in candidates] == [
        "generic-safety",
        "approval-gated-actions",
    ]


def test_reranker_promotes_the_more_query_specific_document() -> None:
    candidates = initial_retrieve(DOCUMENTS, candidate_k=2)

    assert rerank_candidates(QUERY, candidates)[0][0] == "approval-gated-actions"


def test_pipeline_cannot_recover_a_document_that_never_reached_the_candidate_set() -> None:
    assert pipeline_rank(QUERY, DOCUMENTS, candidate_k=1, final_k=1) == [
        "generic-safety",
    ]
    assert pipeline_rank(QUERY, DOCUMENTS, candidate_k=2, final_k=2) == [
        "approval-gated-actions",
        "generic-safety",
    ]
