from __future__ import annotations

import math


def temperature_probabilities(logits: list[float], temperature: float) -> list[float]:
    if temperature <= 0.0:
        raise ValueError("temperature must be positive")
    if not logits:
        return []

    scaled = [logit / temperature for logit in logits]
    max_scaled = max(scaled)
    exps = [math.exp(value - max_scaled) for value in scaled]
    total = sum(exps)
    return [value / total for value in exps]
