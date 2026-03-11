from __future__ import annotations


def select_incident_route(
    route_scores: dict[str, float],
    min_score: float,
    min_margin: float = 0.0,
) -> str:
    if min_margin < 0.0:
        raise ValueError("min_margin must be non-negative")
    if not route_scores:
        raise ValueError("route_scores must be non-empty")

    cleaned: list[tuple[str, float]] = []
    for route_name, score in route_scores.items():
        cleaned_name = route_name.strip()
        if not cleaned_name:
            raise ValueError("route names must be non-empty")
        if score < 0.0:
            raise ValueError("route scores must be non-negative")
        cleaned.append((cleaned_name, float(score)))

    cleaned.sort(key=lambda item: (-item[1], item[0]))
    top_route, top_score = cleaned[0]
    if top_score < min_score:
        return "clarify"

    second_score = cleaned[1][1] if len(cleaned) > 1 else float("-inf")
    if second_score != float("-inf") and top_score - second_score < min_margin:
        return "review"
    return top_route


def remaining_latency_budget(
    total_budget_ms: int,
    elapsed_ms: int,
    reserved_response_ms: int = 0,
) -> int:
    if total_budget_ms < 0 or elapsed_ms < 0 or reserved_response_ms < 0:
        raise ValueError("latency budget values must be non-negative")
    return max(total_budget_ms - elapsed_ms - reserved_response_ms, 0)


def incident_escalation_reason(
    blocked: bool,
    confidence: float,
    min_confidence: float,
    attempt: int,
    max_attempts: int,
    remaining_budget_ms: int,
    required_step_budget_ms: int,
) -> str | None:
    if not 0.0 <= confidence <= 1.0:
        raise ValueError("confidence must satisfy 0 <= value <= 1")
    if not 0.0 <= min_confidence <= 1.0:
        raise ValueError("min_confidence must satisfy 0 <= value <= 1")
    if attempt < 0 or max_attempts < 0:
        raise ValueError("attempt and max_attempts must be non-negative")
    if remaining_budget_ms < 0 or required_step_budget_ms < 0:
        raise ValueError("budget values must be non-negative")

    if blocked:
        return "policy"
    if confidence < min_confidence:
        return "low-confidence"
    if attempt >= max_attempts:
        return "retries-exhausted"
    if remaining_budget_ms < required_step_budget_ms:
        return "latency-budget"
    return None


def triage_trace_packet(
    route: str,
    action: str,
    reason: str | None,
    remaining_budget_ms: int,
) -> dict[str, object]:
    return {
        "route": route,
        "action": action,
        "reason": reason,
        "remaining_budget_ms": remaining_budget_ms,
        "status": "escalated" if action == "escalate" else action,
    }


def incident_triage_workflow(
    route_scores: dict[str, float],
    blocked: bool,
    confidence: float,
    attempt: int,
    max_attempts: int,
    total_budget_ms: int,
    elapsed_ms: int,
    required_step_budget_ms: int,
    min_route_score: float = 0.6,
    min_route_margin: float = 0.1,
    min_confidence: float = 0.7,
    reserved_response_ms: int = 0,
) -> dict[str, object]:
    route = select_incident_route(
        route_scores,
        min_score=min_route_score,
        min_margin=min_route_margin,
    )
    remaining_budget_ms = remaining_latency_budget(
        total_budget_ms,
        elapsed_ms,
        reserved_response_ms=reserved_response_ms,
    )
    reason = incident_escalation_reason(
        blocked=blocked,
        confidence=confidence,
        min_confidence=min_confidence,
        attempt=attempt,
        max_attempts=max_attempts,
        remaining_budget_ms=remaining_budget_ms,
        required_step_budget_ms=required_step_budget_ms,
    )

    if reason is not None:
        action = "escalate"
    elif route in {"clarify", "review"}:
        action = route
    else:
        action = f"execute:{route}"

    return {
        "route": route,
        "action": action,
        "reason": reason,
        "remaining_budget_ms": remaining_budget_ms,
        "trace": triage_trace_packet(route, action, reason, remaining_budget_ms),
    }
