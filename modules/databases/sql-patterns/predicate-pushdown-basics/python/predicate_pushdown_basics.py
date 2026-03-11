"""predicate_pushdown_basics - skip row groups early using cheap min/max metadata."""

from __future__ import annotations


def group_might_match(group: dict[str, object], min_score: int) -> bool:
    return int(group["max_score"]) >= min_score


def pushed_down_group_ids(
    groups: list[dict[str, object]],
    min_score: int,
) -> list[str]:
    return [
        str(group["id"])
        for group in groups
        if group_might_match(group, min_score)
    ]


def matching_rows(
    groups: list[dict[str, object]],
    min_score: int,
) -> list[str]:
    matches: list[str] = []
    for group in groups:
        if not group_might_match(group, min_score):
            continue
        rows = group.get("rows", [])
        assert isinstance(rows, list)
        for row in rows:
            row_score = int(row["score"]) if isinstance(row, dict) else None
            if row_score is not None and row_score >= min_score:
                matches.append(str(row["id"]))
    return matches


def pushdown_summary(
    groups: list[dict[str, object]],
    min_score: int,
) -> dict[str, object]:
    scanned = pushed_down_group_ids(groups, min_score)
    return {
        "total_groups": len(groups),
        "scanned_groups": scanned,
        "scanned_group_count": len(scanned),
        "matching_rows": matching_rows(groups, min_score),
    }
