from __future__ import annotations


def qk_clip(scores: list[list[float]], clip_value: float) -> list[list[float]]:
    if clip_value <= 0.0:
        raise ValueError("clip_value must be positive")

    return [
        [max(-clip_value, min(clip_value, score)) for score in row]
        for row in scores
    ]
