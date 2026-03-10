from __future__ import annotations


def ema_update(
    ema_weights: list[float],
    model_weights: list[float],
    decay: float,
) -> list[float]:
    if len(ema_weights) != len(model_weights):
        raise ValueError("ema_weights and model_weights must have the same length")
    if not 0.0 <= decay <= 1.0:
        raise ValueError("decay must satisfy 0 <= decay <= 1")

    return [
        decay * ema_weight + (1.0 - decay) * model_weight
        for ema_weight, model_weight in zip(ema_weights, model_weights)
    ]
