def _matvec(matrix: list[list[float]], vector: list[float]) -> list[float]:
    return [sum(m * v for m, v in zip(row, vector)) for row in matrix]


def _transpose(matrix: list[list[float]]) -> list[list[float]]:
    if not matrix:
        return []
    return [list(row) for row in zip(*matrix)]


def linear_autoencode(x: list[float], W: list[list[float]]) -> list[float]:
    if not W:
        return []
    z = _matvec(W, x)
    Wt = _transpose(W)
    return _matvec(Wt, z)
