import pytest

from tensor_parallelism import row_parallel_linear_stats


def test_row_parallel_linear_stats_returns_local_width_and_payload() -> None:
    local_input_dim, all_reduce_bytes = row_parallel_linear_stats(
        batch_tokens=128,
        input_dim=4096,
        output_dim=11008,
        num_shards=8,
    )

    assert local_input_dim == 512
    assert all_reduce_bytes == 2818048


def test_row_parallel_linear_stats_allows_single_shard() -> None:
    local_input_dim, all_reduce_bytes = row_parallel_linear_stats(
        batch_tokens=32,
        input_dim=1024,
        output_dim=2048,
        num_shards=1,
        bytes_per_element=4,
    )

    assert local_input_dim == 1024
    assert all_reduce_bytes == 262144


def test_row_parallel_linear_stats_requires_divisible_input_dim() -> None:
    with pytest.raises(ValueError, match="divisible"):
        row_parallel_linear_stats(16, 1025, 2048, 8)
