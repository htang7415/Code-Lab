"""secondary_indexes_in_lsm_systems - secondary indexes trade extra writes for new lookups."""

from __future__ import annotations


def write_entries_per_row(index_count: int) -> int:
    if index_count < 0:
        raise ValueError("index_count must be non-negative")
    return 1 + index_count


def build_secondary_index(
    rows: list[dict[str, object]],
    field: str,
) -> dict[object, list[str]]:
    index: dict[object, list[str]] = {}
    for row in rows:
        value = row.get(field)
        index.setdefault(value, []).append(str(row["id"]))
    return {
        value: sorted(ids)
        for value, ids in index.items()
    }


def lookup_secondary(
    index: dict[object, list[str]],
    value: object,
) -> list[str]:
    return list(index.get(value, []))


def storage_entries(row_count: int, index_count: int) -> int:
    return row_count * write_entries_per_row(index_count)
