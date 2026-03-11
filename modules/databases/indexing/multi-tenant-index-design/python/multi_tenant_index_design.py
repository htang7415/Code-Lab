"""multi_tenant_index_design - estimate how index order affects tenant isolation."""

from __future__ import annotations


def prefix_match_columns(
    index_order: tuple[str, ...],
    filters: dict[str, object],
) -> tuple[str, ...]:
    matched: list[str] = []
    for column in index_order:
        if column not in filters:
            break
        matched.append(column)
    return tuple(matched)


def candidate_row_ids(
    rows: list[dict[str, object]],
    index_order: tuple[str, ...],
    filters: dict[str, object],
) -> list[str]:
    matched_prefix = prefix_match_columns(index_order, filters)
    if not matched_prefix:
        return [str(row["id"]) for row in rows]
    return [
        str(row["id"])
        for row in rows
        if all(row[column] == filters[column] for column in matched_prefix)
    ]


def final_row_ids(
    rows: list[dict[str, object]],
    filters: dict[str, object],
) -> list[str]:
    return [
        str(row["id"])
        for row in rows
        if all(row.get(column) == value for column, value in filters.items())
    ]


def index_cost_summary(
    rows: list[dict[str, object]],
    index_order: tuple[str, ...],
    filters: dict[str, object],
) -> dict[str, object]:
    matched_prefix = prefix_match_columns(index_order, filters)
    candidates = candidate_row_ids(rows, index_order, filters)
    results = final_row_ids(rows, filters)
    return {
        "matched_prefix": list(matched_prefix),
        "candidate_count": len(candidates),
        "result_count": len(results),
        "candidate_ids": candidates,
        "result_ids": results,
    }
