from __future__ import annotations

from sustained_transition_batch import sustained_transition_batch


def test_sustained_transition_batch_returns_vectorized_sustained_indicators() -> None:
    assert sustained_transition_batch([False, True, False]) == [1.0, 0.0, 1.0]


def test_sustained_transition_batch_returns_empty_list_for_empty_batch() -> None:
    assert sustained_transition_batch([]) == []
