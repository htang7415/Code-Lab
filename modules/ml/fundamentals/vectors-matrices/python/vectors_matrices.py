def matvec(a: list[list[float]], x: list[float]) -> list[float]:
    if not a or not a[0]:
        raise ValueError("a must be non-empty")
    width = len(a[0])
    if any(len(row) != width for row in a):
        raise ValueError("a must be rectangular")
    if len(x) != width:
        raise ValueError("x length must match the number of matrix columns")

    return [sum(ai * xi for ai, xi in zip(row, x)) for row in a]
