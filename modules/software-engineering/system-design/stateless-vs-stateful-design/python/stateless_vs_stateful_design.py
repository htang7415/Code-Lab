from __future__ import annotations


def component_style(needs_durable_session: bool, requires_local_cache_consistency: bool) -> str:
    if needs_durable_session or requires_local_cache_consistency:
        return "stateful"
    return "stateless"


def horizontal_scaling_ease(style: str) -> str:
    normalized_style = style.strip().lower()
    if normalized_style == "stateless":
        return "easy"
    if normalized_style == "stateful":
        return "harder"
    raise ValueError("style must be stateless or stateful")


def recovery_complexity(style: str) -> str:
    normalized_style = style.strip().lower()
    if normalized_style == "stateless":
        return "lower"
    if normalized_style == "stateful":
        return "higher"
    raise ValueError("style must be stateless or stateful")
