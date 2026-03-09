from math import comb


def pass_at_k(total_samples: int, correct_samples: int, k: int) -> float:
    if total_samples <= 0 or k <= 0:
        raise ValueError("total_samples and k must be positive")
    if correct_samples < 0 or correct_samples > total_samples:
        raise ValueError("correct_samples must be in [0, total_samples]")
    if k > total_samples:
        raise ValueError("k cannot exceed total_samples")
    if correct_samples == 0:
        return 0.0
    if total_samples - correct_samples < k:
        return 1.0
    return 1.0 - comb(total_samples - correct_samples, k) / comb(total_samples, k)
