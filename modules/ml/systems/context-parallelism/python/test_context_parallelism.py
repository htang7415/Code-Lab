import pytest

from context_parallelism import context_parallel_attention_stats


def test_context_parallel_attention_stats_even_split() -> None:
    local_tokens, remote_kv_bytes = context_parallel_attention_stats(
        sequence_length=8192,
        hidden_size=4096,
        num_shards=8,
    )

    assert local_tokens == 1024
    assert remote_kv_bytes == 117440512


def test_context_parallel_attention_stats_uneven_split() -> None:
    local_tokens, remote_kv_bytes = context_parallel_attention_stats(
        sequence_length=10,
        hidden_size=16,
        num_shards=3,
        bytes_per_element=2,
    )

    assert local_tokens == 4
    assert remote_kv_bytes == 384


def test_context_parallel_attention_stats_validates_inputs() -> None:
    with pytest.raises(ValueError, match="sequence_length"):
        context_parallel_attention_stats(0, 128, 2)
