"""retrieval_failure_analysis - classify retrieval failures before debugging relevance scores."""

from __future__ import annotations


def first_relevant_rank(
    ranked_ids: list[str],
    relevant_ids: set[str],
) -> int | None:
    for index, doc_id in enumerate(ranked_ids, start=1):
        if doc_id in relevant_ids:
            return index
    return None


def has_scope_leak(
    ranked_results: list[dict[str, object]],
    allowed_workspace_id: int,
    k: int,
) -> bool:
    return any(
        int(result["workspace_id"]) != allowed_workspace_id
        for result in ranked_results[:k]
    )


def failure_reason(
    ranked_results: list[dict[str, object]],
    relevant_ids: set[str],
    allowed_workspace_id: int,
    k: int,
) -> str:
    if has_scope_leak(ranked_results, allowed_workspace_id, k):
        return "scope-leak"
    rank = first_relevant_rank(
        [str(result["id"]) for result in ranked_results],
        relevant_ids,
    )
    if rank is None:
        return "no-relevant-hit"
    if rank > k:
        return "ranked-below-k"
    return "ok"


def failure_summary(
    cases: list[dict[str, object]],
    k: int,
) -> dict[str, int]:
    summary = {
        "ok": 0,
        "scope-leak": 0,
        "no-relevant-hit": 0,
        "ranked-below-k": 0,
    }
    for case in cases:
        reason = failure_reason(
            ranked_results=list(case["ranked_results"]),
            relevant_ids=set(case["relevant_ids"]),
            allowed_workspace_id=int(case["allowed_workspace_id"]),
            k=k,
        )
        summary[reason] += 1
    return summary
