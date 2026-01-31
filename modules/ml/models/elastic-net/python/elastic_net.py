def elastic_net_penalty(w: list[float], l1: float, l2: float) -> float:
    return l1 * sum(abs(v) for v in w) + l2 * sum(v * v for v in w)
