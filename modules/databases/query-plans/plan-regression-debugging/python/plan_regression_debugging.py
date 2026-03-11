"""plan_regression_debugging - compare baseline and current plan summaries."""

from __future__ import annotations


def summarize_plan(plan_details: list[str]) -> dict[str, bool]:
    joined = " | ".join(plan_details)
    return {
        "full_scan": "SCAN " in joined,
        "uses_index": "USING INDEX" in joined or "USING COVERING INDEX" in joined,
        "temp_sort": "USE TEMP B-TREE FOR ORDER BY" in joined,
    }


def regression_signals(
    baseline: dict[str, bool],
    current: dict[str, bool],
) -> list[str]:
    signals: list[str] = []
    if not baseline["full_scan"] and current["full_scan"]:
        signals.append("new-full-scan")
    if baseline["uses_index"] and not current["uses_index"]:
        signals.append("lost-index")
    if not baseline["temp_sort"] and current["temp_sort"]:
        signals.append("new-temp-sort")
    return signals


def plan_regressed(
    baseline: dict[str, bool],
    current: dict[str, bool],
) -> bool:
    return len(regression_signals(baseline, current)) > 0
