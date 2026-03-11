from __future__ import annotations

from adapters_and_anti_corruption_layers import (
    preserves_internal_contract,
    translate_billing_event,
    vendor_status_to_internal,
)


def test_vendor_status_to_internal_maps_external_terms() -> None:
    assert vendor_status_to_internal("queued") == "pending"
    assert vendor_status_to_internal("paid") == "settled"
    assert vendor_status_to_internal("unexpected") == "unknown"


def test_translate_billing_event_keeps_only_internal_contract() -> None:
    translated = translate_billing_event(
        {
            "event_id": "evt_7",
            "state": "paid",
            "amount": 4200,
            "currency": "usd",
            "vendor_trace_id": "trace-1",
        }
    )

    assert translated == {
        "id": "evt_7",
        "status": "settled",
        "amount_cents": 4200,
        "currency": "USD",
    }


def test_preserves_internal_contract_rejects_unknown_or_leaky_shapes() -> None:
    translated = translate_billing_event({"event_id": "evt_8", "state": "mystery", "amount": 50, "currency": "usd"})
    assert preserves_internal_contract(translated) is False
    assert preserves_internal_contract({**translated, "vendor_trace_id": "trace-2"}) is False
