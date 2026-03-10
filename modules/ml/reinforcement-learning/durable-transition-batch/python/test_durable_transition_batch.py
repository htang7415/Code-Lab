from __future__ import annotations

from durable_transition_batch import durable_transition_batch


def test_durable_transition_batch_returns_vectorized_durable_indicators() -> None:
    assert durable_transition_batch([False, True, False]) == [1.0, 0.0, 1.0]


def test_durable_transition_batch_returns_empty_list_for_empty_batch() -> None:
    assert durable_transition_batch([]) == []
