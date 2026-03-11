from __future__ import annotations

import pytest

from trace_driven_debugging import debugging_route, failing_spans, slowest_span


SPANS = [
    {"name": "api", "latency_ms": 20.0, "status": "ok"},
    {"name": "cache", "latency_ms": 40.0, "status": "ok"},
    {"name": "db", "latency_ms": 240.0, "status": "error"},
]


def test_failing_spans_and_slowest_span_extract_primary_debugging_signals() -> None:
    assert failing_spans(SPANS) == ["db"]
    assert slowest_span(SPANS) == "db"


def test_debugging_route_prefers_failure_then_latency_then_healthy() -> None:
    assert debugging_route(SPANS, slow_ms_threshold=200.0) == "inspect-failed-span:db"
    assert debugging_route(
        [
            {"name": "api", "latency_ms": 20.0, "status": "ok"},
            {"name": "db", "latency_ms": 240.0, "status": "ok"},
        ],
        slow_ms_threshold=200.0,
    ) == "inspect-slowest-span:db"
    assert debugging_route(
        [{"name": "api", "latency_ms": 20.0, "status": "ok"}],
        slow_ms_threshold=200.0,
    ) == "trace-healthy"


def test_validation_rejects_invalid_span_data() -> None:
    with pytest.raises(ValueError):
        failing_spans([{"name": "", "latency_ms": 10.0, "status": "ok"}])
    with pytest.raises(ValueError):
        debugging_route([{"name": "api", "latency_ms": -1.0, "status": "ok"}], slow_ms_threshold=200.0)
