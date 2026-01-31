def normalize_probs(values: list[float]) -> list[float]:
    s = sum(values)
    return [v / s for v in values]
