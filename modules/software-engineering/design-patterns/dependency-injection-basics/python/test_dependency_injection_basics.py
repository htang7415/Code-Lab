from __future__ import annotations

import pytest

from dependency_injection_basics import audit_entry, issue_refund, refund_ready


def test_refund_ready_blocks_invalid_or_duplicate_requests() -> None:
    assert refund_ready(100, False) is True
    assert refund_ready(0, False) is False
    assert refund_ready(100, True) is False


def test_issue_refund_uses_injected_dependencies() -> None:
    calls: list[tuple[str, int]] = []
    events: list[str] = []

    def fake_gateway(order_id: str, amount_cents: int) -> str:
        calls.append((order_id, amount_cents))
        return f"receipt:{order_id}:{amount_cents}"

    receipt = issue_refund("ord_3", 250, False, fake_gateway, events.append)

    assert receipt == "receipt:ord_3:250"
    assert calls == [("ord_3", 250)]
    assert events == [audit_entry("ord_3", 250, "receipt:ord_3:250")]


def test_issue_refund_fails_before_side_effects() -> None:
    calls: list[tuple[str, int]] = []
    events: list[str] = []

    def fake_gateway(order_id: str, amount_cents: int) -> str:
        calls.append((order_id, amount_cents))
        return "unexpected"

    with pytest.raises(ValueError):
        issue_refund("ord_4", 500, True, fake_gateway, events.append)

    assert calls == []
    assert events == []
