from __future__ import annotations

from runbooks_and_dashboards import (
    missing_dashboard_panels,
    missing_runbook_fields,
    operator_ready,
)


RUNBOOK = {
    "service": "payments",
    "owner": "payments-oncall",
    "page-policy": "24x7",
    "health-check": "GET /healthz",
    "rollback": "redeploy previous version",
}


def test_missing_runbook_fields_finds_critical_gaps() -> None:
    assert missing_runbook_fields(RUNBOOK) == []
    assert missing_runbook_fields({"service": "payments", "owner": "payments-oncall"}) == [
        "health-check",
        "page-policy",
        "rollback",
    ]


def test_missing_dashboard_panels_reports_uncovered_signals() -> None:
    assert missing_dashboard_panels(["latency", "error-rate", "traffic"], ["latency", "traffic"]) == [
        "error-rate"
    ]


def test_operator_ready_requires_both_runbook_and_dashboard_coverage() -> None:
    assert operator_ready(RUNBOOK, ["latency", "error-rate"], ["latency", "error-rate"]) is True
    assert operator_ready(RUNBOOK, ["latency", "error-rate"], ["latency"]) is False
