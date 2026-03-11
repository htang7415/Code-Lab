"""tenant_partitioning_basics - partition by tenant to keep each tenant localized."""

from __future__ import annotations


def validate_strategy(strategy: str) -> None:
    if strategy not in {"tenant", "row"}:
        raise ValueError("strategy must be 'tenant' or 'row'")


def stable_partition(value: str, partition_count: int) -> int:
    if partition_count <= 0:
        raise ValueError("partition_count must be positive")
    stable_hash = sum((index + 1) * ord(char) for index, char in enumerate(value))
    return stable_hash % partition_count


def partition_rows_by_tenant(
    rows: list[dict[str, str]],
    partition_count: int,
) -> dict[int, list[str]]:
    partitions = {partition_id: [] for partition_id in range(partition_count)}
    for row in rows:
        partition_id = stable_partition(str(row["tenant_id"]), partition_count)
        partitions[partition_id].append(str(row["row_id"]))
    return partitions


def partition_rows_by_row_id(
    rows: list[dict[str, str]],
    partition_count: int,
) -> dict[int, list[str]]:
    partitions = {partition_id: [] for partition_id in range(partition_count)}
    for row in rows:
        partition_id = stable_partition(str(row["row_id"]), partition_count)
        partitions[partition_id].append(str(row["row_id"]))
    return partitions


def tenant_partition_span(
    rows: list[dict[str, str]],
    partition_count: int,
    strategy: str,
) -> dict[str, int]:
    validate_strategy(strategy)
    spans: dict[str, set[int]] = {}
    for row in rows:
        tenant_id = str(row["tenant_id"])
        key = str(row["tenant_id"]) if strategy == "tenant" else str(row["row_id"])
        partition_id = stable_partition(key, partition_count)
        spans.setdefault(tenant_id, set()).add(partition_id)
    return {tenant_id: len(partition_ids) for tenant_id, partition_ids in spans.items()}
