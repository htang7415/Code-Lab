from __future__ import annotations

import pytest

from background_jobs_and_workflows import queue_priority, should_background_job, workflow_kind


def test_should_background_job_moves_slow_or_retry_prone_work_out_of_request_path() -> None:
    assert should_background_job(user_waiting=True, duration_ms=1500, retries_expected=False) is True
    assert should_background_job(user_waiting=True, duration_ms=100, retries_expected=False) is False
    assert should_background_job(user_waiting=True, duration_ms=100, retries_expected=True) is True


def test_workflow_kind_distinguishes_multi_step_or_human_gated_processes() -> None:
    assert workflow_kind(needs_human_approval=False, has_multiple_steps=False) == "single-job"
    assert workflow_kind(needs_human_approval=False, has_multiple_steps=True) == "workflow"


def test_queue_priority_depends_on_user_visibility_and_deadline() -> None:
    assert queue_priority(user_visible=True, deadline_ms=2000) == "high"
    assert queue_priority(user_visible=True, deadline_ms=10000) == "medium"
    assert queue_priority(user_visible=False, deadline_ms=None) == "low"

    with pytest.raises(ValueError):
        queue_priority(user_visible=True, deadline_ms=-1)
