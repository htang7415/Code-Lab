from __future__ import annotations


def make_plan(goal: str, steps: list[str]) -> list[dict[str, object]]:
    if not goal.strip():
        raise ValueError("goal must be non-empty")
    cleaned_steps = [step.strip() for step in steps if step.strip()]
    if not cleaned_steps:
        raise ValueError("steps must include at least one non-empty step")
    return [
        {"goal": goal.strip(), "step": step, "done": False}
        for step in cleaned_steps
    ]


def next_pending_step(plan: list[dict[str, object]]) -> int | None:
    for index, step in enumerate(plan):
        if not step.get("done", False):
            return index
    return None


def mark_step_done(plan: list[dict[str, object]], step_index: int) -> list[dict[str, object]]:
    if not 0 <= step_index < len(plan):
        raise IndexError("step_index out of range")
    updated = [dict(step) for step in plan]
    updated[step_index]["done"] = True
    return updated
