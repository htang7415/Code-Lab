from __future__ import annotations

import pytest

from contract_to_production_api_service import (
    handle_payment_request,
    release_decision,
    sli_snapshot,
    structured_event,
)


def test_handle_payment_request_accepts_after_retryable_gateway_failure() -> None:
    request = {
        "order_id": "ord_1",
        "amount_cents": 1200,
        "currency": "USD",
        "idempotency_key": "idem-123",
    }
    seen_keys: set[str] = set()

    outcome = handle_payment_request(request, seen_keys, ["timeout", "ok"])

    assert outcome == {"status": "accepted", "attempts": 2, "retryable": False}
    assert "idem-123" in seen_keys
    assert structured_event("/payments", outcome) == {
        "route": "/payments",
        "status": "accepted",
        "attempts": 2,
        "retryable": False,
    }


def test_handle_payment_request_rejects_invalid_or_duplicate_requests_before_side_effects() -> None:
    seen_keys = {"idem-123"}

    duplicate = handle_payment_request(
        {
            "order_id": "ord_1",
            "amount_cents": 1200,
            "currency": "USD",
            "idempotency_key": "idem-123",
        },
        seen_keys,
        ["ok"],
    )
    rejected = handle_payment_request(
        {"order_id": "", "amount_cents": 0, "currency": "CAD", "idempotency_key": "bad"},
        set(),
        ["ok"],
    )

    assert duplicate == {"status": "duplicate", "attempts": 0, "retryable": False}
    assert rejected["status"] == "rejected"
    assert rejected["attempts"] == 0
    assert rejected["retryable"] is False
    assert "currency must be USD or EUR" in rejected["errors"]


def test_sli_snapshot_and_release_decision_drive_canary_outcomes() -> None:
    snapshot = sli_snapshot(["accepted", "duplicate", "failed"])

    assert snapshot["success_rate"] == pytest.approx(2 / 3)
    assert snapshot["failure_rate"] == pytest.approx(1 / 3)
    assert release_decision(0.995, 180, rollback_ready=True) == "promote"
    assert release_decision(snapshot["success_rate"], 180, rollback_ready=True) == "rollback"
    assert release_decision(snapshot["success_rate"], 180, rollback_ready=False) == "hold"

    with pytest.raises(ValueError):
        sli_snapshot([])
