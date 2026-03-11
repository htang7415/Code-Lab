import pytest

from refresh_backfill_strategies import (
    backfill_rows,
    choose_strategy,
    incremental_rows,
    source_row,
    strategy_summary,
)


def test_forward_window_uses_incremental_refresh():
    rows = [
        source_row(100, 7, 10),
        source_row(110, 7, 20),
        source_row(120, 8, 5),
    ]

    assert choose_strategy(current_watermark=105, request_start=106, request_end=120) == "incremental-refresh"
    assert incremental_rows(rows, current_watermark=105, next_watermark=120) == [110, 120]


def test_historical_gap_uses_backfill_and_invalid_range_raises():
    rows = [
        source_row(90, 7, 10),
        source_row(95, 7, 20),
        source_row(120, 8, 5),
    ]

    assert choose_strategy(current_watermark=105, request_start=90, request_end=100) == "backfill"
    assert backfill_rows(rows, start_time=90, end_time=100) == [90, 95]
    assert strategy_summary(rows, current_watermark=105, request_start=90, request_end=100)["strategy"] == "backfill"

    with pytest.raises(ValueError):
        choose_strategy(current_watermark=105, request_start=100, request_end=90)
