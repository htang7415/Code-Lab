from __future__ import annotations

from continuing_transition_batch import continuing_transition_batch


def test_continuing_transition_batch_returns_vectorized_continuation_indicators() -> None:
    assert continuing_transition_batch([False, True, False]) == [1.0, 0.0, 1.0]


def test_continuing_transition_batch_returns_empty_list_for_empty_batch() -> None:
    assert continuing_transition_batch([]) == []
