from __future__ import annotations

from resilient_transition_batch import resilient_transition_batch


def test_resilient_transition_batch_returns_vectorized_resilient_indicators() -> None:
    assert resilient_transition_batch([False, True, False]) == [1.0, 0.0, 1.0]


def test_resilient_transition_batch_returns_empty_list_for_empty_batch() -> None:
    assert resilient_transition_batch([]) == []
