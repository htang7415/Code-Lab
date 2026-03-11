import math


def mean_negative_log_likelihood(token_probs: list[float]) -> float:
    if not token_probs:
        raise ValueError("token_probs must be non-empty")
    if any(probability <= 0.0 for probability in token_probs):
        raise ValueError("token probabilities must be positive")
    if any(probability > 1.0 for probability in token_probs):
        raise ValueError("token probabilities must be at most 1")
    return -sum(math.log(probability) for probability in token_probs) / len(token_probs)


def perplexity(token_probs: list[float]) -> float:
    return math.exp(mean_negative_log_likelihood(token_probs))
