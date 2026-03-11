"""refresh_backfill_strategies - choose between forward refresh and historical backfill."""

from __future__ import annotations


def source_row(event_time: int, workspace_id: int, amount: int) -> dict[str, int]:
    return {
        "event_time": event_time,
        "workspace_id": workspace_id,
        "amount": amount,
    }


def incremental_rows(
    rows: list[dict[str, int]],
    current_watermark: int,
    next_watermark: int,
) -> list[int]:
    return [
        int(row["event_time"])
        for row in rows
        if current_watermark < int(row["event_time"]) <= next_watermark
    ]


def backfill_rows(
    rows: list[dict[str, int]],
    start_time: int,
    end_time: int,
) -> list[int]:
    return [
        int(row["event_time"])
        for row in rows
        if start_time <= int(row["event_time"]) <= end_time
    ]


def choose_strategy(
    current_watermark: int,
    request_start: int,
    request_end: int,
) -> str:
    if request_end < request_start:
        raise ValueError("request_end must be on or after request_start")
    return "backfill" if request_start <= current_watermark else "incremental-refresh"


def strategy_summary(
    rows: list[dict[str, int]],
    current_watermark: int,
    request_start: int,
    request_end: int,
) -> dict[str, object]:
    strategy = choose_strategy(current_watermark, request_start, request_end)
    event_times = (
        backfill_rows(rows, request_start, request_end)
        if strategy == "backfill"
        else incremental_rows(rows, current_watermark, request_end)
    )
    return {
        "strategy": strategy,
        "event_times": event_times,
        "row_count": len(event_times),
    }
