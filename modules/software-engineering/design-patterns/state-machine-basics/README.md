# State Machine Basics

> Track: `software-engineering` | Topic: `design-patterns`

## Concept

Explicit state machines make workflow rules visible, so invalid transitions are rejected instead of being implied by scattered conditionals.

## Key Points

- State is easiest to reason about when the allowed transitions are declared in one place.
- Workflow correctness matters more than elegance for long-lived business processes.
- Terminal states should be explicit so retries and rollbacks behave predictably.

## Minimal Code Mental Model

```python
assert can_transition("draft", "approved") is True
assert apply_transition("approved", "fulfilling") == "fulfilling"
assert terminal_state("shipped") is True
```

## Function

```python
def can_transition(current: str, nxt: str) -> bool:
def apply_transition(current: str, nxt: str) -> str:
def terminal_state(state: str) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/design-patterns/state-machine-basics/python -q
```
