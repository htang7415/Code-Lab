from retrieval_failure_analysis import (
    failure_reason,
    failure_summary,
    first_relevant_rank,
    has_scope_leak,
)


def test_scope_leak_is_detected_before_ranking_analysis():
    results = [
        {"id": "a", "workspace_id": 8},
        {"id": "b", "workspace_id": 7},
    ]

    assert has_scope_leak(results, allowed_workspace_id=7, k=1)
    assert failure_reason(results, relevant_ids={"b"}, allowed_workspace_id=7, k=1) == "scope-leak"


def test_ranked_below_k_and_missing_hits_are_separated():
    low_rank_results = [
        {"id": "x", "workspace_id": 7},
        {"id": "b", "workspace_id": 7},
    ]
    miss_results = [
        {"id": "x", "workspace_id": 7},
        {"id": "y", "workspace_id": 7},
    ]

    assert first_relevant_rank(["x", "b"], {"b"}) == 2
    assert failure_reason(low_rank_results, {"b"}, allowed_workspace_id=7, k=1) == "ranked-below-k"
    assert failure_reason(miss_results, {"b"}, allowed_workspace_id=7, k=2) == "no-relevant-hit"


def test_failure_summary_counts_case_types():
    cases = [
        {
            "ranked_results": [{"id": "a", "workspace_id": 7}],
            "relevant_ids": {"a"},
            "allowed_workspace_id": 7,
        },
        {
            "ranked_results": [{"id": "x", "workspace_id": 8}],
            "relevant_ids": {"x"},
            "allowed_workspace_id": 7,
        },
        {
            "ranked_results": [{"id": "x", "workspace_id": 7}, {"id": "b", "workspace_id": 7}],
            "relevant_ids": {"b"},
            "allowed_workspace_id": 7,
        },
    ]

    assert failure_summary(cases, k=1) == {
        "ok": 1,
        "scope-leak": 1,
        "no-relevant-hit": 0,
        "ranked-below-k": 1,
    }
