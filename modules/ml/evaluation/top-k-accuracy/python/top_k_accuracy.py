from __future__ import annotations


def top_k_accuracy(predicted_rankings: list[list[int]], labels: list[int], k: int) -> float:
    if len(predicted_rankings) != len(labels):
        raise ValueError("predicted_rankings and labels must have the same length")
    if k <= 0:
        raise ValueError("k must be positive")
    if not labels:
        return 0.0

    correct = 0
    for ranking, label in zip(predicted_rankings, labels):
        if label in ranking[:k]:
            correct += 1
    return correct / len(labels)
