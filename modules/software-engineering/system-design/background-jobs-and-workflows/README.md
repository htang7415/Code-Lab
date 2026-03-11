# Background Jobs And Workflows

> Track: `software-engineering` | Topic: `system-design`

## Concept

Work should leave the request path when it is slow, retry-prone, or composed of multiple durable steps.

## Key Points

- Background jobs reduce request latency by moving non-immediate work out of band.
- Multi-step business processes usually need workflow state, not just one queued function.
- User-visible deadlines still matter even when work is asynchronous.

## Minimal Code Mental Model

```python
background = should_background_job(user_waiting=True, duration_ms=1500, retries_expected=True)
kind = workflow_kind(needs_human_approval=False, has_multiple_steps=True)
priority = queue_priority(user_visible=True, deadline_ms=2000)
```

## Function

```python
def should_background_job(user_waiting: bool, duration_ms: int, retries_expected: bool) -> bool:
def workflow_kind(needs_human_approval: bool, has_multiple_steps: bool) -> str:
def queue_priority(user_visible: bool, deadline_ms: int | None) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/system-design/background-jobs-and-workflows/python -q
```
