from __future__ import annotations


def macro_f1_score(
    true_positives: list[int],
    false_positives: list[int],
    false_negatives: list[int],
) -> float:
    if len(true_positives) != len(false_positives) or len(true_positives) != len(false_negatives):
        raise ValueError("all class-stat lists must have the same length")
    if any(value < 0 for value in true_positives + false_positives + false_negatives):
        raise ValueError("class statistics must be non-negative")
    if not true_positives:
        return 0.0

    total = 0.0
    for tp, fp, fn in zip(true_positives, false_positives, false_negatives):
        precision = 0.0 if tp + fp == 0 else tp / (tp + fp)
        recall = 0.0 if tp + fn == 0 else tp / (tp + fn)
        total += 0.0 if precision + recall == 0.0 else 2.0 * precision * recall / (precision + recall)
    return total / len(true_positives)
