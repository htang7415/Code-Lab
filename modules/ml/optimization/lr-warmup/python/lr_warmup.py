def warmup_lr(lr: float, t: int, warmup_steps: int) -> float:
    return lr * min(1.0, t / warmup_steps)
