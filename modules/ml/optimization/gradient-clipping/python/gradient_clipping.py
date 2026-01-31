import math


def clip_norm(grad: list[float], clip: float) -> list[float]:
    norm = math.sqrt(sum(g * g for g in grad))
    if norm == 0 or norm <= clip:
        return grad
    scale = clip / norm
    return [g * scale for g in grad]
