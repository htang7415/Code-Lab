from __future__ import annotations

from collections.abc import Callable


def refund_ready(amount_cents: int, duplicate_request: bool) -> bool:
    return amount_cents > 0 and not duplicate_request


def audit_entry(order_id: str, amount_cents: int, receipt: str) -> str:
    return f"refund {order_id} {amount_cents} {receipt}"


def issue_refund(
    order_id: str,
    amount_cents: int,
    duplicate_request: bool,
    gateway: Callable[[str, int], str],
    audit_log: Callable[[str], None],
) -> str:
    if not refund_ready(amount_cents, duplicate_request):
        raise ValueError("refund is not allowed")

    receipt = gateway(order_id, amount_cents)
    audit_log(audit_entry(order_id, amount_cents, receipt))
    return receipt
