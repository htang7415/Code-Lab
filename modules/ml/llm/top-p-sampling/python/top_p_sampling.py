from __future__ import annotations


def top_p_filter(probabilities: list[float], p: float) -> list[int]:
    if not 0.0 < p <= 1.0:
        raise ValueError("p must satisfy 0 < p <= 1")
    if not probabilities:
        return []
    if any(probability < 0.0 for probability in probabilities):
        raise ValueError("probabilities must be non-negative")

    total = sum(probabilities)
    if total <= 0.0:
        raise ValueError("probabilities must sum to a positive value")

    normalized = [probability / total for probability in probabilities]
    ranked = sorted(enumerate(normalized), key=lambda item: item[1], reverse=True)

    kept: list[int] = []
    cumulative = 0.0
    for index, probability in ranked:
        kept.append(index)
        cumulative += probability
        if cumulative >= p:
            break
    return kept
