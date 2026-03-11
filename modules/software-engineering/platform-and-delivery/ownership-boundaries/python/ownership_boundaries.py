from __future__ import annotations


def ownership_model(single_team_owner: bool, many_consumers: bool) -> str:
    if single_team_owner and many_consumers:
        return "platform-owner"
    if single_team_owner:
        return "service-owner"
    return "shared-ownership"


def boundary_health(shared_services: int, cross_team_handoffs: int, ambiguous_owner: bool) -> str:
    if shared_services < 0 or cross_team_handoffs < 0:
        raise ValueError("counts must be non-negative")
    if ambiguous_owner:
        return "poor"
    if cross_team_handoffs >= 3 or shared_services >= 4:
        return "strained"
    return "healthy"


def escalation_needed(shared_services: int, cross_team_handoffs: int, ambiguous_owner: bool) -> bool:
    return boundary_health(shared_services, cross_team_handoffs, ambiguous_owner) != "healthy"
