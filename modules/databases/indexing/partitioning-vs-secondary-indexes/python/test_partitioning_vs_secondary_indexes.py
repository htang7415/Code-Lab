import pytest

from partitioning_vs_secondary_indexes import (
    build_monthly_partitions,
    build_workspace_secondary_index,
    query_with_partitioning_only,
    query_with_secondary_index,
    scanned_partition_keys,
)


def test_secondary_index_reduces_row_inspection_inside_pruned_partitions():
    rows = [
        {"id": "e1", "workspace_id": 7, "event_date": "2026-01-05"},
        {"id": "e2", "workspace_id": 7, "event_date": "2026-02-04"},
        {"id": "e3", "workspace_id": 8, "event_date": "2026-02-10"},
        {"id": "e4", "workspace_id": 7, "event_date": "2026-03-12"},
        {"id": "e5", "workspace_id": 8, "event_date": "2026-03-13"},
    ]
    partitions = build_monthly_partitions(rows)
    secondary = build_workspace_secondary_index(partitions)

    partition_only = query_with_partitioning_only(
        partitions,
        workspace_id=7,
        start_date="2026-02-01",
        end_date="2026-03-31",
    )
    with_index = query_with_secondary_index(
        partitions,
        secondary,
        workspace_id=7,
        start_date="2026-02-01",
        end_date="2026-03-31",
    )

    assert partition_only[0] == ["2026-02", "2026-03"]
    assert with_index[0] == ["2026-02", "2026-03"]
    assert partition_only[2] == ["e2", "e4"]
    assert with_index[2] == ["e2", "e4"]
    assert with_index[1] < partition_only[1]


def test_invalid_date_range_raises():
    with pytest.raises(ValueError):
        scanned_partition_keys({}, "2026-03-10", "2026-03-01")
