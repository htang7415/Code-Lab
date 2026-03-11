import pytest

from secondary_indexes_in_lsm_systems import (
    build_secondary_index,
    lookup_secondary,
    storage_entries,
    write_entries_per_row,
)


def test_secondary_index_supports_non_primary_lookups_with_fanout():
    rows = [
        {"id": "u1", "email": "a@example.com", "tier": "pro"},
        {"id": "u2", "email": "b@example.com", "tier": "pro"},
        {"id": "u3", "email": "c@example.com", "tier": "free"},
    ]

    index = build_secondary_index(rows, "tier")

    assert lookup_secondary(index, "pro") == ["u1", "u2"]
    assert lookup_secondary(index, "free") == ["u3"]
    assert lookup_secondary(index, "missing") == []


def test_each_secondary_index_adds_extra_write_entries():
    assert write_entries_per_row(0) == 1
    assert write_entries_per_row(2) == 3
    assert storage_entries(row_count=100, index_count=2) == 300

    with pytest.raises(ValueError):
        write_entries_per_row(-1)
