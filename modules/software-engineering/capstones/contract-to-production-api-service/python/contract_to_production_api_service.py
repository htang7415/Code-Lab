from __future__ import annotations


def validate_payment_request(request: dict[str, object]) -> list[str]:
    errors: list[str] = []
    if not isinstance(request.get("order_id"), str) or not str(request["order_id"]).strip():
        errors.append("order_id must be a non-empty string")
    amount = request.get("amount_cents")
    if not isinstance(amount, int) or amount <= 0:
        errors.append("amount_cents must be a positive integer")
    if request.get("currency") not in {"USD", "EUR"}:
        errors.append("currency must be USD or EUR")
    idem = request.get("idempotency_key")
    if not isinstance(idem, str) or len(idem.strip()) < 6:
        errors.append("idempotency_key must be at least 6 characters")
    return errors


def handle_payment_request(
    request: dict[str, object],
    seen_idempotency_keys: set[str],
    gateway_attempts: list[str],
) -> dict[str, object]:
    errors = validate_payment_request(request)
    if errors:
        return {"status": "rejected", "errors": errors, "attempts": 0, "retryable": False}

    key = str(request["idempotency_key"]).strip()
    if key in seen_idempotency_keys:
        return {"status": "duplicate", "attempts": 0, "retryable": False}

    retryable_statuses = {"timeout", "unavailable"}
    for attempt_number, status in enumerate(gateway_attempts, start=1):
        normalized = status.strip().lower()
        if normalized == "ok":
            seen_idempotency_keys.add(key)
            return {"status": "accepted", "attempts": attempt_number, "retryable": False}
        if normalized not in retryable_statuses:
            return {"status": "failed", "attempts": attempt_number, "retryable": False}

    return {
        "status": "failed",
        "attempts": len(gateway_attempts),
        "retryable": True,
    }


def structured_event(route: str, outcome: dict[str, object]) -> dict[str, object]:
    return {
        "route": route,
        "status": str(outcome.get("status", "unknown")),
        "attempts": int(outcome.get("attempts", 0)),
        "retryable": bool(outcome.get("retryable", False)),
    }


def sli_snapshot(outcomes: list[str]) -> dict[str, float]:
    if not outcomes:
        raise ValueError("outcomes must be non-empty")
    success_statuses = {"accepted", "duplicate"}
    success_count = sum(1 for outcome in outcomes if outcome in success_statuses)
    total = len(outcomes)
    success_rate = success_count / total
    return {
        "success_rate": success_rate,
        "failure_rate": 1.0 - success_rate,
    }


def release_decision(success_rate: float, p95_latency_ms: int, rollback_ready: bool) -> str:
    if success_rate >= 0.99 and p95_latency_ms <= 250:
        return "promote"
    if rollback_ready:
        return "rollback"
    return "hold"
