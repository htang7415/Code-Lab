def silhouette(a: float, b: float) -> float:
    if max(a, b) == 0:
        return 0.0
    return (b - a) / max(a, b)
