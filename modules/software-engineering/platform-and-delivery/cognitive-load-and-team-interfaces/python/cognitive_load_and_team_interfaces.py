from __future__ import annotations


def team_cognitive_load(services: int, workflows: int, pager_domains: int) -> str:
    if min(services, workflows, pager_domains) < 0:
        raise ValueError("inputs must be non-negative")
    score = services + workflows + pager_domains
    if score >= 10:
        return "high"
    if score >= 5:
        return "medium"
    return "low"


def interface_clarity(owned_components: int, shared_components: int) -> str:
    if owned_components < 0 or shared_components < 0:
        raise ValueError("inputs must be non-negative")
    if shared_components == 0:
        return "clear"
    if shared_components < owned_components:
        return "mixed"
    return "blurred"


def boundary_rework_needed(load: str, clarity: str) -> bool:
    return load == "high" or clarity == "blurred"
