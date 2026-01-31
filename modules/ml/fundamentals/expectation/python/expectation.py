def expectation(values: list[float], probs: list[float]) -> float:
    return sum(v * p for v, p in zip(values, probs))
