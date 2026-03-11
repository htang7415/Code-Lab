from __future__ import annotations

import pytest

from progressive_delivery import blast_radius, next_rollout_stage, should_pause_rollout


def test_next_rollout_stage_expands_only_when_healthy() -> None:
    assert next_rollout_stage(current_percentage=10, healthy=True) == 25
    assert next_rollout_stage(current_percentage=10, healthy=False) == 10


def test_blast_radius_estimates_exposed_user_count() -> None:
    assert blast_radius(current_percentage=10, total_users=100000) == 10000


def test_should_pause_rollout_uses_error_rate_guardrail() -> None:
    assert should_pause_rollout(error_rate_delta=0.02, max_allowed_delta=0.01) is True
    assert should_pause_rollout(error_rate_delta=0.005, max_allowed_delta=0.01) is False

    with pytest.raises(ValueError):
        next_rollout_stage(current_percentage=7, healthy=True)
