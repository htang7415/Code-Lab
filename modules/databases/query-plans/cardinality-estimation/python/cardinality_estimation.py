"""cardinality_estimation - small first-principles planner estimates."""

from __future__ import annotations

from math import prod


def estimate_rows(table_rows: int, selectivities: list[float]) -> int:
    if table_rows < 0:
        raise ValueError("table_rows must be non-negative")
    if any(not 0.0 <= value <= 1.0 for value in selectivities):
        raise ValueError("selectivities must be between 0 and 1")
    return round(table_rows * prod(selectivities or [1.0]))


def choose_access_path(
    estimated_rows: int,
    table_rows: int,
    index_available: bool,
    index_fraction_threshold: float = 0.1,
) -> str:
    if not index_available:
        return "seq-scan"
    if table_rows <= 0:
        return "seq-scan"
    if estimated_rows / table_rows <= index_fraction_threshold:
        return "index-scan"
    return "seq-scan"


def q_error(estimated_rows: int, actual_rows: int) -> float:
    if estimated_rows <= 0 or actual_rows <= 0:
        raise ValueError("estimated_rows and actual_rows must be positive")
    larger = max(estimated_rows, actual_rows)
    smaller = min(estimated_rows, actual_rows)
    return larger / smaller


def needs_plan_attention(
    estimated_rows: int,
    actual_rows: int,
    q_error_threshold: float = 4.0,
) -> bool:
    return q_error(estimated_rows, actual_rows) >= q_error_threshold
