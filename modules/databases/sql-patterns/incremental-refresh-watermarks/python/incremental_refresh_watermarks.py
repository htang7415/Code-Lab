"""incremental_refresh_watermarks - advance materialized refreshes with a monotonic watermark."""

from __future__ import annotations


def source_row(updated_at: int, workspace_id: int, amount: int) -> dict[str, int]:
    return {
        "updated_at": updated_at,
        "workspace_id": workspace_id,
        "amount": amount,
    }


def empty_refresh_state() -> dict[str, object]:
    return {
        "watermark": 0,
        "totals": {},
    }


def rows_in_window(
    rows: list[dict[str, int]],
    last_watermark: int,
    next_watermark: int,
) -> list[dict[str, int]]:
    return [
        row
        for row in rows
        if last_watermark < int(row["updated_at"]) <= next_watermark
    ]


def apply_incremental_refresh(
    state: dict[str, object],
    rows: list[dict[str, int]],
    next_watermark: int,
) -> list[int]:
    last_watermark = current_watermark(state)
    if next_watermark < last_watermark:
        raise ValueError("watermark must move forward")

    totals = state["totals"]
    assert isinstance(totals, dict)
    window_rows = rows_in_window(rows, last_watermark, next_watermark)
    for row in window_rows:
        workspace_id = int(row["workspace_id"])
        totals[workspace_id] = int(totals.get(workspace_id, 0)) + int(row["amount"])
    state["watermark"] = next_watermark
    return [int(row["updated_at"]) for row in window_rows]


def current_watermark(state: dict[str, object]) -> int:
    return int(state["watermark"])


def workspace_totals(state: dict[str, object]) -> dict[int, int]:
    totals = state["totals"]
    assert isinstance(totals, dict)
    return {int(workspace_id): int(total) for workspace_id, total in totals.items()}


def full_rebuild(rows: list[dict[str, int]], up_to_watermark: int) -> dict[int, int]:
    totals: dict[int, int] = {}
    for row in rows:
        if int(row["updated_at"]) > up_to_watermark:
            continue
        workspace_id = int(row["workspace_id"])
        totals[workspace_id] = totals.get(workspace_id, 0) + int(row["amount"])
    return totals
