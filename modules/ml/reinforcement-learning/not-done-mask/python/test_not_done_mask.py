import pytest

from not_done_mask import not_done_mask


def test_not_done_mask_maps_done_flags_to_not_done_values() -> None:
    mask = not_done_mask([False, True, False, True])

    assert mask == pytest.approx([1.0, 0.0, 1.0, 0.0])


def test_not_done_mask_returns_empty_list_for_empty_input() -> None:
    assert not_done_mask([]) == []


def test_not_done_mask_allows_all_continuing_batch() -> None:
    assert not_done_mask([False, False]) == pytest.approx([1.0, 1.0])
