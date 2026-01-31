def accumulate(grads: list[list[float]]) -> list[float]:
    if not grads:
        return []
    total = [0.0 for _ in grads[0]]
    for g in grads:
        total = [a + b for a, b in zip(total, g)]
    return total
