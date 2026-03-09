from __future__ import annotations

from undone_indicator import undone_indicator


def test_undone_indicator_maps_done_flags_to_continuation_flags() -> None:
    assert undone_indicator([False, True, False, True]) == [1.0, 0.0, 1.0, 0.0]


def test_undone_indicator_returns_empty_batch_for_empty_input() -> None:
    assert undone_indicator([]) == []
