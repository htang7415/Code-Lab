"""read_amplification_in_lsm_trees - estimate how many files a point read may touch."""

from __future__ import annotations


def tables_checked_without_bloom(level_sstables: list[int]) -> int:
    return sum(max(count, 0) for count in level_sstables)


def tables_checked_with_bloom(
    level_sstables: list[int],
    false_positive_tables: int = 0,
) -> int:
    non_empty_levels = sum(1 for count in level_sstables if count > 0)
    return non_empty_levels + max(false_positive_tables, 0)


def point_lookup_cost(
    level_sstables: list[int],
    false_positive_tables: int = 0,
    table_read_ms: int = 1,
) -> dict[str, int]:
    without_bloom = tables_checked_without_bloom(level_sstables)
    with_bloom = tables_checked_with_bloom(level_sstables, false_positive_tables)
    return {
        "tables_without_bloom": without_bloom,
        "tables_with_bloom": with_bloom,
        "latency_without_bloom_ms": without_bloom * max(table_read_ms, 0),
        "latency_with_bloom_ms": with_bloom * max(table_read_ms, 0),
    }
