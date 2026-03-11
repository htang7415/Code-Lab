from tenant_sharding_basics import default_shard, hottest_shard, route_tenant, shard_loads


def test_hash_routing_is_stable_for_normal_tenants():
    shard = default_shard("tenant-7", shard_count=4)

    assert route_tenant("tenant-7", shard_count=4) == shard
    assert route_tenant("tenant-7", shard_count=4) == shard


def test_hot_tenant_override_can_move_load_off_default_shard():
    tenant_sizes = {"tenant-7": 10, "tenant-8": 12, "tenant-99": 500}
    default_target = default_shard("tenant-99", shard_count=4)
    override_target = (default_target + 1) % 4

    default_loads = shard_loads(tenant_sizes, shard_count=4)
    overridden_loads = shard_loads(
        tenant_sizes,
        shard_count=4,
        overrides={"tenant-99": override_target},
    )

    assert route_tenant("tenant-99", 4, {"tenant-99": override_target}) == override_target
    assert overridden_loads[override_target] >= 500
    assert overridden_loads[default_target] <= default_loads[default_target] - 500
    assert hottest_shard(overridden_loads) == override_target
