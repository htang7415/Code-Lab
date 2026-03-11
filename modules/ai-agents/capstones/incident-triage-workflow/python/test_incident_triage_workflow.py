from __future__ import annotations

from incident_triage_workflow import incident_triage_workflow, select_incident_route


def test_select_incident_route_uses_thresholds_and_margins() -> None:
    assert select_incident_route({"billing": 0.4, "security": 0.3}, min_score=0.6) == "clarify"
    assert (
        select_incident_route(
            {"billing": 0.75, "security": 0.7},
            min_score=0.6,
            min_margin=0.1,
        )
        == "review"
    )


def test_incident_triage_workflow_executes_strong_route_when_feasible() -> None:
    decision = incident_triage_workflow(
        {"security": 0.9, "billing": 0.4},
        blocked=False,
        confidence=0.88,
        attempt=1,
        max_attempts=3,
        total_budget_ms=1200,
        elapsed_ms=300,
        required_step_budget_ms=250,
        reserved_response_ms=150,
    )

    assert decision["route"] == "security"
    assert decision["action"] == "execute:security"
    assert decision["reason"] is None
    assert decision["remaining_budget_ms"] == 750


def test_incident_triage_workflow_escalates_for_policy_or_retries() -> None:
    blocked = incident_triage_workflow(
        {"security": 0.9},
        blocked=True,
        confidence=0.9,
        attempt=0,
        max_attempts=2,
        total_budget_ms=1200,
        elapsed_ms=200,
        required_step_budget_ms=250,
    )
    retries = incident_triage_workflow(
        {"security": 0.9},
        blocked=False,
        confidence=0.9,
        attempt=2,
        max_attempts=2,
        total_budget_ms=1200,
        elapsed_ms=200,
        required_step_budget_ms=250,
    )

    assert blocked["action"] == "escalate"
    assert blocked["reason"] == "policy"
    assert retries["action"] == "escalate"
    assert retries["reason"] == "retries-exhausted"


def test_incident_triage_workflow_escalates_when_latency_budget_is_too_small() -> None:
    decision = incident_triage_workflow(
        {"billing": 0.85},
        blocked=False,
        confidence=0.84,
        attempt=0,
        max_attempts=2,
        total_budget_ms=500,
        elapsed_ms=320,
        required_step_budget_ms=250,
        reserved_response_ms=80,
    )

    assert decision["action"] == "escalate"
    assert decision["reason"] == "latency-budget"
