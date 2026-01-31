def guided_step(base: float, cond: float, scale: float) -> float:
    return base + scale * (cond - base)
