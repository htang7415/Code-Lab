def moe_combine(experts: list[list[float]], gates: list[float], k: int) -> list[float]:
    pairs = sorted(enumerate(gates), key=lambda x: x[1], reverse=True)[:k]
    total = sum(score for _, score in pairs)
    weights = [(idx, score / total) for idx, score in pairs]
    out = [0.0 for _ in experts[0]]
    for idx, w in weights:
        for j, val in enumerate(experts[idx]):
            out[j] += w * val
    return out
