def matvec(a: list[list[float]], x: list[float]) -> list[float]:
    return [sum(ai * xi for ai, xi in zip(row, x)) for row in a]
