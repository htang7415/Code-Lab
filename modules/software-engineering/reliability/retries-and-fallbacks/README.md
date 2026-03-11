# Retries And Fallbacks

> Track: `software-engineering` | Topic: `reliability`

## Concept

Retries are for transient failures on safe operations, and fallbacks are for keeping degraded service alive when retries are no longer worth the cost.

## Key Points

- Retries should prefer idempotent operations.
- Max attempts should be explicit and small.
- Fallback targets should be simpler or cheaper than the primary path.

## Minimal Code Mental Model

```python
action = retry_action("timeout", attempt=1, max_attempts=3, idempotent=True)
delay = retry_delay_ms(base_delay_ms=200, attempt=2, max_delay_ms=1000)
fallback = fallback_target("live-recommendations")
```

## Function

```python
def retry_action(error_type: str, attempt: int, max_attempts: int, idempotent: bool) -> str:
def retry_delay_ms(base_delay_ms: int, attempt: int, max_delay_ms: int) -> int:
def fallback_target(primary_path: str, fallback_map: dict[str, str] | None = None) -> str | None:
```

## Run tests

```bash
pytest modules/software-engineering/reliability/retries-and-fallbacks/python -q
```
