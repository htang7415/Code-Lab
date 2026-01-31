from collections import Counter


def empirical_pmf(samples: list[int]) -> dict[int, float]:
    counts = Counter(samples)
    n = len(samples)
    return {k: v / n for k, v in counts.items()}
