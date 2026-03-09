from __future__ import annotations

import math


def uct_score(
    value_sum: float,
    parent_visits: int,
    child_visits: int,
    exploration: float = 1.4142135623730951,
) -> float:
    if parent_visits <= 0:
        raise ValueError("parent_visits must be positive")
    if child_visits < 0:
        raise ValueError("child_visits must be non-negative")
    if exploration < 0.0:
        raise ValueError("exploration must be non-negative")
    if child_visits == 0:
        return math.inf

    mean_value = value_sum / child_visits
    bonus = exploration * math.sqrt(math.log(parent_visits) / child_visits)
    return mean_value + bonus
