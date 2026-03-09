import math


def perplexity(token_probs: list[float]) -> float:
    if not token_probs:
        raise ValueError("token_probs must be non-empty")
    if any(probability <= 0.0 for probability in token_probs):
        raise ValueError("token probabilities must be positive")
    return math.exp(-sum(math.log(probability) for probability in token_probs) / len(token_probs))
