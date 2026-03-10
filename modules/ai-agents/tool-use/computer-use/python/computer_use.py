from __future__ import annotations


TARGET_ACTIONS = {"click", "type", "scroll", "read"}


def action_requires_target(action_type: str) -> bool:
    normalized = action_type.strip().lower()
    if not normalized:
        raise ValueError("action_type must be non-empty")
    return normalized in TARGET_ACTIONS


def ui_action(action_type: str, target: str | None = None, text: str | None = None) -> dict[str, str | None]:
    normalized = action_type.strip().lower()
    if not normalized:
        raise ValueError("action_type must be non-empty")
    if action_requires_target(normalized) and not (target and target.strip()):
        raise ValueError("target is required for this action")
    if normalized == "type" and not (text and text.strip()):
        raise ValueError("text is required for type actions")
    return {
        "action": normalized,
        "target": target,
        "text": text,
    }


def step_within_budget(step_index: int, max_steps: int) -> bool:
    if step_index < 0:
        raise ValueError("step_index must be non-negative")
    if max_steps <= 0:
        raise ValueError("max_steps must be positive")
    return step_index < max_steps
