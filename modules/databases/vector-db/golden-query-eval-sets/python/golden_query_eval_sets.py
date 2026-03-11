"""golden_query_eval_sets - validate whether a small regression set covers the required query types."""

from __future__ import annotations


def golden_case(query_id: str, expected_top_id: str, query_type: str) -> dict[str, str]:
    return {
        "query_id": query_id,
        "expected_top_id": expected_top_id,
        "query_type": query_type,
    }


def duplicate_query_ids(cases: list[dict[str, str]]) -> list[str]:
    counts: dict[str, int] = {}
    for case in cases:
        query_id = case["query_id"]
        counts[query_id] = counts.get(query_id, 0) + 1
    return sorted(query_id for query_id, count in counts.items() if count > 1)


def missing_required_types(
    cases: list[dict[str, str]],
    required_types: list[str],
) -> list[str]:
    observed = {case["query_type"] for case in cases}
    return sorted(query_type for query_type in required_types if query_type not in observed)


def golden_set_ready(
    cases: list[dict[str, str]],
    required_types: list[str],
    min_case_count: int,
) -> bool:
    if len(cases) < min_case_count:
        return False
    if duplicate_query_ids(cases):
        return False
    if missing_required_types(cases, required_types):
        return False
    return True


def golden_set_summary(
    cases: list[dict[str, str]],
    required_types: list[str],
    min_case_count: int,
) -> dict[str, object]:
    return {
        "case_count": len(cases),
        "duplicate_query_ids": duplicate_query_ids(cases),
        "missing_required_types": missing_required_types(cases, required_types),
        "ready": golden_set_ready(cases, required_types, min_case_count),
    }
