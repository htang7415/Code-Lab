# Computer Use

> Track: `ai-agents` | Topic: `tool-use`

## Concept

Computer use is tool use over a live interface: the agent reads the screen, takes a UI action, and repeats.

## Key Points

- Computer use is stateful because the screen changes after every action.
- The basic loop is observe -> act -> observe again.
- UI actions need stricter validation than plain function calls because bad actions are expensive.

## Minimal Code Mental Model

```python
action = ui_action("click", target="Submit button")
needs_target = action_requires_target("click")
within_budget = step_within_budget(step_index=3, max_steps=10)
```

## Function

```python
def action_requires_target(action_type: str) -> bool:
def ui_action(action_type: str, target: str | None = None, text: str | None = None) -> dict[str, str | None]:
def step_within_budget(step_index: int, max_steps: int) -> bool:
```

## Run tests

```bash
pytest modules/ai-agents/tool-use/computer-use/python -q
```
