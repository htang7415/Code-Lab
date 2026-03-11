from __future__ import annotations


def required_quality_attributes(user_facing: bool, high_scale: bool, strict_correctness: bool) -> list[str]:
    attributes: list[str] = []
    if user_facing:
        attributes.extend(["latency", "availability"])
    if high_scale:
        attributes.append("scalability")
    if strict_correctness:
        attributes.append("correctness")
    return attributes or ["simplicity"]


def dominant_failure_model(external_dependencies: int, stateful_components: int, overload_risk: bool) -> str:
    if external_dependencies < 0 or stateful_components < 0:
        raise ValueError("counts must be non-negative")
    if overload_risk:
        return "overload"
    if external_dependencies >= stateful_components:
        return "dependency-failure"
    return "state-failure"


def architecture_focus(requirements: list[str], failure_model: str) -> str:
    normalized_failure_model = failure_model.strip().lower()
    requirement_set = {requirement.strip().lower() for requirement in requirements if requirement.strip()}

    if normalized_failure_model == "overload":
        return "shed load and protect tail latency"
    if normalized_failure_model == "dependency-failure":
        return "isolate dependencies and add fallbacks"
    if normalized_failure_model == "state-failure":
        return "protect consistency and recovery paths"
    raise ValueError("unknown failure_model")
