import pytest

from expert_parallelism import expert_parallel_dispatch_stats


def test_expert_parallel_dispatch_stats_counts_remote_tokens() -> None:
    load_per_shard, remote_dispatches = expert_parallel_dispatch_stats(
        token_home_shards=[0, 0, 1, 1],
        expert_assignments=[0, 3, 1, 2],
        experts_per_shard=2,
    )

    assert load_per_shard == [2, 2]
    assert remote_dispatches == 2


def test_expert_parallel_dispatch_stats_handles_empty_inputs() -> None:
    load_per_shard, remote_dispatches = expert_parallel_dispatch_stats([], [], experts_per_shard=4)

    assert load_per_shard == []
    assert remote_dispatches == 0


def test_expert_parallel_dispatch_stats_validates_lengths() -> None:
    with pytest.raises(ValueError, match="same length"):
        expert_parallel_dispatch_stats([0], [0, 1], experts_per_shard=2)
