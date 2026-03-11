from reranking_vs_retrieval_budgeting import (
    choose_pipeline,
    fits_budget,
    pipeline_summary,
    rerank_pipeline_cost,
    retrieval_only_cost,
)


def test_reranking_is_chosen_when_it_fits_budget_and_improves_quality():
    summary = pipeline_summary(
        budget_ms=140,
        retrieve_k=20,
        rerank_candidates=50,
        retrieval_cost_per_doc=1,
        rerank_cost_per_doc=2,
        expected_retrieval_mrr=0.62,
        expected_rerank_mrr=0.72,
    )

    assert retrieval_only_cost(20, 1) == 20
    assert rerank_pipeline_cost(20, 50, 1, 2) == 120
    assert summary["choice"] == "retrieval-plus-rerank"
    assert summary["rerank_fits_budget"] is True


def test_tight_budget_or_no_gain_keeps_pipeline_retrieval_only():
    assert fits_budget(120, 100) is False
    assert (
        choose_pipeline(
            budget_ms=100,
            retrieve_k=20,
            rerank_candidates=50,
            retrieval_cost_per_doc=1,
            rerank_cost_per_doc=2,
            expected_retrieval_mrr=0.62,
            expected_rerank_mrr=0.72,
        )
        == "retrieval-only"
    )
    assert (
        choose_pipeline(
            budget_ms=140,
            retrieve_k=20,
            rerank_candidates=50,
            retrieval_cost_per_doc=1,
            rerank_cost_per_doc=2,
            expected_retrieval_mrr=0.72,
            expected_rerank_mrr=0.72,
        )
        == "retrieval-only"
    )
