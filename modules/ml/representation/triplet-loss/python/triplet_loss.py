from __future__ import annotations


def triplet_loss(
    anchor_positive_distance: float,
    anchor_negative_distance: float,
    margin: float = 0.2,
) -> float:
    if margin < 0.0:
        raise ValueError("margin must be non-negative")
    if anchor_positive_distance < 0.0 or anchor_negative_distance < 0.0:
        raise ValueError("distances must be non-negative")

    return max(0.0, anchor_positive_distance - anchor_negative_distance + margin)
