from __future__ import annotations


def pairwise_judge_rates(outcomes: list[int]) -> tuple[float, float, float]:
    if not outcomes:
        return 0.0, 0.0, 0.0
    if any(outcome not in {-1, 0, 1} for outcome in outcomes):
        raise ValueError("outcomes must contain only -1, 0, or 1")

    total = len(outcomes)
    wins = sum(outcome == 1 for outcome in outcomes)
    losses = sum(outcome == -1 for outcome in outcomes)
    ties = sum(outcome == 0 for outcome in outcomes)
    return wins / total, losses / total, ties / total
