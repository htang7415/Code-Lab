"""late_arriving_data_handling - send old rows to a repair path after the watermark passes them."""

from __future__ import annotations


def source_row(event_time: int, workspace_id: int, amount: int) -> dict[str, int]:
    return {
        "event_time": event_time,
        "workspace_id": workspace_id,
        "amount": amount,
    }


def empty_state() -> dict[str, object]:
    return {
        "watermark": 0,
        "totals": {},
        "late_rows": [],
    }


def apply_incremental_rows(
    state: dict[str, object],
    rows: list[dict[str, int]],
    next_watermark: int,
) -> tuple[list[int], list[int]]:
    watermark = int(state["watermark"])
    if next_watermark < watermark:
        raise ValueError("watermark must move forward")

    totals = state["totals"]
    late_rows = state["late_rows"]
    assert isinstance(totals, dict)
    assert isinstance(late_rows, list)

    applied: list[int] = []
    late: list[int] = []
    for row in rows:
        event_time = int(row["event_time"])
        if event_time <= watermark:
            late_rows.append(dict(row))
            late.append(event_time)
            continue
        if event_time <= next_watermark:
            workspace_id = int(row["workspace_id"])
            totals[workspace_id] = int(totals.get(workspace_id, 0)) + int(row["amount"])
            applied.append(event_time)

    state["watermark"] = next_watermark
    return applied, late


def late_event_times(state: dict[str, object]) -> list[int]:
    late_rows = state["late_rows"]
    assert isinstance(late_rows, list)
    return [int(row["event_time"]) for row in late_rows]


def repair_late_rows(state: dict[str, object]) -> list[int]:
    totals = state["totals"]
    late_rows = state["late_rows"]
    assert isinstance(totals, dict)
    assert isinstance(late_rows, list)

    repaired: list[int] = []
    for row in late_rows:
        workspace_id = int(row["workspace_id"])
        totals[workspace_id] = int(totals.get(workspace_id, 0)) + int(row["amount"])
        repaired.append(int(row["event_time"]))
    late_rows.clear()
    return repaired


def workspace_totals(state: dict[str, object]) -> dict[int, int]:
    totals = state["totals"]
    assert isinstance(totals, dict)
    return {int(workspace_id): int(total) for workspace_id, total in totals.items()}
