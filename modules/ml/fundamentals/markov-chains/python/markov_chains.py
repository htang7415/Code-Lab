def next_distribution(p: list[float], t: list[list[float]]) -> list[float]:
    return [sum(p[j] * t[j][i] for j in range(len(p))) for i in range(len(t[0]))]
