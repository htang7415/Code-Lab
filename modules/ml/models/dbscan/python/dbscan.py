def neighbors(points: list[list[float]], idx: int, eps: float) -> list[int]:
    base = points[idx]
    out = []
    for i, p in enumerate(points):
        dist = sum((a - b) ** 2 for a, b in zip(base, p)) ** 0.5
        if dist <= eps:
            out.append(i)
    return out
