from __future__ import annotations


def row_parallel_linear_stats(
    batch_tokens: int,
    input_dim: int,
    output_dim: int,
    num_shards: int,
    bytes_per_element: int = 2,
) -> tuple[int, int]:
    if batch_tokens <= 0:
        raise ValueError("batch_tokens must be positive")
    if input_dim <= 0:
        raise ValueError("input_dim must be positive")
    if output_dim <= 0:
        raise ValueError("output_dim must be positive")
    if num_shards <= 0:
        raise ValueError("num_shards must be positive")
    if bytes_per_element <= 0:
        raise ValueError("bytes_per_element must be positive")
    if input_dim % num_shards != 0:
        raise ValueError("input_dim must be divisible by num_shards")

    local_input_dim = input_dim // num_shards
    all_reduce_bytes = batch_tokens * output_dim * bytes_per_element
    return local_input_dim, all_reduce_bytes
