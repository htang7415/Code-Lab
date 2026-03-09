import pytest

from done_indicator_batch import done_indicator_batch


def test_done_indicator_batch_maps_done_flags_to_numeric_indicators() -> None:
    indicators = done_indicator_batch([False, True, False, True])

    assert indicators == pytest.approx([0.0, 1.0, 0.0, 1.0])


def test_done_indicator_batch_returns_empty_list_for_empty_input() -> None:
    assert done_indicator_batch([]) == []


def test_done_indicator_batch_allows_all_done_batch() -> None:
    assert done_indicator_batch([True, True]) == pytest.approx([1.0, 1.0])
