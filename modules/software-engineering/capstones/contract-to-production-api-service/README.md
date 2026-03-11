# Contract To Production API Service

> Track: `software-engineering` | Topic: `capstones`

## Concept

This capstone combines contract validation, idempotency, retry policy, observability, and rollout decisions into one compact service-delivery flow.

## Key Points

- Validate the request contract before any side effects start.
- Apply idempotency before calling an unreliable dependency.
- Retries need explicit retryable vs terminal failure handling.
- Promotion should depend on canary signals and rollback readiness, not optimism.

## Minimal Code Mental Model

```python
response = handle_payment_request(request, seen_keys, ["timeout", "ok"])
event = structured_event("/payments", response)
snapshot = sli_snapshot(["accepted", "accepted", "failed"])
decision = release_decision(snapshot["success_rate"], 180, rollback_ready=True)
```

## Function

```python
def validate_payment_request(request: dict[str, object]) -> list[str]:
def handle_payment_request(
    request: dict[str, object],
    seen_idempotency_keys: set[str],
    gateway_attempts: list[str],
) -> dict[str, object]:
def structured_event(route: str, outcome: dict[str, object]) -> dict[str, object]:
def sli_snapshot(outcomes: list[str]) -> dict[str, float]:
def release_decision(success_rate: float, p95_latency_ms: int, rollback_ready: bool) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/capstones/contract-to-production-api-service/python -q
```
