from __future__ import annotations

import pytest

from ownership_boundaries import boundary_health, escalation_needed, ownership_model


def test_ownership_model_distinguishes_service_and_platform_ownership() -> None:
    assert ownership_model(single_team_owner=True, many_consumers=True) == "platform-owner"
    assert ownership_model(single_team_owner=True, many_consumers=False) == "service-owner"
    assert ownership_model(single_team_owner=False, many_consumers=True) == "shared-ownership"


def test_boundary_health_declines_with_ambiguity_or_excess_handoffs() -> None:
    assert boundary_health(shared_services=2, cross_team_handoffs=1, ambiguous_owner=False) == "healthy"
    assert boundary_health(shared_services=4, cross_team_handoffs=1, ambiguous_owner=False) == "strained"
    assert boundary_health(shared_services=2, cross_team_handoffs=1, ambiguous_owner=True) == "poor"


def test_escalation_needed_for_strained_or_poor_boundaries() -> None:
    assert escalation_needed(shared_services=5, cross_team_handoffs=4, ambiguous_owner=True) is True
    assert escalation_needed(shared_services=1, cross_team_handoffs=0, ambiguous_owner=False) is False

    with pytest.raises(ValueError):
        boundary_health(shared_services=-1, cross_team_handoffs=0, ambiguous_owner=False)
