# Trace-Driven Debugging

> Track: `software-engineering` | Topic: `observability`

## Concept

Trace-driven debugging uses span latency and failure status to decide where an investigation should start instead of guessing from symptoms alone.

## Key Points

- Failing spans are the fastest path to the broken dependency or workflow step.
- If nothing failed, the slowest span is usually the first latency suspect.
- Traces are most useful when the route from symptom to next inspection step is explicit.

## Minimal Code Mental Model

```python
failed = failing_spans(spans)
slowest = slowest_span(spans)
route = debugging_route(spans, slow_ms_threshold=200.0)
```

## Function

```python
def failing_spans(spans: list[dict[str, object]]) -> list[str]:
def slowest_span(spans: list[dict[str, object]]) -> str | None:
def debugging_route(spans: list[dict[str, object]], slow_ms_threshold: float) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/observability/trace-driven-debugging/python -q
```
