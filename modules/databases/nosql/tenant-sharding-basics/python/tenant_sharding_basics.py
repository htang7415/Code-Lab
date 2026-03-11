"""tenant_sharding_basics - hash-based tenant routing with manual overrides."""

from __future__ import annotations


def default_shard(tenant_id: str, shard_count: int) -> int:
    if shard_count <= 0:
        raise ValueError("shard_count must be positive")
    stable_hash = sum((index + 1) * ord(char) for index, char in enumerate(tenant_id))
    return stable_hash % shard_count


def route_tenant(
    tenant_id: str,
    shard_count: int,
    overrides: dict[str, int] | None = None,
) -> int:
    if overrides is not None and tenant_id in overrides:
        return int(overrides[tenant_id])
    return default_shard(tenant_id, shard_count)


def shard_loads(
    tenant_sizes: dict[str, int],
    shard_count: int,
    overrides: dict[str, int] | None = None,
) -> dict[int, int]:
    loads = {shard_id: 0 for shard_id in range(shard_count)}
    for tenant_id, size in tenant_sizes.items():
        loads[route_tenant(tenant_id, shard_count, overrides)] += int(size)
    return loads


def hottest_shard(loads: dict[int, int]) -> int:
    return max(loads, key=lambda shard_id: (loads[shard_id], -shard_id))
