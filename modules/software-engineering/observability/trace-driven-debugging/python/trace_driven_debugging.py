from __future__ import annotations


def _validated_spans(spans: list[dict[str, object]]) -> list[dict[str, object]]:
    validated: list[dict[str, object]] = []
    for span in spans:
        name = str(span.get("name", "")).strip()
        latency_ms = float(span.get("latency_ms", 0.0))
        if not name:
            raise ValueError("span name must be non-empty")
        if latency_ms < 0:
            raise ValueError("span latency must be non-negative")
        validated.append({"name": name, "latency_ms": latency_ms, "status": str(span.get("status", "")).strip()})
    return validated


def failing_spans(spans: list[dict[str, object]]) -> list[str]:
    validated = _validated_spans(spans)
    return [span["name"] for span in validated if span["status"].lower() not in {"ok", "success"}]


def slowest_span(spans: list[dict[str, object]]) -> str | None:
    validated = _validated_spans(spans)
    if not validated:
        return None
    return max(validated, key=lambda span: span["latency_ms"])["name"]


def debugging_route(spans: list[dict[str, object]], slow_ms_threshold: float) -> str:
    if slow_ms_threshold < 0:
        raise ValueError("slow_ms_threshold must be non-negative")

    validated = _validated_spans(spans)
    failed = failing_spans(validated)
    if failed:
        return f"inspect-failed-span:{failed[0]}"

    if not validated:
        return "no-trace-data"

    slowest_name = slowest_span(validated)
    slowest_latency = max(span["latency_ms"] for span in validated)
    if slowest_name is not None and slowest_latency >= slow_ms_threshold:
        return f"inspect-slowest-span:{slowest_name}"
    return "trace-healthy"
