from __future__ import annotations


def coverage_error(relevance_rankings: list[list[int]]) -> float:
    if not relevance_rankings:
        return 0.0
    if any(label not in {0, 1} for ranking in relevance_rankings for label in ranking):
        raise ValueError("relevance labels must be binary")

    total = 0.0
    for ranking in relevance_rankings:
        last_relevant_rank = max((index + 1 for index, label in enumerate(ranking) if label == 1), default=0)
        total += last_relevant_rank
    return total / len(relevance_rankings)
