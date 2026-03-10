from __future__ import annotations

from alive_transition_batch import alive_transition_batch


def test_alive_transition_batch_returns_vectorized_alive_indicators() -> None:
    assert alive_transition_batch([False, False, True]) == [1.0, 1.0, 0.0]


def test_alive_transition_batch_returns_empty_list_for_empty_batch() -> None:
    assert alive_transition_batch([]) == []
