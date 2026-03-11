from plan_regression_debugging import (
    plan_regressed,
    regression_signals,
    summarize_plan,
)


def test_summarize_plan_extracts_the_main_regression_markers() -> None:
    summary = summarize_plan(
        [
            "SEARCH runs USING INDEX idx_runs_workspace_created (workspace_id=?)",
            "USE TEMP B-TREE FOR ORDER BY",
        ]
    )

    assert summary == {
        "full_scan": False,
        "uses_index": True,
        "temp_sort": True,
    }


def test_regression_signals_detect_lost_index_and_new_sort_work() -> None:
    baseline = summarize_plan(
        ["SEARCH runs USING INDEX idx_runs_workspace_created (workspace_id=?)"]
    )
    current = summarize_plan(
        ["SCAN runs", "USE TEMP B-TREE FOR ORDER BY"]
    )

    assert regression_signals(baseline, current) == [
        "new-full-scan",
        "lost-index",
        "new-temp-sort",
    ]
    assert plan_regressed(baseline, current) is True


def test_same_or_improved_plan_is_not_marked_as_regressed() -> None:
    baseline = summarize_plan(["SCAN runs"])
    current = summarize_plan(["SEARCH runs USING INDEX idx_runs_workspace_created"])

    assert regression_signals(baseline, current) == []
    assert plan_regressed(baseline, current) is False
