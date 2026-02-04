import math


def _cosine_similarity(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    if norm_a == 0.0 or norm_b == 0.0:
        return 0.0
    return dot / (norm_a * norm_b)


def info_nce_loss(
    anchor: list[float],
    positive: list[float],
    negatives: list[list[float]],
    temperature: float = 0.1,
) -> float:
    if temperature <= 0:
        raise ValueError("temperature must be positive")

    pos_score = math.exp(_cosine_similarity(anchor, positive) / temperature)
    neg_scores = [math.exp(_cosine_similarity(anchor, n) / temperature) for n in negatives]
    denom = pos_score + sum(neg_scores)
    return -math.log(pos_score / denom)
