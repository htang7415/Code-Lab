"""reranking_vs_retrieval_budgeting - choose whether reranking quality is worth the extra budget."""

from __future__ import annotations


def retrieval_only_cost(retrieve_k: int, retrieval_cost_per_doc: int) -> int:
    return max(retrieve_k, 0) * max(retrieval_cost_per_doc, 0)


def rerank_pipeline_cost(
    retrieve_k: int,
    rerank_candidates: int,
    retrieval_cost_per_doc: int,
    rerank_cost_per_doc: int,
) -> int:
    return retrieval_only_cost(retrieve_k, retrieval_cost_per_doc) + max(rerank_candidates, 0) * max(rerank_cost_per_doc, 0)


def fits_budget(cost: int, budget_ms: int) -> bool:
    return cost <= budget_ms


def choose_pipeline(
    budget_ms: int,
    retrieve_k: int,
    rerank_candidates: int,
    retrieval_cost_per_doc: int,
    rerank_cost_per_doc: int,
    expected_retrieval_mrr: float,
    expected_rerank_mrr: float,
) -> str:
    rerank_cost = rerank_pipeline_cost(
        retrieve_k,
        rerank_candidates,
        retrieval_cost_per_doc,
        rerank_cost_per_doc,
    )
    if fits_budget(rerank_cost, budget_ms) and expected_rerank_mrr > expected_retrieval_mrr:
        return "retrieval-plus-rerank"
    return "retrieval-only"


def pipeline_summary(
    budget_ms: int,
    retrieve_k: int,
    rerank_candidates: int,
    retrieval_cost_per_doc: int,
    rerank_cost_per_doc: int,
    expected_retrieval_mrr: float,
    expected_rerank_mrr: float,
) -> dict[str, int | float | str | bool]:
    retrieval_cost = retrieval_only_cost(retrieve_k, retrieval_cost_per_doc)
    rerank_cost = rerank_pipeline_cost(
        retrieve_k,
        rerank_candidates,
        retrieval_cost_per_doc,
        rerank_cost_per_doc,
    )
    return {
        "retrieval_cost": retrieval_cost,
        "rerank_cost": rerank_cost,
        "rerank_fits_budget": fits_budget(rerank_cost, budget_ms),
        "choice": choose_pipeline(
            budget_ms,
            retrieve_k,
            rerank_candidates,
            retrieval_cost_per_doc,
            rerank_cost_per_doc,
            expected_retrieval_mrr,
            expected_rerank_mrr,
        ),
        "mrr_gain": expected_rerank_mrr - expected_retrieval_mrr,
    }
