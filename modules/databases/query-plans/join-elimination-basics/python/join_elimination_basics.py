"""join_elimination_basics - skip a parent join when it adds no information."""

from __future__ import annotations


def join_can_be_eliminated(
    selects_parent_columns: bool,
    filters_parent_rows: bool,
    child_fk_not_null: bool,
) -> bool:
    return (not selects_parent_columns) and (not filters_parent_rows) and child_fk_not_null


def query_work(
    child_rows: int,
    parent_lookup_cost: int,
    eliminated: bool,
) -> int:
    base = max(child_rows, 0)
    if eliminated:
        return base
    return base + base * max(parent_lookup_cost, 0)


def plan_summary(
    child_rows: int,
    parent_lookup_cost: int,
    selects_parent_columns: bool,
    filters_parent_rows: bool,
    child_fk_not_null: bool,
) -> dict[str, int | bool]:
    eliminated = join_can_be_eliminated(
        selects_parent_columns,
        filters_parent_rows,
        child_fk_not_null,
    )
    return {
        "eliminated": eliminated,
        "work_with_join": query_work(child_rows, parent_lookup_cost, False),
        "work_after_elimination": query_work(child_rows, parent_lookup_cost, eliminated),
    }
