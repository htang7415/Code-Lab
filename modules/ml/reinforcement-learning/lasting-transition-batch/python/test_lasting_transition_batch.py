from __future__ import annotations

from lasting_transition_batch import lasting_transition_batch


def test_lasting_transition_batch_returns_vectorized_lasting_indicators() -> None:
    assert lasting_transition_batch([False, True, False]) == [1.0, 0.0, 1.0]


def test_lasting_transition_batch_returns_empty_list_for_empty_batch() -> None:
    assert lasting_transition_batch([]) == []
