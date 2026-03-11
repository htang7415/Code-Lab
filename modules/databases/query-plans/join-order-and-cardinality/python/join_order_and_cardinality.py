"""join_order_and_cardinality - estimate how join order changes intermediate work."""

from __future__ import annotations


def filtered_rows(base_rows: int, selectivity: float) -> int:
    if base_rows <= 0 or selectivity <= 0:
        return 0
    return max(1, int(base_rows * selectivity))


def join_output_rows(current_rows: int, average_matches: float) -> int:
    if current_rows <= 0 or average_matches <= 0:
        return 0
    return max(1, int(current_rows * average_matches))


def left_deep_plan_cost(
    table_rows: dict[str, int],
    selectivities: dict[str, float],
    join_order: list[str],
    join_edges: dict[tuple[str, str], float],
) -> dict[str, int]:
    if not join_order:
        return {"start_rows": 0, "output_rows": 0, "work": 0}

    first = join_order[0]
    current_rows = filtered_rows(table_rows[first], selectivities.get(first, 1.0))
    total_work = current_rows

    for left, right in zip(join_order, join_order[1:]):
        if (left, right) not in join_edges:
            raise KeyError((left, right))
        right_rows = filtered_rows(table_rows[right], selectivities.get(right, 1.0))
        total_work += current_rows + right_rows
        current_rows = join_output_rows(current_rows, join_edges[(left, right)])

    return {
        "start_rows": filtered_rows(table_rows[first], selectivities.get(first, 1.0)),
        "output_rows": current_rows,
        "work": total_work,
    }


def cheaper_plan(left: dict[str, int], right: dict[str, int]) -> str:
    return "left" if int(left["work"]) <= int(right["work"]) else "right"
