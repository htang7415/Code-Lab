"""partitioning_vs_secondary_indexes - show why pruning and indexes are complementary."""

from __future__ import annotations

from datetime import date


def month_key(date_text: str) -> str:
    value = date.fromisoformat(date_text)
    return f"{value.year:04d}-{value.month:02d}"


def build_monthly_partitions(
    rows: list[dict[str, object]],
) -> dict[str, list[dict[str, object]]]:
    partitions: dict[str, list[dict[str, object]]] = {}
    for row in rows:
        partitions.setdefault(month_key(str(row["event_date"])), []).append(row)
    return partitions


def scanned_partition_keys(
    partitions: dict[str, list[dict[str, object]]],
    start_date: str,
    end_date: str,
) -> list[str]:
    start = date.fromisoformat(start_date)
    end = date.fromisoformat(end_date)
    if end < start:
        raise ValueError("end_date must be on or after start_date")

    current = start.replace(day=1)
    limit = end.replace(day=1)
    keys: list[str] = []
    while current <= limit:
        key = f"{current.year:04d}-{current.month:02d}"
        if key in partitions:
            keys.append(key)
        if current.month == 12:
            current = date(current.year + 1, 1, 1)
        else:
            current = date(current.year, current.month + 1, 1)
    return keys


def build_workspace_secondary_index(
    partitions: dict[str, list[dict[str, object]]],
) -> dict[str, dict[int, list[dict[str, object]]]]:
    secondary: dict[str, dict[int, list[dict[str, object]]]] = {}
    for partition_key, rows in partitions.items():
        workspace_rows: dict[int, list[dict[str, object]]] = {}
        for row in rows:
            workspace_id = int(row["workspace_id"])
            workspace_rows.setdefault(workspace_id, []).append(row)
        secondary[partition_key] = workspace_rows
    return secondary


def query_with_partitioning_only(
    partitions: dict[str, list[dict[str, object]]],
    workspace_id: int,
    start_date: str,
    end_date: str,
) -> tuple[list[str], int, list[str]]:
    scanned = scanned_partition_keys(partitions, start_date, end_date)
    matches: list[str] = []
    inspected_rows = 0
    start = date.fromisoformat(start_date)
    end = date.fromisoformat(end_date)

    for partition_key in scanned:
        for row in partitions[partition_key]:
            inspected_rows += 1
            row_date = date.fromisoformat(str(row["event_date"]))
            if int(row["workspace_id"]) != workspace_id:
                continue
            if start <= row_date <= end:
                matches.append(str(row["id"]))
    return scanned, inspected_rows, matches


def query_with_secondary_index(
    partitions: dict[str, list[dict[str, object]]],
    secondary_indexes: dict[str, dict[int, list[dict[str, object]]]],
    workspace_id: int,
    start_date: str,
    end_date: str,
) -> tuple[list[str], int, list[str]]:
    scanned = scanned_partition_keys(partitions, start_date, end_date)
    matches: list[str] = []
    inspected_rows = 0
    start = date.fromisoformat(start_date)
    end = date.fromisoformat(end_date)

    for partition_key in scanned:
        candidate_rows = secondary_indexes.get(partition_key, {}).get(workspace_id, [])
        inspected_rows += len(candidate_rows)
        for row in candidate_rows:
            row_date = date.fromisoformat(str(row["event_date"]))
            if start <= row_date <= end:
                matches.append(str(row["id"]))
    return scanned, inspected_rows, matches
