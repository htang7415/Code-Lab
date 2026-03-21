def _validate_positive(*values: int) -> None:
    if any(value <= 0 for value in values):
        raise ValueError("all arguments must be positive")


def attention_score_matrix_bytes(
    sequence_length: int,
    bytes_per_score: int = 2,
    batch_size: int = 1,
    heads: int = 1,
) -> int:
    _validate_positive(sequence_length, bytes_per_score, batch_size, heads)
    return batch_size * heads * sequence_length * sequence_length * bytes_per_score


def attention_tile_bytes(
    query_tile: int,
    key_tile: int,
    bytes_per_score: int = 2,
    batch_size: int = 1,
    heads: int = 1,
) -> int:
    _validate_positive(query_tile, key_tile, bytes_per_score, batch_size, heads)
    return batch_size * heads * query_tile * key_tile * bytes_per_score


def attention_tile_rounds(sequence_length: int, query_tile: int, key_tile: int) -> int:
    _validate_positive(sequence_length, query_tile, key_tile)
    q_tiles = (sequence_length + query_tile - 1) // query_tile
    k_tiles = (sequence_length + key_tile - 1) // key_tile
    return q_tiles * k_tiles


def flashattention_memory_reduction_factor(
    sequence_length: int,
    query_tile: int,
    key_tile: int,
    bytes_per_score: int = 2,
    batch_size: int = 1,
    heads: int = 1,
) -> float:
    full = attention_score_matrix_bytes(
        sequence_length=sequence_length,
        bytes_per_score=bytes_per_score,
        batch_size=batch_size,
        heads=heads,
    )
    tile = attention_tile_bytes(
        query_tile=query_tile,
        key_tile=key_tile,
        bytes_per_score=bytes_per_score,
        batch_size=batch_size,
        heads=heads,
    )
    return full / tile
