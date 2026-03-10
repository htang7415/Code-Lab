from __future__ import annotations

from steady_transition_batch import steady_transition_batch


def test_steady_transition_batch_returns_vectorized_steady_indicators() -> None:
    assert steady_transition_batch([False, True, False]) == [1.0, 0.0, 1.0]


def test_steady_transition_batch_returns_empty_list_for_empty_batch() -> None:
    assert steady_transition_batch([]) == []
