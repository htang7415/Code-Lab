from __future__ import annotations


def expert_parallel_dispatch_stats(
    token_home_shards: list[int],
    expert_assignments: list[int],
    experts_per_shard: int,
) -> tuple[list[int], int]:
    if len(token_home_shards) != len(expert_assignments):
        raise ValueError("token_home_shards and expert_assignments must have the same length")
    if experts_per_shard <= 0:
        raise ValueError("experts_per_shard must be positive")
    if any(shard < 0 for shard in token_home_shards):
        raise ValueError("token_home_shards must be non-negative")
    if any(expert < 0 for expert in expert_assignments):
        raise ValueError("expert_assignments must be non-negative")
    if not token_home_shards:
        return [], 0

    max_target_shard = max(expert // experts_per_shard for expert in expert_assignments)
    num_shards = max(max(token_home_shards), max_target_shard) + 1

    load_per_shard = [0] * num_shards
    remote_dispatches = 0

    for home_shard, expert in zip(token_home_shards, expert_assignments):
        target_shard = expert // experts_per_shard
        load_per_shard[target_shard] += 1
        if target_shard != home_shard:
            remote_dispatches += 1

    return load_per_shard, remote_dispatches
