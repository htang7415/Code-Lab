from __future__ import annotations

from persistent_transition_batch import persistent_transition_batch


def test_persistent_transition_batch_returns_vectorized_persistent_indicators() -> None:
    assert persistent_transition_batch([False, True, False]) == [1.0, 0.0, 1.0]


def test_persistent_transition_batch_returns_empty_list_for_empty_batch() -> None:
    assert persistent_transition_batch([]) == []
