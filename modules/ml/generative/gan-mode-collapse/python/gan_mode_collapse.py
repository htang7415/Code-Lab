def diversity_score(samples: list[float]) -> float:
    return len(set(samples)) / len(samples) if samples else 0.0
