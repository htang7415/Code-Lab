from __future__ import annotations


def top_k_filter(probabilities: list[float], k: int) -> list[int]:
    if k <= 0:
        raise ValueError("k must be positive")
    if not probabilities:
        return []
    if any(probability < 0.0 for probability in probabilities):
        raise ValueError("probabilities must be non-negative")

    ranked = sorted(enumerate(probabilities), key=lambda item: item[1], reverse=True)
    k = min(k, len(ranked))
    return [index for index, _ in ranked[:k]]
