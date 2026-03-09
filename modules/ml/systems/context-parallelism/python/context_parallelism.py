from __future__ import annotations

import math


def context_parallel_attention_stats(
    sequence_length: int,
    hidden_size: int,
    num_shards: int,
    bytes_per_element: int = 2,
) -> tuple[int, int]:
    if sequence_length <= 0:
        raise ValueError("sequence_length must be positive")
    if hidden_size <= 0:
        raise ValueError("hidden_size must be positive")
    if num_shards <= 0:
        raise ValueError("num_shards must be positive")
    if bytes_per_element <= 0:
        raise ValueError("bytes_per_element must be positive")

    local_tokens = math.ceil(sequence_length / num_shards)
    remote_tokens = max(sequence_length - local_tokens, 0)
    remote_kv_bytes = 2 * remote_tokens * hidden_size * bytes_per_element
    return local_tokens, remote_kv_bytes
