import pytest

from chunked_prefill import chunked_prefill_rounds


def test_chunked_prefill_rounds_splits_longer_requests_across_rounds() -> None:
    assert chunked_prefill_rounds([20, 5, 9], chunk_size=8) == [21, 9, 4]


def test_chunked_prefill_rounds_handles_single_request() -> None:
    assert chunked_prefill_rounds([10], chunk_size=4) == [4, 4, 2]


def test_chunked_prefill_rounds_requires_positive_chunk_size() -> None:
    with pytest.raises(ValueError, match="chunk_size"):
        chunked_prefill_rounds([10], chunk_size=0)
