from __future__ import annotations

import pytest

from plan_act_loop import make_plan, mark_step_done, next_pending_step


def test_plan_act_loop_tracks_pending_and_completed_steps() -> None:
    plan = make_plan("Prepare launch report", ["collect metrics", "write summary", "send report"])
    assert next_pending_step(plan) == 0
    plan = mark_step_done(plan, 0)
    assert next_pending_step(plan) == 1


def test_plan_act_loop_validation_rejects_invalid_goals_or_indices() -> None:
    with pytest.raises(ValueError):
        make_plan("", ["step"])
    with pytest.raises(ValueError):
        make_plan("goal", [])
    with pytest.raises(IndexError):
        mark_step_done(make_plan("goal", ["step"]), 2)
