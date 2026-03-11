"""hard_negative_eval_cases - validate retrieval eval cases with strong distractors."""

from __future__ import annotations


def hard_negative_case(
    query_id: str,
    positive_id: str,
    hard_negative_ids: list[str],
    query_type: str,
) -> dict[str, object]:
    return {
        "query_id": query_id,
        "positive_id": positive_id,
        "hard_negative_ids": list(hard_negative_ids),
        "query_type": query_type,
    }


def hard_negative_count(cases: list[dict[str, object]]) -> int:
    total = 0
    for case in cases:
        total += len(case.get("hard_negative_ids", []))
    return total


def invalid_case_ids(cases: list[dict[str, object]]) -> list[str]:
    invalid: list[str] = []
    for case in cases:
        query_id = str(case.get("query_id", "")).strip()
        positive_id = str(case.get("positive_id", "")).strip()
        query_type = str(case.get("query_type", "")).strip()
        hard_negative_ids = case.get("hard_negative_ids", [])

        has_hard_negatives = isinstance(hard_negative_ids, list) and len(hard_negative_ids) > 0
        positive_in_negatives = positive_id != "" and positive_id in hard_negative_ids

        if not query_id or not positive_id or not query_type or not has_hard_negatives or positive_in_negatives:
            invalid.append(query_id)
    return sorted(invalid)


def query_type_counts(cases: list[dict[str, object]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for case in cases:
        query_type = str(case.get("query_type", "")).strip()
        if not query_type:
            continue
        counts[query_type] = counts.get(query_type, 0) + 1
    return counts


def dataset_summary(cases: list[dict[str, object]]) -> dict[str, object]:
    invalid_ids = invalid_case_ids(cases)
    return {
        "case_count": len(cases),
        "hard_negative_total": hard_negative_count(cases),
        "invalid_case_ids": invalid_ids,
        "query_type_counts": query_type_counts(cases),
        "ready": len(cases) > 0 and not invalid_ids,
    }
