from __future__ import annotations


STATUS_MAP = {
    "queued": "pending",
    "paid": "settled",
    "reversed": "failed",
}


def vendor_status_to_internal(status: str) -> str:
    return STATUS_MAP.get(status.strip().lower(), "unknown")


def translate_billing_event(event: dict[str, object]) -> dict[str, object]:
    return {
        "id": str(event.get("event_id", "")).strip(),
        "status": vendor_status_to_internal(str(event.get("state", ""))),
        "amount_cents": int(event.get("amount", 0)),
        "currency": str(event.get("currency", "")).strip().upper(),
    }


def preserves_internal_contract(event: dict[str, object]) -> bool:
    required_keys = {"id", "status", "amount_cents", "currency"}
    if set(event) != required_keys:
        return False
    if not event["id"] or event["status"] == "unknown":
        return False
    if not isinstance(event["amount_cents"], int) or int(event["amount_cents"]) < 0:
        return False
    return len(str(event["currency"])) == 3
