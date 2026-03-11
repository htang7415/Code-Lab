"""retrieval_evaluation_dataset_shapes - validate whether a retrieval eval set covers the basics."""

from __future__ import annotations


def evaluation_case(
    query_id: str,
    relevant_ids: list[str],
    query_type: str,
    allowed_workspace_id: int,
) -> dict[str, object]:
    return {
        "query_id": query_id,
        "relevant_ids": list(relevant_ids),
        "query_type": query_type,
        "allowed_workspace_id": allowed_workspace_id,
    }


def duplicate_query_ids(cases: list[dict[str, object]]) -> list[str]:
    counts: dict[str, int] = {}
    for case in cases:
        query_id = str(case["query_id"])
        counts[query_id] = counts.get(query_id, 0) + 1
    return sorted(query_id for query_id, count in counts.items() if count > 1)


def invalid_case_ids(cases: list[dict[str, object]]) -> list[str]:
    invalid: list[str] = []
    for case in cases:
        query_id = str(case["query_id"])
        relevant_ids = case.get("relevant_ids", [])
        query_type = str(case.get("query_type", ""))
        if not isinstance(relevant_ids, list) or len(relevant_ids) == 0 or not query_type:
            invalid.append(query_id)
    return sorted(invalid)


def query_type_counts(cases: list[dict[str, object]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for case in cases:
        query_type = str(case["query_type"])
        counts[query_type] = counts.get(query_type, 0) + 1
    return counts


def dataset_summary(cases: list[dict[str, object]]) -> dict[str, object]:
    return {
        "case_count": len(cases),
        "duplicate_query_ids": duplicate_query_ids(cases),
        "invalid_case_ids": invalid_case_ids(cases),
        "query_type_counts": query_type_counts(cases),
    }
