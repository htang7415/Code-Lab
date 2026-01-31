"""Group-based optimization demo for GRPO/GSPO."""

from __future__ import annotations

import math
from typing import List


def group_advantages(rewards: List[float], eps: float = 1e-8) -> List[float]:
    if not rewards:
        return []
    mean = sum(rewards) / len(rewards)
    var = sum((r - mean) ** 2 for r in rewards) / len(rewards)
    std = math.sqrt(var)
    return [(r - mean) / (std + eps) for r in rewards]


def _sequence_ratio(old_logps: List[float], new_logps: List[float]) -> float:
    return math.exp(sum(n - o for o, n in zip(old_logps, new_logps)))


def _token_ratio_mean(old_logps: List[float], new_logps: List[float]) -> float:
    ratios = [math.exp(n - o) for o, n in zip(old_logps, new_logps)]
    return sum(ratios) / len(ratios)


def grpo_objective(
    old_logps: List[List[float]],
    new_logps: List[List[float]],
    rewards: List[float],
) -> float:
    advantages = group_advantages(rewards)
    if not advantages:
        return 0.0
    total = 0.0
    for old, new, adv in zip(old_logps, new_logps, advantages):
        total += _token_ratio_mean(old, new) * adv
    return total / len(advantages)


def gspo_objective(
    old_logps: List[List[float]],
    new_logps: List[List[float]],
    rewards: List[float],
) -> float:
    advantages = group_advantages(rewards)
    if not advantages:
        return 0.0
    total = 0.0
    for old, new, adv in zip(old_logps, new_logps, advantages):
        total += _sequence_ratio(old, new) * adv
    return total / len(advantages)
