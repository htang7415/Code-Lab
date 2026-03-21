import pytest

from flashattention_and_io_aware_attention import (
    attention_score_matrix_bytes,
    attention_tile_bytes,
    attention_tile_rounds,
    flashattention_memory_reduction_factor,
)


def test_attention_score_matrix_bytes_matches_quadratic_length_growth() -> None:
    assert attention_score_matrix_bytes(sequence_length=4, bytes_per_score=2, heads=2) == 64


def test_attention_tile_bytes_matches_tile_working_set() -> None:
    assert attention_tile_bytes(query_tile=2, key_tile=4, bytes_per_score=2, heads=2) == 32


def test_attention_tile_rounds_counts_query_and_key_blocks() -> None:
    assert attention_tile_rounds(sequence_length=10, query_tile=4, key_tile=5) == 6


def test_flashattention_memory_reduction_factor_compares_full_to_tile_bytes() -> None:
    assert flashattention_memory_reduction_factor(
        sequence_length=8,
        query_tile=2,
        key_tile=4,
        bytes_per_score=2,
        heads=2,
    ) == pytest.approx(8.0)


def test_flashattention_validates_positive_arguments() -> None:
    with pytest.raises(ValueError, match="positive"):
        attention_score_matrix_bytes(sequence_length=0)
    with pytest.raises(ValueError, match="positive"):
        attention_tile_bytes(query_tile=0, key_tile=4)
    with pytest.raises(ValueError, match="positive"):
        attention_tile_rounds(sequence_length=8, query_tile=4, key_tile=0)
