# Computer Use

> Track: `ai-agents` | Topic: `tool-use`

## Concept

Computer use is tool use over a live interface: the agent reads the screen, takes a UI action, and repeats.

## Key Points

- Computer use is stateful because the screen changes after every action.
- The basic loop is observe -> act -> observe again.
- UI actions need stricter validation than plain function calls because bad actions are expensive.
- Sensitive UI actions often need an explicit checkpoint before the click or submit step.
- Unsafe screens should trigger takeover instead of another autonomous action.

## Minimal Code Mental Model

```python
action = ui_action("click", target="Submit button")
needs_target = action_requires_target("click")
checkpoint = action_requires_checkpoint(action["action"], action["target"])
unsafe = unsafe_screen_detected("Enter your password to continue")
takeover = should_takeover(checkpoint, unsafe)
```

## Function

```python
def action_requires_target(action_type: str) -> bool:
def ui_action(action_type: str, target: str | None = None, text: str | None = None) -> dict[str, str | None]:
def step_within_budget(step_index: int, max_steps: int) -> bool:
def action_requires_checkpoint(
    action_type: str,
    target: str | None = None,
    sensitive_keywords: list[str] | None = None,
) -> bool:
def unsafe_screen_detected(screen_text: str, unsafe_markers: list[str] | None = None) -> bool:
def should_takeover(checkpoint_required: bool, unsafe_screen: bool) -> bool:
```

## Run tests

```bash
pytest modules/ai-agents/tool-use/computer-use/python -q
```
