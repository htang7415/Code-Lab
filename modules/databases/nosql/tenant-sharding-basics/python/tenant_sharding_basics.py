"""tenant_sharding_basics - hash-based tenant routing with manual overrides."""

from __future__ import annotations


def validate_override(shard_id: int, shard_count: int) -> None:
    if shard_id < 0 or shard_id >= shard_count:
        raise ValueError("override shard must be between 0 and shard_count - 1")


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
        override = int(overrides[tenant_id])
        validate_override(override, shard_count)
        return override
    return default_shard(tenant_id, shard_count)


def shard_loads(
    tenant_sizes: dict[str, int],
    shard_count: int,
    overrides: dict[str, int] | None = None,
) -> dict[int, int]:
    loads = {shard_id: 0 for shard_id in range(shard_count)}
    for tenant_id, size in tenant_sizes.items():
        if int(size) < 0:
            raise ValueError("tenant size must be non-negative")
        loads[route_tenant(tenant_id, shard_count, overrides)] += int(size)
    return loads


def hottest_shard(loads: dict[int, int]) -> int:
    return max(loads, key=lambda shard_id: (loads[shard_id], -shard_id))
