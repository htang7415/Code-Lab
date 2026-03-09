from __future__ import annotations

import math


def warmup_cosine_lr(
    base_lr: float,
    step: int,
    warmup_steps: int,
    total_steps: int,
) -> float:
    if base_lr < 0.0:
        raise ValueError("base_lr must be non-negative")
    if step < 0:
        raise ValueError("step must be non-negative")
    if warmup_steps < 0:
        raise ValueError("warmup_steps must be non-negative")
    if total_steps <= 0:
        raise ValueError("total_steps must be positive")
    if warmup_steps > total_steps:
        raise ValueError("warmup_steps cannot exceed total_steps")

    if warmup_steps > 0 and step < warmup_steps:
        return base_lr * step / warmup_steps

    if total_steps == warmup_steps:
        return base_lr

    progress = (step - warmup_steps) / (total_steps - warmup_steps)
    progress = min(max(progress, 0.0), 1.0)
    return 0.5 * base_lr * (1.0 + math.cos(math.pi * progress))
