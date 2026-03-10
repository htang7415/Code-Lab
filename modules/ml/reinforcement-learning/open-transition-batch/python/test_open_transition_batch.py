from __future__ import annotations

from open_transition_batch import open_transition_batch


def test_open_transition_batch_returns_vectorized_open_indicators() -> None:
    assert open_transition_batch([False, True, False]) == [1.0, 0.0, 1.0]


def test_open_transition_batch_returns_empty_list_for_empty_batch() -> None:
    assert open_transition_batch([]) == []
