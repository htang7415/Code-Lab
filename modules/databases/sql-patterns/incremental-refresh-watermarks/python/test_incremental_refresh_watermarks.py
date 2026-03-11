import pytest

from incremental_refresh_watermarks import (
    apply_incremental_refresh,
    current_watermark,
    empty_refresh_state,
    full_rebuild,
    source_row,
    workspace_totals,
)


def test_incremental_refresh_only_applies_rows_beyond_last_watermark():
    rows = [
        source_row(100, 7, 10),
        source_row(105, 7, 20),
        source_row(120, 8, 5),
    ]
    state = empty_refresh_state()

    assert apply_incremental_refresh(state, rows, next_watermark=105) == [100, 105]
    assert workspace_totals(state) == {7: 30}
    assert current_watermark(state) == 105

    assert apply_incremental_refresh(state, rows, next_watermark=120) == [120]
    assert workspace_totals(state) == {7: 30, 8: 5}
    assert workspace_totals(state) == full_rebuild(rows, up_to_watermark=120)


def test_watermark_cannot_move_backwards():
    state = empty_refresh_state()
    apply_incremental_refresh(state, [], next_watermark=10)

    with pytest.raises(ValueError):
        apply_incremental_refresh(state, [], next_watermark=9)
