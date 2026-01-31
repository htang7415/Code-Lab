from __future__ import annotations

import math


def sinusoidal_position(pos: int, d_model: int) -> list[float]:
    values = []
    for i in range(d_model):
        angle = pos / (10000 ** (2 * (i // 2) / d_model))
        if i % 2 == 0:
            values.append(math.sin(angle))
        else:
            values.append(math.cos(angle))
    return values
