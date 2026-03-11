from __future__ import annotations

import pytest

from judge_and_trace_grading import (
    judge_trace_route,
    mean_judge_score,
    trace_grade_packet,
)


def test_judge_and_trace_grading_builds_packet_from_score_and_trace() -> None:
    score = mean_judge_score([0.9, 0.8, 0.7])
    assert score == pytest.approx(0.8)

    packet = trace_grade_packet("run_7", score, ["done", "blocked", "done"])
    assert packet == {
        "run_id": "run_7",
        "judge_score": pytest.approx(0.8),
        "step_statuses": ["done", "blocked", "done"],
        "blocked_or_failed_steps": 1,
    }


def test_judge_and_trace_route_distinguishes_pass_review_and_fail() -> None:
    assert judge_trace_route(0.85, blocked_or_failed_steps=0, threshold=0.8) == "pass"
    assert judge_trace_route(0.85, blocked_or_failed_steps=1, threshold=0.8) == "review"
    assert judge_trace_route(0.72, blocked_or_failed_steps=0, threshold=0.8) == "fail"


def test_judge_and_trace_grading_validation() -> None:
    with pytest.raises(ValueError):
        mean_judge_score([])
    with pytest.raises(ValueError):
        mean_judge_score([1.2])
    with pytest.raises(ValueError):
        trace_grade_packet("", 0.8, ["done"])
    with pytest.raises(ValueError):
        trace_grade_packet("run_7", 0.8, [])
    with pytest.raises(ValueError):
        judge_trace_route(0.8, blocked_or_failed_steps=-1, threshold=0.8)
