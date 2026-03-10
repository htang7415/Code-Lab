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


def judge_calibration_gap(confidences: list[float], correctness: list[int]) -> float:
    if len(confidences) != len(correctness):
        raise ValueError("confidences and correctness must have the same length")
    if any(confidence < 0.0 or confidence > 1.0 for confidence in confidences):
        raise ValueError("confidences must satisfy 0 <= confidence <= 1")
    if any(value not in {0, 1} for value in correctness):
        raise ValueError("correctness must be binary")
    if not confidences:
        return 0.0

    return sum(abs(confidence - value) for confidence, value in zip(confidences, correctness)) / len(confidences)


def judge_agreement_matrix(judge_decisions: list[list[int]]) -> list[list[float]]:
    if not judge_decisions:
        return []

    num_items = len(judge_decisions[0])
    if any(len(decisions) != num_items for decisions in judge_decisions):
        raise ValueError("all judges must score the same number of items")
    if any(decision not in {-1, 0, 1} for decisions in judge_decisions for decision in decisions):
        raise ValueError("judge decisions must contain only -1, 0, or 1")
    if num_items == 0:
        return [[0.0 for _ in judge_decisions] for _ in judge_decisions]

    matrix: list[list[float]] = []
    for left in judge_decisions:
        row: list[float] = []
        for right in judge_decisions:
            matches = sum(left_decision == right_decision for left_decision, right_decision in zip(left, right))
            row.append(matches / num_items)
        matrix.append(row)
    return matrix
