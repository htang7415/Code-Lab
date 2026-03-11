"""point_lookups_vs_range_scans - compare point probes to range reads."""

from __future__ import annotations


def point_lookup_work(index_height: int) -> int:
    """Model the fixed work of descending an index to one row."""
    return max(index_height, 0) + 1


def range_scan_work(index_height: int, matching_rows: int) -> int:
    """Model tree descent plus per-row scan work."""
    return point_lookup_work(index_height) + max(matching_rows, 0)


def choose_access_path(predicate_shape: str, matching_rows: int) -> str:
    """Return the expected access path for a predicate shape."""
    normalized = predicate_shape.strip().lower()
    if normalized == "point":
        return "point-lookup"
    if normalized == "range":
        if max(matching_rows, 0) <= 1:
            return "short-range-scan"
        return "range-scan"
    raise ValueError(f"unsupported predicate shape: {predicate_shape}")


def access_summary(index_height: int, matching_rows: int) -> dict[str, int | str]:
    rows = max(matching_rows, 0)
    point_work = point_lookup_work(index_height)
    range_work = range_scan_work(index_height, rows)
    return {
        "matching_rows": rows,
        "point_lookup_work": point_work,
        "range_scan_work": range_work,
        "recommended_path": "point-lookup" if rows <= 1 else "range-scan",
    }
