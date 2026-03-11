import pytest

from late_arriving_data_handling import (
    apply_incremental_rows,
    empty_state,
    late_event_times,
    repair_late_rows,
    source_row,
    workspace_totals,
)


def test_late_rows_are_skipped_by_normal_refresh_and_repaired_later():
    state = empty_state()
    apply_incremental_rows(
        state,
        [source_row(100, 7, 10), source_row(105, 7, 20)],
        next_watermark=105,
    )

    applied, late = apply_incremental_rows(
        state,
        [source_row(103, 7, 5), source_row(110, 8, 7)],
        next_watermark=110,
    )

    assert applied == [110]
    assert late == [103]
    assert late_event_times(state) == [103]
    assert workspace_totals(state) == {7: 30, 8: 7}

    assert repair_late_rows(state) == [103]
    assert workspace_totals(state) == {7: 35, 8: 7}


def test_watermark_cannot_move_backwards():
    state = empty_state()
    apply_incremental_rows(state, [], next_watermark=10)

    with pytest.raises(ValueError):
        apply_incremental_rows(state, [], next_watermark=9)
